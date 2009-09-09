#include <iostream>
using namespace std;

void parse(istream& in)
{
    char t;
    in >> t;
    if (!isdigit(t))
    {
        cout << "(";
        parse(in);
        cout << " " << t << " ";
        parse(in);
        cout << ")";
    }
    else
        cout << t;
}

int main()
{
    char t;
    while (cin >> t)
    {
        if (!isdigit(t))
        {
            cout << "(";
            parse(cin);
            cout << " " << t << " ";
            parse(cin);
            cout << ")";
        }
        else
            cout << t;
        cout << endl;
    }
}
