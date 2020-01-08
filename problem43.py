import random
import heapq
from dataclasses import dataclass
from random import sample
from problem import Problem


#muchie cu cost
@dataclass
class muchie_cu_cost:
    x: int
    y: int
    cost: int

#pereche de doua valori(folosit in minheap pe post de distanta/tata)
@dataclass
class pereche:
    distanta: int
    tata: int

#nodul are o lista de muchii(ca o lista de adiacente)
@dataclass
class node:
    muchii: list


#de schimbat cu nr problemei corecte
class Problem43(Problem):
    def __init__(self):
      
        #constructie graf muchii random cu cost random
        nr_noduri=random.randint(5,12)
         
        muchii = []
        nr=0
        statement = "Se da graful:\n"
        statement+="nr. de noduri= "+str(nr_noduri)+"\n"
        for i in range (0,nr_noduri):
            for j in range(i+1,nr_noduri):
                k=random.randint(0,1) 
                if (k==1):
                    cost=random.randint(1,15)
                    muchii.append(muchie_cu_cost(i,j,cost))
                    nr=nr+1
                    statement+=str(i)+" "+str(j)+" "+str(cost)+"\n"
          
             
        #text cerinta
       
           
    

        #cerinta += str(muchii)
        statement += "\nRezolvati urmatoarea cerinta:\n"
        statement += "\nAplicati algoritmul lui dijkstra pentru a calcula drumurile si distantele minime de la primul nod catre toate celelalte\n"
        #data memoreaza graful
        data = [muchii, nr_noduri]
        self.solution=""
        super().__init__(statement, data)


    def dijkstra(self, pereches, n):

        #Creare lista de adiacenta(asa se rezolva dijkstra optim)
        noduri = []
        #redimensioneaza noduri[] la n
        for i in range(n):
            noduri.append(node([]))
        #face lista de adiacenta
        for e in pereches:
            noduri[e.x].muchii.append(e)
            noduri[e.y].muchii.append(e)

        #Folosim un vector de perechi pentru rezultat
        #initial distanta catre noduri e infinit(aici am pus 9999 pentru ca nu poate sa ajunga atat de mare(deci e ca un infinit))
        answer= []
        for i in range(n):
            answer.append(pereche(9999,-1))
        #nodul de start e la distanta 0 si este propriul parinte
        answer[0].distanta = 0
        answer[0].parinte = -1
        #Vector de marcaj pentru noduri extrase, initial nu am extras pe nimeni
        vizitat = [False]*n
        #min heap pentru a extrage intotdeauna nodul cel mai apropiat
        minheap= []
        #adaugare nod initial in minheap(nodul 0,distanta 0)
        heapq.heappush(minheap,(0,0))
        #i e numarul de noduri extrase(ne oprim dupa ce le scoatem pe toate(n))
         
        while len(minheap)>0:
            #Scoate nodul cu distanta minima(acum nod calculat corect)
            nod = heapq.heappop(minheap)

           
            #verifica sa nu fi fost deja extras(in minheap putem sa avem dubluri)
            if not (vizitat[nod[1]]):
                #Marcheaza nodul ca extras si creste nr de noduri extrase
                vizitat[nod[1]] = True
                 
                #Am extras un nod cu distanta "infinit", inseamna ca toate care au mai ramas sunt infinit => am terminat
                if answer[nod[1]].distanta == 9999:
                    break
                #Relaxeaza toate muchiile nodului ales
                for e in noduri[nod[1]].muchii:
                    #Relaxeaza daca nodul catre care duce muchia inca nu a fost ales si daca noua distanta e mai mica decat cea deja calculata
                    if not (vizitat[e.y]) and (answer[e.y].distanta > answer[e.x].distanta + e.cost):
                        #Seteaza noua distanta
                        answer[e.y].distanta = answer[e.x].distanta + e.cost
                        #Seteaza noul tata
                        answer[e.y].tata = nod[1]
                        #Pune nodul in minheap(de aici pot aparea dubluri, el poate sa fie deja acolo, de aia verificam extras[])
                        heapq.heappush(minheap,(answer[e.y].distanta, e.y))
        #am terminat, afisam distantele si tatii
        #self.solution+=str(answer)
        return answer

    #functia apelata de site
    def solve(self):
        #apelare functie dijkstra
        solution=""
        solution+="Aplicam algoritmul Dijkstra:\n"
        answer=Problem43.dijkstra(self,self.data[0],self.data[1])
        solution+=str(answer)
        #solution = str(sir)
        statement = self.statement
        return  statement, solution

#afisare rezolvare (asta trebuie sa fie stearsa inainte de a fi pusa pe site)
#test_probl = Problem43()
#[print(x,end = '') for x in test_probl.solve()]
