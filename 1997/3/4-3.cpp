#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct WoodChuck
{
	string name;
	int tooth;
	
	WoodChuck(string n, int t) : name(n), tooth(t)
	{}
	
	bool operator < (WoodChuck& wc)
	{
		return (tooth < wc.tooth);
	}
};

void main()
{
	ifstream in("prob3_in.txt");
	vector<WoodChuck> wc;
	string name;
	int tooth;
	while (in >> name >> tooth)
	{
		WoodChuck tmp(name, tooth);
		wc.push_back(tmp);
	}
	sort(wc.begin(), wc.end());
	for (int i = 0; i < wc.size(); i++)
		cout << wc[i].name << " the woodchuck can chuck " << wc[i].tooth * 5
			<< " kilograms of wood." << endl;
}
