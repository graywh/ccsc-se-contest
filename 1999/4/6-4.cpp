#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream in("prob4_in.txt");
	int dim;
	while (in >> dim)
	{
		int diag = 0;
		bool magic = true;
		vector< vector<int> > grid(dim + 1, vector<int>(dim + 1));
		for (int i = 0; i < dim + 1; i++)
		{
			for(int j = 0; j < dim; j++)
			{
				in >> grid[i][j];
				grid[dim][j] = 0;
			}
			grid[i][dim] = 0;
		}
		grid[dim][dim] = 0;
		for (i = 0; i < dim; i++)
		{
			grid[dim][dim] += grid[i][i];
			diag += grid[dim - i - 1][i];
			for (int j = 0; j < dim; j++)
			{
				grid[i][dim] += grid[i][j];
				grid[dim][j] += grid[i][j];
			}
		}
		for (i = 0; i < dim; i++)
		{
			if (grid[i][dim] != diag)
				magic = false;
			if (grid[dim][i] != diag)
				magic = false;
		}
		if (grid[dim][dim] != diag)
			magic = false;
		if (magic)
			cout << "HOCUS" << endl;
		else
			cout << "POCUS" << endl;
	}
}
