#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(void) {
	string a[8];
	string b;
	int cnt = 0;
	for (int i = 0; i < 8; i++)
	{
		cin >> b;
		a[i] = b;
	}
	for (int i = 0; i < 8; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			if (!((i+j)%2) and a[i].at(j) == 'F') {
				cnt++;
			}
		}
	}
	cout << cnt;
}