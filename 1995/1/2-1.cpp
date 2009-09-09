#include <iostream>
using namespace std;

int main()
{
    int a, b, sum;
    while (cin >> a >> b)
    {
        cout << a << " x " << b << " = ";
        sum = 0;
        while (a > 0)
        {
            if (a % 2)
            {
                cout << b;
                sum += b;
                if (a > 1)
                    cout << " + ";
            }
            a /= 2;
            b *= 2;
        }
        cout << " = " << sum << endl;
    }
}
