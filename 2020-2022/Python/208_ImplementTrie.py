class Trie(object):

    def __init__(self):
        self.children = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        trie = self.children
        
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie['#'] = '#'
        
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        trie = self.children
        
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        
        if '#' in trie:
            return True
        return False
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        trie = self.children
        
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)