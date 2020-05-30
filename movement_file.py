from set_up_map import * 
from settings import * 


class movement:
    def __init__(self, map_class):
        self.old_y = 0
        self.old_x = 0
        self.pos_x = 0 
        self.pos_y = 0
        self.labyrinth = map_class.list_map()
        
    
    def movement_down(self):
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y += 1
        
    
    def movement_up(self):
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y -= 1
        
    
    def movement_right(self):
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_x += 1 
       

    def movement_left(self):
        self.old_y = self.pos_y
        self.old_x = self.pos_x
        self.pos_x -= 1
        

    def detect_wall(self):
        things_position = self.labyrinth[self.pos_y][self.pos_x]
        if things_position == wall:
            self.pos_x = 0 
            self.pos_y = 0
            
        else:
            pass
        return things_position
        

    def walk(self):
        self.labyrinth[self.pos_y][self.pos_x] = hero

    def delete_old_position_x(self):
        self.labyrinth[self.old_y][self.old_x] = path_free

    def delete_old_position_y(self):
        self.labyrinth[self.old_y][self.old_x] = path_free

    

    



        



    




