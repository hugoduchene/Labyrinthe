from position import Position
from set_up_map import Map
import settings



class Point:
    #objet qui va servir à comptabiliser les points du joueurs 

    def __init__(self, map_class):  #j'initialise l'objets qui va gérer les points
        self.map = Map()
        self.position = Position()
        self.pos_computer  = (0, 0)
        self.pos_hero = (0, 0)
        self.point = 0
        self.nbs_objects = 0
        self.list_objects = self.map.put_objetcs(map_class)
        
    
    def count_points(self, map_class, new_map): 
        #méthode qui va servir à incrémenter les points si le joueur prend un objet 
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
        #méthode qui va servir à générer une autre map pour comparer la position de l'objet avec celle du joueur
        for loop in self.list_objects:
            (x, y) = loop
            x = int(x/50)
            y = int(y/50)
            new_map = self.map.list_labyrinth 
            new_map[y][x] = settings.objects
        return new_map
        
        
        
        
        
    

   