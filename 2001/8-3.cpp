#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void main()
{
	ifstream in("prob3.in");
	vector<int> ary;
	int channel = 1, cross, dim, tmp;
	while (!in.eof())
	{
		cross = 0;
		ary.clear();
		while (in >> tmp)
		{
			ary.push_back(tmp);
			if (in.peek() == '\n')
				break;
		}
		if (ary.empty())
			break;
		dim = ary.size();
		for (int i = 1; i < dim; i++)
			for (int j = 0; j < i; j++)
				if (ary[i] < ary[j])
					cross++;
		cout << "There are " << cross << " wire crossings in routing channel " << channel++
			<< endl;
	}
}
