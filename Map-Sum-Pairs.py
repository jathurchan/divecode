class MapSum(object):
    """
    677. Map Sum Pairs

    Implement the MapSum class:
    -   MapSum() Initializes the MapSum object.
    -   void insert(String key, int val) Inserts the key-val pair into the map.
        If the key already existed, the original key-value pair will be overridden to the new one.
    -   int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
    """

    def __init__(self):
        self.data = {}


    def insert(self, key, val):
        self.data[key] = val


    def sum(self, prefix):
        sum = 0
        for key in self.data.keys():
            if self.is_prefix(key, prefix):
                sum += self.data[key]
        return sum


    def is_prefix(self, string, prefix):
        n, p = len(string), len(prefix)
        
        if n < p:
            return False

        i = 0
        while i < p and string[i] == prefix[i]:
            i += 1

        return i == p


# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)