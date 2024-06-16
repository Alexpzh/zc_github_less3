import pygame

# Определение цвета фона
BACKGROUND_COLOR = (0, 0, 0)

class Flame(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.images = []
        for i in range(1, 4):
            image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.circle(image, (255, 0, 0), (25, 25), 25)
            pygame.draw.circle(image, (255, 154, 0), (25, 25), 20)
            pygame.draw.circle(image, (255, 255, 0), (25, 25), 15)
            self.images.append(image)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=pos)
        self.frame = 0
        self.animation_timer = 0

    def update(self, dt):
        self.animation_timer += dt
        if self.animation_timer > 100:
            self.frame += 1
            if self.frame < len(self.images):
                self.image = self.images[self.frame]
            else:
                self.kill()
            self.animation_timer = 0

