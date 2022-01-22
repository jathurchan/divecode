# Top Amazon Questions

- 1 Two Sum - *Easy*
   - Hash Table (maintain a mapping of each element in the array to its index - look up time near constant time)
- 146 LRU Cache - *Medium*
   - Ordered Dictionary: [Ordered Dict](https://docs.python.org/3/library/collections.html#collections.OrderedDict) (hash map: get/put key + linked list: delete first added key)
   - Hashmap + DoubleLinkedList (class DLinkedList, def _add_node, def _remove_node, _move_to_head, _pop_tail, __init__, get, put )
- 42 Trapping Rain Water - *Hard*
   - Dynamic Programming (store highest bar size up to that index over the left + right)
- 200 Number of Islands - *Medium*
   - DFS
- 56 Merge Intervals - *Medium*
- 4 Median of Two Sorted Arrays - *Hard*
- 253 Meeting Rooms II - *Medium*
- 273 Integer to English Words - *Hard*
   - Billion, million, thousand
- 829 Consecutive Numbers Sum - *Hard*
- 23 Merge k Sorted Lists - *Hard*
- 127 Word Ladder - *Hard*
- 239 Sliding Window Maximum - *Hard*
   - Deque
- 49 Group Anagrams - *Medium*
- 79 Word Search - *Medium*
- 696 Count Binary Substrings - *Easy*
   - Array / res, prev, curr
- 212 Word Search II - *Hard*
- 828 Count Unique Characters of All Substrings of a Given String - *Easy*
- 295 Find Median from Data Stream - *Hard*
- 460 LFU Cache - *Hard*
- 1268 Search Suggestions System - *Medium*
   - Binary Search (I=0 j=len(), while(I<j), if >=, j = m else I = mid+1)
   - Trie
- 937 Reorder Data in Log Files - *Easy*
   - Custom Sort with keys (stability of sorting algorithms)
- 863 All Nodes Distance K in Binary Tree - *Medium*
- 973 K Closest Points to Origin - *Medium*
- 994 - Rotting Oranges - *Medium*
   - Queue (BFS): keep track of the candidates that we need to visit during the process. + In-place technique
- 397 First Unique Character in a String - *Easy*
   - Hash map
- 909 Snakes and Ladders - *Medium*
- 12 Integer to Roman - *Medium*
- 1492 The kth Factor of n - *Medium*
- 1152 Analyze User Website Visit Pattern - *Medium*
- 370 Range Addition - *Medium*
- 926 Flip String to Monotone Increasing - *Medium*
- 1710 Maximum Units on a Truck - *Easy*
- 207 Course Schedule - *Medium*
   - Adjacency list
- 1353 Maximum Number of Events That Can be Attended - *Medium*
- 210 Course Schedule II - *Medium*
   - Adjacency list
- 1481 Least Number of Unique Integers after K Removals - *Medium*
- 472 Concatenated Words - *Hard*
   - DFS
- 348 Design Tic-Tac-Toe - *Medium*
- 907 Sum of Subarray Minimums - *Medium*
- 642 Design Search Autocomplete System - *Hard*
- 1167 Minimum Cost to Connect Sticks - *Medium*
   - Heap (priority queue) (heapq)
- 1275 Find Winner on a Tic Tac Toe Game - *Easy*
- 1248 Count Number of Nice Subarrays - *Medium*
- 992 Subarrays with K Different Integers - *Hard*
- 1648 Sell Diminishing-Valued Colored Balls - *Medium*
- 1135 Connecting Cities with Minimum Cost - *Medium*
- 1151 Minimum Swaps to Group All 1’s Together - *Medium*
- 1628 Design an Expression Tree with Evaluate Function - *Medium*
- 1730 Shortest Path to Get Food - *Medium*

## Arrays and Strings

1 [Two Sum](https://leetcode.com/problems/two-sum)

- Brute Force O(n^2), O(1)
- Two-Pass Hash Table O(n), O(n)
- One-Pass Hash Table O(n), O(n)

42 [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

- Brute Force *- O(n^2), O(1)*
- Dynamic Programming *- O(n), O(n)*
- Using Stacks *- O(n), O(n)*
- Using 2 pointers *- O(n), O(1)*

273 [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

- Divide and Conquer *- O(N), O(1)*

239 [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

- Use a Hammer (Bruteforce) *- O(Nk), O(N-k+1)*
- Dequeue *- O(N), O(k)*
- Dynamic Programming *- O(N), O(N)*

49 [Group Anagrams](https://leetcode.com/problems/group-anagrams)

- Categorize by Sorted String *- O(NK logK), O(NK)*
- Categorize by Count *- O(NK), O(NK)*

696 [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings)

- Group by Character *- O(N), O(N)*
- Linear Scan *- O(N), O(1)*

828 [Count Unique Characters of All Substrings of a Given String](https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/)

- Count for every char, how many ways to be found as a unique char using parentheses *- O(N)*

1268 [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/)

- Binary Search *- O(n log n) + O(m log n), between O(1) and O(n)*
- Trie + DFS *- O(M) number of characters in the products, O(n)*
+ 937 [Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
   - Comparator *- O(M N log N), O(M log N)*
   - Sorting by Keys *- O(M N logN), O(M N)*
+ 994 [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)
   - Breadth-First Search *- O(N), O(N)*
   - In-place BFS *- O(N^2), O(N)*
+ 387 [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string)
   - Linear Time Solution *- O(N), O(1)*
+ 909 [Snakes and Ladder](https://leetcode.com/problems/snakes-and-ladders/)
+ 12 [Integer to Roman](https://leetcode.com/problems/integer-to-roman)
   - Greedy *- O(1), O(1)*
   - Hardcode Digits *- O(1), O(1)*
+ 735 [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
   - Stack *- O(N), O(N)*
+ 926 [Flip String to Monotone Increasing](https://leetcode.com/problems/flip-string-to-monotone-increasing/)
   - Prefix Sums *- O(N), O(N)*
+ 370 [Range Addition](https://leetcode.com/problems/range-addition/)
   - Naïve Approach *- O(n k), O(1)*
   - Range Caching *- O(n+k), O(1)*
+ 1152 [Analyze User Website Visit Pattern](https://leetcode.com/problems/analyze-user-website-visit-pattern/)
+ 1710 [Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)
   - Brute Force *- O(n^2), O(1)*
   - Using Array Sort *- O(n log n), O(1)*
   - Using Priority Queue *- O(n log n), O(1)*
+ 472 [Concatenated Words](https://leetcode.com/problems/concatenated-words)
   - DFS
+ 907 [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums)
   - Stack
+ 1167 [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks)
   - Greedy *- O(N log N), O(N)*

## Linked Lists

23 [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

- Brute Force *- O(N log(N)), O(N)*
- Compare One by One *- O(kN), O(n)*
- Optimize 2nd Approach by Priority Queue *- O(N log(k)), O(n)*

## Trees and Graphs

200 [Number of Islands](https://leetcode.com/problems/number-of-islands)

- DFS *- O(MN), O(MN)*
- BFS *- O(MN), O(min(M,N))*
- Union Find (aka Disjoint Set) *- O(MN), O(MN)*

127 [Word Ladder](https://leetcode.com/problems/word-ladder)

- Breadth First Search *- O(M^2N), O(M^2N)*
- Bidirectional Breadth First Search *- O(M^2N), O(M^2N)*

863 [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

- Annotate Parent *- O(N), O(N)*
- Percolate Distance - *O(N), O(N)*

207 [Course Schedule](https://leetcode.com/problems/course-schedule)

- Backtracking *- O(|E| + |V|^2), O(|E| + |V|)*
- Postorder DFS (Depth First Search) *- O(|E| + |V|), O(|E| + |V|)*
- Topological Sort *- O(|E| + |V|), O(|E| + |V|)*

210 [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

- Using Depth First Search *- O(V+E), O(V+E)*
- Using Node Indegree *- O(V+E), O(V+E)*

## Recursion

79 [Word Search](https://leetcode.com/problems/word-search)

- Backtracking *- O(N 3^L), O(L)*

212 [Word Search II](https://leetcode.com/problems/word-search-ii)

- Backtracking with Trie *- O(M(4 3^(L-1))), O(N)*

## Sorting and Searching

56 [Merge Intervals](https://leetcode.com/problems/merge-intervals)

- Connected Components *- O(N^2), O(N^2)*
- Sorting *- O(N (log N)), O(log N)*

4 [*Median of Two Sorted Arrays*](https://leetcode.com/problems/median-of-two-sorted-arrays)

- Binary Search *- O(log(min(M,N))*

253 [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii)

- Priority Queues *- O(Nlog(N)), O(N)*
- Chronological Ordering *- O(N log(N)), O(N)*

973 [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

- Sort with Custom Comparator *- O(N log N), O(N)*
- Max Heap or Max Priority Queue *- O(N log k), O(k)*
- Binary Search *- O(N), O(N)*
- QuickSelect *- O(N), O(1)*
+ 1353 [Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended)
   - Priority Queue *- O(), O()*
+ 1481 [Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals)
+ 642 [Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)
   - Trie

## Design

146 [LRU Cache](https://leetcode.com/problems/lru-cache)

- Ordered Dictionnary *- O(1), O(capacity)*
- Hash Map + DoubleLinkedList *- O(1), O(capacity)*

295 [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)

- Simple Sorting *- O(N logN), O(n)*
- Insertion Sort *- O(n), O(n)*
- Two Heaps *- O(log n), O(n)*
- Multiset and Two Pointers *- O(log N), O(n)*
+ 460 [LFU Cache](https://leetcode.com/problems/lfu-cache/)
+ 348 [Design Tic-Tac-Toe](https://leetcode.com/problems/design-tic-tac-toe)
   - Optimized Brute Force *- O(n), O(n^2)*
   - Optimized Approach *- O(1), O(n)*
+ 1275 [Find Winner on a Tic Tac Toe Game](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/)
   - Brute Force *- O(m n), O(n^2)*
   - Record Each Move *- O(m), O(n)*

## Others

+ 829 [Consecutive Numbers Sum](https://leetcode.com/problems/consecutive-numbers-sum/)
   - Mathematical: Sum of first k Natural Numbers *- O(sqrt(N)), O(1)*
   - Mathematical: Decrease N gradually *- O(sqrt(N)), O(1)*
+ 1492 [The kth Factor of n](https://leetcode.com/problems/the-kth-factor-of-n)
   - Brute Force *- O(N), O(1)*
   - Heap *- O(sqrt(N) log k), O(min (k, log sqrt N))*
   - Math *- O(sqrt(N)), O(min (k, log sqrt N))*

