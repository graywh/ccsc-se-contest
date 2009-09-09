#include <iostream>
#include <iomanip>
#include <string>
#include <map>
using namespace std;

int main()
{
    string str;
    char ch;
    map<string, char> x;

    x[".-"] = 'A';
    x["-..."] = 'B';
    x["-.-."] = 'C';
    x["-.."] = 'D';
    x["."] = 'E';
    x["..-."] = 'F';
    x["--."] = 'G';
    x["...."] = 'H';
    x[".."] = 'I';
    x[".---"] = 'J';
    x["-.-"] = 'K';
    x[".-.."] = 'L';
    x["--"] = 'M';
    x["-."] = 'N';
    x["---"] = 'O';
    x[".--."] = 'P';
    x["--.-"] = 'Q';
    x[".-."] = 'R';
    x["..."] = 'S';
    x["-"] = 'T';
    x["..-"] = 'U';
    x["...-"] = 'V';
    x[".--"] = 'W';
    x["-..-"] = 'X';
    x["-.--"] = 'Y';
    x["--.."] = 'Z';

    while (cin >> str)
    {
        ch = x[str];
        cout << ch;
        cin.get(ch);
        ch = cin.peek();
        if (ch == ' ')
            cout << ch;
    }
    cout << endl;
}
