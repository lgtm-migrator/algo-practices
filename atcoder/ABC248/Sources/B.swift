
import Foundation

func logicB(num: Int, cnt: Int = 0, B: Int, K: Int) -> Int {
    if num >= B {
        return cnt
    }
    return logicB(num: num * K, cnt: cnt + 1, B: B, K: K)
}

func main() {
    let nums = readLine()!.split(separator: " ").map({ Int($0)! })
    print(logicB(num: nums[0], B: nums[1], K: nums[2]))
}
