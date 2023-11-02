/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func averageOfSubtree(_ root: TreeNode?) -> Int {

        func countNumberOfNodes(_ currNode: TreeNode,_ ans: inout Int) -> (Int, Int) {

            var currNum = 1, currSum = currNode.val

            if let left = currNode.left {

                let (n, s) = countNumberOfNodes(left, &ans)
                currNum += n
                currSum += s
            }

            if let right = currNode.right {
                let (n, s) = countNumberOfNodes(right, &ans)
                currNum += n
                currSum += s
            }

            let currAvg: Int = currSum / currNum
            if currAvg == currNode.val {
                ans += 1
            }
            return (currNum, currSum)
        }
        
        if let root = root {
            var answer = 0
            countNumberOfNodes(root, &answer)
            return answer

        } else {
            return 0    // no nodes
        }
    }
}