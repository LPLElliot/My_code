import numpy as np
from pygame.locals import *
import config
death = 0
death_one = 0
open_one = 0
death_two = 0    
open_two = 0
death_three = 0
open_three = 0
death_four = 0
open_four = 0
win = 0
# 定义棋盘大小和玩家标识
# 棋盘状态，使用二维列表表示，0表示空，1表示黑子，2表示白子
# 这里创建一个二维列表来模拟棋盘，每个元素代表棋盘上的一个格子
BOARD_SIZE = 15
board_state = [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]
# 存储每一步棋的信息，这里可以记录下棋的顺序和位置等信息，初始为空列表
move_history = []
# 黑子胜利次数，初始化为0
black_wins = 0
# 白子胜利次数，初始化为0
white_wins = 0
EMPTY = 0
BLACK = 1
WHITE = 2
# 检查是否有玩家获胜
def check_win(board, player):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == player:
                if find_horizontal(board, row, col, player) or find_vertical(board, row, col, player) or find_positive_diagonal(board, row, col, player) or find_negative_diagonal:
                    return True
    return False
def evaluate(board, player):
    score = 0
    opponent = player % 2 +1
    global death 
    global death_one 
    global open_one 
    global death_two   
    global open_two 
    global death_three 
    global open_three 
    global death_four 
    global open_four 
    global win 
    for row in range(BOARD_SIZE - 1):
        for col in range(BOARD_SIZE - 1):
            find_horizontal(board, row, col, player)
            find_vertical(board, row, col, player)
            find_positive_diagonal(board, row, col, player)
            find_negative_diagonal(board, row, col, player)
    score = death_one*1+open_one*3+death_two*10+open_two*40+death_three*100+open_three*1000+death_four*500 +open_four*5000+ win*25000000
    death = 0
    death_one = 0
    open_one = 0
    death_two = 0    
    open_two = 0
    death_three = 0
    open_three = 0
    death_four = 0
    open_four = 0
    win = 0
    for row in range(BOARD_SIZE - 1):
        for col in range(BOARD_SIZE - 1):
            find_horizontal(board, row, col, opponent)
            find_vertical(board, row, col, opponent)
            find_positive_diagonal(board, row, col, opponent)
            find_negative_diagonal(board, row, col, opponent)
    score = score+1+death-(death_one+open_one*3+death_two*10+open_two*40+death_three*100+open_three*3000+death_four*3000+open_four*10000+win*100000)
    return score

# 极大极小搜索算法
def minimax(board, depth, is_maximizing_player, player):
    if depth == 0 or check_win(board, BLACK) or check_win(board, WHITE):
        return evaluate(board, player)
    if is_maximizing_player:
        max_eval = -np.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = player
                    eval = minimax(board, depth - 1, False, player % 2 + 1)
                    board[row][col] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = np.inf
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = player%2+1
                    eval = minimax(board, depth - 1, True, player % 2 + 1)
                    board[row][col] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# 选择最佳落子位置
def find_best_move(board, player):
    best_score = -np.inf
    best_move = None
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = player
                score = minimax(board, 10, False, player)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move
