---
date: 2022.11.04
title: 433. Minimum Genetic Mutation
difficulty:
    - medium
runtime: 15.58 # faster than (in %)
memory usage: 37.78    # less than (in %)
---
## Description
A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

Suppose we need to investigate a mutation from a gene string `startGene` to a gene string `endGene` where one mutation is defined as one single character changed in the gene string.

- For example, `"AACCGGTT" --> "AACCGGTA"` is one mutation.

There is also a gene bank `bank` that records all the valid gene mutations. A gene must be in `bank` to make it a valid gene string.

Given the two gene strings `startGene` and `endGene`and the gene bank `bank`, return *the minimum number of mutations needed to mutate from* `startGene` *to* `endGene`. If there is no such a mutation, return `-1`.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

**Example 1:**

```
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

```

**Example 2:**

```
Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

```

**Constraints:**

- `0 <= bank.length <= 10`
- `startGene.length == endGene.length == bank[i].length == 8`
- `startGene`, `endGene`, and `bank[i]` consist of only the characters `['A', 'C', 'G', 'T']`.

## Approach 1: BFS (Breadth-First Search)


``` python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        b_set = set(bank)
        
        to_visit = deque([(startGene, 0)])
        visited = {startGene}
        
        while to_visit:
            curr_gene, steps = to_visit.popleft()
            if curr_gene == endGene:
                return steps
            
            for i in range(8):
                for c in "ACGT":
                    if c != curr_gene[i]:
                        new_gene = curr_gene[:i] + c + curr_gene[i+1:]
                        
                        if new_gene not in visited and new_gene in b_set:
                            to_visit.append((new_gene, steps+1))
                            visited.add(new_gene)   
        
        return -1
```