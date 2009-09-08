#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>
using namespace std;

struct Node
{
	char val;
	vector<int> child;

	Node(char v = ' ') : val(v){}
};

multiset<string> names;
vector<Node> bill;

void match(string name, int n)
{
	name += bill[n - 1].val;
	if (bill[n - 1].child.empty())
		names.insert(name);
	else
		for (int i = 0; i < bill[n - 1].child.size(); i++)
			match(name, bill[n - 1].child[i]);
}

int main()
{
	ifstream in("prob1_in.txt");
	int num, m, p, cnt = 1;
	char v, s;
	bool full, part;
	string comp;
	multiset<string>::iterator itr;
	while (in >> num >> m >> v)
	{
		cout << "Sample " << cnt << ": ";
		bill.resize(num);
		bill[0] = Node(v);
		for (int i = 0; i < m; i++)
		{
			in >> p >> num >> s >> v;
			bill[num - 1] = Node(v);
			bill[p - 1].child.push_back(num);
		}
		match("", 1);
		full = true;
		part = false;
		itr = names.begin();
		comp = *itr;
		for (itr; itr != names.end(); itr++)
		{
			if (*itr != comp)
				full = false;
			if (names.count(*itr) > 1)
				part = true;
		}
		if (full)
			cout << "Exact match - summon the grand jury." << endl;
		else if (part)
			cout << "Partial match - close, but no cigar." << endl;
		else
			cout << "No match - sorry, Ken." << endl;
		bill.clear();
		names.clear();
		cnt++;
	}
}