def find_horizontal(board, row, col, player):
    count = 0
    empty_count = 0
    global death 
    global death_one 
    global open_one 
    global death_two   
    global open_two 
    global death_three 
    global open_three 
    global death_four 
    global open_four 
    global win 
    a = 0
    for i in range(max(0, col - 5), min(BOARD_SIZE, col + 6)):
        if board[row][i] == player:
            count += 1
        elif count > 0 and board[row][i] == EMPTY:
            empty_count += 1
            if empty_count > 1:
                count = 0
                empty_count = 0
        else:
            count = 0
            empty_count = 0
        match count:
            case 1:
                if i == 0:
                    if board[row][i+1] == player % 2 + 1:
                        death +=1
                    elif board[row][i+1] == 0:
                        death_one = death_one + 1
                elif i == 14:
                    if board[row][i-1] == player % 2 + 1:
                        death +=1
                    elif board[row][i-1] == 0:
                        death_one +=1
                else:
                    if board[row][i+1] == player % 2 + 1 and board[row][i-1] == player % 2 + 1:
                        death +=1
                    elif board[row][i+1] == 0 and board[row][i+1] == 0:
                        open_one +=1
                    elif board[row][i+1] == 0 and board[row][i-1] == player % 2 + 1 or board[row][i+1] == player % 2 + 1 and board[row][i+1] == 0:
                        death_one +=1
            case 2:
                if empty_count == 1:
                    if i == 2:
                        if board[row][i+1] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == 0:
                            death_two +=1
                    elif i == 12:
                        if board[row][i-3] == player % 2 + 1:
                            death +=1
                        elif board[row][i-3] == 0:
                            death_two +=1
                    else:
                        if  board[row][i+1] == player % 2 + 1 and board[row][i-3] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == player % 2 + 1 and board[row][i-3] == 0 or board[row][i+1] == 0 and board[row][i-3] == player % 2 + 1:
                            death_two +=1
                        elif board[row][i+1] == 0 and board[row][i-3] == 0:
                            open_two +=1
                else:
                    if i == 1:
                        if board[row][i+1] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == 0:
                            death_two +=1
                    elif i == 13:
                        if board[row][i-2] == player % 2 + 1:
                            death +=1
                        elif board[row][i-2] == 0:
                            death_two +=1
                    else:
                        if  board[row][i+1] == player % 2 + 1 and board[row][i-2] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == player % 2 + 1 and board[row][i-2] == 0 or board[row][i+1] == 0 and board[row][i-2] == player % 2 + 1:
                            death_two +=1
                        elif board[row][i+1] == 0 and board[row][i-2] == 0:
                            open_two +=1
            case 3:
                if empty_count == 1:
                    if i == 3:
                        if board[row][i+1] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == 0:
                            death_three +=1
                    elif i == 11:
                        if board[row][i-4] == player % 2 + 1:
                            death +=1
                        elif board[row][i-4] == 0:
                            death_three +=1
                    else:
                        if  board[row][i+1] == player % 2 + 1 and board[row][i-4] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == player % 2 + 1 and board[row][i-4] == 0 or board[row][i+1] == 0 and board[row][i-4] == player % 2 + 1:
                            death_three +=1
                        elif board[row][i+1] == 0 and board[row][i-4] == 0:
                            open_three +=1
                else:
                    if i == 2:
                        if board[row][i+1] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == 0:
                            death_three +=1
                    elif i == 12:
                        if board[row][i-3] == player % 2 + 1:
                            death +=1
                        elif board[row][i-3] == 0:
                            death_three +=1
                    else:
                        if  board[row][i+1] == player % 2 + 1 and board[row][i-3] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == player % 2 + 1 and board[row][i-3] == 0 or board[row][i+1] == 0 and board[row][i-3] == player % 2 + 1:
                            death_three +=1
                        elif board[row][i+1] == 0 and board[row][i-3] == 0:
                            open_three +=1
            case 4:
                if empty_count == 1:
                    death_four +=1
                else:
                    if i == 3:
                        if board[row][i+1] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == 0:
                            death_four +=1
                    elif i == 12:
                        if board[row][i-4] == player % 2 + 1:
                            death +=1
                        elif board[row][i-4] == 0:
                            death_four +=1
                    else:
                        if  board[row][i+1] == player % 2 + 1 and board[row][i-4] == player % 2 + 1:
                            death +=1
                        elif board[row][i+1] == player % 2 + 1 and board[row][i-4] == 0 or board[row][i+1] == 0 and board[row][i-4] == player % 2 + 1:
                            death_four +=1
                        elif board[row][i+1] == 0 and board[row][i-4] == 0:
                            open_four +=1
            case 5:
                if empty_count == 1:
                    death_four +=1
                else:
                    win +=1
            case _:
                a = 0
    
    return win

