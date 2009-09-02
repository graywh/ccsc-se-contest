#include <iostream>
#include <fstream>
#include <queue>
using namespace std;

void main()
{
	ifstream in("mono_in.txt");
	while (!in.eof())
	{
		queue<char> line;
		bool mono = true;
		char ch;
		in.get(ch);
		line.push(ch);
		bool up = (ch < in.peek());
		while (true)
		{
			in.get(ch);
			line.push(ch);
			if (in.peek() == '\n' || in.eof())
				break;
			if ((up && ch >= in.peek()) || (!up && ch <= in.peek()))
				mono = false;
		}
		while (!line.empty())
		{
			if (mono)
				cout << line.front();
			line.pop();
		}
	}
}
