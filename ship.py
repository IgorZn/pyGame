import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # speed
        self.settings = ai_game.settings

        # load pic of ship and get form
        self.image = pygame.image.load('images/ship.bmp')

        # получить квадрад/прямоугольник
        self.rect = self.image.get_rect()

        # сохр. коор-ты в Х
        self.x = float(self.rect.x)

        # each new ship appear at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # flag state
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update x coordinate in relation of flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """rend ship at current position"""
        self.screen.blit(self.image, self.rect)