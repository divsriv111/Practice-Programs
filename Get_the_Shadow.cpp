#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int Find(long a[], int n)
{
    int x1 = a[0];
    int x2 = 1;

    for (long i = 1; i < n; i++)
    {
        x1 = x1 ^ a[i];
        int j = i - 1;
        if (a[abs(a[j])] >= 0)
            a[abs(a[j])] = -a[abs(a[j])];
        else
            cout << abs(a[j]) << " ";
    }

    for (long i = 2; i <= n + 1; i++)
        x2 = x2 ^ i;

    cout << (x1 ^ x2) << endl;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int t;
    long n;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        long arr[n];
        for (long j = 0; j < n; j++)
        {
            cin >> arr[j];
        }
        Find(arr, n);
    }

    return 0;
}