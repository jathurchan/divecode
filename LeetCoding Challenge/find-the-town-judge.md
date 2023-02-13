---
date: 2023.01.23
title: 997. Find the Town Judge
difficulty:
    - easy
runtime: 99.48 # faster than (in %)
memory usage: 59.7    # less than (in %)
---
## Description
In a town, there are `n` people labeled from `1` to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties **1** and **2**.

You are given an array `trust` where `trust[i] = [ai, bi]` representing that the person labeled `ai` trusts the person labeled `bi`.

Return *the label of the town judge if the town judge exists and can be identified, or return* `-1` *otherwise*.

**Example 1:**

```
Input: n = 2, trust = [[1,2]]
Output: 2

```

**Example 2:**

```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

```

**Example 3:**

```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

```

**Constraints:**

- `1 <= n <= 1000`
- `0 <= trust.length <= 104`
- `trust[i].length == 2`
- All the pairs of `trust` are **unique**.
- `ai != bi`
- `1 <= ai, bi <= n`

## Approach 1: Array
Time complexity: `O(n+p)`    |    Space complexity: `O(n)`
where `n` is the number of people and `p` is the number of trust relationships.

``` python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        candidates = [0]*n
        for a, b in trust:
            candidates[a-1] = -1    # a trust someone else
            if candidates[b-1] >= 0:
                candidates[b-1] += 1
        
        for i in range(n):
            if candidates[i] == n-1:
                return i+1
                
        return -1
```

``` cpp
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        std::vector<int> candidates(n, 0);
        for (vector<int>& relation: trust) {
            candidates[relation[0]-1] = -1;
            if (candidates[relation[1]-1] >= 0) {
                candidates[relation[1]-1]++;
            }
        }

        for (auto i = 0; i < n; i++) {
            if (candidates[i] == n-1) {
                return i+1;
            }
        }

        return -1;
    }
};
```

```java
class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] candidates = new int[n];
        for (int[] relation: trust) {
            candidates[relation[0]-1] = -1;
            if (candidates[relation[1]-1] >= 0) {
                candidates[relation[1]-1]++;
            }
        }
        for (int i = 0; i < n; i++) {
            if (candidates[i] == n-1) return i+1;
        }
        return -1;
    }
}
```