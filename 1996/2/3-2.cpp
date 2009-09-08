#include <iostream>
#include <fstream>
#include <string>
using namespace std;

long daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
string days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

int jan1(long mm, long dd, long yyyy)
{
    return ((36 + (yyyy - 1) + ((yyyy - 1) / 4) - ((yyyy - 1) / 100) + ((yyyy - 1) / 400)) % 7);
}

int leap(long yyyy)
{
    return (((((yyyy % 4) == 0) && ((yyyy % 100) != 0))) || ((yyyy % 400) == 0));
}

int validDay(long mm, long dd, long yyyy)
{
    return (daysInMonth[mm - 1] + (leap(yyyy) && mm == 2));
}

int valid(long mm, long dd, long yyyy)
{
    return ((mm > 0) && (mm <= 12) && (dd > 0) && (dd <= validDay(mm, dd, yyyy)) && (yyyy > 0));
}

int main()
{
    ifstream in("dates.dat");
    long mm, dd, yyyy, dp;
    dp = dd = mm = yyyy = 0;
    char ch;
    while (in >> mm >> ch >> dd >> ch >> yyyy)
    {
        if (!valid(mm,dd,yyyy))
        {
            cout << "Invalid date in the input." << endl;
            continue;
        }
        for (int i = 0; i < (mm - 1); i++)
            dp += daysInMonth[i];
        dp += dd;
        dp += jan1(mm,dd,yyyy);
        dp--;
        cout << mm << "/" << dd << "/" << yyyy << " falls on a " << days[dp % 7] << endl;
        dp = dd = mm = yyyy = 0;
    }
}
