#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("prob1_in.txt");
	int lines;
	char ch;
	bool mov = true;
	int ary[26] = {0};
	char aryc[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
		'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
	in >> lines;
	while (in.get(ch))
	{
		if (ch == EOF)
			break;
		if (isalpha(ch))
			ary[toupper(ch) - 'A']++;
	}
	while (mov)
	{
		mov = false;
		for (int i = 0; i < 25; i++)
			if (ary[i] < ary[i + 1])
			{
				mov = true;
				ary[i] ^= ary[i + 1];
				ary[i + 1] ^= ary[i];
				ary[i] ^= ary[i + 1];
				aryc[i] ^= aryc[i + 1];
				aryc[i + 1] ^= aryc[i];
				aryc[i] ^= aryc[i + 1];
			}
	}
	for (int i = 0; i < 26; i++)
		if (ary[i] > 0)
			cout << aryc[i] << " " << ary[i] << endl;
}
