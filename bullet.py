import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, mainbullet):
        super(Bullet, self)._init_()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 10)
        self.color = 255,255,255
        self.rect.centerx = mainbullet.rect.centerx
        self.rect.top = mainbullet.rect.top
        self.speed = 5.1
        self.y = float(self.rect.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)



    def update_bullet(self):
        self.y = self.speed
        self.rect.y = self.y












































