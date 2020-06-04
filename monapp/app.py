from monapp.model.hero_file import Hero
from monapp.model.set_up_map import Map
import settings
from monapp.model.position import Position
import pygame 
from monapp.model.score import Point
from monapp.view.sprites_hero import HeroSprite
from monapp.view.sprites_composing import ComposingSprite


class Application:
    """ object that manages user actions """
    def __init__(self):
        #object initialization
        self.Composing_sprite_class = ComposingSprite()
        self.hero_sprite_class = HeroSprite()
        self.position_class = Position()
        self.map_class = Map() 
        self.score_class = Point(self.map_class.list_labyrinth)
        self.movement_class = Hero(self.map_class)
        self.new_map = self.map_class.list_map()
        self.screen = pygame.display.set_mode((750, 750))
        self.background = pygame.image.load(settings.Path_image_Background)
        self.win_image = pygame.image.load(settings.Path_image_win)
        self.defeat_image = pygame.image.load(settings.Path_image_defeat)
        self.new_map = self.score_class.generate_new_map()
        self.nbs_point = 0






    def main_display(self):
        """method loading that displays the components"""
        self.screen.blit(self.background, (0,0))
        

        self.nbs_point = self.score_class.count_points(self.map_class.list_labyrinth, self.new_map)
        self.Composing_sprite_class.display_sprite_wall(self.screen, self.map_class.list_labyrinth)

        self.Composing_sprite_class.display_sprite_object(self.screen, self.map_class.list_labyrinth)
        self.Composing_sprite_class.display_sprite_guardian(self.screen, self.map_class.list_labyrinth)
        self.Composing_sprite_class.display_sprite_point(self.screen, self.nbs_point)



    def main_loop(self):
        """method that will handle the events"""
        value = True 

        while value:

            self.main_display()
        
            
        
            (x, y) = self.hero_sprite_class.display_sprite_hero(self.screen, self.map_class.list_labyrinth)
        
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    value = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and x < 700:
                        self.movement_class.movement_right()
                        self.movement_class.detect_wall()
                        self.movement_class.walk()
                        self.movement_class.delete_old_position()
                    if event.key == pygame.K_LEFT and x > 0:
                        self.movement_class.movement_left()
                        self.movement_class.detect_wall()
                        self.movement_class.walk()
                        self.movement_class.delete_old_position()
                    if event.key == pygame.K_DOWN and y < 700:
                        self.movement_class.movement_down()
                        self.movement_class.detect_wall()
                        self.movement_class.walk()
                        self.movement_class.delete_old_position()
                    if event.key == pygame.K_UP and y > 0:
                        self.movement_class.movement_up()
                        self.movement_class.detect_wall()
                        self.movement_class.walk()
                        self.movement_class.delete_old_position()
                        
            """manages the end screen"""
            if (x, y) == (700, 700) and self.nbs_point == 3:
                self.screen.blit(self.win_image, (0,0))
            elif (x, y) == (700, 700) and self.nbs_point != 3:
                self.screen.blit(self.defeat_image, (0,0))
            else:
                pass

            pygame.display.update()

                

        