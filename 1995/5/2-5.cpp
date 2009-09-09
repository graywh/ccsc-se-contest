#include <iostream>
#include <string>
#include <stack>
using namespace std;

int getOne(int n)
{
    return (n % 10);
}

int getTen(int n)
{
    return ((n % 100) / 10);
}

int getHund(int n)
{
    return (n / 100);
}

int main()
{
    int cnt = 1;
    while (!cin.eof())
    {
        stack<char> msg;
        stack<int> code;
        string act;
        int n;
        char ch, ch1, ch2;
        cin >> act;
        cin.get(ch);
        if (act == "encode")
        {
            cout << "\nMessage " << cnt << " (encoded): ";
            while (cin.get(ch))
            {
                if (ch == '\n')
                    break;
                if ((int)ch > 99)
                    code.push(getHund((int)ch));
                code.push(getTen((int)ch));
                code.push(getOne((int)ch));
            }
            while (!code.empty())
            {
                cout << code.top();
                code.pop();
            }
        }
        else if (act == "decode")
        {
            cout << "\nMessage " << cnt << " (decoded): ";
            while (cin.get(ch1))
            {
                if (ch1 == '\n')
                    break;
                cin.get(ch2);
                n = 10 * (ch2 - '0') + (ch1 - '0');
                if (n < 23)
                {
                    cin.get(ch);
                    n+=100;
                }
                ch = (char)n;
                msg.push(ch);
            }
            while (!msg.empty())
            {
                cout << msg.top();
                msg.pop();
            }
        }
        cnt++;
    }
    cout << endl;
}
