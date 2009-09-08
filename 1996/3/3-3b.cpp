#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream in("words.txt");
	char ch, tc;
	int cnt = 0;
	while (in.get(ch))
	{
		switch (ch)
		{
		case ',': case '.': case ';': case ':': case '?': case '!': case ' ': case '\n':
			cnt++;
			tc = in.peek();
			while (tc == ' ' || tc == '\n' || tc == '.' || tc == ',' || tc == ':' ||
				tc == ';' || tc == '?' || tc == '!')
			{
				in.ignore();
				tc = in.peek();
			}
		}
	}
	cout << "This file contains " << cnt << " words." << endl;
}
