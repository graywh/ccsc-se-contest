#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void printary(vector< vector<char> >& ary)
{
    for (int i = 0; i < 20; i++)
    {
        for (int j = 0; j < 20; j++)
        {
            if (ary[i][j] == 'X')
                cout << ' ';
            else
                cout << 'O';
        }
    }
}

int count(int x, int y, vector< vector<char> >& ary)
{
    int cnt = 0;
    for (int i = -1; i < 2; i++)
        for (int j = -1; j < 2; j++)
        {
            if ((x + i) >= 0 && (x + i) < 20 && (y + j) >= 0 && (y + j) < 20)
                if (ary[x + i][y + j] == 'O')
                    cnt++;
        }
    return cnt;
}

int main()
{
    int yr, x, y;
    vector< vector<char> > tmp(20, vector<char> (20));
    vector< vector<char> > ary(20, vector<char> (20, 'X'));
    ifstream in("prob5_in.txt");

    in >> yr;
    while (in >> x >> y)
        ary[x][y] = 'O';

    cout << "********************" << endl;

    for (int j = 0; j < yr; j++)
    {
        tmp = ary;
        printary(ary);
        cout << "********************" << endl;

        for (int i = 0; i < 20; i++)
        {
            for (int z = 0; z < 20; z++)
            {
                int cnt = count(i, z, ary);
                if (cnt <= 1 || cnt >= 4)
                    tmp[i][z] = 'X';
                if (cnt == 3)
                    tmp[i][z] = 'O';
            }
        }

        ary = tmp;
    }
}
