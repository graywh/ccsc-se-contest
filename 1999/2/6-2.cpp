#include <iostream>
#include <fstream>
#include <deque>
using namespace std;

void main()
{
	ifstream in("prob2.in");
	int numcoins;
	while (in >> numcoins)
	{
		deque<int> p1, p2;
		int worst = (numcoins * (numcoins + 1) / 4),
			best = (numcoins * (numcoins + 1) / 2) - worst,
			sum1 = 0, sum2 = 0;
		for (int i = numcoins; i > 0; i--)
		{
			if ((sum1 + i) <= best)
			{
				sum1 += i;
				p1.push_front(i);
			}
			else
			{
				sum2 += i;
				p2.push_front(i);
			}
		}
		cout << "Number of coins: " << numcoins << endl << "Pile 1 contains ";
		for (i = 0; i < p1.size(); i++)
			cout << p1[i] << ((i == p1.size() - 1) ? " ":", ");
		cout << "with value " << sum1 << "." << endl << "Pile 2 contiains ";
		for (i = 0; i < p2.size(); i++)
			cout << p2[i] << ((i == p2.size() - 1) ? " ":", ");
		cout << "with value " << sum2 << "." << endl;
	}
}  
