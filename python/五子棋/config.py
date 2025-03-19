import pygame
from pygame.locals import *

# 初始化Pygame的混音器，用于播放音频
pygame.mixer.init()

# 颜色定义
BLACK = (0, 0, 0)  # 黑色
WHITE = (255, 255, 255)  # 白色
GRAY = (128, 128, 128)  # 灰色
BOARD_COLOR = (200, 150, 100)  # 棋盘的背景颜色
TEXT_COLOR = BLACK  # 界面中文字的颜色（黑色）

# 按钮的默认颜色
BUTTON_COLOR = (200, 200, 200)
# 鼠标悬停在按钮上时的颜色
BUTTON_HOVER_COLOR = (220, 220, 220)

# 界面尺寸相关参数
MENU_WIDTH = 996  # 菜单界面的宽度
MENU_HEIGHT = 560  # 菜单界面的高度
BOARD_SIZE = 15  # 棋盘的大小（棋盘是正方形，这里指边长的格子数）
GRID_SIZE = 40  # 棋盘上每个格子的大小（以像素为单位）
MARGIN_SIZE = 20  # 棋盘边缘的空白大小（以像素为单位）
GAME_WIDTH = ((BOARD_SIZE - 1) * GRID_SIZE) + (2 * MARGIN_SIZE)  # 游戏界面的宽度
GAME_HEIGHT = (BOARD_SIZE * GRID_SIZE) + (4 * MARGIN_SIZE)  # 游戏界面的高度
# 结束界面
GAME_OVER_WIDTH = 600
GAME_OVER_HEIGHT = 600

# 字体设置相关参数
font_path = "C:/Windows/Fonts/simsun.ttc"  # 字体文件的路径，这里使用系统自带的宋体
FONT_SIZE_MENU = 30  # 菜单中文字的字体大小
FONT_SIZE_GAME_BOARD = 24  # 游戏棋盘上文字的字体大小
FONT_SIZE_GAME_OVER = 50  # 结束界面中文字的字体大小

# 菜单背景图片的路径
MENU_BACKGROUND_IMAGE_PATH = r"python/五子棋/picture/开始界面.jpg"
# 胜利背景图
GAME_OVER_BACKGROUND_IMAGE_PATH = r"python/五子棋/picture/胜利.PNG"

# 游戏窗口的图标图像
icon_image = pygame.image.load("python/五子棋/picture/icon.png")

# 游戏的背景音乐
BACKGROUND_MUSIC = pygame.mixer.Sound("python/五子棋/music/背景音.mp3")
# 下棋时的落子音效
DROP_SOUND = pygame.mixer.Sound("python/五子棋/music/落子.mp3")
#按钮音效
BUTTON_SOUND = pygame.mixer.Sound("python/五子棋/music/按钮.wav")
#胜利音效
VICTORY_SOUND = pygame.mixer.Sound("python/五子棋/music/胜利.wav")

# 按钮的宽度和高度
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
# 按钮之间的垂直间距
BUTTON_VERTICAL_SPACE = 40
# 按钮的水平对齐方式（0: 左对齐, 1: 居中对齐, 2: 右对齐）
BUTTON_HORIZONTAL_ALIGNMENT = 1
# 按钮的垂直对齐方式（0: 顶部对齐, 1: 居中对齐, 2: 底部对齐）
BUTTON_VERTICAL_ALIGNMENT = 1

# 菜单按钮的信息列表，每个字典包含按钮的文本、位置和点击后要返回的值
MENU_BUTTONS_INFO = [
    {"text": "双人对战", "x": 100, "y": 340, "action_return_value": "双人对战"},
    {"text": "人机对战", "x": 100, "y": 400, "action_return_value": "人机对战"},
    {"text": "退出游戏", "x": 100, "y": 460, "action_return_value": "退出游戏"}
]
# 游戏按钮相关配置
UNDO_BUTTON_INFO = [
    {"text": "悔棋", "x": GAME_WIDTH // 2 - BUTTON_WIDTH // 2+180, "y": GAME_HEIGHT - 60, "action_return_value": "悔棋"},
    {"text": "返回主菜单", "x": GAME_WIDTH // 2 - BUTTON_WIDTH // 2-180, "y": GAME_HEIGHT - 60, "action_return_value": "main_menu"}
]
# 结束按钮的信息列表，每个字典包含按钮的文本、位置和点击后要返回的值
GAME_OVER_BUTTONS_INFO = [
    {"text": "返回主菜单", "x": 300, "y": 480 // 2 + 130, "action_return_value": "main_menu"},
    {"text": "再来一把", "x": 300 // 2 - 110, "y": 480 // 2 + 130, "action_return_value": "play_again"}
]
#难度选择按钮
GAME_DIF_BBUTTONS_INFO=[
    {"text": "入门", "x": GAME_WIDTH // 2 - 100, "y": GAME_HEIGHT // 2 - 50 , "action_return_value": "1"},
    {"text": "进阶", "x": GAME_WIDTH // 2 - 100, "y": GAME_HEIGHT // 2 + 25 , "action_return_value": "2"}
]