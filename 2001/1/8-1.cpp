#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

void main()
{
	ifstream in("prob1.in");
	int cnt, n, tmp;
	while (in >> n)
	{
		cnt = 0;
		tmp = n;
		while ((tmp != 4) && (tmp != 2) && (tmp != 1))
		{
			cnt++;
			if (!(tmp % 2))
				tmp /= 2;
			else
				tmp = (tmp * 3) + 1;
		}
		cout << cnt << " steps were necessary for " << n << endl;
	}
}
