#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int CountSetBit(int n)
{
    int res = 0;
    while (n > 0)
    {
        n = n & (n - 1);
        res++;
    }
    return res;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int n = 13;
    cout << CountSetBit(n);
    return 0;
}