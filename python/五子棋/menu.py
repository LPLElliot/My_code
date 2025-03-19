import pygame
import sys
from pygame.locals import *
import config
from button import Button

# 主菜单
def main_menu():
    #初始化pygame的所有子模块
    pygame.init()
    # 窗口参数
    screen = pygame.display.set_mode((config.MENU_WIDTH, config.MENU_HEIGHT))
    # 标题
    pygame.display.set_caption("菜单")
    # 按钮参数
    buttons = [Button.from_config(info) for info in config.MENU_BUTTONS_INFO]
    # 加载背景图
    try:
        #从磁盘读取指定路径的图像文件，并将其转换为pygame内部可以处理的图像对象
        background_image_original = pygame.image.load(config.MENU_BACKGROUND_IMAGE_PATH)
        #对图像进行缩放操作。接受两个参数：要缩放的原始图像对象（background_image_original）和目标尺寸(config.MENU_WIDTH, config.MENU_HEIGHT)
        background_image = pygame.transform.scale(background_image_original, (config.MENU_WIDTH, config.MENU_HEIGHT))
        #删除原始图像对象background_image_original
        del background_image_original
    #如果在try块中加载图片或对图片进行缩放操作时出现pygame.error异常
    except pygame.error as e:
        print(f"加载菜单背景图片出错: {e}")
        #这个函数会关闭pygame所有已初始化的模块，释放与pygame相关的资源
        pygame.quit()
        #函数用于终止 Python 程序的执行，参数1表示程序以错误状态退出
        sys.exit(1)
    #通过这个操作，背景图片被绘制到游戏窗口上，成为窗口的背景
    screen.blit(background_image, (0, 0))
    #这个循环负责不断更新和渲染主菜单界面，以及处理用户的输入事件
    while True:
        #在每次循环中获取所有当前发生的pygame事件
        for event in pygame.event.get():
            # 退出
            if event.type == pygame.QUIT:
                pygame.quit()
                #终止整个 Python 程序的运行，正常关闭程序
                sys.exit()
            #一个遍历buttons列表的循环，用于处理每个按钮相关的事件
            for button in buttons:
                #调用按钮对象的handle_event方法，并将当前事件对象作为参数传递给它，判断是否发生了与按钮相关的操作
                result = button.handle_event(event)
                if result:
                    #有相关操作发生，将按钮处理事件得到的结果返回
                    return result
        #再次遍历buttons列表，在窗口上绘制每个按钮
        for button in buttons:
            button.draw(screen)
        #更新游戏窗口显示
        pygame.display.update()