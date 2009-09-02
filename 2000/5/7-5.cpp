#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

struct Point
{
	double x, y;
	Point() : x(0), y(0)
	{}
};

double distance(Point a, Point b)
{
	return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2));
}

void main()
{
	ifstream in("prob5_in.txt");
	int ships, n1, n2, cnt = 1;
	double min, tmp;
	vector<Point> plot;
	while (in >> ships)
	{
		plot.reserve(ships);
		for (int i = 0; i < ships; i++)
			in >> plot[i].x >> plot[i].y;
		min = distance(plot[0], plot[1]);
		n1 = 0;
		n2 = 1;
		for (i = 0; i < ships - 1; i++)
		{
			for (int j = i + 1; j < ships; j++)
			{
				tmp = distance(plot[i], plot[j]);
				if (tmp < min)
				{
					min = tmp;
					n1 = i;
					n2 = j;
				}
			}
		}
		cout << "Fleet " << cnt++ << ": Ship " << n1 + 1 << " and Ship " << n2 + 1
			<< " are the closest pair." << endl;
		plot.clear();
	}
}
