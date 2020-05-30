from position import * 
from set_up_map import *
from settings import *



class point:

    def __init__(self):
        self.map = Map()
        self.map = self.map
        self.position = position()
        self.pos_computer  = (0, 0)
        self.pos_hero = (0, 0)
        self.point = 0
        self.nbs_objects = 0
    
    def count_points(self, map_class):
        for m in self.position.research_pos(map_class, hero):
            self.pos_hero = m 
        for x, y in self.position.research_pos(self.map.list_labyrinth, objects):
            self.pos_computer = (x, y)
            
            if self.pos_hero == (100, 0) and self.point < 1:
                self.point = 1
            if self.pos_hero == (450, 150) and self.point < 2:
                self.point = 2
            if self.pos_hero == (400, 500) and self.point < 3:
                self.point = 3
        return self.point
                
        
    

   