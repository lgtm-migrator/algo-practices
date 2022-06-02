import Foundation

func ABC250_A(H: Int, W: Int, R: Int, C: Int) -> Int {
  var ret = 0
  for h in 1...H {
    for w in 1...W {
      if abs(w - R) + abs(h - C) == 1 {
        ret += 1
      }
    }
  }
  return ret
}
