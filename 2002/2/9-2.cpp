#include <iostream>
using namespace std;

int main()
{
    int x, y, total, min;
    while (cin >> min)
    {
        x = min / 60;
        y = min % 60;
        total = x / 2 * 900;
        total -= x / 2 * 600;
        if (x % 2 == 0)
            total += y * 15;
        else
        {
            total += 900;
            total -= y * 10;
        }
        if ((min <= 720) && (min >= 0))
            cout << total << endl;
    }
}
