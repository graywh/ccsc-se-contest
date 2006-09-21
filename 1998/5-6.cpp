#include <iostream>
#include <fstream>
using namespace std;

int mos[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

void main()
{
	ifstream in("prob6.in");
	int tmp, day, month, year;
	while (in >> tmp)
	{
		month = 0;
		mos[1] = 28;
		year = 1900 + tmp / 1000;
		if (year == 1900)
			year += 100;
		if (year % 4 == 0)
			mos[1]++;
		day = tmp % 1000;
		while (day > mos[month])
			day -= mos[month++];
		if (month < 9)
			cout << '0';
		cout << month + 1 << '/';
		if (day < 10)
			cout << '0';
		cout << day << '/' << year << endl;
	}
}
