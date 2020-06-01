from set_up_map import Map 
import settings

class Hero:
    #Object managing the movement of the hero    
    def __init__(self, map_class):
        #initialization of the object
        self.old_y = 0
        self.old_x = 0
        self.pos_x = 0 
        self.pos_y = 0
        self.labyrinth = map_class.list_map()
        
    
    def movement_down(self):
        #movement down + calculation of its old position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y += 1
        
    
    def movement_up(self):
        #movement upwards + calculation of its old position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y -= 1
        
    
    def movement_right(self):
        #movement to the right + calculation of its old position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_x += 1 
       

    def movement_left(self):
        #movement to the left + calculation of its old position        
        self.old_y = self.pos_y
        self.old_x = self.pos_x
        self.pos_x -= 1
        

    def detect_wall(self):
        #method to find the walls and if the person touches one of them then he goes back to the beginning.
        things_position = self.labyrinth[self.pos_y][self.pos_x]
        if things_position == settings.wall:
            self.pos_x = 0 
            self.pos_y = 0
            
        else:
            pass
        return things_position
        

    def walk(self):
        #method to advance by replacing the vacuum with the personal one
        self.labyrinth[self.pos_y][self.pos_x] = settings.hero

    def delete_old_position(self):
        #method to remove the old position so the hero doesn't duplicate himself 
        self.labyrinth[self.old_y][self.old_x] = settings.path_free

    

    

    



        



    




