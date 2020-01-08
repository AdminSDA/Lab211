from problem import Problem
import random
from random import randrange
class Problem42(Problem):
    def __init__(self):
        statement = '42. Primind urmatorul graf, construiti arborele partial de cost minim (Kruskal):\n'
        n=randrange(6,10)
        m=randrange(n,2*n)
        cop=m
        viz=[0]*n
        a=[[-1 for i in range(1,n+1)] for j in range(1,n+1)]
        while cop!=0:
            st=randrange(1,n+1)
            dr=randrange(1,n+1)
            p=randrange(1,100)
            while st==dr:
                dr = randrange(1, n+1)
            #statement+='('+str(st)+", "+str(dr)+") --> " +str(p)+'\n'
            cop-=1
            a[st-1][dr-1]=p
            viz[st-1]=viz[dr-1]=1
            a[dr-1][st-1]=p
        nrm=0
        for i in range(0,n):
            for j in range(0,n):
                if a[i][j]!=-1:
                    nrm+=1
        nrm=int(nrm/2)
        while nrm!=m:
            aux=m-nrm
            while aux!=0:
                st = randrange(1, n+1)
                dr = randrange(1, n+1)
                p = randrange(1, 100)
                while st == dr:
                    dr = randrange(1, n+1)
                #statement += '(' + str(st) + ", " + str(dr) + ") --> " + str(p) + '\n'
                a[st - 1][dr - 1] = p
                a[dr - 1][st - 1] = p
                viz[st - 1] = viz[dr - 1] = 1
                aux-=1
            nrm = 0
            for i in range(0, n):
                for j in range(0, n):
                    if a[i][j] != -1:
                        nrm += 1
            nrm = int(nrm / 2)
        #if nrm!=m:
        cn=n
        nr=0
        sters=[]
        for i in range(0,n):
            if viz[i]==0:
                cn=cn-1
                sters.append(i+1)
                for k in range(0,n):
                    a[i][k]=0
                    nr+=1
                    a[k][i]=0
                    nr+=1
        matr=a



        if nr!=0:
            matr = [[-1 for i in range(0, cn)] for j in range(0, cn)]
            k=0
            for i in range(0, n):
                l = 0
                for j in range(0, n):
                    if a[i][j] != 0:
                        matr[k][l] = a[i][j]
                        l = l + 1
                if l!=0:
                    k=k+1
        data=matr
        #if sters!=[]:
            #statement+='\nNodurile sterse sunt: '+str(sters)
        for i in range(0,cn):
            for j in range(0,cn):
                if matr[i][j]>0 and i<=j:
                    statement += '(' + str(i+1) + ", " + str(j+1) + ") --> " + str(matr[i][j]) + '\n'
        super().__init__(statement, data)

    def solve(self):
        data = self.data
        #solution='Matricea de adiacenta este '+str(data)+'\n'
        n = len(data) #nr de noduri

        cost = []
        nod1 = []
        nod2 = []
        for i in range(0, n):
            for j in range(0, n):
                if (data[i][j] != -1) and (i < j):
                    cost.append(data[i][j])
                    nod1.append(j + 1)
                    nod2.append(i + 1)



        cul = []
        for i in range(0, n+1):
            cul.append(i)
        m = len(cost)  #nr de muchii
        # ordonez costurile si nodurile corespunzatoare.
        for i in range(0, m - 1):
            for j in range(i + 1, m):
                if cost[i] > cost[j]:
                    aux = cost[i]
                    cost[i] = cost[j]
                    cost[j] = aux
                    aux = nod1[i]
                    nod1[i] = nod1[j]
                    nod1[j] = aux
                    aux = nod2[i]
                    nod2[i] = nod2[j]
                    nod2[j] = aux


        nr = 0


        solution = ' '
        for i in range(0, m):
            if cul[nod1[i]] != cul[nod2[i]]:
                ca = max(cul[nod1[i]], cul[nod2[i]])
                ci = min(cul[nod1[i]], cul[nod2[i]])
                for j in range(0, n):
                    if cul[j] == ci:
                        cul[j] = ca
                solution +='('+str(nod1[i]) + ',' + str(nod2[i]) + ')--> (' + str(cost[i]) +') '+'\n'
                nr += 1
            if nr == n - 1:
                break
        return solution
