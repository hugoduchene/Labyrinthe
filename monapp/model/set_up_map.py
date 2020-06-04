import settings
from random import randint
from monapp.model.position import Position

class Map:
    """object used to display the maze and these components"""
    def __init__(self):
        """initialization of the map object"""
        self.list_objects = []
        self.position = Position()
        self.list_labyrinth = self.load_map()
        self.list_labyrinth = [list(s) for s in self.list_labyrinth]
    
    def load_map(self):
        """loading the file with the maze"""
        with open(settings.Path, 'r') as file:
            list_labyrinth = file.readlines()
        return list_labyrinth
    
    def display_map(self):
        """ display map in the terminal """
        for line in self.list_labyrinth:
            update_list = "".join(line)
            print(update_list, end="")

    def list_map(self):
        """returns the double list"""
        return self.list_labyrinth

    def put_objetcs(self, map_class):
        """Put the objects randomly into the maze """
        place_object = self.position.research_pos(map_class, settings.Path_free)

        for loop in range(3):
            length_list = len(place_object)
            nbs_random = randint(0, length_list)
            self.list_objects.append(place_object[nbs_random])
            (x, y) = self.list_objects[loop]
            x = int(x/50)
            y = int(y/50)
            map_class[y][x] = settings.Objects
        print(self.list_objects)
        return self.list_objects
            
        
        
    
    

        

                

        
        
        
        
        



