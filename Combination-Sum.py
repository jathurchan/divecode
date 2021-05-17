class Solution(object):
    """
    39. Combination Sum

    Given an array of distinct integers candidates and a target integer target, return a list of all unique
    combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. Two combinations are unique
    if the frequency of at least one of the chosen numbers is different.
    It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

    Constraints:

        -   1 <= candidates.length <= 30
        -   1 <= candidates[i] <= 200
        -   All elements of candidates are distinct.
        -   1 <= target <= 500
    """

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        combinations = []
        candidates = sorted(candidates)

        def dfs(cands, tgt, path, combinations):
            if tgt < 0:
                return
            if tgt == 0:
                combinations.append(path)
                return
            for i in range(len(cands)):
                dfs(cands[i:], tgt-cands[i], path+[cands[i]], combinations)
        
        dfs(candidates, target, [], combinations)

        return combinations