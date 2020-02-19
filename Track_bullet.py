from pygame.locals import *
import itertools, sys, time, random, math, pygame
from diJi import DJ
from random import randint
from boom import Boom


class Track_bullet(pygame.sprite.Sprite):
    def __init__(self,image_file,start_x,start_y):
        super().__init__()
        self.image=pygame.image.load(image_file).convert_alpha()
        self.image=pygame.transform.rotate(self.image, -90)
        #self.image=pygame.transform.scale(self.image,(32, 20))
        self.w=(self.image.get_width())
        self.h=(self.image.get_height())
        self.rect=self.image.get_rect()
        self.rect.x=start_x 
        self.rect.y=start_y
        self.v=10
        self.fangle=0
        self.display=True
        
        
    def restart(self,x,y):
        self.rect.x=x
        self.rect.y=y
        self.display=True

    
    
    def rotate(self):
        if self.display:
            new_image=pygame.transform.rotate(self.image, -(self.fangle))
            return new_image
        else:
            return 
        

    def update(self,target_x,target_y):
        if self.display:
            deta_x=target_x-self.rect.x
            deta_y=target_y-self.rect.y
            angle = math.atan2(deta_y, deta_x)
            self.fangle=math.degrees(angle)#弧度转角度
            distance=math.sqrt(math.pow(deta_x,2)+math.pow(deta_y,2))
            #self.x +=math.cos(angle)*self.v
            #self.y +=math.sin(angle)*self.v
            self.rect.x+=(deta_x/distance)*self.v
            self.rect.y+=(deta_y/distance)*self.v
        else:
            self.rect.x=0
            self.rect.y=0
        
        
        
   
    
'''

pygame.init()
screen = pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("爆炸")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

b=Track_bullet('bullet5.png',500,500)
b.v=10
#b.rotate(-45)
#b_list=pygame.sprite.Group()
diji_list=pygame.sprite.Group()
boom_list=pygame.sprite.Group()
#b_list.add(b)
diJiimage_name='ZSFJ3.png'
for i in range(2):
    
    dj=DJ()
    dj.load(diJiimage_name,90,90,3)
    dj.position=randint(-30,400),randint(-200, -50)
    dj.id=5
    diji_list.add(dj)

deta_x=0
deta_y=0
fangle=0
x,y=b.rect.x, b.rect.y
while True:
    time=framerate.tick(20)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    old_distance=10000
    distance=1000
    for i,dj in enumerate(diji_list):
        if b.display:
            distance=int(math.sqrt(math.pow(dj.X-b.rect.x,2)+math.pow(dj.Y-b.rect.y,2)))
            old_distance=min(distance,old_distance)
            if old_distance==distance:
                b.update(dj.frame_width/2+dj.X, dj.frame_height/2+dj.Y)
                b_image=b.rotate()

            if pygame.sprite.collide_rect(b, dj):#返回布尔值
                bb=Boom()
                bb.load('explosion_aigei_com.png',128,170,4)
                bb.position=dj.X-bb.frame_width/2+dj.frame_width/2, dj.Y-bb.frame_height/2+dj.frame_height/2
                boom_list.add(bb)
                dj.restart()
                dj.X=dj.x
                dj.Y=dj.y
                b.restart(300,500)

        if dj.y<600:
            dj.y +=dj.speed*time/1000.0
            dj.Y=dj.y
        else:
            dj.restart()
            dj.X=dj.x
            dj.Y=dj.y
    

    for bb in boom_list:
        if bb.Kill:
            boom_list.remove(b)
            bb.kill()
            
    screen.fill((0,0,0))
    diji_list.update(ticks)
    boom_list.update(ticks)
    if b.display:
        screen.blit(b_image,(b.rect.x, b.rect.y))
    diji_list.draw(screen)
    boom_list.draw(screen)
    pygame.display.update()
'''
