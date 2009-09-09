#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main()
{
    int steps;
    double distance;
    string dummy, direction, locale;
    stack<double> drives;
    stack<string> turns, places;

    while (cin >> steps)
    {
        cin.ignore(10, '\n');
        getline(cin,locale);
        places.push(locale);
        for(int i = 0; i < (steps / 2); i++)
        {
            cin >> dummy >> direction >> dummy;
            cin.get();
            getline(cin, locale);
            cin >> dummy >> distance >> dummy;
            turns.push(direction);
            places.push(locale);
            drives.push(distance);
        }
        cin >> dummy >> direction >> dummy;
        cin.get();
        getline(cin, locale);
        turns.push(direction);
        places.push(locale);

        cout << places.top() << endl;
        places.pop();
        for(int i = 0; i < (steps / 2); i++)
        {
            cout << "Turn " << (turns.top()=="right"?"left":"right") << " at "
                << places.top() << endl << "Go " << drives.top() << " miles" << endl;
            turns.pop();
            places.pop();
            drives.pop();
        }
        cout << "Turn " << (turns.top()=="right"?"left":"right") << " at "
            << places.top() << endl;
        turns.pop();
        places.pop();
        cout << endl;
    }
}
