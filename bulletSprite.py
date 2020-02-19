import pygame
import random
import math
from spritesheet_functions import SpriteSheet



class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet. """
 
    def __init__(self, start_x, start_y, dest_x, dest_y,imageName,is_rotate=False,angle=0):
        """ Constructor.
        It takes in the starting x and y location.
        It also takes in the destination x and y position.
        """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Set up the image for the bullet
        
        self.sprite_sheet = SpriteSheet(imageName,is_rotate,angle)
        self.w,self.h=self.sprite_sheet.sprite_sheet.get_size()
        self.image = self.sprite_sheet.get_image(0,0,self.w,self.h)

        self.rect = self.image.get_rect()
        self.target_angle=0

        start_x-=self.w/2
        start_y-=self.h/2
        dest_x-=self.w/2
 
        # Move the bullet to our starting location
        self.rect.x = start_x
        self.rect.y = start_y
 
        # Because rect.x and rect.y are automatically converted
        # to integers, we need to create different variables that
        # store the location as floating point numbers. Integers
        # are not accurate enough for aiming.
        self.floating_point_x = start_x
        self.floating_point_y = start_y
 
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
 
        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        velocity = 20
        self.change_x = math.cos(angle) * velocity
        self.change_y = math.sin(angle) * velocity

        
        

    def update(self):
        """ Move the bullet. """
 
        # The floating point x and y hold our more accurate location.
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x
 
        # The rect.x and rect.y are converted to integers.
        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)
 
        # If the bullet flies of the screen, get rid of it.
        if self.rect.x < 0 or self.rect.x > 480 or self.rect.y < 10 or self.rect.y > 650:
            self.kill()




