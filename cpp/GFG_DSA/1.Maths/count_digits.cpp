#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int CountDigit(int n)
{
    return floor(log10(n) + 1);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int n;
    cin >> n;
    cout << CountDigit(n);

    return 0;
}