#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
    string st;
    char tmp;
    stack<char> mem;
    int extra = 0;
    while (cin >> st)
    {
        for (int i = 0; i < st.length(); i++)
        {
            tmp = st.at(i);
            if (!isdigit(tmp))
            {
                cout << "(";
                mem.push(tmp);
            }
            else
            {
                cout << tmp;
                while ((!mem.empty()) && (isdigit(st[i + 1])))
                {
                    cout << " " << mem.top() << " " << st[i + 1] << ")";
                    mem.pop();
                    i++;
                }
                if ((!mem.empty()) && (i < st.length()))
                {
                    cout << " " << mem.top() << " ";
                    mem.pop();
                    extra++;
                }
            }
        }
        for (extra; extra > 0; extra--)
            cout << ")";
        cout << endl;
    }
}
