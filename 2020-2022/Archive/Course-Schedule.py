class Solution(object):
    """
    207. Course Schedule

    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must
    take course bi first if you want to take course ai.
    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
    Return true if you can finish all courses. Otherwise, return false.
    """

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        matrix = [[float('inf')] * numCourses for _ in range(numCourses)] 
        
        for i in range(numCourses):
            matrix[i][i] = 0
        
        for pair in prerequisites:
            matrix[pair[0]][pair[1]] = 1
            
            if pair[0] == pair[1]:
                return False
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        
        for list in matrix:
            print(list)

        res = True
        i = 0
        while i < numCourses and res:
            j = i+1
            while j < numCourses and res:
                if matrix[i][j] < float('inf') and matrix[j][i] < float('inf'):
                    res = False
                j += 1
            i += 1

        return res

sol = Solution()
print(sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
        