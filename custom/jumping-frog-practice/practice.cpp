#include <iostream>
using namespace std;

int countF()
{
    while(cin.peek() != EOF && tolower(cin.peek())!='f')
        cin.ignore();
    return (cin.get()==EOF?0:1+countF());
}

int main()
{
    cout << "Mark Twain used " << countF() << " F's in this story." << endl;
}
