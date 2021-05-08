#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void merge(int arr1[], int arr2[], int n, int m)
{
    int result[n + m];
    int i, j, k = 0;
    int val1 = arr1[i];
    int val2 = arr1[j];

    while (1)
    {
        if (i == n && j == m)
            break;
        if (val1 <= val2)
        {
            result[k++] = val1;
            val1 = arr1[++i];
        }
        else
        {
            result[k++] = val1;
            val1 = arr1[++i];
        }
        }
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    return 0;
}