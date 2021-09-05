#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool IsPalindrome(string &str, int start, int end)
{
    if (start >= end)
        return true;

    return (str[start] == str[end]) && IsPalindrome(str, start + 1, end - 1);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    string s = "abba";
    cout << IsPalindrome(s, 0, s.length() - 1);
    s = "acbac";
    cout << IsPalindrome(s, 0, s.length() - 1);

    return 0;
}