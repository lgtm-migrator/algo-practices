#include <atcoder/all>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>

using namespace atcoder;
using namespace std;
using ll = long long;

int main()
{
    double a, b, d;
    cin >> a >> b >> d;
    double radi = d * M_PI / 180 + atan2(b * 1000, a * 1000);
    double length = sqrt(a * a + b * b);
    // cout << radi << " " << length << endl;
    double x = length * cos(radi);
    double y = length * sin(radi);
    cout.precision(10);
    cout << x << " ";
    cout << y << endl;
    return 0;
}
