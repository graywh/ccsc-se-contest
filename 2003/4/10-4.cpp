#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	ifstream in("prob4.in");
	char ch;
	bool b = true;
	while (in.get(ch))
	{
		if (ch == EOF)
			break;
		if (ch == '\"')
		{
			cout << (b ? "``" : "''");
			b = !b;
		}
		else
			cout << ch;
	}
}
