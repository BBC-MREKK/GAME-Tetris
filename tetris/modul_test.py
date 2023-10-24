import unittest
from main import Tetris

class TetrisTestCase(unittest.TestCase):
    def setUp(self):
        self.tetris = Tetris()

    def test_reset_tetromino(self):
        self.tetris.reset_tetromino()
        self.assertTrue(len(self.tetris.tetromino) == 4)

    def test_get_tetromino_coords(self):
        self.tetris.reset_tetromino()
        coords = self.tetris.get_tetromino_coords()
        self.assertTrue(len(coords) == 4)  

    def test_apply_tetromino(self):
        self.tetris.reset_tetromino()
        initial_score = self.tetris.score
        self.tetris.apply_tetromino()
        self.assertTrue(self.tetris.score > initial_score)  


if __name__ == '__main__':
    unittest.main()