#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

void main()
{
	ifstream in("prob3_in.txt");
	map<int, string> conv;
	conv[1] = "Bogey";
	conv[0] = "Par";
	conv[-1] = "Birdie";
	conv[-2] = "Eagle";
	conv[-3] = "Double Eagle";
	int n, h, s;
	in >> n;
	for (int i = 0; i < n; i++)
	{
		in >> h >> s;
		if (h + 1 < s)
			cout << "Double Bogey" << endl;
		else if (s == 1)
			cout << "Hole-in-one" << endl;
		else
			cout << conv[s - h] << endl;
	}
}
