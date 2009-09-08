#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

int main()
{
	ifstream in("prob5_in.txt");
	stack<int> incoming, newstack;
	vector< stack<int> > holds;
	int num, cnt, train = 0, tmp, out;
	while (in >> cnt)
	{
		train++;
		in >> num;
		for (int i = 0; i < cnt; i++)
		{
			in >> tmp;
			incoming.push(tmp);
		}
		holds.reserve(num);
		out = 0;
		while (incoming.size() > 0)
		{
			char cur = incoming.top();
			incoming.pop();
			if (cur - 1 == out)
			{
				out = cur;
				bool move;
				do
				{
					move = false;
					for (int i = 0; i < holds.size(); i++)
					{
						if (holds[i].top() - 1 == out)
						{
							move = true;
							out = holds[i].top();
							holds[i].pop();
						}
					}
				}
				while (move);
			}
			else
			{
				for (int i = 0; i < holds.size(); i++)
				{
					if (holds[i].empty())
					{
						holds[i].push(cur);
						break;
					}
					else if (cur < holds[i].top())
					{
						holds[i].push(cur);
						break;
					}
				}
				if (i == holds.size())
				{
					holds.push_back(newstack);
					holds[i].push(cur);
				}
			}
		}
		if (holds.size() == num)
			cout << "Train " << train << " can be rearranged." << endl;
		else
			cout << "Train " << train << " cannot be rearranged. At least "
				<< holds.size() << " holding tracks would be needed." << endl;
		holds.clear();
	}
}
