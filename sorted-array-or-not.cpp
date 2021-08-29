#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool IsSorted(int a[], int n)
{
    if (n <= 0)
        return true;
    int max = a[0];
    for (int i = 1; i < n; i++)
    {
        if (max > a[i])
            return false;
        else
            max = a[i];
    }
    return true;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int a[] = {8, 7, 6, 5, 4, 3, 2};
    int b[] = {1, 2, 3, 4, 7, 8, 9};
    int c[] = {1};
    int n = sizeof(a) / sizeof(a[0]);
    int m = sizeof(b) / sizeof(b[0]);

    cout << IsSorted(a, n) << endl;
    cout << IsSorted(b, m) << endl;
    cout << IsSorted(c, 1) << endl;

    return 0;
}