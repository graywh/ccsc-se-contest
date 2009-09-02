#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	ifstream in("prob5_in.txt");
	string line;
	vector<int> tasks;
	int sum1, sum2;
	while (getline(in, line))
	{
		if (line.empty())
		{
			cout << 0 << endl;
			continue;
		}
		sum1 = 0;
		sum2 = 0;
		tasks.clear();
		for (int i = 1; i < line.length() - 1; i++)
		{
			int cur = 0;
			if (isdigit(line[i]))
			{
				cur = (int)(line[i] - '0');
				i++;
				if (isdigit(line[i]))
				{
					cur = cur * 10 + (int)(line[i] - '0');
					i++;
					if (isdigit(line[i]))
						cur = cur * 10 + (int)(line[i] - '0');
				}
				tasks.push_back(cur);
			}
		}
		if (tasks.size() == 0)
			cout << 0 << endl;
		else
		{
			sort(tasks.begin(), tasks.end());
			reverse(tasks.begin(), tasks.end());
			sum1 = tasks[0];
			for (int i = 1; i < tasks.size(); i++)
			{
				int cur = tasks[i];
				if (sum1 >= sum2)
					sum2 += cur;
				else
					sum1 += cur;
			}
			cout << (sum1 > sum2 ? sum1 : sum2) << endl;
		}
	}
}
