import pygame
from plane_sprites import *


class PlaneGame(object):
    """
    飞机大战主游戏
    """

    def __init__(self):
        print("游戏初始化。。。")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建精灵和精灵组
        self.__create_sprites()
        # 设置定时器事件(定时创建敌机)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 设置定时器事件(定时发射子弹)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def start_game(self):
        print("启动游戏。。。")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新精灵组
            self.__update_sprites()
            # 更新屏幕显示
            pygame.display.update()

    def __create_sprites(self):
        # 创建精灵和精灵组
        # 创建背景精灵
        bg1 = Background()
        bg2 = Background(True)
        # 创建背景精灵组
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄的精灵
        self.hero = Hero()
        # 创建英雄的精灵组
        self.hero_group = pygame.sprite.Group(self.hero)

    def __event_handler(self):
        # 事件监听
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__gameOver()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("创建敌机。。。")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵加入敌机精灵组
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("英雄向右移动。。。")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            print("英雄向右移动。。。")
            self.hero.speed = 2
        elif keys_pressed[pygame.K_LEFT]:
            print("英雄向左移动。。。")
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        # 碰撞检测
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄飞机
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表是否有内容
        if len(enemies):
            print("英雄牺牲。。。游戏结束。。。")
            self.hero.kill()
            PlaneGame.__gameOver()

    def __update_sprites(self):
        # 更新精灵组
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __gameOver():
        # 游戏结束
        print("退出游戏。。。")
        # 卸载所有模块
        pygame.quit()
        # 退出系统
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
