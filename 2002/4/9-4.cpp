#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	ifstream in("prob4_in.txt");
	int x, cnt;
	string line;
	while (getline(in, line))
	{
		if (line.empty())
		{
		}
		cnt = 0;
		x = 1;
		for (int i = 0; i < line.length(); i++)
		{
			if (x >= 0)
			{
				cnt++;
				if (line[i] == 'e')
					x++;
				else
					x--;
			}
		}
		cout << (x >= 0 ? -1 : cnt) << endl;
	}
}
