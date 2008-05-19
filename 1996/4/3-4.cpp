#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void main()
{
	ifstream in("buffy.dat");
	vector< vector<string> > ary;
	vector<string> tvec;
	long rows, cols;
	int msg = 1;
	string input;
	while (in >> rows >> cols)
	{
		for (int i = 0; i < rows; i++)
		{
			for (int j = 0; j < cols; j++)
			{
				in >> input;
				tvec.push_back(input);
			}
			ary.push_back(tvec);
			tvec.clear();
		}
		
		cout << "Message " << msg << " => ";
		
		int j = cols - 1;
		for (int i = 0; i < rows; i++)
		{
			cout << ary[i][j] << " ";
			j--;
			if (j < 0)
				j = cols - 1;
		}
		cout << endl;
		msg++;
		
		for (int i = 0; i < rows; i++)
			ary[i].clear();
		ary.clear();
	}
}
