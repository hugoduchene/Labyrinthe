import settings
from random import randint
from position import Position

class Map:
    def __init__(self):
        self.list_objects = []
        self.position = Position()
        self.list_labyrinth = self.load_map()
        self.list_labyrinth = [list(s) for s in self.list_labyrinth]
    
    def load_map(self):
        with open(settings.path, 'r') as file:
            list_labyrinth = file.readlines()
        return list_labyrinth
    
    def display_map(self):
        for line in self.list_labyrinth:
            update_list = "".join(line)
            print(update_list, end="")

    def list_map(self):
        return self.list_labyrinth

    def put_objetcs(self, map_class):
        place_object = self.position.research_pos(map_class, settings.path_free)

        for loop in range(3):
            length_list = len(place_object)
            nbs_random = randint(0, length_list)
            self.list_objects.append(place_object[nbs_random])
            (x, y) = self.list_objects[loop]
            x = int(x/50)
            y = int(y/50)
            map_class[y][x] = settings.objects
        print(self.list_objects)
        return self.list_objects
            
        
        
    
    

        

                

        
        
        
        
        



