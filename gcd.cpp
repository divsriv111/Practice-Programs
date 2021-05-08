#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int gcdOptimized(int a, int b)
{
    // O(log(min(a, b)))
    if (b == 0)
        return a;
    else
        gcdOptimized(b, a % b);
}

int gcd(int a, int b)
{
    int n = min(a, b);
    for (n; n > 0; n--)
    {
        if (a % n == 0 && b % n == 0)
            return n;
    }
    return 1;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int a, b;
    cin >> a >> b;
    cout << gcdOptimized(a, b);

    return 0;
}