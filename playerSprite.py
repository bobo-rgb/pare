from pygame.locals import *
import itertools, sys, time, random, math, pygame
from MyLibrary import *


class Player(MySprite):
    def __init__(self):
        MySprite.__init__(self)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.master_image=pygame.transform.scale(self.master_image, (720, 600))
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

'''
pygame.init()
screen = pygame.display.set_mode((480,650),0,32)
pygame.display.set_caption("精灵类测试")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

player=Player()
player.load('player.png',200,180,4)
player.position=200,250
player_list=pygame.sprite.Group()
player_list.add(player)
player.direction=0
player_move=False
v_x=0

while True:
    framerate.tick(30)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] or keys[K_d]:
        player.direction=2
        player_move=True
        v_x=1
        
        
    elif keys[K_LEFT] or keys[K_a]:
        player.direction=1
        v_x=-1
        player_move=True
        
    else:
        player.direction=3
        v_x=0
        player_move=False

    player.first_frame = player.direction*player.columns
    player.last_frame = player.first_frame+player.columns-1
    if player_move:
        player.X+=v_x*5
    

    screen.fill((255,255,255))
    
    player_list.update(ticks)
    player_list.draw(screen)
    
    pygame.display.update()
'''

        
