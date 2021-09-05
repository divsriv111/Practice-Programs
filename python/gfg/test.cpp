#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void count2(int n)
{
    static int d = 1;
    cout << n;
    cout << d;
    d++;
    if (n > 1)
        count2(n - 1);
    cout << d;
}

int f(int n)
{
    static int i = 1;
    if (n >= 5)
        return n;
    n = n + i;
    i++;
    return f(n);
}

int main()
{
    cout << f(1);
    return 0;
}