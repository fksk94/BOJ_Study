#include <iostream>

using namespace std;

int main(void) {
	int N, a, b, cnt = 0;
	bool ch = false;
	cin >> N >> a >> b;
	for (int j = 2; j < N*2+1; j*=2)
	{
		for (int i = 1; i < N; i += j)
		{
			if (i <= a && i <= b && a < i + j && b < i + j) {
				ch = true;
				break;
			}
		}
		cnt += 1;
		if (ch) {
			break;
		}
	}
	cout << cnt;
}