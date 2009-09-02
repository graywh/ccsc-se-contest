#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void main()
{
	ifstream in("prob6_in.txt");
	vector<int> test, perc;
	vector<float> test2;
	int bagC, cont, tmp, val, cnt = 1;
	float max;
	while (in >> bagC >> cont)
	{
		for (int i = 0; i < cont * 2; i++)
		{
			in >> tmp;
			test.push_back(tmp);
		}
		for (int j = 0; j < cont; j++)
		{
			test2.push_back((test[j + cont]) / (float)test[j]);
			perc.push_back(0);
		}
		tmp = 0;
		while (tmp <= bagC)
		{
			max = 0;
			val = 0;
			for (int k = 0; k < cont; k++)
				if (test2[k] > max)
				{
					max = test2[k];
					val = k;
				}
			if (max != 0)
			{
				if (tmp + test[val] <= bagC)
				{
					tmp += test[val];
					perc[val] = 100;
				}
				else
				{
					perc[val] = (bagC - tmp) * 100 / test[val];
					tmp = bagC;
				}
				test2[val] = 0;
			}
			else
				break;
		}
		cout << "Game " << cnt++ << endl << "------" << endl;
		for (int q = 0; q < cont; q++)
			cout << "Container " << q + 1 << ": " << perc[q] << "%" << endl;
		cout << endl;
		test.clear();
		test2.clear();
		perc.clear();
	}
}
