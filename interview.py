"""Script to complete interview challenge"""

import random

SCORE_DICT = {"E": 1, "A": 1, "I": 1, "O": 1,
              "N": 1, "R": 1, "T": 1, "L": 1, "S": 1, "U": 1, "D": 2, "G": 2, "B": 3, "C": 3, "M": 3, "P": 3,
              "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4, "K": 5, "J": 8, "X": 8, "Q": 10, "Z": 10}


def get_score(word: str) -> int:
    """Returns integer score for a given string input"""

    score_dict = SCORE_DICT

    score = 0
    if word:
        for current_letter in word:
            score += score_dict[current_letter]
    else:
        raise ValueError("No input provided")

    return score


def assign_tiles() -> list:
    """assigns 7 random tiles to a player"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUWXYZ"

    player_list = []

    for each_letter in range(7):
        player_list.append(random.choice(alphabet))

    return player_list


def assign_tiles_weighted() -> list:
    """assign 7 random tiles to a player with restrictions on tiles"""

    BAG = ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
           'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
           'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
           'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
           'N', 'N', 'N', 'N', 'N', 'N',
           'R', 'R', 'R', 'R', 'R', 'R',
           'T', 'T', 'T', 'T', 'T', 'T',
           'L', 'L', 'L', 'L', 'U', 'U', 'U', 'U',
           'S', 'S', 'S', 'S', 'D', 'D', 'D', 'D',
           'G', 'G', 'G', 'B', 'B', 'C', 'C', 'M', 'M',
           'P', 'P', 'F', 'F', 'H', 'H', 'V', 'V',
           'W', 'W', 'Y', 'K', 'J', 'X', 'Q', 'Z']
    player_tiles = []

    for each_letter in range(7):
        tile = random.choice(BAG)
        player_tiles.append(tile)
        BAG.remove(tile)

    return player_tiles
