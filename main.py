import pygame
import random

pygame.init()

FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/4ca3dd872b78ad87757acf5fccd6edb7.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

vx = 5
vy = 5
running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                vx = random.randint(-5, 5)
                vy = random.randint(-5, 5)

    target_x += vx * 0.05
    target_y += vy * 0.05
    if target_x < 0:
        target_x = 0
        vx =-vx
    if target_x > SCREEN_WIDTH - target_width:
        target_x = SCREEN_WIDTH - target_width
        vx = -vx
    if target_y < 0:
        target_y = 0
        vy = -vy
    if target_y > SCREEN_HEIGHT - target_height:
        target_y = SCREEN_HEIGHT - target_height
        vy = -vy


    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()
    pass

pygame.quit()