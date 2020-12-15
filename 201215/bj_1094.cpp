#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(void) {
	int N;
	cin >> N;
	int cnt = 0;
	int i = 64;
	while (i != 0) {
		if (N >= i) {
			cnt++;
		}
		N %= i;
		i /= 2;
		if (N == 0) {
			cout << cnt;
			return 0;
		}
	}
}