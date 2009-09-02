#!/usr/bin/env python

import sys

conv = {"B#":"C",
        "C#":"Db",
        "D#":"Eb",
        "E#":"F",
        "F#":"Gb",
        "G#":"Ab",
        "A#":"Bb",
        "Bb":"A#",
        "Cb":"B",
        "Db":"C#",
        "Eb":"D#",
        "Fb":"E",
        "Gb":"F#",
        "Ab":"G#"}

interval = {"second":1,
            "third":2,
            "fourth":3,
            "fifth":4,
            "sixth":5,
            "seventh":6,
            "octave":0}

notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
change = [2, 2, 1, 2, 2, 2]

while 1:
    line = sys.stdin.readline()
    if line == "":
        break
    keyn = line.split()
    line = sys.stdin.readline()
    keyn = keyn[0]
    print "Key of %s:" % keyn,
    if len(keyn) > 1 and keyn[1] == "#":
        keyn = conv[keyn]
    i = 0
    while notes[i] != keyn:
        i += 1
    key = []
    output = []
    key.append(notes[i])
    for j in xrange(6):
        i = (i + change[j]) % 12
        key.append(notes[i])
    while 1:
        if line == "":
            break
        unpack = line.split(None,3)
        note = unpack[0]
        di = unpack[1]
        intrvl = unpack[2]
        if len(unpack) > 3:
            line = unpack[3]
        else:
            line = ""
        i = 0
        sharp = 0
        valid = 0
        out = note
        if len(keyn) < 2 and len(note) > 1:
            sharp = (note[1] == "#")
        if sharp:
            note = conv[note]
        while i < 7 and not valid:
            valid = (key[i] == note)
            i += 1
        if valid:
            intr = interval[intrvl]
            if di == "up":
                i = (i + intr - 1) % 7
            else:
                i = (i - intr + 6) % 7
            out += " %s %s => " % (di, intrvl)
            if sharp:
                note = conv[key[i]]
            else:
                note = key[i]
            if len(keyn) < 2 and len(note) > 1:
                if note[1] == "#":
                    out += note
                else:
                    out += conv[note]
            else:
                out += note
        else:
            out += " is an invalid note for this key"
        output.append(out)
    print "; ".join([s for s in output])
