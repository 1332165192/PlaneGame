import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 英雄发射子弹定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, imgage_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        # 图像
        self.image = pygame.image.load(imgage_name)
        # 位置
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed

    def update(self, *args):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    # is_alt：是否是另一张图片
    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        # 调用父类实现
        super().update(args)
        # 判断是否移出屏幕，移出屏幕将图像位置设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 创建敌机精灵
        super().__init__("./images/enemy1.png")
        # 设置敌机的初始速度
        self.speed = random.randint(1, 3)
        # 设置敌机初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        pass

    def update(self, *args):
        # 调用父类方法，保持垂直方向的飞行
        super().update(args)
        # 判断敌机是否飞出屏幕，飞出屏幕则从精灵组中删除敌机精灵
        if self.rect.y >= SCREEN_RECT.height:
            print("敌机飞出屏幕。。。")
            # 将精灵从精灵组中移除
            self.kill()
        pass

    def __del__(self):
        print("敌机挂了。。。")


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self, *args):
        # 父类方法不满足条件故不用调用父类方法
        self.rect.x += self.speed
        # 设置英雄不能飞出屏幕
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        # 发射子弹
        print("发射子弹...")
        # 创建子弹精灵
        for i in (0, 1, 2):
            bullet = Bullet()
            # 设置子弹精灵的初始位置
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            # 将子弹精灵添加到子弹精灵组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self, *args):
        super().update(args)
        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹被销毁...")
