#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    string line, word;
    vector<string> sentence, sorted, reversed;
    int cnt = 1;
    while (getline(cin, line))
    {
        cout << "Sentence " << cnt++ << " is ";
        for (int i = 0; i < line.length(); i++)
        {
            switch(line[i])
            {
                case ' ': case '.': case ',': case '-': case '\n':
                    if (!word.empty())
                        sentence.push_back(word);
                    word.clear();
                    break;
                default:
                    word.push_back(tolower(line[i]));
            }
        }
        sorted = sentence;
        sort(sorted.begin(), sorted.end());
        reversed = sorted;
        reverse(reversed.begin(), reversed.end());
        if ((sorted != sentence) && (reversed != sentence))
            cout << "non-";
        cout << "monotonic." << endl;
        sentence.clear();
        word.clear();
        line.clear();
    }
}
