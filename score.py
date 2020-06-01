from position import Position
from set_up_map import Map
import settings



class Point:
    #object that will be used to keep track of the player's points
    def __init__(self, map_class):  #I initialize the object that will handle the points
        self.map = Map()
        self.position = Position()
        self.pos_computer  = (0, 0)
        self.pos_hero = (0, 0)
        self.point = 0
        self.nbs_objects = 0
        self.list_objects = self.map.put_objetcs(map_class)
        
    
    def count_points(self, map_class, new_map): 
        #method that will be used to increment the points if the player takes an object 
        for m in self.position.research_pos(map_class, settings.hero):
            self.pos_hero = m
            (x_hero, y_hero) = self.pos_hero
            x_hero = int(x_hero/50)
            y_hero = int(y_hero/50)
        
        for pos_objects in self.list_objects:
            if pos_objects == self.pos_hero:
                if new_map[y_hero][x_hero] == settings.objects:
                    self.point += 1
                    new_map[y_hero][x_hero] = settings.path_free
                elif new_map[y_hero][x_hero] == settings.path_free:
                    pass
        return self.point
                
    
    def generate_new_map(self):
        #method that will be used to generate another map to compare the position of the object with that of the player
        for loop in self.list_objects:
            (x, y) = loop
            x = int(x/50)
            y = int(y/50)
            new_map = self.map.list_labyrinth 
            new_map[y][x] = settings.objects
        return new_map
        
        
        
        
        
    

   