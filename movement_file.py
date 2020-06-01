from set_up_map import Map 
import settings

class Hero:
    #Objet gérant les déplacements de l'héro
    def __init__(self, map_class):
        #initialisation de l'objet
        self.old_y = 0
        self.old_x = 0
        self.pos_x = 0 
        self.pos_y = 0
        self.labyrinth = map_class.list_map()
        
    
    def movement_down(self):
        #mouvement vers le bas + calcul de son ancienne position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y += 1
        
    
    def movement_up(self):
        #mouvement vers le haut + calcul de son ancienne position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_y -= 1
        
    
    def movement_right(self):
        #mouvement vers la droite + calcul de son ancienne position
        self.old_x = self.pos_x
        self.old_y = self.pos_y
        self.pos_x += 1 
       

    def movement_left(self):
        #mouvement vers la gauche + calcul de son ancienne position
        self.old_y = self.pos_y
        self.old_x = self.pos_x
        self.pos_x -= 1
        

    def detect_wall(self):
        #méthode servant à trouver les murs et si le perso en touche un alors il revient au début
        things_position = self.labyrinth[self.pos_y][self.pos_x]
        if things_position == settings.wall:
            self.pos_x = 0 
            self.pos_y = 0
            
        else:
            pass
        return things_position
        

    def walk(self):
        #méthode servant à avancer en remplacer la vide par le perso
        self.labyrinth[self.pos_y][self.pos_x] = settings.hero

    def delete_old_position(self):
        #méthode servant à supprimer l'ancienne position pour que le héro ne se duplique pas
        self.labyrinth[self.old_y][self.old_x] = settings.path_free

    

    

    



        



    




