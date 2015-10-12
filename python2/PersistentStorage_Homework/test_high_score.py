# 2015 July 7th
#
""" Unittest module for high_score.py """

import unittest
import high_score
import tempfile
import os
import glob
import shutil

class TestHighScore(unittest.TestCase):
    
    def setUp(self):
        """ Moves working directory to temporary one for new shelve file. """
        self.original_directory = os.getcwd()
        self.temp_dir = tempfile.mkdtemp("test_high_score")
        os.chdir(self.temp_dir)
        # Save function to test in a variable
        self.HighScore = high_score.set_high_score
            
    def test_setHighScore(self):
        """ Sets several scores for several new players. """
        
        self.assertEqual(-100, self.HighScore('Carlos', -100))
        self.assertGreater(-99, self.HighScore('Carlos', -100))
        self.assertEqual(0, self.HighScore('Carlos', 0))
        self.assertLess(0, self.HighScore('Saurav', 100))
        self.assertEqual(1000, self.HighScore('Saurav', 1000))
        self.assertLess(100, self.HighScore('Saurav', 1000))
        self.assertEqual(0, self.HighScore('Carlos', -1))
    
    def test_many_scores(self):
        """ Sets (or tries to) a score several times to a single player. """

        self.assertEqual(50, self.HighScore('Kirby', 50))
        self.assertEqual(150, self.HighScore('Kirby', 150))
        self.assertEqual(150, self.HighScore('Kirby', 40))
        self.assertEqual(150, self.HighScore('Kirby', 95))
        self.assertTrue(self.HighScore('Kirby', 180) == 180,
                        'Kirby should have 180 as a top score')
        
    def tearDown(self):
        """Deletes the created shelve files and the temporary directory. """
        # Since I lack the option for Additional Comments in Ellipse, I'll
        # state that I'm deleting the shelve files here just to practice the
        # use of glob, even though I'm deleting the temporary directory anyway
        # Since the function to test doesn't take a path parameter (and there
        # is no class or other function to help), I don't think it's a good
        # idea to delete a predetermined file that already contains data that
        # we may not want to delete just because of testing...
        [os.remove(fn) for fn in glob.glob("score_board.shlf*")]
        os.chdir(self.original_directory)
        shutil.rmtree(self.temp_dir)


if __name__ == "__main__":
    unittest.main()
