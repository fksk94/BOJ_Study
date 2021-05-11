#include <iostream>
#include <string>

using namespace std;

string s;

int main(void) {
	cin >> s;
	char before = s[0];
	int cnt = 1;
	for (int i = 0; i < s.length(); i++)
	{
		if (before == s[i]) {
			continue;
		}
		else {
			before = s[i];
			cnt += 1;
		}
	}
	cout << cnt/2;
}