import pygame
import settings
from position import Position


class Hero_sprite:
    #objet servant à afficher le héro 

    def __init__(self):
        #initialisation de l'objet
        self.image_hero = pygame.image.load(settings.path_image_hero)
        self.position = Position()

    def display_sprite_hero(self, screen, map_class):
        #affichage du héro à la bonne position , il renvoie la pos sous forme de tuple
        position_hero = self.position.research_pos(map_class, settings.hero)
        screen.blit(self.image_hero, position_hero[0])
        (x, y) = position_hero[0]

        return (x, y)
