#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int main() {
	int N, m, M, T, R, cnt, time;
	cin >> N >> m >> M >> T >> R;
	cnt = 0;
	time = 0;
	int first_m = m;
	int max_rutin = 10000;
	
	if (M - m < T) {
		cout << -1 << endl;
		return 0;
	}

	while (cnt < N)
	{
		if (m + T <= M)
		{
			m = m + T;
			cnt++;
			time++;
		}
		else {
			time++;
			m = max(m - R, first_m);
		}
	}
	cout << time << endl;
	return 0;
}