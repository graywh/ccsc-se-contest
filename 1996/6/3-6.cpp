#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream in("pig.dat");
    char ch;
    string word, tmp, tmp2;

    while (in >> word)
    {
        ch = word.at(word.length() - 1);
        if (ch == ',' || ch == '.' || ch == '!' || ch == '?')
            word.erase(word.length() - 1, 1);
        word.erase(word.length() - 2, 2);
        tmp = word.substr(word.length() - 2, 2);
        if (    tmp == "th" || tmp == "kn" || tmp == "wh" || tmp == "tr" || tmp == "sh" || tmp == "fl" ||
                tmp == "Th" || tmp == "Kn" || tmp == "Wh" || tmp == "Tr" || tmp == "Sh" || tmp == "Fl")
            tmp2 = tmp + word.substr(0, word.length() - 2);
        else
        {
            tmp = word.substr(word.length() - 1, 1);
            if (tmp == "y")
                tmp2 = word.substr(0, word.length() - 1);
            else
                tmp2 = tmp + word.substr(0, word.length() - 1);
        }
        cout << tmp2;
        if (ch == ',' || ch == '.' || ch == '!' || ch == '?')
            cout << ch;
        cout << ' ';
    }
    cout << endl;
}
