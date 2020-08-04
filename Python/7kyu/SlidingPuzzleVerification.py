#Sliding Puzzle Verification
#https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc

def is_solved(board):
    total = []
    board_length = len(board)
    for i in range(board_length):
        total += board[i]

    for idx, val in enumerate(total):
        if idx != val:
            return False

    return True
