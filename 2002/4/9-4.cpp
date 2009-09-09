#include <iostream>
#include <string>
using namespace std;

int main()
{
    int x, cnt;
    string line;
    while (getline(cin, line))
    {
        if (line.empty())
        {
        }
        cnt = 0;
        x = 1;
        for (int i = 0; i < line.length(); i++)
        {
            if (x >= 0)
            {
                cnt++;
                if (line[i] == 'e')
                    x++;
                else
                    x--;
            }
        }
        cout << (x >= 0 ? -1 : cnt) << endl;
    }
}
