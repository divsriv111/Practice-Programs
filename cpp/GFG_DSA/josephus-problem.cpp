#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Jos(int n, int k)
{
    if (n == 1)
        return 0;

    return (Jos(n - 1, k) + k) % n;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    cout << Jos(5, 3);
    return 0;
}