#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

class Grid
{
public:
	vector< vector<char> > g;
	int x, y;
	bool pd;
	
	void Move(int d, int l, bool ps)
	{
		pd = ps;
		while (l > 0)
		{
			if (pd)
				g[x][y] = '*';
			switch (d)
			{
			case 3:
				y++;
				break;
			case 4:
				y++;
				x++;
				break;
			case 5:
				x++;
				break;
			case 6:
				x++;
				y--;
				break;
			case 7:
				y--;
				break;
			case 8:
				x--;
				y--;
				break;
			case 1:
				x--;
				break;
			case 2:
				x--;
				y++;
				break;
			}
			moving(x,y);
			if (pd)
				g[x][y] = '*';
			l--;
		}
	}

	Grid()
	{
		g = vector< vector<char> >(21, vector<char>(21, 'X'));
		x = 10;
		y = 10;
		pd = false;
	}

	void Draw()
	{
		for (int i = 0; i < 21; i++)
		{
			for (int j = 0; j < 21; j++)
			{
				if (x == i && y == j)
					cout << 'O';
				else
					cout << g[i][j];
			}
		}
	}

private:
	void moving(int& x, int& y)
	{
		if (x > 20)
			x = 0;
		if (x < 0)
			x = 10;
		if (y > 20)
			y = 0;
		if (y < 0)
			y = 20;
	}
};

void main()
{
	ifstream in("prob6_in.txt");

	int dir, len, ps;
	Grid myg;

	while (in >> dir >> len >> ps)
		myg.Move(dir, len, ps);
	myg.Draw();
}