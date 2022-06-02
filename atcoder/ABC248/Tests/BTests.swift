import XCTest
@testable import ABC248

class Tests: XCTestCase {
    func test_B() {
        var ret = logicB(num: 1, B: 4, K: 2)
        XCTAssertEqual(ret, 2)
        ret = logicB(num: 7, B: 7, K: 10)
        XCTAssertEqual(ret, 0)
    }
}
