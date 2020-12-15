#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
	int* a = new int[1000000]{0,};
	int d, e, f;
	cin >> d;
	for (int i = 0; i < d; i++)
	{
		cin >> e >> f;
		while (e > 0) {
			if (f - 1 == -1) {
				cout << -1 << endl;
				return 0;
			}
			if (a[f - 1] == 1) {
				f--;
			}
			else {
				a[f - 1]++;
				f--;
				e--;
			}
		}
		if (i == d - 1) {
			for (int j = 0; j < 1000000; j++)
			{
				if (a[j] == 1) {
					cout << j << endl;
					return 0;
				}
			}
		}
	}
}