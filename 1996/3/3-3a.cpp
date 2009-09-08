#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream in("words.txt");
	string word;
	int cnt = 0;
	while (in >> word)
		cnt++;
	cout << "This file contains " << cnt << " words." << endl;
}
