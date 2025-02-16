import copy
import random
import pandas as pd
class InvalidMoveError(Exception):
    def __init__(self, move_coords):
        self.move_coords = move_coords
    def __str__(self):
        return f'Player has already made a move at {self.move_coords}.'

class TicTacToe:
    def __init__(self):
        self.xo_count = 0


    def new_board(self):
        return [[None, None, None], [None, None, None], [None, None, None]]

    def render(self, board):
        i = 0
        j = 0
        display_board = copy.deepcopy(board)
        for row in board:
            for square in row:
                if board[i][j] == None:
                    display_board[i][j] = str(' ')
                j += 1
            j = 0
            i += 1
        rendered_board = '  | 0 | 1 | 2 \n ------------- \n 0| '+display_board[0][0]+' | '+display_board[0][1]+' | '+display_board[0][2] + '\n 1| '+display_board[1][0]+' | '+display_board[1][1]+' | '+display_board[1][2]+ '\n 2| '+display_board[2][0]+' | '+display_board[2][1]+' | '+display_board[2][2]+ '\n'
        return rendered_board

    def get_move(self):
        x_coord_str = input("What is your move's x-coordinate? ")
        x_coord = int(x_coord_str)
        y_coord_str = input("What is your move's y-coordinate? ")
        y_coord = int(y_coord_str)
        return (x_coord, y_coord)

    def is_valid_move(self, move_coords, board):
        if board[move_coords[1]][move_coords[0]] == None:
            return True
        else:
            return False

    def make_move(self, move_coords, board, team):
        while True:
            if self.is_valid_move(move_coords, board):
                break
            else:
                raise InvalidMoveError(move_coords)
        new_board = board
        new_board[move_coords[1]][move_coords[0]] = team
        return new_board

    xo_count = 0
    def alternate_move(self):
        move = 'X' if self.xo_count % 2 == 0 else 'O'
        self.xo_count += 1
        return move
    
    def get_winner(self, board):
        # Test winning diagonally
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
            return f'{board[0][0]} wins!'
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
            return f'{board[0][2]} wins!'
        # Test winning horizontally
        for i in range(0,3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
                return f'{board[0][i]} wins!'
        # Test winning vertically
        for i in range(0,3):
            if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
                return f'{board[i][0]} wins!'
        # If no winner, return none
        return None

    def check_draw(self, board):
        none_moves = []
        if self.get_winner(board) is None:
            for row in board:
                for square in row:
                    if square is None:
                        none_moves.append(square)
            if len(none_moves) == 0:
                return "Draw!"
        return None
    
    def find_valid_moves(self, board):
        valid_moves = []
        i = 0
        j = 0
        for row in board:
            for square in row:
                if square is None:
                    valid_moves.append((i,j))
                i += 1
            i = 0
            j += 1
        return valid_moves

    def random_ai(self, board, current_player):
        valid_moves = self.find_valid_moves(board)
        random_move_coords = random.choice(valid_moves)
        return random_move_coords
        
    def finds_winning_moves_ai(self, board, current_player):
        valid_moves = self.find_valid_moves(board)
        for move in valid_moves:
            test_board = copy.deepcopy(board)
            test_board = game.make_move(move, test_board, current_player)
            if self.get_winner(test_board) == f'{current_player} wins!':
                return move
        return self.random_ai(board, current_player)

    def finds_winning_and_losing_moves_ai(self, board, current_player):
        valid_moves = self.find_valid_moves(board)
        for move in valid_moves:
            test_board_defense = copy.deepcopy(board)
            test_board_offense = copy.deepcopy(board)
            next_player = self.alternate_move()
            self.xo_count -= 1
            test_board_defense = self.make_move(move, test_board_defense, next_player)
            test_board_offense = self.make_move(move, test_board_offense, current_player)
            if self.get_winner(test_board_defense) == f'{next_player} wins!':
                return move
            elif self.get_winner(test_board_offense) == f'{current_player} wins!':
                return move
        return self.random_ai(board, current_player)
    
    def human_player(self, board, current_player):
        return self.get_move()

if __name__ == '__main__':


    def play(strategy1, strategy2):
        game = TicTacToe()
        board = game.new_board()
        while True:
            try:
                current_player = game.alternate_move()
                if current_player == 'X':
                    move = strategy1(game, board, current_player)
                elif current_player == 'O':
                    move = strategy2(game, board, current_player)
                # print(move)
                board = game.make_move(move, board, current_player)
                print(game.render(board))
                if game.get_winner(board) is not None:
                    print(game.get_winner(board))
                    print('Game over')
                    if current_player == 'X':
                        return 1 # Return 1 if strategy 1 wins
                    elif current_player == 'O':
                        return 2 # Return 2 if strategy 2 wins
                if game.check_draw(board) is not None:
                    print(game.check_draw(board))
                    print('Game over')
                    return 0 # Return 0 if draw
            except InvalidMoveError as e:
                print(f"Invalid move: {e} Please try again")
                game.xo_count -= 1
                continue
    
    def repeated_battle(strategy1, strategy2):
        results = {'draw': 0, 'strategy_1': 0, 'strategy_2': 0}
        results['draw'] = 0
        results['strategy_1'] = 0
        results['strategy_2'] = 0
        for i in range(0, 1000):
            result = play(strategy1, strategy2)
            if result == 0:
                results['draw'] += 1
            elif result == 1:
                results['strategy_1'] += 1
            else:
                results['strategy_2'] += 1
        return results

    outcome = repeated_battle(TicTacToe.finds_winning_and_losing_moves_ai, TicTacToe.random_ai)

    print(outcome)