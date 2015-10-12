#!/usr/local/bin/python3
#
# Lesson 13: Time-Based Computations Homework Project
#
'''
Created on Aug 30, 2015

@author: cmontesr

mathquiz.py: Line-command where the user answers five random
            integer (range (0-10) sums; time results are displayed
            at the end.
'''

from random import randint
from math import fsum
from decimal import Decimal
from os import path
import logging

NUMBER_QUESTIONS = 5

def int_pair_generator():
    """
    Generator of pairs of random integer tuples.
    :return: Yielded tuple formed by a pair of random integers (1-10)
    """
    for i in range(NUMBER_QUESTIONS):
        yield (randint(1, 10), randint(1, 10))
        
def verify_sum(int_pair, guess_sum):
    """
    Verifies that guess_sum is the result of int_pair's sum.
    :param int_pair: Tuple of two integers
    :param guess_sum: Integer addition guessed by the user
    :return: Boolean value based on both values' comparison
    """
    try:
        return sum(int_pair) == int(guess_sum)
    except ValueError:
        return False

def time_results(time_scores):
    """
    Checks a collection of times and returns a total and average.
    :param times_scores: Collection of float times
    :return: Tuple containing the total time and average of the collection
    """
    total = fsum(time_scores)
    return (total, total / len(time_scores))

def start_logging():
    """
    Starts logging of the project, at the INFO level.
    """
    logging.basicConfig(filename=path.join("src", "mathquiz.log"),
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    
    from argparse import ArgumentParser
    import time
    
    # Allow to set the number of questions to be asked per game
    parser = ArgumentParser(description="Integer addition game")
    parser.add_argument("-q", "--questions", dest="no_questions",
                        type=int, default=5,
                        action="store", help="How many questions to be asked")
    
    options = parser.parse_args()
    
    if options.no_questions and options.no_questions > 0:
        NUMBER_QUESTIONS = options.no_questions
    
    start_logging()
    logging.info("New session of {0} questions".format(NUMBER_QUESTIONS))
    
    while True:
        # New set of integer pairs:
        pair_gen = int_pair_generator()
        # List that keeps pairs of amount of time and success per guess
        guesses_list = []
        
        for i in range(NUMBER_QUESTIONS):
            pair = next(pair_gen)
            # Measure time it took for the user to answer
            start = time.time()
            guess = input("What is the sum of {0} and {1}? ".format(*pair))
            end = time.time()
            
            success = "right" if verify_sum(pair, guess) else "wrong"
            total_time = (abs(float(Decimal(start) - Decimal(end))))
            
            print("{0} is {1}!".format(guess, success))
            
            # Append the absolute total time that this guess took, and success
            guesses_list.append((total_time, success))
            # Log entry
            logging.info("Question {0}: {1} answer took {2} seconds".format(
                        i, success, total_time))
        
        # Print the time and success of each guess; start adding total time
        g_str = "Question {0} took about {1} seconds to complete and was {2}."
        total_time = 0
        
        for i, t in enumerate(guesses_list):
            total_time += Decimal(t[0])
            print(g_str.format(i + 1, round(t[0]), t[1]))
            
        average = total_time / len(guesses_list)
            
        # Print and log the final results
        print("You took {0:.1f} to finish the quiz".format(total_time))
        print("Your average time was {0:.1f} per question\n".format(average))
        
        logging.info("Total time for last set: {0} secs".format(total_time))
        logging.info("Average time for last set: {0} secs".format(average))
        
        if str.upper(input("Try again? Y/N ")) != "Y":
            break
