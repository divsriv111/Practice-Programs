#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	cin >> a >> b >> c;
	if (a > b)
		if (a > c)
			cout << endl
			<< a;
		else
			cout << endl
			<< c;
	else if (b > c)
		cout << endl
		<< b;
	else
		cout << c;
}
