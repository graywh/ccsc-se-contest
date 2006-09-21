#include <iostream>
#include <fstream>
#include <stack>
#include <string>
using namespace std;

void main()
{
	ifstream in("directions.txt");
	int steps;
	double distance;
	string dummy, direction, locale;
	stack<double> drives;
	stack<string> turns, places;

	while (in >> steps)
	{
		in.ignore(10, '\n');
		getline(in,locale);
		places.push(locale);
		for(int i = 0; i < (steps / 2); i++)
		{
			in >> dummy >> direction >> dummy;
			in.get();
			getline(in, locale);
			in >> dummy >> distance >> dummy;
			turns.push(direction);
			places.push(locale);
			drives.push(distance);
		}
		in >> dummy >> direction >> dummy;
		in.get();
		getline(in, locale);
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
