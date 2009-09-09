#include <iostream>
using namespace std;

int main()
{
    char ch;
    bool b = true;
    while (cin.get(ch))
    {
        if (ch == EOF)
            break;
        if (ch == '\"')
        {
            cout << (b ? "``" : "''");
            b = !b;
        }
        else
            cout << ch;
    }
}
