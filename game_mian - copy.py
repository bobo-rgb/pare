bulletimageName="bullet6.png"
bulletimageName_dj='bullet5.png'
playerimageName="player.png"
background3_image_filename = 'img_bg_level_3.jpg'
diJiimage_name='ZSFJ3.png'
button_image='button_p.png'
start_bg_image='bg1.jpg'
LOGO_image='LOGO.png'
producer_logo_image='tencentlogo.png'
word1_image='start.png'
word2_image='quit.png'
end_bg_image='bg.jpg'
track_bullet_image='bullet5.png'

SCREEN_WIDTH = 510
SCREEN_HEIGHT = 650
WHITE = (255, 255, 255)
RED=(241, 45, 29)
COLOR1=(245,63,10)#朱橙
COLOR2=(82,62,193)#紫
COLOR3=(15,2,253)#深蓝


import pygame
import random
from pygame.locals import *
from random import randint #引入随机数
import math
from spritesheet_functions import SpriteSheet
from boom import Boom
from bulletSprite import Bullet
from diJi import DJ
from playerSprite import Player
from Track_bullet import Track_bullet




class backGround(object):
    def __init__(self,backgroundimage):
        self.imageBackground = pygame.image.load(backgroundimage).convert()

    def isOver(self,y):
        screen.blit(self.imageBackground, (0,y))


class dynamicBackGround(object):
    def __init__(self,backgroundimage,ibg,jbg):
        self.a=backGround(backgroundimage)
        self.b=backGround(backgroundimage)
        self.i=ibg
        self.j=jbg

    def dynamic(self):
        if self.i>SCREEN_HEIGHT:
            self.i=-885
        
        if self.j>SCREEN_HEIGHT:
            self.j=-885

        self.a.isOver(self.i)
        self.b.isOver(self.j)
        self.j+=1
        self.i+=1



