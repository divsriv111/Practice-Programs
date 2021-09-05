#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void PrintPrimeFactors(int n)
{
    int two = 0;
    int three = 0;
    int five = 0;
    int other = 0;
    int factor = 0;

    if (n <= 1)
        return;
    while (n % 2 == 0)
    {
        two++;
        n = n / 2;
    }
    while (n % 3 == 0)
    {
        three++;
        n = n / 3;
    }
    for (int i = 5; i * i <= n; i = i + 6)
    {
        while (n % i == 0)
        {
            if (i == 2)
                two++;
            else if (i == 3)
                three++;
            else if (i == 5)
                five++;
            n = n / i;
        }

        while (n % (i + 2) == 0)
        {
            if ((i + 2) == 2)
                two++;
            else if ((i + 2) == 3)
                three++;
            else if ((i + 2) == 5)
                five++;
            n = n / (i + 2);
        }
    }

    if (n > 3)
        other++;

    factor = (1 + two) + (1 + three) + (1 + five) + (1 + other);
    cout << factor + 1;
}

int main()
{
    // //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // //end region
    int n;
    cin >> n;
    PrintPrimeFactors(n);

    return 0;
}