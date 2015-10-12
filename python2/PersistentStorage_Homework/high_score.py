#!/usr/local/bin/python3
#
# High Score Board
# high_score.py
#
# 2015 July 9th
#
""" Keeps a high score board for individual users in the form
of a shelve file. """
    
import shelve

def set_high_score(name, score):
    """ Stores high scores for unique players in a shelve.
    :param name: String detailing the player's name
    :param score: Number detailing the player's high score
    :return: Player's current highest score (integer)
    """
    
    shelve_file = "score_board.shlf"
    score_board = shelve.open(shelve_file)
    high_score = score_board.get(name, None)
    
    if high_score is None or score >= high_score:
        score_board[name] = score
        high_score = score
        
    score_board.close()
    
    return high_score
