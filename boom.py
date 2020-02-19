from pygame.locals import *
import itertools, sys, time, random, math, pygame
from MyLibrary import *
''' 爆炸特效  '''


class Boom(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        self.frame=7
        self.L1=False
        self.L2=False
        self.Kill=False
        #爆炸音效
        self.soundPlayOne=True
        self.sound = pygame.mixer.Sound('Moorhuhn Kart 2_aigei_com.wav')
        self.sound.set_volume(1.0)

    def update(self, current_time, rate=30):
        if self.soundPlayOne:
            self.sound.play()
            self.soundPlayOne=False
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = 4
                self.L1=True
            if self.frame>7 and self.L1:
                self.frame=0
                self.L2=True
            if self.frame>3 and self.L2:
                self.Kill=True
                self.frame=3
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame



'''
pygame.init()
screen = pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("爆炸")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

boom=Boom()
boom.load('explosion_aigei_com.png',128,170,4)
boom.position=250,250
boom_group=pygame.sprite.Group()
boom_group.add(boom)


while True:
    framerate.tick(20)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()



    screen.fill((255,255,255))
    for b in boom_group:
        if b.Kill:
            boom_group.remove(b)
            
    boom_group.update(ticks)
    boom_group.draw(screen)
    pygame.display.update()
'''
