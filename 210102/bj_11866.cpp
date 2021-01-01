#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main(void) {
	int N, K;
	queue<int> q;
	cin >> N >> K;
	cout << "<";
	for (int i = 1; i <= N; i++) {
		q.push(i);
	}
	while (!q.empty()) {
		for (int j = 0; j < K - 1; j++) {
			q.push(q.front());
			q.pop();
		}
		cout << q.front();
		q.pop();
		if (!q.empty())
			cout << ", ";
	}
	cout << ">";
}