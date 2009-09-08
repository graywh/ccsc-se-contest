#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <string>
#include <map>
using namespace std;

int main()
{
	ifstream in("prob4_in.txt");
	string name;
	map<int,int> points;
	points[0] = 500;
	points[1] = 300;
	points[2] = 250;
	points[3] = 200;
	points[4] = 150;
	points[5] = 100;
	points[6] = 75;
	points[7] = 50;
	points[8] = 25;
	points[9] = 10;
	while (in >> name)
	{
		cout << endl << "Score Summary for " << name << endl
			<< "-----------------------" << endl;
		int score = 0, d = 0, x = 0, y = 0, n = 0;
		double dist = 0;
		for (int i = 1; i < 6; i++)
		{
			in >> x >> y;
			dist = sqrt(x * x + y * y);
			d = dist / 50;
			if ((int)dist == dist)
				if ((((int)dist % 50) == 0) && (d > 0))
					d--;
			n = points[d];
			score += n;
			cout << "   Hit " << i << " =" << setw(13) << n << endl;
			d = 0;
		}
		cout << "              ---------" << endl
			<< "   Score =" << setw(13) << score << endl;
	}
}
