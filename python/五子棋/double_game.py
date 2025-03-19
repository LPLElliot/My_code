import sys
import time
import pygame
from pygame.locals import *
import config
from button import Button

#判断是否返回主界面参数
global if_menu
if_menu = False

# 检查新落子位置周围是否有五子连珠的，同时判断是否平局
def check_win_around(row, col):
    #棋子周围的四个位置
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

    # 检查棋盘是否已满（没有空位置）
    if all(all(cell!= 0 for cell in row) for row in board_state):
        return "平局"

    return False

# 绘制棋子的函数，在指定的屏幕位置绘制指定颜色的棋子
def draw_stone(screen, row, col, color):
    #中心坐标
    center_x = config.MARGIN_SIZE + col * config.GRID_SIZE
    center_y = config.MARGIN_SIZE + row * config.GRID_SIZE
    #绘制
    pygame.draw.circle(screen, color, (center_x, center_y), config.GRID_SIZE // 2 - 12)

# 绘制棋盘的函数
def draw_board(screen):
    #背景填充
    screen.fill(config.BOARD_COLOR)

    start_x = config.MARGIN_SIZE
    start_y = config.MARGIN_SIZE

    board_width = config.BOARD_SIZE * config.GRID_SIZE
    board_height = config.BOARD_SIZE * config.GRID_SIZE
    pygame.draw.rect(screen, config.BOARD_COLOR, (start_x, start_y, board_width, board_height))

    # 绘制横竖线
    for i in range(config.BOARD_SIZE):
        # 横向划线
        pygame.draw.line(screen, config.BLACK, (start_x, start_y + i * config.GRID_SIZE), (start_x + board_width - config.GRID_SIZE, start_y + i * config.GRID_SIZE))
        # 纵向划线
        pygame.draw.line(screen, config.BLACK, (start_x + i * config.GRID_SIZE, start_y), (start_x + i * config.GRID_SIZE, start_y + board_height - config.GRID_SIZE))

    # 绘制天元（棋盘正中心）
    tianyuan_row = config.BOARD_SIZE // 2
    tianyuan_col = config.BOARD_SIZE // 2
    draw_stone(screen, tianyuan_row, tianyuan_col, config.GRAY)
    # 绘制左上角星位
    left_top_row = 3  # 第4条线，索引从0开始，所以是3
    left_top_col = 3
    draw_stone(screen, left_top_row, left_top_col, config.GRAY)
    # 绘制右上角星位
    right_top_row = 3
    right_top_col = config.BOARD_SIZE - 4  # 第12条线，索引从0开始，所以是BOARD_SIZE - 4
    draw_stone(screen, right_top_row, right_top_col, config.GRAY)
    # 绘制左下角星位
    left_bottom_row = config.BOARD_SIZE - 4
    left_bottom_col = 3
    draw_stone(screen, left_bottom_row, left_bottom_col, config.GRAY)
    # 绘制右下角星位
    right_bottom_row = config.BOARD_SIZE - 4
    right_bottom_col = config.BOARD_SIZE - 4
    draw_stone(screen, right_bottom_row, right_bottom_col, config.GRAY)

# 重置棋盘状态的函数，将整个棋盘状态设置为空（0）
def reset_board():
    global board_state, move_history,if_menu
    if_menu = False
    move_history = [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]
    board_state = [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]

#主函数
def double_game_loop():
    #棋盘状态，上次棋盘状态，按钮状态，主菜单状态
    global board_state, move_history, button_able,if_menu

    pygame.init()
    reset_board()

    screen = pygame.display.set_mode((config.GAME_WIDTH, config.GAME_HEIGHT))
    pygame.display.set_caption("双人对战中")

    # 初始回合为黑棋
    turn = 1
    # 绘制棋盘
    draw_board(screen)
    # 创建悔棋按钮
    buttons = [Button.from_config(info) for info in config.UNDO_BUTTON_INFO]
    for undo_button in buttons:
        undo_button.draw(screen)
    button_able=True
    #初始化显示文本
    font_game = pygame.font.Font(config.font_path, config.FONT_SIZE_GAME_BOARD)
    #黑棋先手
    text = "黑"
    Keep_text = font_game.render(f"{text}棋回合", True, config.BLACK)
    #判定区域
    Keep_rect = Keep_text.get_rect(center=(298, 613))
    #显示
    screen.blit(Keep_text, Keep_rect)
    pygame.display.update(Keep_rect)
    # 获取Keep_rect的左上角x坐标
    x = Keep_rect.x
    # 获取Keep_rect的左上角y坐标
    y = Keep_rect.y
    # 获取Keep_rect的宽度
    width = Keep_rect.width
    # 获取Keep_rect的高度
    height = Keep_rect.height
    #覆盖文本的参数
    cover_layer_rec = pygame.Surface((width, height))
    cover_layer_rec.fill(config.BOARD_COLOR)
    cover_layer_rec_rect = cover_layer_rec.get_rect(topleft=(x, y))
    #覆盖棋盘的参数
    cover_board = pygame.Surface((config.BOARD_SIZE * config.GRID_SIZE + 40, config.BOARD_SIZE * config.GRID_SIZE + 20))
    cover_board.fill(config.BOARD_COLOR)  # 填充为棋盘颜色
    cover_board_rect = cover_board.get_rect(topleft=(0, 0))
    #更新文本函数
    def keep_text(turn):
        text = "黑"
        if turn == 2:
            text = "白"
        Keep_text = font_game.render(f"{text}棋回合", True, config.BLACK)
        Keep_rect = Keep_text.get_rect(center=(298, 613))
        screen.blit(Keep_text, Keep_rect)
        pygame.display.update(Keep_rect)

    #刷新状态
    pygame.display.flip()

    while True:
        #循环判断事件
        for event in pygame.event.get():
            #按钮事件判断
            for undo_button in buttons:
                button_clicked_value = undo_button.handle_event(event)
                #点击悔棋并且按钮可用并且棋盘上有棋子
                if (button_able == True and button_clicked_value == "悔棋" and board_state!= [[0] * config.BOARD_SIZE for _ in range(config.BOARD_SIZE)]):
                    # 先覆盖之前的棋盘
                    screen.blit(cover_board, cover_board_rect)
                    # 绘制棋盘
                    draw_board(screen)
                    pygame.display.update(cover_board_rect)
                    # 根据记录的数组绘制棋子
                    for i in range(len(move_history)):
                        for j in range(len(move_history[i])):
                            value = move_history[i][j]
                            if value == 1:
                                draw_stone(screen, i, j, config.BLACK)
                            elif value == 2:
                                draw_stone(screen, i, j, config.WHITE)
                    pygame.display.update(cover_board_rect)
                    #玩家更新
                    if (turn == 1):
                        turn = 2
                    else:
                        turn = 1
                    #棋盘更新
                    board_state = [row[:] for row in move_history]
                    #重置按钮
                    button_able = False
                #点击返回主菜单
                elif(button_clicked_value == "main_menu"):
                    #激活
                    if_menu = True
            #点击退出
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #鼠标有点击事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #先更新文本
                pygame.display.update(cover_layer_rec_rect)
                #读取鼠标坐标处理
                x, y = event.pos
                adjusted_x = x - config.MARGIN_SIZE
                adjusted_y = y - config.MARGIN_SIZE
                row = round(adjusted_y / config.GRID_SIZE)
                col = round(adjusted_x /config.GRID_SIZE)
                #若激活，退出
                if(if_menu == True):
                    return
                #点击到了棋盘空处
                if 0 <= row < config.BOARD_SIZE and 0 <= col < config.BOARD_SIZE and board_state[row][col] == 0:
                    #按钮激活
                    button_able = True
                    #记录棋盘
                    move_history = [row[:] for row in board_state]
                    #下棋判断
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
                    #每次有棋子落下就判断输赢
                    if check_win_around(row, col):
                        time.sleep(1)
                        return "黑" if turn == 2 else "白"
                #点击事件结束后更新文本但不显示
                screen.blit(cover_layer_rec, cover_layer_rec_rect)
                keep_text(turn)
                #更新棋盘
                pygame.display.update(cover_board_rect)
        #移动事件完成后更新按钮状态
        for undo_button in buttons:
            undo_button.draw(screen)
        pygame.display.update()