#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int oper(int pos, string prefix)
{
	int q = 0;
	cout << "(";
	if (!isdigit(prefix[pos + 1]))
		q = oper(pos + 1, prefix);
	else
		cout << prefix[pos + 1];
	cout << " " << prefix[pos] << " ";
	if (!isdigit(prefix[pos + 2 + q]))
		q += oper(pos + 2 + q, prefix);
	else
		cout << prefix[pos + 2 + q];
	cout << ")";
	return q + 2;
}

int main()
{
	ifstream in("prob5_in.txt");
	string prefix;
	while (in >> prefix)
	{
		if (!isdigit(prefix[0]))
			oper(0, prefix);
		else
			cout << prefix[0];
		cout << endl;
	}
}
