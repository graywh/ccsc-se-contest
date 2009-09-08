#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main()
{
	int sum = 0, cnt = 0, num = 6, dig = 0;
	cout << "Perfect Number    Number of Digits" << endl
		<< "----------------------------------" << endl;
	while (cnt < 4)
	{
		for (int i = 1; i <= num / 2; i++)
		{
			if ((num % i) == 0)
				sum += i;
		}
		if (sum == num)
		{
			while (num / (int)pow(10, ++dig));
			cout << "     " << setw(4) << num << "              " << setw(4) << dig << endl;
			dig = 0;
			cnt++;
		}
		sum = 0;
		num += 2;
	}
/*
	cout << "        6                 1" << endl
		<< "       28                 2" << endl
		<< "      496                 3" << endl
		<< "     8128                 4" << endl;
*/
}
