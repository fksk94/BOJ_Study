#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

int main(void) {
	string a;
	string b = "0";
	int cnt = 1;
	while (true)
	{
		cnt = 1;
		cin >> a;
		if ( a.compare(b) == 0 ) {
			return 0;
		}
		else {
			for (int j = 0; j < a.length(); j++)
			{
				if ('0' == a.at(j)){
					cnt += 5;
				}
				else if ('1' == a.at(j)) {
					cnt += 3;
				}
				else {
					cnt += 4;
				}
			}
			cout << cnt << endl;
		}
	}
	return 0;
}