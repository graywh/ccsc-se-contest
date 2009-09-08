#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main()
{
    ifstream in("prob4_in.txt");
    int i, intr;
    string keyn, note, dir, intrvl, test;
    bool first, valid, sharp;
    vector<string> key;
    map<string, string> conv;
    map<string, int> interval;
    string notes[] = {"C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"};
    int change[] = {2, 2, 1, 2, 2, 2};

    conv["B#"] = "C";
    conv["C#"] = "Db";
    conv["D#"] = "Eb";
    conv["E#"] = "F";
    conv["F#"] = "Gb";
    conv["G#"] = "Ab";
    conv["A#"] = "Bb";
    conv["Bb"] = "A#";
    conv["Cb"] = "B";
    conv["Db"] = "C#";
    conv["Eb"] = "D#";
    conv["Fb"] = "E";
    conv["Gb"] = "F#";
    conv["Ab"] = "G#";

    interval["second"] = 1;
    interval["third"] = 2;
    interval["fourth"] = 3;
    interval["fifth"] = 4;
    interval["sixth"] = 5;
    interval["seventh"] = 6;
    interval["octave"] = 0;

    while (in >> keyn)
    {
        first = true;
        cout << "Key of " << keyn << ": ";
        if (keyn[1] == '#')
            keyn = conv[keyn];
        i = 0;
        while (notes[i] != keyn)
            i++;
        key.push_back(notes[i]);
        for (int j = 0; j < 6; j++)
        {
            i = (i + change[j]) % 12;
            key.push_back(notes[i]);
        }
        while (in >> note >> dir >> intrvl)
        {
            i = 0;
            sharp = false;
            valid = false;
            if (!first)
                cout << "; ";
            else
                first = false;
            cout << note;
            if (keyn.length() < 2 && note.length() > 1)
                sharp = (note[1] == '#');
            if (sharp)
                note = conv[note];
            while ((i < 7) && (!valid))
                valid = (key[i++] == note);
            if (valid)
            {
                intr = interval[intrvl];
                if (dir == "up")
                    i = (i + intr - 1) % 7;
                else
                    i = (i - intr + 6) % 7;
                cout << " " << dir << " " << intrvl << " => ";
                if (sharp)
                    note = conv[key[i]];
                else
                    note = key[i];
                if ((keyn.length() < 2) && (note.length() > 1))
                    if (note[1] == '#')
                        cout << note;
                    else
                        cout << conv[note];
                else
                    cout << note;
            }
            else
                cout << " is an invalid note for this key";
            while (in.peek() == ' ')
                in.ignore();
            if (in.peek() == '\n')
                break;
        }
        key.clear();
        cout << endl;
    }
}
