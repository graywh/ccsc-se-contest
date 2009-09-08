#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
using namespace std;

struct Domino
{
	int side1, side2;
	Domino(int a, int b) : side1(a), side2(b)
	{}
};

vector<Domino> table;

int findSolutions(vector< vector<int> >& grid, vector< vector<int> >& map, int dom)
{
	int num = 0;
	if (dom == 29)
	{
		for (int r = 0; r < 7; r++)
		{
			for (int c = 0; c < 8; c++)
				cout << setw(3) << map[r][c];
			cout << endl;
  		}
  		cout << endl;
  		return 1;
	}
	
	for (int r = 0; r < 7; r++)
		for (int c = 1; c < 8; c++)
			if (((grid[r][c - 1] == table[dom].side1 && grid[r][c] == table[dom].side2) ||
			   (grid[r][c - 1] == table[dom].side2 && grid[r][c] == table[dom].side1)) &&
			   (map[r][c - 1] == -1 && map[r][c] == -1))
			{
				map[r][c - 1] = map[r][c] = dom;
				num += findSolutions(grid, map, dom+1);
				map[r][c - 1] = map[r][c] = -1;
   			}

	for (int r = 1; r < 7; r++)
		for (int c = 0; c < 8; c++)
			if (((grid[r - 1][c] == table[dom].side1 && grid[r][c] == table[dom].side2) ||
			   (grid[r - 1][c] == table[dom].side2 && grid[r][c] == table[dom].side1)) &&
			   (map[r - 1][c] == -1 && map[r][c] == -1))
			{
				map[r - 1][c] = map[r][c] = dom;
				num += findSolutions(grid, map, dom+1);
				map[r - 1][c] = map[r][c] = -1;
   			}
   	
   	return num;
}

int main()
{
	vector< vector<int> > grid(7, vector<int>(8));
	vector< vector<int> > map(7, vector<int>(8, -1));

	table.push_back(Domino(7,7));	table.push_back(Domino(0,0));
	table.push_back(Domino(0,1));	table.push_back(Domino(0,2));
	table.push_back(Domino(0,3));	table.push_back(Domino(0,4));
	table.push_back(Domino(0,5));	table.push_back(Domino(0,6));
	table.push_back(Domino(1,1));	table.push_back(Domino(1,2));
	table.push_back(Domino(1,3));	table.push_back(Domino(1,4));
	table.push_back(Domino(1,5));	table.push_back(Domino(1,6));
	table.push_back(Domino(2,2));	table.push_back(Domino(2,3));
	table.push_back(Domino(2,4));	table.push_back(Domino(2,5));
	table.push_back(Domino(2,6));	table.push_back(Domino(3,3));
	table.push_back(Domino(3,4));	table.push_back(Domino(3,5));
	table.push_back(Domino(3,6));	table.push_back(Domino(4,4));
	table.push_back(Domino(4,5));	table.push_back(Domino(4,6));
	table.push_back(Domino(5,5));	table.push_back(Domino(5,6));
	table.push_back(Domino(6,6));
	
	ifstream in("prob6_in.txt");
	int gridnumber = 1;

	while ((char)in.peek() != -1)
	{
		for (int r = 0; r < 7; r++)
			for (int c = 0; c < 8; c++)
				in >> grid[r][c];
		in.ignore(100, '\n');
		
		cout << "Grid #" << gridnumber << ":" << endl << endl;
		for (int r = 0; r < 7; r++)
		{
			for (int c = 0; c < 8; c++)
				cout << " " << grid[r][c];
			cout << endl;
		}
		cout << endl;

		cout << "Maps resulting from grid #" << gridnumber << " are:" << endl << endl;
		int numsols = findSolutions(grid, map, 1);
		cout << "There are " << numsols << " solution(s) for grid #" << gridnumber++
			 << "." << endl << endl;
	}
	in.close();
}
