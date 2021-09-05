#include <iostream>
#include <bits/stdc++.h>
using namespace std;

void TOH(int n, char A, char B, char C)
{
    if (n == 1)
    {
        cout << "Move 1 from " << A << " to " << C << endl;
        return;
    }
    TOH(n - 1, A, C, B);
    cout << "Move " << n << " from " << A << " to " << C << endl;
    TOH(n - 1, B, A, C);
}

int main()
{
    //region READ FROM FILE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    //end region
    TOH(5, 'A', 'C', 'B');
    return 0;
}