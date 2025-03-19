import time
import pygame
import sys
import config
import random
import hard
from button import Button

# 人机对战游戏循环
def vs_ai_game_loop():
    #全局变量
    global board_state, move_history, button_able, if_menu, difficulty,cover_layer_rec_rect,cover_layer_rec,keep_text, cover_board_rect, cover_board
    #字体设置
    font_game = pygame.font.Font(config.font_path, config.FONT_SIZE_GAME_BOARD)
    pygame.init()
    reset_board()
    screen = pygame.display.set_mode((config.GAME_WIDTH, config.GAME_HEIGHT))
    pygame.display.set_caption("人机对战中")
    # 创建难度选择窗口
    difficulty_window = pygame.Surface((300, 200))
    difficulty_window.fill(config.BOARD_COLOR)
    # 创建难度选择按钮
    diffcult_buttons = [Button.from_config(info) for info in config.GAME_DIF_BBUTTONS_INFO]
    # 绘制难度选择界面
    screen.fill(config.BOARD_COLOR)
    chose_text = font_game.render(f"选择难度", True, config.BLACK)
    chose_rect=chose_text.get_rect(center=(config.GAME_WIDTH // 2 , config.GAME_HEIGHT // 2 - 100 ))
    screen.blit(chose_text, chose_rect)
    #绘制按钮
    for button in diffcult_buttons:
        button.draw(screen)
    pygame.display.flip()
    #难度判断
    difficulty = None
    while difficulty is None:
        for event in pygame.event.get():
            for button in diffcult_buttons:
                result = button.handle_event(event)
                if result == "1":
                    difficulty = 1
                elif result == "2":
                    difficulty = 2
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for button in diffcult_buttons:
            button.draw(screen)
        pygame.display.flip()
    # 根据选择的难度设置相应的AI落子函数
    if difficulty == 1:
        ai_move_function = ai_move
    elif difficulty == 2:
        ai_move_function = hard_ai_move
    # 清除难度选择界面
    screen.fill(config.BOARD_COLOR)
 
    #绘制棋盘
    draw_board(screen)
    # 创建悔棋按钮
    buttons = [Button.from_config(info) for info in config.UNDO_BUTTON_INFO]
    for undo_button in buttons:
        undo_button.draw(screen)
    button_able = True
    # 初始回合为ai
    turn = 2
    # 现在玩家
    current_player = 1 
    #显示文本信息
    text = "玩家" 
    Keep_text = font_game.render(f"{text}的回合", True, config.BLACK)
    Keep_rect = Keep_text.get_rect(center=(298, 613))
    screen.blit(Keep_text, Keep_rect)
    pygame.display.update(Keep_rect)
    #覆盖文本，和双人对战一致
    x = Keep_rect.x
    y = Keep_rect.y
    width = Keep_rect.width
    height = Keep_rect.height
    cover_layer_rec = pygame.Surface((width, height))
    cover_layer_rec.fill(config.BOARD_COLOR)
    cover_layer_rec_rect = cover_layer_rec.get_rect(topleft=(x, y))
    cover_board = pygame.Surface((config.BOARD_SIZE * config.GRID_SIZE + 40, config.BOARD_SIZE * config.GRID_SIZE + 20))
    cover_board.fill(config.BOARD_COLOR)
    cover_board_rect = cover_board.get_rect(topleft=(0, 0))

    def keep_text(turn):
        text = "玩家" if turn == 1 else "人机"
        Keep_text = font_game.render(f"{text}的回合", True, config.BLACK)
        Keep_rect = Keep_text.get_rect(center=(298, 613))
        screen.blit(Keep_text, Keep_rect)
        pygame.display.update(Keep_rect)

    #更新棋盘
    pygame.display.flip()
    while True:
        #获取事件
        for event in pygame.event.get():
                #按钮事件
                for undo_button in buttons:
                    button_clicked_value = undo_button.handle_event(event)
                    #悔棋判断
                    if (button_able == True and button_clicked_value == "悔棋" and
                        current_player == 1 and board_state!= [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]):
                        #和双人对战相同操作
                        screen.blit(cover_board, cover_board_rect)
                        draw_board(screen)
                        pygame.display.update(cover_board_rect)
                        for i in range(len(move_history)):
                            for j in range(len(move_history[i])):
                                value = move_history[i][j]
                                if value == 1:
                                    draw_stone(screen, i, j, config.BLACK)
                                elif value == 2:
                                    draw_stone(screen, i, j, config.WHITE)
                        pygame.display.update(cover_board_rect)
                        #悔棋结束还是玩家回合
                        turn = 1
                        board_state = [row[:] for row in move_history]
                        button_able = False
                    #点击主菜单   
                    elif (button_clicked_value == "main_menu"):
                        if_menu = True
                #退出
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #玩家点击
                elif event.type == pygame.MOUSEBUTTONDOWN and turn == 1:

                    screen.blit(cover_layer_rec, cover_layer_rec_rect)
                    pygame.display.update(cover_layer_rec_rect)

                    x, y = event.pos
                    adjusted_x = x - config.MARGIN_SIZE
                    adjusted_y = y - config.MARGIN_SIZE
                    row = round(adjusted_y / config.GRID_SIZE)
                    col = round(adjusted_x / config.GRID_SIZE)

                    if (if_menu == True):
                        return
                    
                    if 0 <= row < config.BOARD_SIZE and 0 <= col < config.BOARD_SIZE and board_state[row][col] == 0:
                        button_able = True
                        move_history = [row[:] for row in board_state]
                        if turn == 1:
                            board_state[row][col] = 1
                            move_history[row][col] = 0
                            draw_stone(screen, row, col, config.BLACK)
                            pygame.display.update(cover_board_rect)
                            turn = 2
                            config.DROP_SOUND.play()
                        else:
                            board_state[row][col] = 2
                            move_history[row][col] = 0
                            draw_stone(screen, row, col, config.WHITE)
                            pygame.display.update(cover_board_rect)
                            turn = 1
                            config.DROP_SOUND.play()
                        if check_win_around(row, col):
                            time.sleep(1)
                            return "玩家"
                    screen.blit(cover_layer_rec, cover_layer_rec_rect)
                    keep_text(turn)
                    pygame.display.update(cover_board_rect)

                if turn == 2 :  # AI回合开始
                    turn = 1
                    result=ai_move_function(screen)
                    if(result==2):
                        time.sleep(1)
                        return "人机"
                    screen.blit(cover_layer_rec, cover_layer_rec_rect)
                    keep_text(turn) 
                    pygame.display.update(cover_board_rect)

        for undo_button in buttons:
            undo_button.draw(screen)
        pygame.display.update()

# 入门ai（随机落子）
def ai_move(screen):
    global board_state, turn 

    while True:
        #随机挑选空白位置
        row = random.randint(0, config.BOARD_SIZE - 1)
        col = random.randint(0, config.BOARD_SIZE - 1)
        while board_state[row][col] != 0:
            row = random.randint(0, config.BOARD_SIZE - 1)
            col = random.randint(0, config.BOARD_SIZE - 1)
        board_state[row][col] = 2
        time.sleep(0.5)
        draw_stone(screen, row, col, config.WHITE)
        pygame.display.update(cover_board_rect)
        config.DROP_SOUND.play()
        turn = 1  # 更新回合数为玩家回合
        result = check_win_around(row, col)
        if result=="白":
            return 2
        break

def hard_ai_move(screen):
    global board_state, turn  

    while True:
        best_move = hard.find_best_move(board_state,2)
        row = best_move[0] 
        col = best_move[1] 
        if board_state[row][col] == 0:
            board_state[row][col] = 2
        draw_stone(screen, row, col, config.WHITE)
        pygame.display.update(cover_board_rect)
        config.DROP_SOUND.play()
        turn = 1  # 更新回合数为玩家回合
        result = check_win_around(row, col)
        if result=="白":
            return 2
        break

# 检查胜利函数（与双人对战中的相同）
def check_win_around(row, col):
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    check_range = 5
    stone = board_state[row][col]
    for direction in directions:
        count = 1
        for i in range(1, check_range):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if 0 <= new_row < config.BOARD_SIZE and 0 <= new_col < config.BOARD_SIZE and board_state[new_row][new_col] == stone:
                count += 1
            else:
                break
        for i in range(1, check_range):
            new_row = row - i * direction[0]
            new_col = col - i * direction[1]
            if 0 <= new_row < config.BOARD_SIZE and 0 <= new_col < config.BOARD_SIZE and board_state[new_row][new_col] == stone:
                count += 1
            else:
                break
        if count >= 5:
            return "黑" if stone == 1 else "白"
    if all(all(cell!= 0 for cell in row) for row in board_state):
        return "平局"
    return False

# 绘制棋子函数（与双人对战中的相同）
def draw_stone(screen, row, col, color):
    center_x = config.MARGIN_SIZE + col * config.GRID_SIZE
    center_y = config.MARGIN_SIZE + row * config.GRID_SIZE
    pygame.draw.circle(screen, color, (center_x, center_y), config.GRID_SIZE // 2 - 12)

# 绘制棋盘函数（与双人对战中的相同）
def draw_board(screen):
    screen.fill(config.BOARD_COLOR)
    start_x = config.MARGIN_SIZE
    start_y = config.MARGIN_SIZE
    board_width = config.BOARD_SIZE * config.GRID_SIZE
    board_height = config.BOARD_SIZE * config.GRID_SIZE
    pygame.draw.rect(screen, config.BOARD_COLOR, (start_x, start_y, board_width, board_height))
    for i in range(config.BOARD_SIZE):
        pygame.draw.line(screen, config.BLACK, (start_x, start_y + i * config.GRID_SIZE), (start_x + board_width - config.GRID_SIZE, start_y + i * config.GRID_SIZE))
        pygame.draw.line(screen, config.BLACK, (start_x + i * config.GRID_SIZE, start_y), (start_x + i * config.GRID_SIZE, start_y + board_height - config.GRID_SIZE))
    tianyuan_row = config.BOARD_SIZE // 2
    tianyuan_col = config.BOARD_SIZE // 2
    draw_stone(screen, tianyuan_row, tianyuan_col, config.GRAY)
    left_top_row = 3
    left_top_col = 3
    draw_stone(screen, left_top_row, left_top_col, config.GRAY)
    right_top_row = 3
    right_top_col = config.BOARD_SIZE - 4
    draw_stone(screen, right_top_row, right_top_col, config.GRAY)
    left_bottom_row = config.BOARD_SIZE - 4
    left_bottom_col = 3
    draw_stone(screen, left_bottom_row, left_bottom_col, config.GRAY)
    right_bottom_row = config.BOARD_SIZE - 4
    right_bottom_col = config.BOARD_SIZE - 4
    draw_stone(screen, right_bottom_row, right_bottom_col, config.GRAY)

# 重置棋盘函数（新加难度）
def reset_board():
    global board_state, move_history, if_menu,difficulty
    if_menu = False
    difficulty = None
    move_history = [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]
    board_state = [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]