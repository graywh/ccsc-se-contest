#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

set<string> nouns;
set<string> verbs;
set<string> other;

void stringToLower(string& s)
{
	for (int i = 0; i < s.length(); i++)
		s[i] = tolower(s[i]);
}

int classify(string s)
{
	if (nouns.find(s) != nouns.end())
		return 1;
	else if (verbs.find(s) != verbs.end())
		return 2;
	else if (other.find(s) != other.end())
		return 3;
	else
		return 0;
}

bool isUnknown(vector<int> vs)
{
	for (int i = 0; i < vs.size(); i++)
		if (vs[i] == 0)
			return true;
	return false;
}

bool isSimp(vector<int> vs)
{
	vector<int> simp;
	simp.push_back(1);
	simp.push_back(2);
	return (vs == simp);
}

bool isComp(vector<int> vs)
{
	vector<int> comp;
	comp.push_back(1);
	comp.push_back(2);
	comp.push_back(1);
	return (vs == comp);
}

int main()
{
	ifstream in("prob6_in.txt");
	ifstream data("static.dat");
	int n, v, o, cl;
	string tmp;
	char ch;
	vector<string> sent;
	vector<int> sc;
	data >> n >> v >> o;
	for (int i = 0; i < n; i++)
	{
		data >> tmp;
		nouns.insert(tmp);
	}
	for (i = 0; i < v; i++)
	{
		data >> tmp;
		verbs.insert(tmp);
	}
	for (i = 0; i < o; i++)
	{
		data >> tmp;
		other.insert(tmp);
	}
	data.close();
	while (!in.eof())
	{
		sc.clear();
		sent.clear();
		while (in.peek() != '\n')
		{
			if (!in.eof())
			{
				in >> tmp;
				ch = tmp[tmp.size() - 1];
				if (ch == '.' || ch == ',' || ch == ';' || ch == '?' || ch == '!')
					tmp.erase(tmp.end() - 1);
				if (!tmp.empty())
				{
					stringToLower(tmp);
					sent.push_back(tmp);
				}
			}
			else
				break;
		}
		if (!sent.empty())
		{
			for (int i = 0; i < sent.size(); i++)
			{
				cl = classify(sent[i]);
				if (cl < 3)
					sc.push_back(cl);
			}
			if (isUnknown(sc))
				cout << "contains unknown word" << endl;
			else if (isSimp(sc))
				cout << "simple" << endl;
			else if (isComp(sc))
				cout << "complex" << endl;
			else
				cout << "other" << endl;
		}
		in.ignore(1, '\n');
	}
}
