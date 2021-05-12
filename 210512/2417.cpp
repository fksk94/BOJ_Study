#include <iostream>
#include <cmath>
#include <cstdlib>

using namespace std;

int main(void) {
	unsigned long long N, res;
	cin >> N;
	if (N == 0) {
		cout << 0;
	}
	else {
		res = sqrt(N);
		if (N % res) {
			cout << res + 1;
		}
		else {
			cout << res;
		}
	}
}