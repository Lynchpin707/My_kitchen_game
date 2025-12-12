import pygame
from settings import *

class Overlay:
    def __init__(self, player):
        
        # General setups
        self.display_surface = pygame.display.get_surface()
        self.player = player
        
        overlay_path = './graphics/overlay/'
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        
        self.ingredients_surf = {ingredient: pygame.image.load(f'{overlay_path}{ingredient}.png').convert_alpha() for ingredient in player.ingredients}
        

    def display(self):
        # Tools
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAY_POSITIONS['tool'])
        self.display_surface.blit(tool_surf, tool_rect)
        # Ingredients
        ingredient_surf = self.ingredients_surf[self.player.selected_ingredient]
        ingredient_rect = ingredient_surf.get_rect(midbottom = OVERLAY_POSITIONS['ingredient'])
        self.display_surface.blit(ingredient_surf, ingredient_rect)