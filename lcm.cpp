#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int gcd(int a, int b)
{
    // O(log(min(a, b)))
    if (b == 0)
        return a;
    else
        gcd(b, a % b);
}

//a * b = HCF(a,b) * LCM(a,b)
int lcm(int a, int b)
{
    return (a * b) / gcd(a, b);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int a, b;
    cin >> a >> b;
    cout << lcm(a, b);

    return 0;
}