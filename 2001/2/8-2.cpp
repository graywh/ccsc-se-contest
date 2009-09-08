#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

struct Point
{
    int row, col;

    Point(int r = 0, int c = 0) : row(r), col(c)
    {}

    Point(const Point& p) : row(p.row), col(p.col)
    {}

    Point operator +(Point p)
    {
        return Point(row + p.row, col + p.col);
    }

    bool operator ==(Point p)
    {
        return ((row == p.row) && (col == p.col));
    }

    bool operator <(Point p)
    {
        return ((row < p.row) || (col < p.col));
    }

    friend ostream& operator <<(ostream& out, Point p)
    {
        out << "row: " << p.row << ", col: " << p.col;
        return out;
    }
};

bool operator <(const Point p, Point q)
{
    return ((p.row < q.row) || (p.col < q.col));
}

bool isValid(Point p, int dim)
{
    return ((p.row > 0) && (p.row <= dim) && (p.col > 0) && (p.col <= dim));
}

int main()
{
    ifstream in("prob2_in.txt");
    set<Point> visited;
    queue<Point> visit;
    int gridDim, num, cnt;
    Point start, end, here, hereU, hereD, hereL, hereR;
    const Point UP(-1, 0), DOWN(1, 0), LEFT(0, -1), RIGHT(0, 1);
    bool complete;
    while (in >> gridDim)
    {
        in >> start.row >> start.col >> end.row >> end.col;
        cnt = 0;
        complete = false;
        vector< vector<int> > grid(gridDim, vector<int>(gridDim, 0));
        visited.clear();
        while (!visit.empty())
            visit.pop();
        for (int i = 0; i < gridDim; i++)
            for (int j = 0; j < gridDim; j++)
                in >> grid[i][j];
        visit.push(start);
        while (!complete)
        {
            num = visit.size();
            cnt++;
            for (i = 0; i < num; i++)
            {
                here = visit.front();
                visited.insert(here);
                visit.pop();
                if (here == end)
                {
                    complete = true;
                    break;
                }
                hereU = here + UP;
                hereD = here + DOWN;
                hereL = here + LEFT;
                hereR = here + RIGHT;
                if (isValid(hereU, gridDim) && (visited.find(hereU) == visited.end()))
                {
                    if (grid[hereU.row - 1][hereU.col - 1] == 0)
                        visit.push(hereU);
                }
                if (isValid(hereD, gridDim) && (visited.find(hereD) == visited.end()))
                {
                    if (grid[hereD.row - 1][hereD.col - 1] == 0)
                        visit.push(hereD);
                }
                if (isValid(hereL, gridDim) && (visited.find(hereL) == visited.end()))
                {
                    if (grid[hereL.row - 1][hereL.col - 1] == 0)
                        visit.push(hereL);
                }
                if (isValid(hereR, gridDim) && (visited.find(hereR) == visited.end()))
                {
                    if (grid[hereR.row - 1][hereR.col - 1] == 0)
                        visit.push(hereR);
                }
            }
            if (visit.empty())
                break;
        }
        if (complete)
            cout << endl << "There are " << cnt << " squares on a shortest path";
        else
            cout << endl << "No paths were found";
        cout << " from (" << start.row << "," << start.col << ") to (" << end.row << ","
            << end.col << ")." << endl << endl;
    }
}
