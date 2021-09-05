#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool IsPalindrome(int n)
{
    int rev = 0, original = n;
    while (n != 0)
    {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return original == rev;
}

int main()
{
    //region READ FROM FILE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    //end region

    int n;
    cin >> n;
    cout << IsPalindrome(n);

    return 0;
}