def find_vertical(board, row, col, player):
    count = 0
    empty_count = 0
    global death 
    global death_one 
    global open_one 
    global death_two   
    global open_two 
    global death_three 
    global open_three 
    global death_four 
    global open_four 
    global win 
    a=0
    for i in range(max(0, row - 5), min(BOARD_SIZE, row + 5)):
        if board[i][col] == player:
            count += 1
        elif count > 0 and board[i][col] == EMPTY:
            empty_count += 1
            if empty_count > 1:
                count = 0
                empty_count = 0
        else:
            count = 0
            empty_count = 0
        match count:
            case 1:
                if i == 0:
                    if board[i + 1][col] == player % 2 + 1:
                        death += 1
                    elif board[i + 1][col] == 0:
                        death_one += 1
                elif i == 14:
                    if board[i - 1][col] == player % 2 + 1:
                        death += 1
                    elif board[i - 1][col] == 0:
                        death_one += 1
                else:
                    if board[i + 1][col] == player % 2 + 1 and board[i - 1][col] == player % 2 + 1:
                        death += 1
                    elif board[i + 1][col] == 0 and board[i + 1][col] == 0:
                        open_one += 1
                    elif board[i + 1][col] == 0 and board[i - 1][col] == player % 2 + 1 or board[i + 1][col] == player % 2 + 1 and board[i + 1][col] == 0:
                        death_one += 1
            case 2:
                if empty_count == 1:
                    if i == 2:
                        if board[i + 1][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == 0:
                            death_two += 1
                    elif i == 12:
                        if board[i - 3][col] == player % 2 + 1:
                            death += 1
                        elif board[i - 3][col] == 0:
                            death_two += 1
                    else:
                        if board[i + 1][col] == player % 2 + 1 and board[i - 3][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == player % 2 + 1 and board[i - 3][col] == 0 or board[i + 1][col] == 0 and board[i - 3][col] == player % 2 + 1:
                            death_two += 1
                        elif board[i + 1][col] == 0 and board[i - 3][col] == 0:
                            open_two += 1
                else:
                    if i == 1:
                        if board[i + 1][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == 0:
                            death_two += 1
                    elif i == 13:
                        if board[i - 2][col] == player % 2 + 1:
                            death += 1
                        elif board[i - 2][col] == 0:
                            death_two += 1
                    else:
                        if board[i + 1][col] == player % 2 + 1 and board[i - 2][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == player % 2 + 1 and board[i - 2][col] == 0 or board[i + 1][col] == 0 and board[i - 2][col] == player % 2 + 1:
                            death_two += 1
                        elif board[i + 1][col] == 0 and board[i - 2][col] == 0:
                            open_two += 1
            case 3:
                if empty_count == 1:
                    if i == 3:
                        if board[i + 1][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == 0:
                            death_three += 1
                    elif i == 11:
                        if board[i - 4][col] == player % 2 + 1:
                            death += 1
                        elif board[i - 4][col] == 0:
                            death_three += 1
                    else:
                        if board[i + 1][col] == player % 2 + 1 and board[i - 4][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == player % 2 + 1 and board[i - 4][col] == 0 or board[i + 1][col] == 0 and board[i - 4][col] == player % 2 + 1:
                            death_three += 1
                        elif board[i + 1][col] == 0 and board[i - 4][col] == 0:
                            open_three += 1
                else:
                    if i == 2:
                        if board[i + 1][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == 0:
                            death_three += 1
                    elif i == 12:
                        if board[i - 3][col] == player % 2 + 1:
                            death += 1
                        elif board[i - 3][col] == 0:
                            death_three += 1
                    else:
                        if board[i + 1][col] == player % 2 + 1 and board[i - 3][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == player % 2 + 1 and board[i - 3][col] == 0 or board[i + 1][col] == 0 and board[i - 3][col] == player % 2 + 1:
                            death_three += 1
                        elif board[i + 1][col] == 0 and board[i - 3][col] == 0:
                            open_three += 1
            case 4:
                if empty_count == 1:
                    death_four += 1
                else:
                    if i == 3:
                        if board[i + 1][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == 0:
                            death_four += 1
                    elif i == 12:
                        if board[i - 4][col] == player % 2 + 1:
                            death += 1
                        elif board[i - 4][col] == 0:
                            death_four += 1
                    else:
                        if board[i + 1][col] == player % 2 + 1 and board[i - 4][col] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][col] == player % 2 + 1 and board[i - 4][col] == 0 or board[i + 1][col] == 0 and board[i - 4][col] == player % 2 + 1:
                            death_four += 1
                        elif board[i + 1][col] == 0 and board[i - 4][col] == 0:
                            open_four += 1
            case 5:
                if empty_count == 1:
                    death_four += 1
                else:
                    win +=1
            case _:
                a = 0
    return win
def find_positive_diagonal(board, row, col, player):
    count = 0
    empty_count = 0
    global death 
    global death_one 
    global open_one 
    global death_two   
    global open_two 
    global death_three 
    global open_three 
    global death_four 
    global open_four 
    global win 
    a=0
    for i, j in zip(range(max(0, row - 5), min(BOARD_SIZE, row + 5)), range(max(0, col - 5), min(BOARD_SIZE, col + 5))):
        if board[i][j] == player:
            count += 1
        elif count > 0 and board[i][j] == EMPTY:
            empty_count += 1
            if empty_count > 1:
                count = 0
                empty_count = 0
        else:
            count = 0
            empty_count = 0
        match count:
            case 1:
                if i == 0 or j == 0:
                    if board[i + 1][j + 1] == player % 2 + 1:
                        death += 1
                    elif board[i + 1][j + 1] == 0:
                        death_one += 1
                elif i == 14 or j == 14:
                    if board[i - 1][j - 1] == player % 2 + 1:
                        death += 1
                    elif board[i - 1][j - 1] == 0:
                        death_one += 1
                else:
                    if board[i + 1][j + 1] == player % 2 + 1 and board[i - 1][j - 1] == player % 2 + 1:
                        death += 1
                    elif board[i + 1][j + 1] == 0 and board[i + 1][j + 1] == 0:
                        open_one += 1
                    elif board[i + 1][j + 1] == 0 and board[i - 1][j - 1] == player % 2 + 1 or board[i + 1][j + 1] == player % 2 + 1 and board[i + 1][j + 1] == 0:
                        death_one += 1
            case 2:
                if empty_count == 1:
                    if i == 2 or j == 2:
                        if board[i + 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == 0:
                            death_two += 1
                    elif i == 12 or j == 12:
                        if board[i - 3][j - 3] == player % 2 + 1:
                            death += 1
                        elif board[i - 3][j - 3] == 0:
                            death_two += 1
                    else:
                        if board[i + 1][j + 1] == player % 2 + 1 and board[i - 3][j - 3] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == player % 2 + 1 and board[i - 3][j - 3] == 0 or board[i + 1][j + 1] == 0 and board[i - 3][j - 3] == player % 2 + 1:
                            death_two += 1
                        elif board[i + 1][j + 1] == 0 and board[i - 3][j - 3] == 0:
                            open_two += 1
                else:
                    if i == 1 or j == 1:
                        if board[i + 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == 0:
                            death_two += 1
                    elif i == 13 or j == 13:
                        if board[i - 2][j - 2] == player % 2 + 1:
                            death += 1
                        elif board[i - 2][j - 2] == 0:
                            death_two += 1
                    else:
                        if board[i + 1][j + 1] == player % 2 + 1 and board[i - 2][j - 2] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == player % 2 + 1 and board[i - 2][j - 2] == 0 or board[i + 1][j + 1] == 0 and board[i - 2][j - 2] == player % 2 + 1:
                            death_two += 1
                        elif board[i + 1][j + 1] == 0 and board[i - 2][j - 2] == 0:
                            open_two += 1
            case 3:
                if empty_count == 1:
                    if i == 3 or j == 3:
                        if board[i + 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == 0:
                            death_three += 1
                    elif i == 11 or j == 11:
                        if board[i - 4][j - 4] == player % 2 + 1:
                            death += 1
                        elif board[i - 4][j - 4] == 0:
                            death_three += 1
                    else:
                        if board[i + 1][j + 1] == player % 2 + 1 and board[i - 4][j - 4] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == player % 2 + 1 and board[i - 4][j - 4] == 0 or board[i + 1][j + 1] == 0 and board[i - 4][j - 4] == player % 2 + 1:
                            death_three += 1
                        elif board[i + 1][j + 1] == 0 and board[i - 4][j - 4] == 0:
                            open_three += 1
                else:
                    if i == 2 or j == 2:
                        if board[i + 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == 0:
                            death_three += 1
                    elif i == 12 or j == 12:
                        if board[i - 3][j - 3] == player % 2 + 1:
                            death += 1
                        elif board[i - 3][j - 3] == 0:
                            death_three += 1
                    else:
                        if board[i + 1][j + 1] == player % 2 + 1 and board[i - 3][j - 3] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == player % 2 + 1 and board[i - 3][j - 3] == 0 or board[i + 1][j + 1] == 0 and board[i - 3][j - 3] == player % 2 + 1:
                            death_three += 1
                        elif board[i + 1][j + 1] == 0 and board[i - 3][j - 3] == 0:
                            open_three += 1
            case 4:
                if empty_count == 1:
                    death_four += 1
                else:
                    if i == 3 or j == 3:
                        if board[i + 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == 0:
                            death_four += 1
                    elif i == 12 or j == 12:
                        if board[i - 4][j - 4] == player % 2 + 1:
                            death += 1
                        elif board[i - 4][j - 4] == 0:
                            death_four += 1
                    else:
                        if board[i + 1][j + 1] == player % 2 + 1 and board[i - 4][j - 4] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j + 1] == player % 2 + 1 and board[i - 4][j - 4] == 0 or board[i + 1][j + 1] == 0 and board[i - 4][j - 4] == player % 2 + 1:
                            death_four += 1
                        elif board[i + 1][j + 1] == 0 and board[i - 4][j - 4] == 0:
                            open_four += 1
            case 5:
                if empty_count == 1:
                    death_four += 1
                else:
                    win += 1
            case _:
                a = 0
    return win
def find_negative_diagonal(board, row, col, player):
    count = 0
    empty_count = 0
    global death 
    global death_one 
    global open_one 
    global death_two   
    global open_two 
    global death_three 
    global open_three 
    global death_four 
    global open_four 
    global win 
    a=0
    for i, j in zip(range(min(BOARD_SIZE-1, row + 5), max(0, row - 5), -1), range(max(0, col - 5), min(BOARD_SIZE, col + 5))):
        if board[i][j] == player:
            count += 1
        elif count > 0 and board[i][j] == EMPTY:
            empty_count += 1
            if empty_count > 1:
                count = 0
                empty_count = 0
        else:
            count = 0
            empty_count = 0
        match count:
            case 1:
                if i == BOARD_SIZE - 1 or j == 0:
                    if board[i - 1][j + 1] == player % 2 + 1:
                        death += 1
                    elif board[i - 1][j + 1] == 0:
                        death_one += 1
                elif i == 0 or j == 14:
                    if board[i + 1][j - 1] == player % 2 + 1:
                        death += 1
                    elif board[i + 1][j - 1] == 0:
                        death_one += 1
                else:
                    if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                        death += 1
                    elif board[i - 1][j + 1] == 0 and board[i - 1][j + 1] == 0:
                        open_one += 1
                    elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1 or board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0:
                        death_one += 1
            case 2:
                if empty_count == 1:
                    if i == BOARD_SIZE - 3 or j == 2:
                        if board[i - 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == 0:
                            death_two += 1
                    elif i == 2 or j == 12:
                        if board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j - 1] == 0:
                            death_two += 1
                    else:
                        if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0 or board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1:
                            death_two += 1
                        elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0:
                            open_two += 1
                else:
                    if i == BOARD_SIZE - 2 or j == 1:
                        if board[i - 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == 0:
                            death_two += 1
                    elif i == 3 or j == 13:
                        if board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j - 1] == 0:
                            death_two += 1
                    else:
                        if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0 or board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1:
                            death_two += 1
                        elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0:
                            open_two += 1
            case 3:
                if empty_count == 1:
                    if i == BOARD_SIZE - 4 or j == 3:
                        if board[i - 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == 0:
                            death_three += 1
                    elif i == 3 or j == 11:
                        if board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j - 1] == 0:
                            death_three += 1
                    else:
                        if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0 or board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1:
                            death_three += 1
                        elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0:
                            open_three += 1
                else:
                    if i == BOARD_SIZE - 3 or j == 2:
                        if board[i - 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == 0:
                            death_three += 1
                    elif i == 4 or j == 12:
                        if board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j - 1] == 0:
                            death_three += 1
                    else:
                        if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0 or board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1:
                            death_three += 1
                        elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0:
                            open_three += 1
            case 4:
                if empty_count == 1:
                    death_four += 1
                else:
                    if i == BOARD_SIZE - 4 or j == 3:
                        if board[i - 1][j + 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == 0:
                            death_four += 1
                    elif i == 4 or j == 12:
                        if board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i + 1][j - 1] == 0:
                            death_four += 1
                    else:
                        if board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == player % 2 + 1:
                            death += 1
                        elif board[i - 1][j + 1] == player % 2 + 1 and board[i + 1][j - 1] == 0 or board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == player % 2 + 1:
                            death_four += 1
                        elif board[i - 1][j + 1] == 0 and board[i + 1][j - 1] == 0:
                            open_four += 1
            case 5:
                if empty_count == 1:
                    death_four += 1
                else:
                    win += 1
            case _:
                a = 0   
    return win
