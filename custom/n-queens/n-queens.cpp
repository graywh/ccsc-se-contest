#include <iostream>
#include <vector>
using namespace std;

int count;

void dump(vector<int>& g, int dim)
{
    for (int i = 0; i < dim; i++)
    {
        for (int j = 0; j < dim; j++)
        {
            if (g[i * dim + j] == 1)
                cout << 'Q';
            else
                cout << '*';
        }
        cout << endl;
    }
}

bool isValid(vector<int>& g, int dim, int d)
{
    int y = d % dim;
    int x = d / dim;
    for (int i = 0; i < dim; i++)
    {
        if (i != x)
            if (g[i * dim + y] == 1)
                return false;
        if (i != y)
            if (g[x * dim + i] == 1)
                return false;
    }
    for (i = 1; i < dim; i++)
    {
        if (x + i < dim && y + i < dim)
            if (g[(x + i) * dim + y + i] == 1)
                return false;
        if (x + i < dim && y - i > -1)
            if (g[(x + i) * dim + y - i] == 1)
                return false;
        if (x - i > -1 && y + i < dim)
            if (g[(x - i) * dim + y + i] == 1)
                return false;
        if (x - i > -1 && y - i > -1)
            if (g[(x - i) * dim + y - i] == 1)
                return false;
    }
    return true;
}

void findQueen(vector<int>& g, int dim, int q)
{
    if (q == dim)
    {
        dump(g, dim);
        count++;
        cout << endl;
        return;
    }
    for (int i = q * dim; i < (q + 1) * dim; i++)
    {
        if (isValid(g, dim, i))
        {
            g[i] = 1;
            findQueen(g, dim, q + 1);
            g[i] = 0;
        }
    }
    return;
}

int main()
{
    int dim;
    while (cin >> dim)
    {
        vector<int> grid(dim * dim, 0);
        count = 0;
        findQueen(grid, dim, 0);
        cout << "There are " << count << " solutions for n = " << dim << endl << endl;
    }
}
