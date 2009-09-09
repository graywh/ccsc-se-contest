#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> ary;
    int channel = 1, cross, dim, tmp;
    while (!cin.eof())
    {
        cross = 0;
        ary.clear();
        while (cin >> tmp)
        {
            ary.push_back(tmp);
            if (cin.peek() == '\n')
                break;
        }
        if (ary.empty())
            break;
        dim = ary.size();
        for (int i = 1; i < dim; i++)
            for (int j = 0; j < i; j++)
                if (ary[i] < ary[j])
                    cross++;
        cout << "There are " << cross << " wire crossings in routing channel " << channel++ << endl;
    }
}
