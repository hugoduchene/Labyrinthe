import pygame
import settings
from position import Position


class Hero_sprite:
    #object used to display the hero 

    def __init__(self):
        #initialization of the object
        self.image_hero = pygame.image.load(settings.path_image_hero)
        self.position = Position()

    def display_sprite_hero(self, screen, map_class):
        #Posing the hero in the right position, it returns the pose as a tuple 
        position_hero = self.position.research_pos(map_class, settings.hero)
        screen.blit(self.image_hero, position_hero[0])
        (x, y) = position_hero[0]

        return (x, y)
