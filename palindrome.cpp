#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool IsPalindrome(unsigned long long n)
{
    unsigned long long temp = n;
    unsigned long long rev = 0;
    while (temp > 0)
    {
        int a = temp % 10;
        rev = (rev * 10) + a;
        temp = temp / 10;
    }
    return n == rev;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region
    unsigned long long n;
    cin >> n;
    cout << IsPalindrome(n);

    return 0;
}