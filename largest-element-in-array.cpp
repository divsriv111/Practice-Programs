#include <iostream>
#include <bits/stdc++.h>
using namespace std;

/*Returns index of largest element in an array*/
int LargestElementIndex(int a[], int n)
{
    int index = 0;
    for (int i = 0; i < n; i++)
    {
        if (a[i] > a[index])
            index = i;
    }
    return index;
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int a[] = {1, 2, 3, 99, 6};
    int n = sizeof(a) / sizeof(a[0]);
    cout << LargestElementIndex(a, n);

    return 0;
}