diJiimage_name='ZSFJ3.png'
background3_image_filename = 'img_bg_level_3.jpg'



from pygame.locals import *
import itertools, sys, time, random, math, pygame
from random import randint #引入随机数
from MyLibrary import *
''' 敌机 '''


class DJ(MySprite):
    def __init__(self):
        MySprite.__init__(self)
        self.speed=randint(100,300)
        self.x = randint(-30,400)
        self.y = randint(-300, -50)
        self.id=0
        
    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.master_image= pygame.transform.scale(self.master_image,(270, 90))
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1


    def restart(self):
        self.x = randint(-30,400)
        self.y = randint(-300, -80)
        self.speed = randint(100,300)
        self.id=0
        
    def update(self, current_time, rate=30):
        #update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
'''
class backGround(object):
    def __init__(self,backgroundimage):
        self.imageBackground = pygame.image.load(backgroundimage).convert()

    def isOver(self,y):
        screen.blit(self.imageBackground, (0,y))


class dynamicBackGround(object):
    def __init__(self,backgroundimage,ibg,jbg,nbg):
        self.a=backGround(backgroundimage)
        self.b=backGround(backgroundimage)
        self.i=ibg
        self.j=jbg
        self.n=nbg
        self.w=10

    def dynamic(self):
        if self.i>650:
            self.i=-886
        
        if self.j>650:
            self.j=-886

        self.a.isOver(self.i)
        if self.n>0:
            
            self.b.isOver(self.j)
            self.j+=0.2
        #pygame.time.delay(20)
        self.n+=0.2
        self.i+=0.2

   

# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
 
screen = pygame.display.set_mode([480, 650])

all_sprites_list = pygame.sprite.Group()

for i in range(5):
    
    dj=DJ()
    dj.load(diJiimage_name,90,90,3)
    dj.position=randint(-30,400),randint(-200, -80)
    all_sprites_list.add(dj)


dBG3=dynamicBackGround(background3_image_filename,-118,-769,-118)
        
done=False
clock = pygame.time.Clock()
while not done:
    time=clock.tick(30)
    ticks = pygame.time.get_ticks()
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #all_sprites_list.update()
    screen.fill((255,255,255))

    for dj in all_sprites_list:
        if dj.y<610:
            dj.y +=dj.speed*time/1000.0
            dj.Y=dj.y
        else:
            dj.restart()
            dj.X=dj.x
    dBG3.dynamic()#将背景图画上去    
    all_sprites_list.update(ticks)

    all_sprites_list.draw(screen)
   
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    

pygame.quit()
'''
