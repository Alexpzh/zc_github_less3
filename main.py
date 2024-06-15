import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/4ca3dd872b78ad87757acf5fccd6edb7.jpg")
pygame.display.set_icon(icon)

running = True
while running:
    pass

pygame.quit()