import pygame 
from position import Position
import settings


class Wall_sprite:
    #objet servant à afficher les murs du labyrinthe
    def __init__(self):
        #initialisation de l'objet
        self.image_wall = pygame.image.load(settings.path_image_wall)
        self.position = Position()

    def display_sprite_wall(self, screen, map_class):
        #méthode servant à blit les murs dans le labyrinthe
        for i in self.position.research_pos(map_class, settings.wall):
            screen.blit(self.image_wall, i)
