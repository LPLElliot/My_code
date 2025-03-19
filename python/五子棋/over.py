import pygame
import sys
from pygame.locals import *
import config
from button import Button

# 游戏结束界面函数，显示游戏结束信息和相关按钮，并处理用户交互
def game_over(winner):
    #初始化pygame的所有子模块
    pygame.init()
    # 窗口参数
    screen = pygame.display.set_mode((config.GAME_OVER_WIDTH, config.GAME_OVER_HEIGHT))
    # 标题
    pygame.display.set_caption("游戏结束")
    #获取预先配置好的胜利音效对象
    config.VICTORY_SOUND.play()
    #设置其音量为 2
    config.VICTORY_SOUND.set_volume(2)
    # 加载背景
    try:
        #从磁盘读取指定路径的图像文件，并将其转换为pygame内部可以处理的图像对象
        background_image_original = pygame.image.load(config.GAME_OVER_BACKGROUND_IMAGE_PATH)
        #对图像进行缩放操作。接受两个参数：要缩放的原始图像对象（background_image_original）和目标尺寸(config.MENU_WIDTH, config.MENU_HEIGHT)
        background_image = pygame.transform.scale(background_image_original, (config.GAME_OVER_WIDTH, config.GAME_OVER_HEIGHT))
        #删除原始图像对象background_image_original
        del background_image_original
    #如果在try块中加载图片或对图片进行缩放操作时出现pygame.error异常
    except pygame.error as e:
        print(f"加载菜单背景图片出错: {e}")
        #这个函数会关闭pygame所有已初始化的模块，释放与pygame相关的资源
        pygame.quit()
        #函数用于终止 Python 程序的执行，参数1表示程序以错误状态退出
        sys.exit(1)
    #创建一个用于游戏结束界面显示文字的字体对象
    font_game_over = pygame.font.Font(config.font_path, config.FONT_SIZE_GAME_OVER)
    if winner == "平局":
        winner_text = font_game_over.render(winner, True, config.TEXT_COLOR)
    elif winner == "黑" or winner == "白":
        winner_text = font_game_over.render(f"{winner}棋获胜！", True, config.TEXT_COLOR)
    elif winner == "人机" or winner == "玩家":
        winner_text = font_game_over.render(f"{winner}获胜！", True, config.TEXT_COLOR)
    #生成的获胜者信息文本位置
    winner_rect = winner_text.get_rect(center=(config.GAME_OVER_WIDTH // 2, config.GAME_OVER_HEIGHT // 2 - 150))
    #根据config.GAME_OVER_BUTTONS_INFO中的配置信息创建游戏结束界面上的按钮对象
    buttons = [Button.from_config(info) for info in config.GAME_OVER_BUTTONS_INFO]
    # 将缩放后的背景图片绘制到游戏结束界面窗口的左上角（坐标为 (0, 0)），使其成为界面的背景
    screen.blit(background_image, (0, 0))
    #将生成的获胜者信息文本按照其矩形区域的设置（通过winner_rect）绘制到游戏结束界面窗口上的相应位置，展示出游戏的获胜情况。
    screen.blit(winner_text, winner_rect)
    #再次遍历buttons列表，在窗口上绘制每个按钮
    for button in buttons:
        button.draw(screen)
    #更新游戏结束界面的显示
    pygame.display.flip()
    while True:
        #每次循环中获取所有当前发生的pygame事件
        for event in pygame.event.get():
            #检查当前事件是否为pygame.QUIT事件，即用户点击游戏结束界面窗口的关闭按钮时触发的事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #遍历buttons列表中的所有按钮对象，用于处理每个按钮相关的事件
            for button in buttons:
                #判断是否发生了与按钮相关的操作，并返回相应的结果
                result = button.handle_event(event)
                if result:
                    #按钮处理事件得到的结果返回
                    return result
        for button in buttons:
            #将按钮绘制到游戏结束界面窗口screen上
            button.draw(screen)
        #更新游戏结束界面的显示，将之前绘制的所有元素（包括重新绘制的按钮）更新到实际的游戏结束界面窗口中
        pygame.display.update()