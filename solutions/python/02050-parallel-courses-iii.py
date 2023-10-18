class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        graph = defaultdict(list)
        for prevCourse, nextCourse in relations:
            graph[prevCourse-1].append(nextCourse-1)
        
        @cache
        def computeRemMonths(courseIdx):
            if not graph[courseIdx]:  # already computed
                return time[courseIdx]
            
            ans = 0

            for nextCourseIdx in graph[courseIdx]:
                ans = max(ans, computeRemMonths(nextCourseIdx))

            return ans + time[courseIdx]
        
        ans = 0
        for i in range(n):
            ans = max(ans, computeRemMonths(i))

        return ans