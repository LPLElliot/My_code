import pygame
from pygame.locals import *
import config
from enum import Enum

# ButtonState枚举类，用于表示按钮的状态（启用或禁用）
class ButtonState(Enum):
    ENABLED = True
    DISABLED = False
# Button类，用于创建游戏中的按钮
class Button:
    def __init__(self, text, x=None, y=None, state=ButtonState.ENABLED, return_value=None):
        # 按钮显示的文本内容
        self.text = text
        # 按钮的状态（启用或禁用）
        self.state = state
        # 按钮被点击时要返回的值
        self.return_value = return_value
        # 按钮的默认颜色，根据是否在菜单中选择不同的配置颜色
        self.color = config.BUTTON_COLOR if "menu" in locals() else config.BUTTON_COLOR
        # 鼠标悬停在按钮上时的颜色，根据是否在菜单中选择不同的配置颜色
        self.hover_color = config.BUTTON_HOVER_COLOR if "menu" in locals() else config.BUTTON_HOVER_COLOR
        # 按钮文本的颜色，根据是否在菜单中选择不同的配置颜色
        self.text_color = config.MENU_TEXT_COLOR if "menu" in locals() else config.TEXT_COLOR
        # 使用配置中的字体路径和菜单字体大小创建字体对象
        self.font = pygame.font.Font(config.font_path, config.FONT_SIZE_MENU)
        # 使用字体对象渲染按钮文本，颜色为text_color
        self.text_render = self.font.render(text, True, self.text_color)
        # 如果传入了x和y坐标，则使用传入的值，否则通过配置计算按钮位置
        if x is not None and y is not None:
            self.x = x
            self.y = y
        else:
            self.x, self.y = self.calculate_button_position()
        # 根据按钮类型（菜单或游戏结束）从配置中获取按钮的宽度和高度
        button_width = config.BUTTON_WIDTH if "menu" in locals() else config.BUTTON_WIDTH
        button_height = config.BUTTON_HEIGHT if "menu" in locals() else config.BUTTON_HEIGHT
        # 创建按钮的矩形区域，设置圆角半径
        self.rect = pygame.Rect(self.x, self.y, button_width, button_height)
        self.rect_radius = 20
        self.is_hovered = False
    @classmethod
    def from_config(cls, config_dict):
        return cls(
            config_dict["text"],
            config_dict.get("x", None),
            config_dict.get("y", None),
            ButtonState(config_dict.get("enabled", True)),
            config_dict.get("action_return_value", None)
        )
    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=self.rect_radius)
        # 计算文本在按钮中的居中位置并绘制
        text_x = self.rect.x + (self.rect.width - self.text_render.get_width()) / 2
        text_y = self.rect.y + (self.rect.height - self.text_render.get_height()) / 2 +3
        screen.blit(self.text_render, (text_x, text_y))
    def handle_event(self, event):
        # 如果按钮处于启用状态，并且鼠标按下事件发生在按钮区域内，则返回按钮被点击时要返回的值
        if self.state == ButtonState.ENABLED and event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            config.BUTTON_SOUND.play()
            config.BUTTON_SOUND.set_volume(0.5)
            return self.return_value
        # 如果鼠标移动事件发生，检查鼠标是否在按钮区域内，更新is_hovered属性
        elif event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)