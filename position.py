class position:
    
    def research_pos(self, map_list, character):
        list_pos = []
        for y in range(15):  # les x sont la coordonnée verticale ?
            for x, c in enumerate(map_list[y]):
                if  character in c and c == character:
                    list_pos.append((x*50, y*50))  # à inverser en  (y, x) sinon
        return list_pos




