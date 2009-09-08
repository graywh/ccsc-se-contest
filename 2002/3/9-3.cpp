#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int main()
{
    ifstream in("prob3_in.txt");
    string line;
    set<int> groups;
    while (in >> line)
    {
        groups.clear();
        int cnt = 0;
        for (int i = 0; i < line.length(); i++)
        {
            if (line[i] == 'A')
                cnt++;
            else
            {
                if (cnt > 0)
                    groups.insert(cnt);
                cnt = 0;
            }
        }
        if (cnt > 0)
            groups.insert(cnt);
        cout << groups.size() << endl;
    }
}
