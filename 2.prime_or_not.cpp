#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long div = 2, a;
    cin >> a;
    while (div < a)
    {
        if (a % div == 0)
        {
            cout << endl
                 << "Not Prime";
            break;
        }
        div++;
    }
}