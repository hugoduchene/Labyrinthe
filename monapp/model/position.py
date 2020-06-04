class Position:
    """Object used to find the position of the different components of the map"""
    
    def research_pos(self, map_list, character):
        """method that returns a list of positions (x,y)""" 
        list_pos = []
        for y in range(15):  
            for x, c in enumerate(map_list[y]):
                if  character in c and c == character:
                    list_pos.append((x*50, y*50))  
        return list_pos




