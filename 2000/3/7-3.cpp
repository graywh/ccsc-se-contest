#include <iostream>
#include <fstream>
#include <string>
using namespace std;

void main()
{
	ifstream in("prob3_in.txt");
	bool nofreqs;
	int ln = 1, cnt, freq[26] = {0};
	string line;
	char ch;
	while (getline(in, line))
	{
		nofreqs = true;
		cnt = 0;
		for (int i = 0; i < line.length(); i++)
		{
			ch = tolower(line[i]);
			if (isalpha(ch))
				freq[ch - 'a']++;
			cnt++;
		}
		cout << "Line " << ln++ << ": ";
		for (int i = 0; i < 26; i++)
		{
			if ((20 * freq[i]) > (3 * cnt))
			{
				cout << (char)(i + 'A') << " is a super freq. ";
				nofreqs = false;
			}
			freq[i] = 0;
		}
		if (nofreqs)
			cout << "There are no super freqs.";
		cout << endl;
	}
}
