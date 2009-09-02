#!/usr/bin/env python

import sys

morse = {
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

def splt(x):
    for i in x:
        prnt(conv(i.replace("   ", " * ").split()))

def conv(x):
    for i in x:
        yield morse[i]

def prnt(x):
    for i in x:
        sys.stdout.write(i)

splt(file("prob2_in.txt"))
