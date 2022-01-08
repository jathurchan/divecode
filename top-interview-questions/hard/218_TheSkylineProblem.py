class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        # Sort buildings by their x-coordinates of the left edges
        buildings.sort(key=lambda b: b[0])
        
        active_buildings = []   # sorted by x-coordinate of the right edge
        max_height = 0 # current maximum height (for active buildings)
        
        def updateMax(bs):  # update max height
            maxH = 0
            for b in bs:
                if b[2] > maxH:
                    maxH = b[2]
            return maxH
        
        for building in buildings:
            
            i, n = 0, len(active_buildings)
            
            while active_buildings and active_buildings[0][1] < building[0]: # end before building?
                
                ending_building = active_buildings.pop(0)
                
                new_max = updateMax(active_buildings)
                
                if new_max != max_height:   # update max_height and add the new point
                    max_height = new_max
                    res.append([ending_building[1], max_height, 1]) # 1 for ending
            
            if max_height < building[2]:    # new building higher
                max_height = building[2]
                res.append([building[0], building[2], 0])   # add beginning (0 for beginning)
            
            # insert building into active_buildings (preserving the order)
            i, n = 0, len(active_buildings)
            while i < n and active_buildings[i][1] < building[1]:
                i += 1
            active_buildings.insert(i, building)
        
        while active_buildings:
            ending_building = active_buildings.pop(0)

            new_max = updateMax(active_buildings)
            if new_max != max_height:   # update max_height and add the new point
                max_height = new_max
                res.append([ending_building[1], max_height, 1]) # for ending
        
        # Erase false duplicates ([[1,2,1],[1,2,2],[1,2,3]])
        print(res)
        new_res = []
        
        j, p = 0, len(res)
        
        while j < p:
            
            cnt = 1
            c_max = res[j][1]
            
            while j + cnt < p and res[j][0] == res[j+cnt][0]:
                if res[j][2] == 0:
                    c_max = max(c_max, res[j+cnt][1])
                else:
                    c_max = min(c_max, res[j+cnt][1])   # ending so take the minimum
                cnt += 1
                
            new_res.append([res[j][0], c_max])
            
            j += cnt
        
        return new_res