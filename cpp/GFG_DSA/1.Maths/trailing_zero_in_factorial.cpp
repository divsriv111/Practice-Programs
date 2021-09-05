#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int CountTrailingZeros(int n)
{
    int res = 0;
    for (int i = 5; i <= n; i *= 5)
    {
        res = res + n / i;
    }
    return res;
}

int main()
{
    //region READ FROM FILE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    //end region

    int n;
    cin >> n;
    cout << CountTrailingZeros(n);
    return 0;
}