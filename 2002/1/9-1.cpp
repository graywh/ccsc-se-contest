#include <iostream>
using namespace std;

int main()
{
    int sum, a, b, c, N, tmp;
    char dud;
    while (cin >> a >> dud >> b >> dud >> c >> dud >> N)
    {
        sum = a + b + c;
        for (int i = 3; i < N; i++)
        {
            tmp = a + b + c;
            sum += tmp;
            a = b;
            b = c;
            c = tmp;
        }
        cout << "The answer is: " << sum << endl;
    }
}
