from problem import Problem
import random
import math

def heap(vector, n, i, stanga, dreapta):
    max = i;
    if stanga < n and vector[stanga] > vector[max]:
        max = stanga;
    if dreapta < n and vector[dreapta] > vector[max]:
        max = dreapta 
    if max != i:
       vector[i], vector[max] = vector[max], vector[i]
       heap(vector, n, max, 2*max + 1, 2*max + 2)
   
    
def algorithm(vector, k, temp): # k - cel mai mic element 
    n = len(vector)
    i = int(n / 2) - 1
    while i >= 0:             
        heap(vector, n, i, 2*i+1, 2*i+2) # scriem in heap
        i = i - 1
        
    i = n - 1
    
    while i >= 0:
        vector[0], vector[i] = vector[i], vector[0]
        heap(vector, i, 0, 1, 2)    
        i = i - 1 
    
    eliminare(vector, k, temp)
    
def eliminare(vector, k, temp):
    i = 0
    while i < k:
        temp.append(vector[i]);
        i = i + 1;
    
    
             
class Problem29(Problem):
    def __init__(self):
        # Lungimea vectorului este intre 6-30 elemente (1-100)
        lungime = random.randint(6, 30)
        self.k = random.randint(3, lungime);
        data = [];
        data = random.sample(range(1, 100), lungime)
        # Adaugam 0 la final
        data[lungime-1] = 0;
        a1 = random.randint(self.k, lungime - self.k);
        a2 = random.randint(1, self.k);
        data[a1]=0;
        data[a2]=0;
        statement = 'Primiti numere naturale > 0 si atunci cand primiti 0, trebuie sa afisati cele mai mari k elemente.\n '
        statement += 'Se dau numerele: ' + ', '.join(map(str, data)) + '.\n k = ' + str(self.k) + '\n'
        super().__init__(statement, data)

    def solve(self):
        solution=""
        vecmax = self.data;    
        e = len(vecmax);
        i = 0;
        counter = 0;
        vector = [];
        while i < e:
            if len(vector) >= self.k and vecmax[i] == 0:
                        solution += 'Index ' + str(counter) + '\nVectorul este:\n'
                        solution += str(vector) + '\nDupa algoritm vectorul devine: \n'
                        temp = [];
                        algorithm(vector, self.k, temp)
                        solution += str(temp) + '\n'
                        vector = temp;
                        counter = counter + 1;
        
            if vecmax[i] != 0:
               vector.append(vecmax[i]);
            i = i + 1;
        return solution;
