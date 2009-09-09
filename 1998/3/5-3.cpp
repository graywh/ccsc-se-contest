#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    int z, i, m, l;
    cout << "Z  I  M  L  Length" << endl
        <<  "------------------" << endl;
    while (cin >> z >> i >> m >> l)
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
