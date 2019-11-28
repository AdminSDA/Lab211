import random
from problem import Problem

_BTinfo = [1, 5, 4, -1, -1, -1, -1, 9, 8, 3, -1, 0, 0, 0, 0, -1, -1, -1, 2]
_RSD = [1, 5, 3, -1, -1, -1, 4, 9, -1, 2, -1, -1, 8, -1, -1]

BTinfo = []
RSD = []

childs = [0] * 10;

def GenerateChilds():
    childs[1] = 2;
    for i in range(2, 10):
        childs[i] = random.randint(0, 2)
    childs[0] = sum(childs)
    if (childs[0] > 9):
        childs[0] = 0
        GenerateChilds()

BTinfo = [0] * 19
BTinfo[0] = 1
remainingNodes = 0

def GenerateRandomBTinfo(remainingNodes):

    node = 2

    for i in range(2, 19, 2):
        currentNode = int(i/2)

        if childs[currentNode] == 0:
            leftValue = -1
            rightValue = -1
        elif childs[currentNode] == 1:
            remainingNodes -= 1
            j = random.randint(i-1, i)
            if j == i-1:
               leftValue = node
               rightValue = -1
            else:
               leftValue = -1
               rightValue = node
            node += 1

        else:
            remainingNodes -= 2
            leftValue = node
            rightValue = node + 1

            node = max(leftValue, rightValue) + 1

        BTinfo[i-1] = leftValue
        BTinfo[i] = rightValue

def GenerateRSD(value):
    RSD.append(value)
    if (value == -1 or value == 0 or value > 9):
        return
    GenerateRSD (BTinfo[2*value-1])
    GenerateRSD (BTinfo[2*value])

buffer = []

noIter = 0;

def PrintBT(value):

    if (value == -1):
        print ('N')
    else:
        print (value)

    if (value != -1):
        buffer.append(BTinfo[2*value-1])
        buffer.append(BTinfo[2*value])

    if (buffer != []):
        temp = buffer[0]
        buffer.pop(0)
        PrintBT(temp)

#Pentru cazul in care citim RSD si vrem sa obtinem BTinfo.
#BTinfo = [0] * (2 * max(RSD) + 1)
#BTinfo[0] = 1

def GenerateBTinfo(next, prev, lastNatural, check_right):
    read = RSD[next]
    next = next + 1

    temp = lastNatural
    if (read != -1):
        lastNatural = read

    if (read != -1):
        if (check_right == 1):
            BTinfo[2 * prev] = read
            check_right = 0
        else:
            BTinfo[2 * prev - 1] = read
        prev = read

    if (read == -1):

        if (check_right == 1):
            BTinfo[2 * prev] = read
        else:
            BTinfo[2 * prev - 1] = read

        check_right = 1
        if (prev == -1):
            prev = lastNatural

        if (BTinfo[2 * prev] != 0 and BTinfo[2 * prev - 1] != 0):
            x = lastNatural
            while 1:
                parent = (BTinfo.index(x) + 1) // 2
                if BTinfo[2 * parent] == 0:
                    lastNatural = parent
                    break
                else:
                    x = parent

        prev = lastNatural

    if (next < len(RSD)):
        GenerateBTinfo(next, prev, lastNatural, check_right)

def FindSolution ():

    GenerateChilds()
    remainingNodes = childs[0]
    GenerateRandomBTinfo(remainingNodes)

    ##Pentru cazul in care citim RSD si vrem sa obtinem BTinfo.
    #GenerateBTinfo(1, 1, 1, 0)

    GenerateRSD (BTinfo[0])

    statement = 'Parcurgerea in preordine (RSD) data este: '

    for number in RSD:
        if number == 0:
            statement += '';
        elif number == -1:
            statement += 'N '
        else:
            statement += str(number) + ' '

    statement += '.\nGenerati arborele asociat.\n'

    statement += '\nArborele generat este următorul:\n'

    solution = statement

    return solution

class Problem15(Problem):

    def solve(self):
        solution = FindSolution()
        return solution
