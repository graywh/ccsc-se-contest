
def recursive(data, index, count):
    if index == 81:
        print 'Solution %s:' % (count + 1)
        print '\n'.join([''.join([str(i) for i in l]) for l in data])
        return count + 1
    while data[index / 9][index % 9] > 0:
        index += 1
        if index == 81:
            print 'Solution %s:' % (count + 1)
            print '\n'.join([''.join([str(i) for i in l]) for l in data])
            return count + 1
    for n in xrange(1,10):
        data[index / 9][index % 9] = n
        #print index
        #print '\n'.join([''.join([str(i) for i in l]) for l in data])
        #print
        if validRow(data, index) and validCol(data, index) and validSub(data, index):
                count = recursive(data, index + 1, count)
        data[index / 9][index % 9] = 0
    return count

def validRow(data, index):
    row = index / 9
    results = []
    for i in xrange(9):
        if data[row][i] > 0 and data[row][i] in results:
            return False
        else:
            results.append(data[row][i])
    return True

def validCol(data, index):
    col = index % 9
    results = []
    for i in xrange(9):
        if data[i][col] > 0 and data[i][col] in results:
            return False
        else:
            results.append(data[i][col])
    return True

def validSub(data, index):
    sub = (index / 27) * 27 + ((index % 9) / 3) * 3
    results = []
    for i in xrange(9):
        if data[(sub / 9) + (i / 3)][(sub % 9) + (i % 3)] > 0 and data[(sub / 9) + (i / 3)][(sub % 9) + (i % 3)] in results:
            return False
        else:
            results.append(data[(sub / 9) + (i / 3)][(sub % 9) + (i % 3)])
    return True

if __name__ == '__main__':
    fin = file('puzzle.txt', 'r')

    while True:
        data = [
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]
                ]
        line = fin.readline()
        if line == "" or line is None:
            break
        for j in xrange(9):
            data[0][j] = int(line[j])
        for i in xrange(1,9):
            line = fin.readline()
            for j in xrange(9):
                data[i][j] = int(line[j])

        testIndex = 0
        while data[testIndex / 9][testIndex % 9] == 0:
            testIndex += 1
            if testIndex == 81:
                break
        #print '\n'.join([''.join([str(i) for i in l]) for l in data])
        count = recursive(data, 0, 0)
        print
        print '%s solutions found' % (count)
        print
    
    fin.close()
