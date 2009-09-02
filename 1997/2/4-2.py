#!/usr/bin/python

import sys

x = {
    '.-'  :'A', '-...':'B', '-.-.':'C',
    '-..' :'D', '.'   :'E', '..-.':'F',
    '--.' :'G', '....':'H', '..'  :'I',
    '.---':'J', '-.-' :'K', '.-..':'L',
    '--'  :'M', '-.'  :'N', '---' :'O',
    '.--.':'P', '--.-':'Q', '.-.' :'R',
    '...' :'S', '-'   :'T', '..-' :'U',
    '...-':'V', '.--' :'W', '-..-':'X',
    '-.--':'Y', '--..':'Z', '*'   :' '
}

for line in sys.stdin:
    if line == "":
        break
    if line[-1] == "\n":
        line = line[:-1]
    line = line.replace("   ", " * ")
    codes = line.split()
    for code in codes:
        sys.stdout.write(x[code])
