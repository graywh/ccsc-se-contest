#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void moveRight(vector< vector<char> >&, int, int);
void moveLeft(vector< vector<char> >&, int, int);
void moveDown(vector< vector<char> >&, int, int);
void moveUp(vector< vector<char> >&, int, int);

bool pathFound;
int dimC, dimR;

bool isValid(vector< vector<char> >& grid, int r, int c)
{
    return ((r > -1) && (r < dimR) && (c > -1) && (c < dimC) && (grid[r][c] == 'Y'));
}

void dumpGrid(vector< vector<char> >& grid)
{
    for (int i = 0; i < dimR; i++)
    {
        cout << "   ";
        for (int j = 0; j < dimC; j++)
        {
            if ((grid[i][j] == 'X') || (grid[i][j] == 'Y'))
                cout << "-";
            else
                cout << "0";
        }
        cout << endl;
    }
}

int main()
{
    ifstream in("prob1_in.txt");
    int cnt = 1;
    while (in >> dimR >> dimC)
    {
        vector< vector<char> > grid(dimR, vector<char>(dimC));
        pathFound = false;
        for (int i = 0; i < dimR; i++)
            for (int j = 0; j < dimC; j++)
                in >> grid[i][j];
        cout << "\nMaze " << cnt << ":" << endl;
        moveRight(grid, 0, 0);
        if (!pathFound)
            cout << "   No path exists." << endl;
        cnt++;
    }
}

void moveRight(vector< vector<char> >& grid, int r, int c)
{
    grid[r][c] = 'A';
    if ((r == dimR - 1) && (c == dimC - 1))
    {
        pathFound = true;
        dumpGrid(grid);
    }
    if (isValid(grid, r + 1, c))
        moveDown(grid, r + 1, c);
    if (!pathFound && isValid(grid, r, c + 1))
        moveRight(grid, r, c + 1);
    if (!pathFound && isValid(grid, r - 1, c))
        moveUp(grid, r - 1, c);
    grid[r][c] = 'Y';
}

void moveLeft(vector< vector<char> >& grid, int r, int c)
{
    grid[r][c] = 'A';
    if ((r == dimR - 1) && (c == dimC - 1))
    {
        pathFound = true;
        dumpGrid(grid);
    }
    if (isValid(grid, r - 1, c))
        moveUp(grid, r - 1, c);
    if (!pathFound && isValid(grid, r, c - 1))
        moveLeft(grid, r, c - 1);
    if (!pathFound && isValid(grid, r + 1, c))
        moveDown(grid, r + 1, c);
    grid[r][c] = 'Y';
}

void moveDown(vector< vector<char> >& grid, int r, int c)
{
    grid[r][c] = 'A';
    if ((r == dimR - 1) && (c == dimC - 1))
    {
        pathFound = true;
        dumpGrid(grid);
    }
    if (isValid(grid, r, c - 1))
        moveLeft(grid, r, c - 1);
    if (!pathFound && isValid(grid, r + 1, c))
        moveDown(grid, r + 1, c);
    if (!pathFound && isValid(grid, r, c + 1))
        moveRight(grid, r, c + 1);
    grid[r][c] = 'Y';
}

void moveUp(vector< vector<char> >& grid, int r, int c)
{
    grid[r][c] = 'A';
    if ((r == dimR - 1) && (c == dimC - 1))
    {
        pathFound = true;
        dumpGrid(grid);
    }
    if (isValid(grid, r, c + 1))
        moveRight(grid, r, c + 1);
    if (!pathFound && isValid(grid, r - 1, c))
        moveUp(grid, r - 1, c);
    if (!pathFound && isValid(grid, r, c - 1))
        moveLeft(grid, r, c - 1);
    grid[r][c] = 'Y';
}
