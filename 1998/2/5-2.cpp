#include <iostream>
#include <vector>
using namespace std;

vector< vector<int> > grid;

void clear(int x, int y)
{
    grid[x][y] = 0;
    for (int i = -1; i < 2; i++)
        for (int j = -1; j < 2; j++)
            if (grid[x + i][y + j])
                clear(x + i, y + j);
}

int main()
{
    int dim, targets = 0;
    char ch;
    cin >> dim;
    grid.resize(dim + 2);
    for (int i = 0; i < dim + 2; i++)
    {
        grid[i].resize(dim + 2);
        for (int j = 0; j < dim + 2; j++)
            grid[i][j] = 0;
    }
    for (i = 1; i <= dim; i++)
        for (int j = 1; j <= dim; j++)
        {
            cin.get(ch);
            if (ch == '\n')
                cin.get(ch);
            grid[i][j] = (ch - '0');
        }
    for (i = 1; i <= dim; i++)
        for (int j = 1; j <= dim; j++)
            if (grid[i][j])
            {
                targets++;
                clear(i, j);
            }
    cout << "There are " << targets << " targets in the current image." << endl;
}
