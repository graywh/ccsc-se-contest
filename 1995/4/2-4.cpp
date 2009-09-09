#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    string ary = "0000000", chk = "1000001";
    int cnt;
    for (int i = 0; i < 6; i++)
        cin >> ary[i];
    while (cin >> ary[6])
    {
        if (ary == chk)
        {
            while (true)
            {
                cnt = 0;
                for (int i = 0; i < 7; i++)
                    cin >> ary[i];
                if (ary == chk) break;
                for (i = 0; i < 7; i++)
                    cnt += (int)(ary[i] - '0') * pow(2, 6 - i);
                cout << (char)cnt;
            }
        }
        for (int i = 0; i < 6; i++)
            ary[i] = ary[i + 1];
    }
    cout << endl;
}
