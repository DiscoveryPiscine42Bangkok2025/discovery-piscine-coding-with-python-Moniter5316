#check Pawn can attack King 
def can_pawn_attack(board, piece, row, col):
    if piece != "P":
        return False
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]):
            if board[r][c] == "K":
                return True
    return False

# check Rook can attack King 
def can_rook_attack(board, piece, row, col):
    if piece != "R":
        return False
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]):
            if board[r][c] == "K":
                return True
            if board[r][c] != ".":
                break  
            r += dr
            c += dc
    return False

# check Bishop can attack King 
def can_bishop_attack(board, piece, row, col):
    if piece != "B":
        return False
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]):
            if board[r][c] == "K":
                return True
            if board[r][c] != ".":
                break
            r += dr
            c += dc
    return False

# check Queen can attack King 
def can_queen_attack(board, piece, row, col):
    if piece != "Q":
        return False
    directions = [  
        (-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]# รวมแนวตรง + เฉียง
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[0]):
            if board[r][c] == "K":
                return True
            if board[r][c] != ".":
                break
            r += dr
            c += dc
    return False


def checkmate(board_str):
    
    board = [row.strip() for row in board_str.strip().splitlines() if row.strip()]

    for row_idx, row in enumerate(board):
        for col_idx, piece in enumerate(row):
            if piece in "PRBQ":  
                if (
                    can_pawn_attack(board, piece, row_idx, col_idx) or
                    can_rook_attack(board, piece, row_idx, col_idx) or
                    can_bishop_attack(board, piece, row_idx, col_idx) or
                    can_queen_attack(board, piece, row_idx, col_idx)
                ):
                    print("Success")
                    return True

    print("Fail")
    return False
