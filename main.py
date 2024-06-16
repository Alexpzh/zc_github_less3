import pygame
import random
import sys
import bah
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

#color_txt = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
TXT_COLOR = (255, 255, 255)
# Установите шрифт и размер текста
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()
flames = pygame.sprite.Group()
all_hits = 0
cnt_hits = 0
proc_hits = 0
vx = 5
vy = 5
running = True
while running:
    screen.fill(color)
    dt = clock.tick(30)

    #   Вывод результата попаданий
    if all_hits > 0:
        proc_hits = cnt_hits/all_hits * 100
    text = font.render(f"Кликов: {all_hits} Успех: {cnt_hits} Процент: {round(proc_hits,2)}", True, TXT_COLOR)

    # Получите размеры текста
    text_rect = text.get_rect()
    # Установите позицию текста в правом верхнем углу
    text_rect.topright = (SCREEN_WIDTH - 10, 10)  # Отступ в 10 пикселей от правого верхнего угла

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            all_hits += 1
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                cnt_hits += 1
                #
                flame = bah.Flame((mouse_x, mouse_y))
                flames.add(flame)
                #
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                vx = random.randint(-5, 5)
                vy = random.randint(-5, 5)

    target_x += vx * 2
    target_y += vy * 2
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
    screen.blit(text, text_rect)
    #
    flames.update(dt)
    flames.draw(screen)

    pygame.display.update()

pygame.quit()