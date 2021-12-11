#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

string ReverseStr(string s)
{
    string r = "";
    for (int i = s.length() - 1; i > -1; i--)
        r = r + s[i];
    return r;
}

int main()
{
    //region READ FROM FILE
    freopen("../input.txt", "r", stdin);
    freopen("../output.txt", "w", stdout);
    //end region

    string n;
    getline(cin, n);
    cout << ReverseStr(n);
    return 0;
}