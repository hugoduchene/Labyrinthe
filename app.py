from movement_file import Hero
from set_up_map import Map
import settings
from position import Position
import pygame 
from score import Point


position_class = Position()

map_class = Map() 
score_class = Point(map_class.list_labyrinth)


movement_class = Hero(map_class)
new_map = map_class.list_map()

pygame.init()

pygame.display.set_caption("labyrinth of mcgyver")
screen = pygame.display.set_mode((750, 750))

background = pygame.image.load(settings.path_image_Background)
wall_image = pygame.image.load(settings.path_image_wall)
win_image = pygame.image.load(settings.path_image_win)
hero_image = pygame.image.load(settings.path_image_hero)
objects_image = pygame.image.load(settings.path_image_objects)
guardian_image = pygame.image.load(settings.path_image_guardian)
defeat_image = pygame.image.load(settings.path_image_defeat)

new_map = score_class.generate_new_map()



    


value = True 

while value:
    
    screen.blit(background, (0,0))
    

    nbs_point = score_class.count_points(map_class.list_labyrinth, new_map)
    
    
    
    
    
    
    
    
    
    for i in position_class.research_pos(map_class.list_labyrinth, settings.wall):
        screen.blit(wall_image, i)
    
    for u in position_class.research_pos(map_class.list_labyrinth, settings.objects):
        screen.blit(objects_image, u)
    
    for g in position_class.research_pos(map_class.list_labyrinth, settings.guardian):
        screen.blit(guardian_image, g)
    
    position_hero = position_class.research_pos(map_class.list_labyrinth, settings.hero)
    screen.blit(hero_image, position_hero[0])
    
    (x, y) = position_hero[0]
    

    
    

    font = pygame.font.SysFont("comicsansms", 20)
    label = font.render("score : " + str(nbs_point), 0, (255,255,255))
    screen.blit(label, (660,0))


    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            value = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x < 700:
                movement_class.movement_right()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_x()
            if event.key == pygame.K_LEFT and x > 0:
                movement_class.movement_left()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_x()
            if event.key == pygame.K_DOWN and y < 700:
                movement_class.movement_down()
                movement_class.detect_wall()
                movement_class.walk()
                movement_class.delete_old_position_y()
            if event.key == pygame.K_UP and y > 0:
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