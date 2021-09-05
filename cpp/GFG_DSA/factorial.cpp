#include <iostream>
#include <bits/stdc++.h>
using namespace std;

unsigned long long IterativeFactorial(long n)
{
    //iterative
    unsigned long long result = 1;
    for (long i = 2; i <= n; i++)
        result = result * i;

    return result;
}

unsigned long long RecursiveFactorial(long n)
{
    //resursive
    if (n == 0)
        return 1;
    return n * RecursiveFactorial(n - 1);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    long n;
    cin >> n;
    cout << IterativeFactorial(n);

    return 0;
}