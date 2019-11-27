import random
import heapq
from random import sample
from problem import Problem


class Problem28(Problem):
    def __init__(self):
        v = sample(range(1,50), 20)
        i = random.randint(5,8)
        v[i] = 0;
        j = random.randint(14,17)
        v[j] = 0;
        v[19] = 0;
        statement = 'Primiti numere naturale > 0 si atunci cand primiti 0 trebuie sa afisati valoarea mediana'
        statement += 'din vector.\nValoarea mediana este v[mij] daca v e sortat si len e impar, altfel e '
        statement += '(v[mij1]+v[mij2])/2 daca e par.\n'
        statement += str(v)
        data = [v, i ,j]
        super().__init__(statement, data)

    def solve(self):
        solution ='\tCream heap-urile: \n\n'
        data = self.data
        m = 0
        v = data[0]
        i = data[1]
        j= data[2]
        hmin=[]
        hmax=[]
        if v[0] > v[1]:
            heapq.heappush(hmin,v[0])
            heapq.heappush(hmax,-v[1])
        else:
            heapq.heappush(hmin, v[1])
            heapq.heappush(hmax, -v[0])
        minsize=1
        maxsize=1
        for i in range(2,len(v)):
            if v[i] != 0:
                    if v[i] > -hmax[0]:
                        heapq.heappush(hmin,v[i])
                        minsize += 1
                    else:
                        heapq.heappush(hmax,-v[i])
                        maxsize += 1
                    if abs(maxsize-minsize) > 1:
                        if maxsize > minsize:
                            k = heapq.heappop(hmax)
                            maxsize -= 1
                            heapq.heappush(hmin,-k)
                            minsize +=1
                        else:
                            k = heapq.heappop(hmin)
                            minsize -= 1
                            heapq.heappush(hmax,-k)
                            maxsize +=1
            else:
                for item in range(0,len(hmax)):
                    hmax[item] = -hmax[item]
                m += 1
                if minsize > maxsize:
                    median = hmin[0]
                elif minsize < maxsize:
                    median = hmax[0]
                elif minsize == maxsize:
                    median = (hmin[0] + hmax[0]) / 2



                solution += 'Min heap: ' + str(hmin) + "\n"
                vv = hmin
                p = 0
                for i in range(0, len(vv)):
                    p = p + 2 ** i
                    if p >= len(vv):
                        break
                nr = i + 1
                ultim_niv = 2 ** (nr - 1) - (p - len(vv))
                a1 = 0
                a2 = 1
                h = 1
                for j in range(0, nr):
                    if j == nr - 1:
                        w = []
                        for l in range(a1, a1 + ultim_niv):
                            w.append(vv[l])
                        space = (2 ** (nr - 1 - j) - 1) * '  '
                        space1 = (2 * (nr - j) - 1) * '  '
                        solution += space + space1.join(map(str, w))+'\n'
                    else:
                        w = []
                        for l in range(a1, a2):
                            w.append(vv[l])
                        a1 = a2
                        a2 = a2 + 2 ** (j + 1)
                        space = (2 ** (nr - 1 - j) - 1) * '  '
                        space1 = (2 ** (nr - j) - 1) * '  '
                        h += 1
                        solution += space + space1.join(map(str, w))+'\n'



                solution += 'Max heap: ' + str(hmax) + "\n"
                vvv = hmax
                p = 0
                for i in range(0, len(vvv)):
                    p = p + 2 ** i
                    if p >= len(vvv):
                        break
                nr = i + 1
                ultim_niv = 2 ** (nr - 1) - (p - len(vvv))
                a1 = 0
                a2 = 1
                h = 1
                for j in range(0, nr):
                    if j == nr - 1:
                        w = []
                        for l in range(a1, a1 + ultim_niv):
                            w.append(vvv[l])
                        space = (2 ** (nr - 1 - j) - 1) * '  '
                        space1 = (2 * (nr - j) - 1) * '  '
                        solution += space + space1.join(map(str, w)) + '\n'
                    else:
                        w = []
                        for l in range(a1, a2):
                            w.append(vvv[l])
                        a1 = a2
                        a2 = a2 + 2 ** (j + 1)
                        space = (2 ** (nr - 1 - j) - 1) * '  '
                        space1 = (2 ** (nr - j) - 1) * '  '
                        h += 1
                        solution += space + space1.join(map(str, w)) + '\n'




                solution +='Mediana ' + str(m) +" este: " + str(median)
                solution +='\n\n'
                for item in range(0,len(hmax)):
                    hmax[item] = -hmax[item]



        return solution