class Button(object):
    def __init__(self, image, position, txt, txt_size, txt_sum, txt_color=(0,0,0), word_file='C:/Windows/Fonts/simkai.ttf'):
        self.image = pygame.image.load(image).convert_alpha()
        self.w, self.h = self.image.get_size()
        self.x, self.y = position
        self.txt=txt
        self.txt_size=txt_size
        self.txt_sum=txt_sum
        self.txt_color=txt_color
        self.press=False
        self.in_button=False
        self.txt_x,self.txt_y=self.x+self.w/2-self.txt_size*self.txt_sum/2, self.y+self.h/2-self.txt_size/2
        self.text=Text(txt_size,word_file)

    def show_and_press(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()

        if self.txt!=' ':
            self.text.text_2(self.txt, self.txt_x, self.txt_y, self.txt_color)

        if self.x < mouse_x < self.x + self.w and self.y < mouse_y < self.y+self.h:
            screen.blit(self.image, (self.x,self.y))
            self.in_button=True

        else:
            self.in_button=False

        
    
class Text(object):
    def __init__(self,word_size=18,word_file='C:/Windows/Fonts/simkai.ttf'):
        self.my_font=pygame.font.Font(word_file,word_size)

    def text(self,Str,text1,text2,textx,texty,color=WHITE):
        #文本输出样式1
        textstr=Str+str(text1)+text2
        text_screen=self.my_font.render(textstr,True,color)
        screen.blit(text_screen,(textx,texty))

    def text_2(self,Str,textx,texty,color=WHITE):
        #文本输出样式2
        textstr=Str
        text_screen=self.my_font.render(textstr,True,color)
        screen.blit(text_screen,(textx,texty))
        



       


def playing():
    pygame.mixer.music.play(-1, 0)
    # 播放背景音乐，第一个参数为播放的次数（-1表示无限循环），第二个参数是设置播放的起点（单位为秒）
    # --- Sprite lists 
    boom_list=pygame.sprite.Group() 
    # List of each bullet
    bullet_list = pygame.sprite.Group()
    diji_list=pygame.sprite.Group()
    dj_bullet_list=pygame.sprite.Group()
    for i in range(3):
        dj=DJ()
        dj.load(diJiimage_name,90,90,3)
        dj.position=randint(-30,400),randint(-200, -50)
        diji_list.add(dj)

    dBG3=dynamicBackGround(background3_image_filename,-118,-886)

    player=Player()
    player.load(playerimageName,180,150,4)
    player.position=200,500
    player_list=pygame.sprite.Group()
    player_list.add(player)
    player.direction=0
    player_move=False
    v_x=0

    track_bullet=Track_bullet(track_bullet_image,0,0)
    track_bullet.display=False

    # Loop until the user clicks the close button.
    done = False
    open_bullet=True
    open_bullet_dj=True
    open_dj_sum=0
    open_bullet_time=30
    open_bullet_time_dj=30
    game_over_sum=0
    score=0
    # -------- Main Program Loop -----------
    while not done:
        time=clock.tick(30)
        ticks = pygame.time.get_ticks()
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] or keys[K_d]:
            player.direction=2
            player_move=True
            v_x=1
        elif keys[K_LEFT] or keys[K_a]:
            player.direction=1
            v_x=-1
            player_move=True
        elif keys[K_SPACE]:
            if open_bullet:
                # Create the bullet based on where we are, and where we want to go.
                bullet = Bullet(player.X+player.frame_width/2, player.Y+player.frame_height/2, player.X+player.frame_width/2, 0,bulletimageName,True,90)
 
                # Add the bullet to the lists
                bullet_list.add(bullet)
                open_bullet=False
        #开追踪弹
        elif keys[K_b]:
            if not track_bullet.display:
                track_bullet.restart(player.X+player.frame_width/2, player.Y+player.frame_height/2)
        else:
            player.direction=3
            v_x=0
            player_move=False

        player.first_frame = player.direction*player.columns
        player.last_frame = player.first_frame+player.columns-1
        if player_move:
            player.X+=v_x*7 #主机速度
            
        #追踪弹用到
        old_distance=10000
        distance=1000

        #碰撞检测
        for dj in diji_list:
            if pygame.sprite.spritecollide(dj, bullet_list, True, None):
                b=Boom()
                b.load('explosion_aigei_com.png',128,170,4)
                b.position=dj.X-b.frame_width/2+dj.frame_width/2, dj.Y-b.frame_height/2+dj.frame_height/2
                boom_list.add(b)
                dj.restart()
                dj.X=dj.x
                dj.Y=dj.y
                score+=1
            if dj.y<700:
                dj.y +=dj.speed*time/1000.0
                dj.Y=dj.y
            else:
                dj.restart()
                dj.X=dj.x
                dj.Y=dj.y
            if open_bullet_dj:#敌机开弹
                bullet_dj=Bullet(dj.X+dj.frame_width/2, dj.Y+dj.frame_height/2, dj.X+dj.frame_width/2, dj.Y+dj.frame_height/2+10,bulletimageName_dj,True,180)
                open_dj_sum+=1
                dj_bullet_list.add(bullet_dj)
            if pygame.sprite.spritecollide(player,diji_list,False,None):
                d=int(math.sqrt((player.X+player.frame_width/2-dj.X-dj.frame_width/2)**2+(player.Y+player.frame_height/2-dj.Y-dj.frame_height/2)**2))
                if d<80:
                    game_over_sum+=1
                    dj.restart()
                    dj.X=dj.x
                    dj.Y=dj.y
                
                    b=Boom()
                    b.load('explosion_aigei_com.png',128,170,4)
                    b.position=player.X-b.frame_width/2+player.frame_width/2, player.Y-b.frame_height/2+player.frame_height/2
                    boom_list.add(b)

            if track_bullet.display:#追踪敌机及碰撞检测
                distance=int(math.sqrt(math.pow(dj.X-track_bullet.rect.x,2)+math.pow(dj.Y-track_bullet.rect.y,2)))
                old_distance=min(distance,old_distance)
                if old_distance==distance:
                    track_bullet.update(dj.frame_width/2+dj.X, dj.frame_height/2+dj.Y)
                    tb_image=track_bullet.rotate()
                if pygame.sprite.collide_rect(track_bullet, dj):#返回布尔值
                    bb=Boom()
                    bb.load('explosion_aigei_com.png',128,170,4)
                    bb.position=dj.X-bb.frame_width/2+dj.frame_width/2, dj.Y-bb.frame_height/2+dj.frame_height/2
                    boom_list.add(bb)
                    dj.restart()
                    dj.X=dj.x
                    dj.Y=dj.y
                    track_bullet.display=False
                    score+=1
                    

        for dj_billet in dj_bullet_list:
            if pygame.sprite.spritecollide(player,dj_bullet_list,False,None):
                d=int(math.sqrt((player.X+player.frame_width/2-dj_billet.rect.x-dj_billet.w/2)**2+(player.Y+player.frame_height/2-dj_billet.rect.y-dj_billet.h/2)**2))
                if d<80:
                    game_over_sum+=1
                    dj_bullet_list.remove(dj_billet)
                    dj_billet.kill()

                    b=Boom()
                    b.load('explosion_aigei_com.png',128,170,4)
                    b.position=player.X-b.frame_width/2+player.frame_width/2, player.Y-b.frame_height/2+player.frame_height/2
                    boom_list.add(b)
            if pygame.sprite.spritecollide(dj_billet,bullet_list,True,None):
                b=Boom()
                b.load('explosion_aigei_com.png',128,170,4)
                b.position=dj_billet.rect.x-b.frame_width/2+dj_billet.w/2, dj_billet.rect.y-b.frame_height/2+dj_billet.h/2
                boom_list.add(b)

                dj_bullet_list.remove(dj_billet)
                dj_billet.kill()

            if track_bullet.display:#追踪敌机及碰撞检测
                if pygame.sprite.collide_rect(track_bullet, dj_billet):#返回布尔值
                    b=Boom()
                    b.load('explosion_aigei_com.png',128,170,4)
                    b.position=dj_billet.rect.x-b.frame_width/2+dj_billet.w/2, dj_billet.rect.y-b.frame_height/2+dj_billet.h/2
                    boom_list.add(b)
                    track_bullet.display=False
                    dj_bullet_list.remove(dj_billet)
                    dj_billet.kill()
                

        if open_dj_sum>2:
            open_bullet_dj=False
            open_dj_sum=0

        #开弹冷却时间
        if not open_bullet:
            open_bullet_time-=1
            if open_bullet_time<=0:
                open_bullet=True
                open_bullet_time=20

        open_bullet_time_dj-=1
        if open_bullet_time_dj<=0:
            open_bullet_dj=True
            open_bullet_time_dj=40

        if open_bullet:
            t=100
        else:
            t=(20-open_bullet_time)*5

        # Call the update() method on all the sprites
        #all_sprites_list.update()
        boom_list.update(ticks)
        bullet_list.update()
        dj_bullet_list.update()
        diji_list.update(ticks)
        player_list.update(ticks)

        for b in boom_list:
            if b.Kill:
                boom_list.remove(b)
                b.kill()

        # Clear the screen
        screen.fill(WHITE)
        dBG3.dynamic()#将背景图画上去
        if track_bullet.display:
            screen.blit(tb_image,(track_bullet.rect.x, track_bullet.rect.y))

        # Draw all the spites
        boom_list.draw(screen)
        dj_bullet_list.draw(screen)
        bullet_list.draw(screen)
        diji_list.draw(screen)
        txt1.text('冷却:',t,'%',15,610)
        score_txt.text('击毁:',score,'架',10,10)
        score_txt.text('生命值:',(5-game_over_sum)*20,'%',380,10)
        player_list.draw(screen)

        #被击中5次死亡
        if game_over_sum>=5:
            done=True

        # --- Limit to 20 frames per second
        pygame.display.update()

    return score
    

