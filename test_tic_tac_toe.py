import unittest
from tic_tac_toe_engine import TicTacToe
class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a new TicTacToe game before each test"""
        self.game = TicTacToe()
    
    def test_row_win_x(self):
        board = [
            ['X','X','X'],
            ['O',None,'O'],
            [None,'O',None]
        ]
        message = "Expected get_winner to return 'X wins!'"
        self.assertEqual(self.game.get_winner(board),'X wins!',message)
    
    def test_row_win_o(self):
        board = [
            [None,'X',None],
            ['O','O','O'],
            ['X','X',None]
        ]
        message = "Expected get_winner to return 'O wins!'"
        self.assertEqual(self.game.get_winner(board),'O wins!',message)
    
    def test_no_win(self):
        board = [
            ['X','O','X'],
            ['O','X','O'],
            ['O','X','O']
        ]
        message = "Expected no winner"
        self.assertIsNone(self.game.get_winner(board), message)
    
    def test_x_diag_win(self):
        board = [
            ['X','X',None],
            ['O','X','O'],
            ['O','X','X']
        ]
        message = "Expected get_winner to return 'X wins!'"
        self.assertEqual(self.game.get_winner(board),'X wins!',message)
    
    def test_o_diag_win(self):
        board = [
            ['X','X','O'],
            ['X','O','O'],
            ['O','X','X']
        ]
        message = "Expected get_winner to return 'O wins!'"
        self.assertEqual(self.game.get_winner(board),'O wins!',message)
    
    def test_o_vert_win(self):
        board = [
            ['O','X','O'],
            ['O','O','X'],
            ['O','X','X']
        ]
        message = "Expected get_winner to return 'O wins!'"
        self.assertEqual(self.game.get_winner(board),'O wins!',message)

    def test_x_vert_win(self):
        board = [
            ['O','X','X'],
            ['X','O','X'],
            ['O','X','X']
        ]
        message = "Expected get_winner to return 'X wins!'"
        self.assertEqual(self.game.get_winner(board),'X wins!',message)
    
    def test_draw(self):
        board = [
            ['O','X','O'],
            ['X','X','O'],
            ['X','O','X']
        ]
        message = "Expected a draw"
        self.assertEqual(self.game.check_draw(board),"Draw!",message)
    
    def test_game_not_over(self):
        board = [
            ['O','X','X'],
            ['X','O',None],
            ['O','X','X']
        ]
        message = "Game should not have ended in draw yet"
        self.assertIsNone(self.game.check_draw(board),message)

if __name__ == '__main__':
    unittest.main()
