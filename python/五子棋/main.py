import pygame
import sys
import config
import double_game
import vs_ai

from menu import main_menu
from over import game_over

# 主函数，游戏的入口点，负责初始化游戏和协调各个模块的流程
def main():
    # 初始化
    pygame.init()
    # 设置logo
    pygame.display.set_icon(config.icon_image)
    # 加载背景音乐
    background_music = pygame.mixer.Sound(config.BACKGROUND_MUSIC)
    background_music.set_volume(0.3)  # 设置音量
    background_music.play(-1)  # -1表示无限循环播放
    # 运行状态
    running = True
    while running:
        #返回主菜单选项
        option = main_menu()

        if option == "双人对战":
            while True:  # 开始双人对战循环
                result = double_game.double_game_loop()
                play_again = playing(result)
                if play_again!= 1:  # 如果playing函数不返回1，跳出循环
                    break

        elif option == "人机对战":
            while True:  # 开始双人对战循环
                result = vs_ai.vs_ai_game_loop()
                play_again = playing(result)
                if play_again!= 1:  # 如果playing函数不返回1，跳出循环
                    break

        elif option == "退出游戏":
            running = False
            pygame.quit()
            sys.exit()


# 游戏逻辑函数
def playing(gaming_result):
    while True:
        winner = gaming_result
        if_menu = gaming_result

        if if_menu is None:
            double_game.reset_board()
            break  # 直接返回菜单
        #进入结束界面
        else:
            result = game_over(winner)
            if result == "main_menu":
                double_game.reset_board()
                break
            elif result == "play_again":
                return 1
            
if __name__ == "__main__":
    main()