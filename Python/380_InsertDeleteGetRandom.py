class RandomizedSet(object):

    def __init__(self):
        self.hash_map = {}
        self.array_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hash_map:
            return False
        else:
            self.hash_map[val] = len(self.array_list)
            self.array_list.append(val)
            return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.hash_map:
            
            index = self.hash_map[val]
            
            self.hash_map[self.array_list[-1]] = index
            self.array_list[index] = self.array_list[-1]
            
            self.array_list.pop()
            del self.hash_map[val]
            
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.array_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()