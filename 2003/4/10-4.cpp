#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("prob4_in.txt");
    char ch;
    bool b = true;
    while (in.get(ch))
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
