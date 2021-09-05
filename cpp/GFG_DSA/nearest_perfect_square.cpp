#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool isPerfectSquare(long long x)
{
    if (x >= 0)
    {
        long long sr = sqrt(x);
        return (sr * sr == x);
    }
    return false;
}

unsigned long long NearSquare(unsigned long long n)
{
    if (n == 1)
        return 0;
    if (n < 5)
        return 2;
    while (!isPerfectSquare(--n))
        ;

    return n;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int t;
    unsigned long long n;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        cout << NearSquare(n) << endl;
    }

    return 0;
}