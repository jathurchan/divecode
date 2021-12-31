class Leaderboard(object):

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId, score):
        """
        :type playerId: int
        :type score: int
        :rtype: None
        """
        if playerId in self.scores:
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score
        

    def top(self, K):
        """
        :type K: int
        :rtype: int
        """
        s_scores = sorted(self.scores.items(), key=lambda x:x[1], reverse=True)
        
        top_scores = [v for _,v in s_scores ]
        
        total = 0
        
        for v in top_scores[:K]:
            total += v
        
        return total
        
        

    def reset(self, playerId):
        """
        :type playerId: int
        :rtype: None
        """
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)