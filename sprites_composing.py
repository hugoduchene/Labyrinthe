import pygame 
from position import Position
import settings


class Composing_sprite:
    #object used to display the components of the maze
    def __init__(self):
        #initialisation de l'objet
        self.image_guardian = pygame.image.load(settings.path_image_guardian)
        self.image_object = pygame.image.load(settings.path_image_objects)
        self.image_wall = pygame.image.load(settings.path_image_wall)
        self.position = Position()

    def display_sprite_wall(self, screen, map_class):
        #object used to display the walls of the maze
        for i in self.position.research_pos(map_class, settings.wall):
            screen.blit(self.image_wall, i)
    
    def display_sprite_object(self, screen, map_class):
        ##object used to display the objects of the maze
        for i in self.position.research_pos(map_class, settings.objects):
            screen.blit(self.image_object, i)
    
    def display_sprite_guardian(self, screen, map_class):
        #object used to display the gardian of the maze
        for g in self.position.research_pos(map_class, settings.guardian):
            screen.blit(self.image_guardian, g)

    def display_sprite_point(self, screen, nbs_point):
        #object used to display the points of the maze
        font = pygame.font.SysFont("comicsansms", 20)
        label = font.render("score : " + str(nbs_point), 0, (255,255,255))
        screen.blit(label, (660,0))
