#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long N, num = 2;
    cin >> N;
    while (num <= N)
    {
        long div = 2;
        while (div < num)
        {
            if (num % div == 0)
                num++;
            else
                div++;
        }
        cout << endl
             << num;
        num++;
    }
}