import pygame
import time
start_time = pygame.time.get_ticks()
WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 70
BTN_HEIGHT = 70
HP_WIDTH = 70
HP_HEIGHT = 70
LIFE_WIDTH = 40
LIFE_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("Map.png"), (WIN_WIDTH, WIN_HEIGHT))
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
enemy_image = pygame.transform.scale(pygame.image.load("enemy.png"), (HP_WIDTH, HP_HEIGHT))
muse_image = pygame.transform.scale(pygame.image.load("muse.png"), (BTN_WIDTH, BTN_HEIGHT))
sound_image = pygame.transform.scale(pygame.image.load("sound.png"), (BTN_WIDTH, BTN_HEIGHT))
continue_image = pygame.transform.scale(pygame.image.load("continue.png"), (BTN_WIDTH, BTN_HEIGHT))
pause_image = pygame.transform.scale(pygame.image.load("pause.png"), (BTN_WIDTH, BTN_HEIGHT))
hp_image = pygame.transform.scale(pygame.image.load("hp.png"), (LIFE_WIDTH, LIFE_HEIGHT))
hp_gray_image = pygame.transform.scale(pygame.image.load("hp_gray.png"), (LIFE_WIDTH, LIFE_HEIGHT))
# set the title
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("My first game")


class Game:
    def __init__(self):
        # window

        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # draw background
            win.blit(background_image, (0, 0))

            # draw enemy and health bar
            win.blit(enemy_image, (0, 250))
            pygame.draw.rect(win, (255, 0, 0), [20, 240, 40,5])
            # draw menu (and buttons)
            pygame.draw.rect(win, (0, 0, 0), [0, 0, 1024, 70])     #menu
            win.blit(muse_image,(760,0))
            win.blit(sound_image, (820, 0))
            win.blit(continue_image, (880, 0))
            win.blit(pause_image, (940, 0))
            win.blit(hp_image, (570, 0))
            win.blit(hp_image, (540, 0))
            win.blit(hp_image,(510,0))
            win.blit(hp_image, (480, 0))
            win.blit(hp_image, (450, 0))
            win.blit(hp_image, (450, 30))
            win.blit(hp_image, (480, 30))
            win.blit(hp_gray_image, (510, 30))
            win.blit(hp_gray_image, (540, 30))
            win.blit(hp_gray_image, (570, 30))
            # draw time

            pygame.display.update()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()
pygame.quit()


