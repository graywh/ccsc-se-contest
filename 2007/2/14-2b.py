import sys

keys = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77', 'r': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '*',
        }

def pause(p, n):
    if p[0] == n[0] and p != "*":
        return "(PAUSE)"
    else:
        return ""

def convert(l):
    for c in l:
        yield c

def reduct(a, b):
    if a is not None:
        sys.stdout.write(pause(a,b))
    sys.stdout.write(b)

lines = sys.stdin.read().splitlines()

for l in lines:
    if l[0] == "*":
        break
    reduce(reduct, convert(l), None)
    sys.stdout.write("\n")
