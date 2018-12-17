#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def cyan_color(skk): print("\033[96m {}\033[00m" .format(skk))


def red_color(skk): print("\033[91m {}\033[00m" .format(skk))


def green_color(skk): print("\033[92m {}\033[00m" .format(skk))


class Player:

    def move(self, same_move):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self, random_move):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        text = input(" Rock, paper or scissors? ")
        move = text.lower()
        while move not in moves:
            text = input(" Rock, paper or scissors? ")
            move = text.lower()
        return move

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        self.opponent_move = ""
        self.reflect_move = ""
        self.first_round = 0

    def learn(self, my_move, their_move):
        self.opponent_move = my_move
        self.reflect_move = their_move
        return self.reflect_move

    def move(self, reflect_move):
        if self.first_round:
            return self.reflect_move
        else:
            m = random.choice(moves)
            self.first_round = 1
            return m


class CyclePlayer(Player):

    def __init__(self):
        self.opponent_move = ""
        self.cycle_move = ""
        self.first_round = 0

    def learn(self, my_move, their_move):
        self.cycle_move = my_move
        self.opponent_move = their_move
        return self.cycle_move

    def move(self, cycle_move):
        if self.first_round:
            if self.cycle_move == "rock":
                self.cycle_move = "paper"
            elif self.cycle_move == "paper":
                self.cycle_move = "scissors"
            else:
                self.cycle_move = "rock"
            return self.cycle_move
        else:
            m = random.choice(moves)
            self.first_round = 1
            return m


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def beats(self, one, two):

        if one == 'rock' and two == 'scissors':
            red_color("** PLAYER ONE WIN **")
            self.score1 += 1
        elif one == 'scissors' and two == 'paper':
            red_color("** PLAYER ONE WIN **")
            self.score1 += 1
        elif one == 'paper' and two == 'rock':
            red_color("** PLAYER ONE WIN **")
            self.score1 += 1
        elif one == two:
            red_color("** TIE **")
        else:
            red_color("** PLAYER TWO WIN **")
            self.score2 += 1
        cyan_color(f"""Score: Player One {self.score1}, \
Player Two {self.score2}
                    """)

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move(move1)
        print(f" You played {move1}")
        print(f" Opponent played {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.beats(move1, move2)

    def play_multi_game(self):
        green_color("""
 GAME START!
              """)
        for round in range(99):
            if self.score1 < 3 and self.score2 < 3:
                print(f" Round {round}:")
                self.play_round()
        green_color(f"FINAL SCORE: Player One {self.score1}, \
Player Two {self.score2}")
        red_color("""
 GAME OVER!
                  """)

    def play_single_game(self):
        green_color("""
 GAME START!
              """)
        print(f" Round {1}:")
        self.play_round()
        green_color(f"FINAL SCORE: Player One {self.score1}, \
Player Two {self.score2}")
        red_color("""
GAME OVER!
              """)

    def play_game(self):
        types = ["single", "multi"]
        type = (input("'Single' or 'Multi' round? ")).lower()
        while type not in types:
            type = (input("'Single' or 'Multi' round? ")).lower()
        if type == "single":
            self.play_single_game()
        else:
            self.play_multi_game()


if __name__ == '__main__':
    behaviors = [Player(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    behavior = random.choice(behaviors)
    human = HumanPlayer()
    game = Game(human, behavior)
    game.play_game()
