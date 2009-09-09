#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int num, caproom, best;
vector<int> carts;

int sumVector(vector<int>& v)
{
    int sum = 0;
    if (!v.empty())
        for (int i = 0; i < v.size(); i++)
            sum += v[i];
    return sum;
}

void pick(int last, int sum, int cnt)
{
    if (cnt < num)
    {
        for (int i = last + 1; i < carts.size() - num + cnt + 1; i++)
            pick(i, sum + carts[i], cnt + 1);
    }
    else if ((cnt == num) && (sum <= caproom) && (sum > best))
        best = sum;
}

int main()
{
    int cnt = 1, n, tmp;
    while (cin >> caproom >> n)
    {
        vector<int> findnum;
        carts.clear();
        for (int i = 0; i < n; i++)
        {
            cin >> tmp;
            carts.push_back(tmp);
        }
        sort(carts.begin(), carts.end());
        tmp = 0;
        while ((sumVector(findnum) <= caproom) && (tmp < n))
            findnum.push_back(carts[tmp++]);
        num = findnum.size() - 1;
        reverse(carts.begin(), carts.end());
        best = 0;
        pick(-1, 0, 0);
        cout << "Ship " << cnt++ << endl
            <<  "------" << endl
            <<  "Number of containers loaded: " << num << endl
            <<  "Weight under capacity: " << caproom - best << endl << endl;
    }
}
