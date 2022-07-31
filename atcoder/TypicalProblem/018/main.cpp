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

double CalculateDegree(const double bottom, const double z)
{
    return atan(z / bottom) * 180 / M_PI;
}

double CalculateBottom(const double x, const double y)
{
    return sqrt(pow(x, 2) + pow(y, 2));
}

double CalculateZ(const double radianTheta, const double L)
{
    return L / 2 - L / 2 * cos(radianTheta);
}

double CalculateRadianTheta(const double ei, const double T)
{
    return ei / T * 2 * M_PI;
}

int main()
{
    double T;
    cin >> T;
    double L, X, Y;
    cin >> L >> X >> Y;
    double Q;
    cin >> Q;
    vector<double> E;
    for (ll i = 0; i < Q; i++)
    {
        ll e;
        cin >> e;
        E.push_back(e);
    }
    for (double e : E)
    {
        double theta = CalculateRadianTheta(e, T);
        double z = CalculateZ(theta, L);
        double y = Y - (-L / 2) * sin(theta);
        double bottom = CalculateBottom(X, y);
        double degree = CalculateDegree(bottom, z);
        cout << fixed << setprecision(10) << degree << endl;
    }
    return 0;
}
