import pygame
from settings import *
from support import *
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
    #Attributs
        
        #Graphics
        self.import_assets()
        self.status = 'down'
        self.frame_index = 0
        
        #General
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        
        # Position and mouvement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        # timers
        self.timers = {
            'tool use': Timer(350, self.use_tool),
            'tool switch': Timer(200), 
            'ingredient use': Timer(350, self.use_ingredient),
            'ingredient switch': Timer(200)
            
        }
        
        # tools
        self.tools = ['hoe', 'axe', 'water']
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        
        # Ingredients
        self.ingredients = ['corn', 'tomato']
        self.ingredient_index = 0
        self.selected_ingredient = self.ingredients[self.ingredient_index]
        
    def use_tool(self):
        print(self.selected_tool)
        
    def use_ingredient(self):
        print(self.selected_ingredient)
        
    def import_assets(self):
        self.animations = {'up': [],'down': [],'left': [],'right': [],
						   'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[],
						   'right_hoe':[],'left_hoe':[],'up_hoe':[],'down_hoe':[],
						   'right_axe':[],'left_axe':[],'up_axe':[],'down_axe':[],
						   'right_water':[],'left_water':[],'up_water':[],'down_water':[]}

        for animation in self.animations.keys():
            full_path = './graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
    
    def animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]      
            
    def input(self):
        keys = pygame.key.get_pressed()
        
        if not self.timers['tool use'].active:
            # Vertical directions
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = 'down'
            else :
                self.direction.y = 0  
            # Hirozental directions
            if keys[pygame.K_RIGHT]:   
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0
                
            # Tool use
            if keys[pygame.K_SPACE]:
                self.timers['tool use'].activate() 
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
            
            # Change tool
            if keys[pygame.K_q] and not self.timers['tool switch'].active:
                self.timers['tool switch'].activate()
                self.tool_index += 1
                if self.tool_index >= len(self.tools):
                    self.tool_index = 0
                self.selected_tool = self.tools[self.tool_index]  
                
            # Ingredient use
            if keys[pygame.K_LCTRL]:
                self.timers['ingredient use'].activate() 
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
                print('use ingredient')
                
            # Change Ingredient
            if keys[pygame.K_e] and not self.timers['ingredient switch'].active:
                self.timers['ingredient switch'].activate()
                self.ingredient_index += 1
                if self.ingredient_index >= len(self.ingredients):
                    self.ingredient_index = 0
                self.selected_ingredient = self.ingredients[self.ingredient_index]
                print(self.selected_ingredient)
                     
    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] +  '_idle'
        
        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool
    
    def  update_timers(self):
        for timer in self.timers.values():
            timer.update()
                    
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
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)