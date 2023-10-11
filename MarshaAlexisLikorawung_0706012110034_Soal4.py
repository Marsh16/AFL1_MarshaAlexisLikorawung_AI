import copy

def initialize_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print('|'.join(row))
    print('-' * 13)

def get_possible_actions(board):
    actions = []
    for col in range(7):
        if board[0][col] == ' ':
            actions.append(col)
    return actions

def result(board, action, player):
    new_board = copy.deepcopy(board)
    for row in range(5, -1, -1):
        if new_board[row][action] == ' ':
            new_board[row][action] = player
            break
    return new_board

def winner(board):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(6):
        for col in range(7):
            if board[row][col] != ' ':
                for dr, dc in directions:
                    for i in range(1, 4):
                        r, c = row + i * dr, col + i * dc
                        if r < 0 or r >= 6 or c < 0 or c >= 7 or board[r][c] != board[row][col]:
                            break
                    else:
                        return board[row][col]
    return None

def terminal(board):
    return winner(board) is not None or ' ' not in board[0]

def utility(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

def minimax(board, depth, maximizing_player):
    if depth == 0 or terminal(board):
        return None, utility(board)

    if maximizing_player:
        max_eval = float('-inf')
        best_action = None
        for action in get_possible_actions(board):
            new_board = result(board, action, 'X')
            _, eval = minimax(new_board, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_action = action
        return best_action, max_eval

    else:
        min_eval = float('inf')
        best_action = None
        for action in get_possible_actions(board):
            new_board = result(board, action, 'O')
            _, eval = minimax(new_board, depth - 1, True)
            if eval < min_eval:
                min_eval = eval
                best_action = action
        return best_action, min_eval

def play():
    board = initialize_board()
    player = input("Choose your character (X or O): ")
    ai_player = 'X' if player == 'O' else 'O'
    
    current_player = 'X' # X always starts first
    while True:
        print_board(board)
        if current_player == player:
            column = int(input(f'Player {player}, enter column (0-6): '))
        else:
            column, _ = minimax(board, 4, True)
        if column in get_possible_actions(board):
            board = result(board, column, current_player)
            if terminal(board):
                print_board(board)
                if winner(board):
                    print(f'Player {winner(board)} wins!')
                else:
                    print('It\'s a draw!')
                break
            current_player = ai_player if current_player == player else player
        else:
            print("Invalid move. Try again.")

if __name__ == '__main__':
    play()
