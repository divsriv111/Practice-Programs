/* Check kth bit is set or not*/
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void CheckKBit(int n, int k)
{
    //right shift bit method

    if ((n >> (k - 1) & 1) == 1)
        cout << "Yes";
    else
        cout << "No";
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int n, k;
    n = 13;
    k = 3;
    //cin >> n >> k;
    CheckKBit(n, k);
    return 0;
}