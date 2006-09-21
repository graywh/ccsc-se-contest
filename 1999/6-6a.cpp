#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	ifstream in("prob6.in");
	int caproom, cnt = 1, n, tmp;
	vector<int> conts;
	vector<int> ship;
	while (in >> caproom >> n)
	{
		for (int i = 0; i < n; i++)
		{
			in >> tmp;
			conts.push_back(tmp);
		}
		sort(conts.begin(), conts.end());
		reverse(conts.begin(), conts.end());
		while (caproom >= conts.back())
		{
			ship.push_back(conts.back());
			caproom -= conts.back();
			conts.pop_back();
		}
		if (caproom > 0)
			for (int i = 0; i < conts.size(); i++)
				for (int j = 0; j < ship.size(); j++)
					if ((caproom + ship[j] >= conts[i]) && (ship[j] < conts[i]))
					{
						caproom += ship[j];
						caproom -= conts[i];
						ship[j] = conts[i];
					}
		cout << "Ship " << cnt++ << endl << "------" << endl
			<< "Number of containers loaded: " << ship.size() << endl
			<< "Weight under capacity: " << caproom << endl << endl;
		ship.clear();
		conts.clear();
	}
}
