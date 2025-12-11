import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        #Attributs
        #Graphics
        self.import_assets()
        #General
        self.image = pygame.Surface((32, 64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        # Position and mouvement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
    
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': []}
        
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
            
    def input(self):
        keys = pygame.key.get_pressed()
        
        # Vertical directions
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else :
            self.direction.y = 0  
        # Hirozental directions
        if keys[pygame.K_RIGHT]:   
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize() #to fix the diagonal speed issue
        
        #Horizental mouvement
        self.pos.x += self.direction.x * self.speed*dt
        self.rect.centerx = self.pos.x
        #Vertical mouvement
        self.pos.y += self.direction.y * self.speed*dt
        self.rect.centery= self.pos.y
    
    def update(self, dt):
        self.input()
        self.move(dt)