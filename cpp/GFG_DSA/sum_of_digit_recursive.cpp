#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int SumOfDigit(int n)
{
    if (n == 0)
        return 0;

    return SumOfDigit(n / 10) + n % 10;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    cout << SumOfDigit(9987);

    return 0;
}