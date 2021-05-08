#include <iostream>
#include <bits/stdc++.h>
using namespace std;

double method1(long n)
{
    //iterative method
    int count = 0;
    while (n != 0)
    {
        n = n / 10;
        ++count;
    }
    return count;
}

double method2(long n)
{
    //recursive solution
    if (n == 0)
        return 0;
    return 1 + method2(n / 10);
}

double method3(long n)
{
    //log method
    return floor(log10(n) + 1);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    long N;
    cin >> N;
    cout << method1(N) << endl;
    cout << method2(N) << endl;
    cout << method3(N) << endl;
    return 0;
}
