#include <iostream>
#include <fstream>
using namespace std;

ifstream in("frog.in");

int countF()
{
	while(in.peek() != EOF && tolower(in.peek())!='f')
		in.ignore();
	return (in.get()==EOF?0:1+countF());
}

void main()
{
	cout << "Mark Twain used " << countF() << " F's in this story." << endl;
}
