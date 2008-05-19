#!/usr/bin/python
if __name__ == "__main__":
    for line in file("mono.in", "r").read().splitlines():
        mono = 1
        up = line[0] < line[1]
        for i in xrange(len(line) - 1):
            if up and line[i] >= line[i + 1] or not up and line[i] <= line[i + 1]:
                mono = 0
        if mono == 1:
            print line
