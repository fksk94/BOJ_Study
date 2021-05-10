#include <iostream>

using namespace std;

int main(void) {
	int i = 1;
	while (true) {
		int L, P, V;
		cin >> L >> P >> V;
		if (L == 0 && P == 0 && V == 0) {
			break;
		}
		int res = L * (V / P);
		if (L < V - P * (V / P)) {
			res += L;
		}
		else {
			res += V - P * (V / P);
		}
		cout << "Case " << i << ": " << res << endl;
		i++;
	}
}