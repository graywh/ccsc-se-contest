#include <iostream>
#include <string>
using namespace std;

int main()
{
    string word;
    int cnt = 0;
    while (cin >> word)
        cnt++;
    cout << "This file contains " << cnt << " words." << endl;
}
