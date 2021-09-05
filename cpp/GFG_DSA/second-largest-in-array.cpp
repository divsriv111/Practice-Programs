#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int secondLargest(int a[], int n)
{
    if (n == 0 || n == 1)
        return -1;

    int second_max_index = 0;
    for (int i = 1; i < n; i++)
    {
        if (a[i] < a[second_max_index])
        {
            second_max_index = i;
        }
    }
    return second_max_index;
}

int main()
{
    //region READ FROM FILE
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    //end region

    int a[] = {1, 2, 3, 4, 5};
    int b[] = {10, 10, 7};
    int n = 5;
    cout << secondLargest(b, 3) << endl;
    cout << secondLargest(a, n);
    return 0;
}