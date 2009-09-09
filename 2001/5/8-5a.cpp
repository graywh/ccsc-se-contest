#include <iostream>
#include <fstream>
using namespace std;

void parse(ifstream& in)
{
	char t;
	in >> t;
	if (!isdigit(t))
	{
		cout << "(";
		parse(in);
		cout << " " << t << " ";
		parse(in);
		cout << ")";
	}
	else
		cout << t;
}

int main()
{
	ifstream in("prob5.in");
	char t;
	while (in >> t)
	{
		if (!isdigit(t))
		{
			cout << "(";
			parse(in);
			cout << " " << t << " ";
			parse(in);
			cout << ")";
		}
		else
			cout << t;
		cout << endl;
	}
}
