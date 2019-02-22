#enemy type
#enemy size
#asteriod (Multiple small and medium circular orbs that fly around, and you have to navigate through them)
#bandits (one or two large enemies that fly around and shoot at you as you try to escape)
#fake merchant (bandits) (one medium enemy that shoots at you)
#military? (one large and 2 small enemies that fly and shoot at you)

import pygame
from pygame.locals import *

WIDTH = 500
HEIGHT = 500

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((5,255,5))
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.rect.move_ip(0,-5)
            print("W pressed")
        if pressed_keys[K_a]:
            self.rect.move_ip(-5,0)
            print("A pressed")
        if pressed_keys[K_s]:
            self.rect.move_ip(0,5)
            print("S pressed")
        if pressed_keys[K_d]:
            self.rect.move_ip(5,0)
            print("D pressed")
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT      
        
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if (((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or (event.type == pygame.QUIT)):
            print("Game closing")
            running = False
            pygame.quit()

    pressed_keys = pygame.key.get_pressed()
    screen.clear(0)
    player.update(pressed_keys)
    screen.blit(player.surf,(player.rect))
    pygame.display.flip()




