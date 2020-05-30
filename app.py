from movement_file import * 
from set_up_map import * 
from settings import *
from position import *
import pygame 
from score import *

score_class = point()

position_class = position()

map_class = Map() 

movement_class = movement(map_class)
new_map = map_class.list_map()

pygame.init()

pygame.display.set_caption("labyrinth of mcgyver")
screen = pygame.display.set_mode((750, 750))

background = pygame.image.load(path_image_Background)
wall_image = pygame.image.load(path_image_wall)
win_image = pygame.image.load(path_image_win)
hero_image = pygame.image.load(path_image_hero)
objects_image = pygame.image.load(path_image_objects)
guardian_image = pygame.image.load(path_image_guardian)
defeat_image = pygame.image.load(path_image_defeat)




value = True 

while value:
    
    screen.blit(background, (0,0))
    

    
    
    

    
    for i in position_class.research_pos(map_class.list_labyrinth, wall):
        screen.blit(wall_image, i)
    
    for u in position_class.research_pos(map_class.list_labyrinth, objects):
        screen.blit(objects_image, u)
    
    for g in position_class.research_pos(map_class.list_labyrinth, guardian):
        screen.blit(guardian_image, g)
    
    position_hero = position_class.research_pos(map_class.list_labyrinth, hero)
    screen.blit(hero_image, position_hero[0])
    

    nbs_point = score_class.count_points(map_class.list_labyrinth)
    nbs_point = nbs_point
    

    font = pygame.font.SysFont("comicsansms", 20)
    label = font.render("score : " + str(nbs_point), 0, (255,255,255))
    screen.blit(label, (660,0))


    #print(o[0])
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                movement_class.movement_right()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_x()
            if event.key == pygame.K_LEFT:
                movement_class.movement_left()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_x()
            if event.key == pygame.K_DOWN:
                movement_class.movement_down()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_y()
            if event.key == pygame.K_UP:
                movement_class.movement_up()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_y()
                

    if position_hero[0] == (700, 700) and nbs_point == 3:
        screen.blit(win_image, (0,0))
    elif position_hero[0] == (700, 700) and nbs_point != 3:
        screen.blit(defeat_image, (0,0))
    else:
        pass

    pygame.display.update()

        

pygame.quit()