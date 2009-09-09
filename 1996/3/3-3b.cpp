#include <iostream>
#include <string>
using namespace std;

int main()
{
    char ch, tc;
    int cnt = 0;
    while (cin.get(ch))
    {
        switch (ch)
        {
            case ',': case '.': case ';': case ':': case '?': case '!': case ' ': case '\n':
                cnt++;
                tc = cin.peek();
                while (tc == ' ' || tc == '\n' || tc == '.' || tc == ',' || tc == ':' ||
                        tc == ';' || tc == '?' || tc == '!')
                {
                    cin.ignore();
                    tc = cin.peek();
                }
        }
    }
    cout << "This file contains " << cnt << " words." << endl;
}
