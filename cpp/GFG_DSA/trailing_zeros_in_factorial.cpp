#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int countTrailingZeros(int n)
{
    int res = 0;

    for (int i = 5; i <= n; i = i * 5)
    {
        res = res + (n / i);
    }

    return res;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    long n;
    cin >> n;
    cout << countTrailingZeros(n);

    return 0;
}