def startUI():
    dealy=0
    if quit_button.press or start_button.press:
        dealy=100
    else:
        sound = pygame.mixer.Sound('ready_go.wav')
        sound.set_volume(1.0)
        sound.play()
    
    done=False
    start_button.press=False
    quit_button.press=False
    while not done:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #接收到退出事件后退出程序
                pygame.quit()
                exit()

            if event.type==pygame.MOUSEBUTTONDOWN :
                if start_button.in_button:
                    start_button.press=True
                if quit_button.in_button:
                    quit_button.press=True

              
        if dealy>50:
            screen.blit(start_bg,(0,0))
            screen.blit(logo,(55,100))
            screen.blit(word1,(189,350))
            screen.blit(word2,(205,449))
            start_button.show_and_press()
            quit_button.show_and_press()
            
        else:
            dealy+=1
            screen.blit(producer,(0,0))
        
        if quit_button.press or start_button.press:
            done=True
        
        pygame.display.update()
    
    return quit_button.press


def endUI(score):
    done=False
    pygame.mixer.music.stop()
    end_button.press=False
    while not done:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #接收到退出事件后退出程序
                pygame.quit()
                exit()

            if event.type==pygame.MOUSEBUTTONDOWN :
                if end_button.in_button:
                    end_button.press=True
                    
        screen.blit(end_bg,(0,0))
        txt2.text_2('GAME OVER!',150,250,RED)
        txt2.text('共击毁：',score,'架',150,350,RED)
        end_button.show_and_press()
        if end_button.press:
            done=True

        pygame.display.update()
    

if __name__=='__main__':
    # --- Create the window
 
    # Initialize Pygame
    pygame.init()
 
    # Set the height and width of the screen
 
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    start_bg=pygame.image.load(start_bg_image)
    start_bg=pygame.transform.scale(start_bg,(510, 700))
    end_bg=pygame.image.load(end_bg_image)
    end_bg=pygame.transform.scale(end_bg,(510, 700))
    logo=pygame.image.load(LOGO_image).convert_alpha()
    logo=pygame.transform.scale(logo,(400, 150))
    producer=pygame.image.load(producer_logo_image).convert_alpha()
    producer=pygame.transform.scale(producer,(510, 650))
    word1=pygame.image.load(word1_image).convert_alpha()
    word1=pygame.transform.scale(word1,(132, 48))
    word2=pygame.image.load(word2_image).convert_alpha()

    start_button=Button(button_image,(189,350),' ',30,1,word_file='C:/Windows/Fonts/STXINGKA.TTF')
    quit_button=Button(button_image,(189,450),' ',30,1,word_file='C:/Windows/Fonts/STXINGKA.TTF')
    end_button=Button(button_image,(189,450),'回主界面',40,4,txt_color=RED,word_file='C:/Windows/Fonts/STXINGKA.TTF')
    
    txt1=Text(18)
    score_txt=Text(20)
    txt2=Text(40,'C:/Windows/Fonts/STXINGKA.TTF')
    pygame.mixer.music.load('bgmusic.mp3')# 加载背景音乐文件

    game_quit=False
    
    while not game_quit:
        game_quit=startUI()
        if not game_quit:
            score=playing()
            endUI(score)
    pygame.quit() 
    

