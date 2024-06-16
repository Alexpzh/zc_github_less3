import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/4ca3dd872b78ad87757acf5fccd6edb7.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/apple_red")
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))





running = True
while running:
    pass

pygame.quit()