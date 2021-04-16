import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((
            self.settings.screen_width,
            self.settings.screen_height
        ))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """React on button down"""
        keys = {
            pygame.K_RIGHT: 'self.ship.moving_right',
            pygame.K_LEFT: 'self.ship.moving_left',
            pygame.K_SPACE: self._fire_bullet,
            pygame.K_q: sys.exit
        }
        for key, item in keys.items():
            if event.key == key:
                if callable(keys[key]):
                    keys[key]()
                else:
                    exec(f'{keys[key]} = True')

        # if event.key == pygame.K_RIGHT:
        #     # move to right
        #     self.ship.moving_right = True
        # if event.key == pygame.K_LEFT:
        #     # move to left
        #     self.ship.moving_left = True
        # if event.key == pygame.K_q:
        #     sys.exit()

    def _check_keyup_events(self, event):
        """React on button unrelease"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()