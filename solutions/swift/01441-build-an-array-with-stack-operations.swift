class Solution {
    func buildArray(_ target: [Int], _ n: Int) -> [String] {
        var ans: [String] = []
        var currentIndex = 0, num = 1

        for num in 1...n {
            if currentIndex == target.count {
                break
            }
            ans.append("Push")
            if target[currentIndex] == num {
                currentIndex += 1
            } else {
                ans.append("Pop")
            }
        }

        return ans

    }
}