#include <iostream>
#include <set>

using namespace std;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
int board[5][5];
set<int> s;

void dfs(int i, int j, int sum_val, int cnt) {
	if (cnt == 6) {
		s.insert(sum_val);
		return;
	}
	for (int k = 0; k < 4; k++) {
		int x = i;
		int y = j;
		x += dx[k];
		y += dy[k];
		if (x >= 0 && y >= 0 && x < 5 && y < 5) {
			dfs(x, y, sum_val*10 + board[x][y], cnt+1);
		}
	}
}

int main(void) {
	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			cin >> board[i][j];
		}
	}

	for (int i = 0; i < 5; i++)
	{
		for (int j = 0; j < 5; j++)
		{
			dfs(i, j, 0, 0);
		}
	}
	cout << s.size();
}