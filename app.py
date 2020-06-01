from movement_file import Hero
from set_up_map import Map
import settings
from position import Position
import pygame 
from score import Point
from sprites_hero import Hero_sprite
from sprites_composing import Composing_sprite

Composing_sprite_class = Composing_sprite()
hero_sprite_class = Hero_sprite()
position_class = Position()
map_class = Map() 
score_class = Point(map_class.list_labyrinth)


movement_class = Hero(map_class)
new_map = map_class.list_map()

pygame.init()

pygame.display.set_caption("labyrinth of mcgyver")
screen = pygame.display.set_mode((750, 750))

background = pygame.image.load(settings.path_image_Background)

win_image = pygame.image.load(settings.path_image_win)


guardian_image = pygame.image.load(settings.path_image_guardian)
defeat_image = pygame.image.load(settings.path_image_defeat)

new_map = score_class.generate_new_map()



    


value = True 

while value:
    
    screen.blit(background, (0,0))
    

    nbs_point = score_class.count_points(map_class.list_labyrinth, new_map)
    Composing_sprite_class.display_sprite_wall(screen, map_class.list_labyrinth)
    
    Composing_sprite_class.display_sprite_object(screen, map_class.list_labyrinth)
    Composing_sprite_class.display_sprite_guardian(screen, map_class.list_labyrinth)
    Composing_sprite_class.display_sprite_point(screen, nbs_point)
    
    
    (x, y) = hero_sprite_class.display_sprite_hero(screen, map_class.list_labyrinth)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < 700:
                movement_class.movement_right()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position()
            if event.key == pygame.K_LEFT and x > 0:
                movement_class.movement_left()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position()
            if event.key == pygame.K_DOWN and y < 700:
                movement_class.movement_down()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position()
            if event.key == pygame.K_UP and y > 0:
                movement_class.movement_up()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position()
                

    if (x, y) == (700, 700) and nbs_point == 3:
        screen.blit(win_image, (0,0))
    elif (x, y) == (700, 700) and nbs_point != 3:
        screen.blit(defeat_image, (0,0))
    else:
        pass

    pygame.display.update()

        

pygame.quit()