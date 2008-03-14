import sys

inflation = 1.03 ** 50

def newprice(x):
    return (round(x * inflation, 2))

menu = {
        'A': ('Hamburger', 0.25),
        'B': ('Cheeseburger', 0.30),
        'C': ('Chili Dog', 0.35),
        'D': ('Sub Sandwich', 0.65),
        'E': ('Baked Pizza', 0.75),
        'F': ('French Fries', 0.25),
        'G': ('Pepsi-Cola', 0.25),
        'H': ('Orange Soda', 0.15),
        'I': ('Hot Coffee', 0.10),
        'J': ('Milk', 0.15),
        'K': ('Apple Pie', 0.30),
        'L': ('Frosty Shake', 0.40),
        'M': ('Popcorn', 0.15),
        }

lines = sys.stdin.read().splitlines()

order = 1
total = 0
print "ORDER %s" % order

for l in lines:
    n, i = l.split()
    n = int(n)
    if n == 0:
        print "ORDER %s TOTAL in 1957 = $%0.2f" % (order, round(total, 2))
        print "ORDER %s TOTAL in 2007 = $%0.2f" % (order, newprice(total))
        order += 1
        total = 0
        if i == "Z":
            break
        else:
            print
            print "ORDER %s" % order
    else:
        item = menu[i]
        print "%s %s" % (n, item[0])
        total += n * item[1]
