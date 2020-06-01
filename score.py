from position import * 
from set_up_map import *
from settings import *



class point:

    def __init__(self, map_class):
        self.map = Map()
        self.position = position()
        self.pos_computer  = (0, 0)
        self.pos_hero = (0, 0)
        self.point = 0
        self.nbs_objects = 0
        self.list_objects = self.map.put_objetcs(map_class)
        
    
    def count_points(self, map_class, new_map):
        for m in self.position.research_pos(map_class, hero):
            self.pos_hero = m
            (x_hero, y_hero) = self.pos_hero
            x_hero = int(x_hero/50)
            y_hero = int(y_hero/50)
        
        for pos_objects in self.list_objects:
            if pos_objects == self.pos_hero:
                if new_map[y_hero][x_hero] == "u":
                    self.point += 1
                    new_map[y_hero][x_hero] = "0"
                elif new_map[y_hero][x_hero] == "0":
                    pass
        return self.point
                
    
    def generate_new_map(self):
        for loop in self.list_objects:
            (x, y) = loop
            x = int(x/50)
            y = int(y/50)
            new_map = self.map.list_labyrinth 
            new_map[y][x] = "u"
        return new_map
        
        
        
        
        
    

   