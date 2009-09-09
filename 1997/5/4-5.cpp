#include <iostream>
#include <queue>
using namespace std;

int main()
{
    while (!cin.eof())
    {
        queue<char> line;
        bool mono = true;
        char ch;
        cin.get(ch);
        line.push(ch);
        bool up = (ch < cin.peek());
        while (true)
        {
            cin.get(ch);
            line.push(ch);
            if (cin.peek() == '\n' || cin.eof())
                break;
            if ((up && ch >= cin.peek()) || (!up && ch <= cin.peek()))
                mono = false;
        }
        while (!line.empty())
        {
            if (mono)
                cout << line.front();
            line.pop();
        }
    }
}
