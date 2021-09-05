#include <iostream>
#include <bits/stdc++.h>
using namespace std;

double Factorial(int n)
{
    if (n == 0)
        return 1;
    return n * Factorial(n - 1);
}

int main()
{
    //region READ FROM FILE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    //end region

    int n;
    cin >> n;
    cout << Factorial(n);
    return 0;
}