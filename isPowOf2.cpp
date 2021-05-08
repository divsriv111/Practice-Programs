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

bool NaiveMethod(int n)
{
    if (CountSetBit(n) == 1)
        return true;
    return false;
}

bool isPow2(int n)
{
    return (n != 0) && ((n & (n - 1)) == 0);
}
int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region
    int n = 16;
    cout << NaiveMethod(n) << endl;
    cout << isPow2(n);

    return 0;
}