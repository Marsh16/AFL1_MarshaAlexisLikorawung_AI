# buat playernya
class Player:
    def __init__(self):
        self.choice = self.choose_character()

    def choose_character(self):
        while True:
            choice = input("Choose your character (X or O): ").upper()
            if choice in ['X', 'O']:
                return choice
            else:
                print('Invalid choice. Choose X or O.')

# untuk Inisialisasi papan permainan yang kosong.
def initialize_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

# untuk Cetak papan permainan ke konsol.
def print_board(state):
    for row in state:
        print('|'.join(row))
    print('-' * 13)

# untuk dapat daftar kolom yang masih dapat diisi.
def action(state):
    actions = []
    for col in range(7):
        if state[0][col] == ' ':
            actions.append(col)
    return actions

# untuk mendisplaykan/menunjukan papan baru setelah pemain melakukan tindakan di kolom tertentu.
def result(state, actions, player):
    new_board = [row[:] for row in state]
    for row in range(5, -1, -1):
        if new_board[row][actions] == ' ':
            new_board[row][actions] = player
            break
    return new_board

# Memeriksa apakah ada pemenang pada papan permainan.
def winner(state):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for row in range(6):
        for col in range(7):
            if state[row][col] != ' ':
                for dr, dc in directions:
                    for i in range(1, 4):
                        r, c = row + i * dr, col + i * dc
                        if r < 0 or r >= 6 or c < 0 or c >= 7 or state[r][c] != state[row][col]:
                            break
                    else:
                        return state[row][col]
    return None

# Memeriksa apakah permainan sudah berakhir (ada pemenang atau papan penuh).
def terminal_test(state):
    return winner(state) is not None or ' ' not in state[0]

# Mengembalikan nilai utilitas dari keadaan papan permainan.
def utility(state):
    win = winner(state)
    if win == 'X':
        return 1
    elif win == 'O':
        return -1
    else:
        return 0

# Algoritma minimax untuk mencari langkah terbaik.
def minimax(state, depth, is_maximizing):
    if depth == 0 or terminal_test(state):
        return None, utility(state)

    if is_maximizing:
        max_eval = float('-inf')
        best_action = None
        for actions in action(state):
            new_state = result(state, actions, 'X')
            _, eval = minimax(new_state, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_action = actions
        return best_action, max_eval
    else:
        min_eval = float('inf')
        best_action = None
        for actions in action(state):
            new_state = result(state, actions, 'O')
            _, eval = minimax(new_state, depth - 1, True)
            if eval < min_eval:
                min_eval = eval
                best_action = actions
        return best_action, min_eval

# Memulai permainan Connect Four, untuk pemilihan player dan pemilihan kolom yang mau diisi ada error handling 
def play():
    player = Player()
    board = initialize_board()

    ai_player = 'X' if player.choice == 'O' else 'O'
    current_player = 'X' # X always starts first
    while True:
        print_board(board)
        if current_player == player.choice:
            while True:
                try:
                    column = int(input(f'Player {player.choice}, enter column (0-6): '))
                    if column in [0,1,2,3,4,5,6]:
                        break
                    else:
                        print("Invalid input. Please enter (0-6): ")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")
        else:
            column, _ = minimax(board, 4, True)
        if column in action(board):
            board = result(board, column, current_player)
            if terminal_test(board):
                print_board(board)
                if winner(board):
                    print(f'Player {winner(board)} wins!')
                else:
                    print('It\'s a draw!')
                break
            current_player = ai_player if current_player == player.choice else player.choice
        else:
            print("Invalid move. Try again.")

#run gamenya
if __name__ == '__main__':
    play()