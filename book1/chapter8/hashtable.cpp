#include <iostream>
#include <unordered_set>
#include <cassert>

using namespace std;

int main()
{
    unordered_set<string> names{"1st element", "2nd element", "3rd element"};
    names.insert("4th element");
    names.erase("1st element");
    assert(!names.count("1st element"));
    assert(names.count("2nd element"));
    return 0;
}