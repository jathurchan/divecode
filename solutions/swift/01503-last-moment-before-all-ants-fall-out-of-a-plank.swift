class Solution {
    func getLastMoment(_ n: Int, _ left: [Int], _ right: [Int]) -> Int {
        var ans = Int.min
        for pos in left {
            ans = max(ans, pos)
        }
        for pos in right {
            ans = max(ans, n-pos)
        }

        return ans
    }
}