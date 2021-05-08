#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void PrintArray(int a[], int n)
{
    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
}

void DeleteArrayElement(int a[], int n, int x)
{
    bool flag = false;
    for (int i = 0; i < n; i++)
    {
        if (flag)
            break;

        if (a[i] == x)
        {
            for (int j = i; j < n - 1; j++)
            {
                a[j] = a[j + 1];
            }
            flag = true;
        }
    }
    PrintArray(a, n - 1);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region

    int a[] = {3, 8, 12, 5, 6};
    int x = 8;
    int n = sizeof(a) / sizeof(a[0]);
    DeleteArrayElement(a, n, x);

    return 0;
}