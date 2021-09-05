#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int GCD(int a, int b)
{
    if (b == 0)
        return a;
    return GCD(b, a % b);
}

int main()
{
    //region READ FROM FILE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    //end region

    int a, b;
    cin >> a >> b;
    cout << GCD(a, b);
    return 0;
}