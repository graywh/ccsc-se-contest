#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int leapdays[] = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string months[] = {"January", "February", "March", "April", "May", "June", "July",
	"August", "September", "October", "November", "December"};

int main()
{
	ifstream in("prob2_in.txt");
	string line, day, month, monthday, tmp;
	int yyyy, mm, dd, newmm, newdd;
	while (getline(in, line))
	{
		if (line == "From veep@whitehouse.gov")
		{
			getline(in, line);
			if (line == "To buddha@whitehouse.gov")
			{
				days[1] = 28;
				dd = 0;
				in >> tmp >> day >> month >> monthday >> yyyy;
				if (monthday.length() == 2)
					dd = monthday[0] - '0';
				else
				{
					dd += (monthday[0] - '0') * 10;
					dd += (monthday[1] - '0');
				}
				if (((yyyy % 4 == 0) && (yyyy % 100)) || (yyyy % 400 == 0))
					days[1]++;
				for (int i = 0; i < 12; i++)
					if (month == months[i])
						mm = i;
				newmm = mm;
				newdd = dd + 7;
				if (newdd > days[mm])
				{
					newdd -= days[mm];
					newmm++;
				}
				if (newmm == 12)
				{
					newmm = 0;
					yyyy++;
				}
				cout << "From buddha@whitehouse.gov" << endl << "To veep@whitehouse.gov"
					<< endl << "Date " << day << " " << month << " " << monthday << " "
					<< yyyy << endl << "Subject Re: BM" << endl << endl
					<< "Thank you for advising me of your BM. You may not have" << endl
					<< "another BM until " << day << " " << months[newmm] << " " << newdd
					<< ", " << yyyy << endl << endl;
			}
		}
	}
}
