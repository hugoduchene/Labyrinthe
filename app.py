from movement_file import * 
from set_up_map import * 
from settings import *

map_class = Map() 

movement_class = movement(map_class)
new_map = map_class.list_map()

while movement_class.detect_wall != exit_labyrinth:
    map_class.display_map()
    enter_customer = input("(gauche = q, droite = a, haut = z, bas = s) >")

    if enter_customer == "q":
        movement_class.movement_left()
        movement_class.detect_wall()
        movement_class.walk()
        movement_class.delete_old_position_x()
    if enter_customer == "a":
        movement_class.movement_right()
        movement_class.detect_wall()
        movement_class.walk()
        movement_class.delete_old_position_x()
    if enter_customer == "z":
        movement_class.movement_up()
        movement_class.detect_wall()
        movement_class.walk()
        movement_class.delete_old_position_y()
    if enter_customer == "s":
        movement_class.movement_down()
        movement_class.detect_wall()
        movement_class.walk()
        movement_class.delete_old_position_y()

    
