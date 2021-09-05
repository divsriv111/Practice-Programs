#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void PrintPowerSet(string str)
{
    /*Elements in power set = 2^n - 1
    we will have a counter variable which will start from 0 to 2^n -1.
    Each value of counter variable will be converted to bits 
    and each bit will represent the element of the string.
    000 -> ""
    001 -> "a"
    010 -> "b"
    011 -> "ab"
    */
    int n = str.length();

    int powSize = pow(2, n);

    for (int counter = 0; counter < powSize; counter++)
    {
        for (int j = 0; j < n; j++)
        {
            if ((counter & (1 << j)) != 0)
                cout << str[j];
        }

        cout << endl;
    }
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    string s = "abc";
    PrintPowerSet(s);

    return 0;
}