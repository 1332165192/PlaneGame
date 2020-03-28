import pygame

"""第一版飞机"""

# 初始化pygame
pygame.init()

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.绘制图像
screen.blit(bg, (0, 0))
# 3.更新显示(最后统一调用)
# pygame.display.update()

# 绘制英雄的飞机
# 1.加载图像数据
hero = pygame.image.load("./images/me1.png")
# 2.绘制图像
screen.blit(hero, (150, 500))
# 3.更新显示
pygame.display.update()

# 创建游戏时钟对象
clock = pygame.time.Clock()

# 记录英雄飞机的初始位置
hero_rect = pygame.Rect(200, 700, 102, 126)
# print(hero_rect.x)

# 游戏循环
i = 0
while True:
    # 设置屏幕刷新帧率(即指定循环内代码执行的频率)
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏。。。")
            # 卸载所有模块
            pygame.quit()
            # 退出系统
            exit()

    # 修改英雄飞机的位置
    hero_rect.y -= 1
    if hero_rect.y + hero_rect.height <= 0:
        hero_rect.y = 700

    # 绘制游戏背景
    screen.blit(bg, (0, 0))
    # 绘制英雄图像
    screen.blit(hero, hero_rect)
    # 更新显示
    pygame.display.update()
    print(i)
    i += 1
    pass

# 退出pygame
pygame.quit()

if __name__ == '__main__':
    pass
