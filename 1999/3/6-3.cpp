#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class PTree
{
private:
	struct Node
	{
		char data;
		Node* left, * right;
		Node(char d) : data(d), right(NULL), left(NULL) {}
	};
	
	Node* root;
	bool isPalin;
	string pal;
	
	Node* create(ifstream& in)
	{
		Node* tmp;
		char ch, dummy;
		in >> dummy >> ch;
		if (ch == ')')
			return NULL;
		tmp = new Node(ch);
		tmp->left = create(in);
		tmp->right = create(in);
		in >> dummy;
		return tmp;
	}
	
	void traverseAll(Node* n, string s)
	{
		s.push_back(n->data);
		if ((n->left == NULL) && (n->right == NULL))
			isPalin = isPalindrome(s);
		if (isPalin)
			pal = s;
		if ((n->left != NULL) && !isPalin)
			traverseAll(n->left, s);
		if ((n->right != NULL) && !isPalin)
			traverseAll(n->right, s);
	}
	
	bool isPalindrome(string s)
	{
		for (unsigned i = 0; i < (s.size() - i); i++)
			if (s[i] != s[s.size() - i - 1])
				return false;
		return true;
	}

public:
	bool make(ifstream& in)
	{
		isPalin = false;
		root = create(in);
		string s;
		traverseAll(root, s);
		return true;
	}
	
	bool isPal()
	{
		return isPalin;
	}
	
	string getPal()
	{
		return pal;
	}
};

void main()
{
	ifstream in("prob3_in.txt");
	int cnt = 1;
	PTree t;
	while (!in.eof())
	{
		t.make(in);
		cout << "Tree " << cnt << " is ";
		if (t.isPal())
			cout << "a palintree. Its palindrome is " << t.getPal() << "." << endl;
		else
			cout << "not a palintree." << endl;
		cnt++;
	}
}
