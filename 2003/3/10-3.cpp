#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    map<int, string> conv;
    conv[1] = "Bogey";
    conv[0] = "Par";
    conv[-1] = "Birdie";
    conv[-2] = "Eagle";
    conv[-3] = "Double Eagle";
    int n, h, s;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> h >> s;
        if (h + 1 < s)
            cout << "Double Bogey" << endl;
        else if (s == 1)
            cout << "Hole-in-one" << endl;
        else
            cout << conv[s - h] << endl;
    }
}
