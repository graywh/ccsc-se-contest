#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void main()
{
	ifstream in("prob3_in.txt");
	int z, i, m, l;
	cout << "\nZ  I  M  L  Length" << endl
		<< "------------------" << endl;
	while (in >> z >> i >> m >> l)
	{
		int cnt = 0, start;
		cout << setiosflags(ios::left) << setw(3) << z << setw(3) << i << setw(3) << m
			<< setw(3) << l;
		l = start = ((z * l + i) % m);
		if (m == 1)
		{
			cout << "ERROR" << endl;
			break;
		}
		else
		{
			do
			{
				l = ((z * l + i ) % m);
				cnt++;
			}
			while (start != l);
			cout << setw(3) << cnt << endl;
		}
	}
}
