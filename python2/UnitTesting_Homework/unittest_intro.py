#!/usr/local/bin/python3
#
# Unittest Introduction
# unittest_intro.py
#
# 2015 July 4th
#
""" Demonstrates the use of unittest by refactoring a simple function. """

import re
import string
import unittest

def title(text):
    """ Returns a string with the first occurrence of a letter in uppercase.
    :param text: String to be modified.
    :return: String with the first occurrence of a letter in uppercase.
    """
    new_string = []
    
    def iterate_through_word(word):
        """ Iterates through a set of characters (word).
        :param word: Set of characters to transform
        :return: String with the first occurrence of a letter in uppercase, and the rest in lowercase
        """
        new_word = []
        for count, letter in enumerate(word):
            if letter in string.ascii_letters:
                new_word.append(letter.upper())
                return "".join(new_word) + word[count + 1:].lower()
            new_word.append(letter.lower())
            
        return "".join(new_word)
    
    for word in re.split("({0})".format(regular_expr_punctuation()), text):
        new_string.append(iterate_through_word(word))
        
    return "".join(new_string)

def regular_expr_punctuation():
    """ Gives a string containing a list of punctuation characters as a regular expression.
    :return: String of punctuation characters as a regular expression.
    """
    characters = ["\s"]
    trouble_chars = ["\\", "|", ".", "^", "$", "*", "+", "[", "]", "{", "}", "(", ")", "\"", "?"]
    for char in string.punctuation:
        characters.append(char if char not in trouble_chars else "\\" + char)
    
    return "|".join(characters)

class TestCube(unittest.TestCase):
    
    def test_normal_string(self):
        test_string = "the luck of the fryish"
        self.assertEqual(title(test_string), test_string.title())
        
    def test_complex_string(self):
        test_string = "-+_31416o papRika 09w +iR"
        self.assertEqual(title(test_string), test_string.title())
        
    def test_large_string(self):
        test_string = """
        The 2008 election campaign was remarkable for the fact that the Democratic and Republican presidential and vice-presidential
        candidates possessed elements of Irish ancestry. Much more remarkable of course was the fact that the victor was Barack Obama,
        the United States's first African-American President. Obama is Kenyan in his paternal ancestry,
        but his forebears on his maternal side include a great-great-great grandfather Falmouth or Fulmuth Kearney or Carney,
        born in Ireland about 1832 and emigrated to the US in 1850, whose father is stated to be
        Joseph Kearney, a shoemaker of Moneygall, County Offaly (http://www.wargs.com/political/obama.html).
        US genealogist Megan Smolenyak first established Obama's Moneygall connection, and for further information on her researches
        see http://www.rootstelevision.com/blogs/megans-rootsworld.
        """

        self.assertEqual(title(test_string), test_string.title())
        
    def test_bad_input1(self):
        self.assertRaises(TypeError, title, 4)
        
    def test_bad_input2(self):
        self.assertRaises(TypeError, title, ['a', 'b'])

if __name__ == "__main__":
    unittest.main()
