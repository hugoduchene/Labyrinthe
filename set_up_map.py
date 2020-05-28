from settings import * 

class Map:
    def __init__(self):
        self.list_labyrinth = self.load_map()
        self.list_labyrinth = [list(s) for s in self.list_labyrinth]
    
    def load_map(self):
        with open(path, 'r') as file:
            list_labyrinth = file.readlines()
        return list_labyrinth
    
    def display_map(self):
        for line in self.list_labyrinth:
            update_list = "".join(line)
            print(update_list, end="")

    def list_map(self):
        
        return self.list_labyrinth




