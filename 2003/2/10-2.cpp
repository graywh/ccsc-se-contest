#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <cmath>
using namespace std;

int decimator(string hex)
{
    int total = 0, val;
    for (int i = 0; i < hex.length(); i++)
    {
        if (isalpha(hex[i]))
            val = (int)(hex[i] - 'A' + 10);
        else
            val = (int)(hex[i] - '0');
        total += (val * pow(16, hex.length() - i - 1));
    }
    return total;
}

string binar(int n)
{
    string b;
    for (int i = 0; i < 12; i++)
    {
        b = (char)(n % 2 + '0') + b;
        n /= 2;
    }
    return b;
}

int main()
{
    ifstream in("prob2_in.txt");
    int num, n1, n2;
    string h1, h2;
    char op;
    in >> num;
    for (int n = 0; n < num; n++)
    {
        in >> h1 >> op >> h2;
        n1 = decimator(h1);
        n2 = decimator(h2);
        h1 = binar(n1);
        h2 = binar(n2);
        cout << h1 << " " << op << " " << h2 << " = "
            << (op == '+' ? n1 + n2 : n1 - n2) << endl;
    }
}
