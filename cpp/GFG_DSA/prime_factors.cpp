#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void PrintPrimeFactors(int n)
{
    // O( sqrt(n))
    if (n <= 1)
        return;
    while (n % 2 == 0)
    {
        cout << 2;
        n = n / 2;
    }
    while (n % 3 == 0)
    {
        cout << 3;
        n = n / 3;
    }
    for (int i = 5; i * i <= n; i = i + 6)
    {
        while (n % i == 0)
        {
            cout << i;
            n = n / i;
        }

        while (n % (i + 2) == 0)
        {
            cout << (i + 2);
            n = n / (i + 2);
        }
    }

    if (n > 3)
        cout << n;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int n;
    cin >> n;
    PrintPrimeFactors(n);

    return 0;
}