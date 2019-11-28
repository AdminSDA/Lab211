from problem import Problem
import random

def find_zeros(array):
     i=0
     while i < len(array):
        if array[i] == 0:
               return 0
        i = i + 1                      
         
def search_arr(vector, x):
     i = 0
     while i < len(vector):
            if vector[i] == x:
                return i;
           
            i += 1
               
     return 'error';
     
                   
def knumar(vector, stanga, dreapta, k, solution, pas):
        lungimea = dreapta - stanga + 1;
        if k > 0 and k <= lungimea:
                if pas == 1:
                    solution += 'Pasul ' + str(stanga) + ' din ' + str(dreapta) + ': \n'
                mediana_part_cinci = []
                i = 0
                while i < lungimea: #T(12/5*n) ~ O(n)
                    e = lungimea - i
                    if e > 5:
                        e = 5
                    mediana = []
                    j = 0
                    while j < e: #(j< 1, 2, 3, 4, 5) #T(5)
                          mediana.append(vector[i + j + stanga])
                          j += 1
                    mediana.sort()  #T(5log5) ~ T(6)
                    # per total ~ T(12) => ~ T(12) ~ O(1)
                    mediana_part_cinci.append(mediana[e // 2])
                    i += 5
         
                i = i // 5
                med = knumar(mediana_part_cinci, 0, i - 1, i // 2, solution, 0) #O(1)
                if i == 1:
                    med = mediana_part_cinci[0] 
                contor = verificare(vector, stanga, dreapta, med) #returneaza si ordoneaza vectorul in ordinea k
                contor1 = contor - stanga
                if pas == 1:
                     solution += 'Numarul ' + str(med) + ' este al ' + str(contor1) + ' lea numar cel mai mic numar din sir '    
                if (contor1 == k - 1):  
                    return vector[contor]  
                if (contor1 > k - 1):
                    return knumar(vector, stanga, contor - 1, k, solution, 1)  
 
                return knumar(vector, contor + 1, dreapta, k - contor1 - 1, solution, 1)  
 
 
 
def swap(vector, a, b):  
    temp = vector[a]  
    vector[a] = vector[b]  
    vector[b] = temp  
 
 
def verificare(vector, start, sfarsit, numarul):
    for i in range(start, sfarsit):
        if vector[i] == numarul:
            swap(vector, sfarsit, i)
            break
 
    numarul = vector[sfarsit]
    i = start  
    for j in range(start, sfarsit):  #T(r - l)
        if vector[j] <= numarul:
           swap(vector, i, j)  
           i += 1
       
    swap(vector, i, sfarsit)  
    return i
    
class Problem29(Problem):
    def __init__(self):
        k = random.randint(6,10)
        k1 = k * 2
        data = random.sample(range(100), k1);
 
        statement = '29. Se primesc numerele: ' + ', '.join(map(str, data)) + '. '
        statement += 'Introduceti primele ' + str(k) + ' elemente in doi vectori ' + '\n'
        statement += 'Inseram intr-un vector v1 primele elemente mai mari decat 0\n'
        statement += 'daca primim un zero inainte, inseamna ca nu avem k elemente, deci le afisam pe toate.'
        statement += 'Acum in acel vector v1 avem k elemente.'
        statement += '\nContinuam sa citim urmatoarele k elemente intr-un vector v2.\n'      
        statement += 'Cand primim 0 sau si v2 contine k elemente, punem la gramada elemente lui v1 si ale lui v2 '
        statement += ' si aplicam statistici de ordine sa obtinem cele mai mici k elemente din v1 si v2.'
        self.data = data
        self.k = k
        super().__init__(statement, data)
 
    def solve(self):
        solution = 'Implementam primele k numere in vectorul v1 \n'
        i = 0
        temp = []
        while i < self.k:
            temp.append(self.data[i])
            i = i + 1
       
        solution += 'Cautam zerouri daca apar in primul vector: \n'    
        if find_zeros(temp) == 0:
             solution += 'Au aparut zerouri in v1 deci se va afisa: \n'
             i = 0
             final = []
             save = 0
             while i < len(self.data):
                 if self.data[i] != 0:
                     save = i
                     final.append(self.data[i])
                 
                 i = i + 1
             solution += 'Primele ' + str(save) + ' numere sunt: \n'
             solution += str(final)
 
        else:
                solution += 'Nu au aparut zerouri in v1 deci continuam... \n'    
                i = self.k
                j = i * 2
                solution += 'Importam numere in vectorul v2: \n'
                while i < j:
                    if self.data[i] == 0:
                          break
                    temp.append(self.data[i])
                    i = i + 1
                e = knumar(temp, 0, len(temp) - 1, self.k, solution, 1)
                if self.k == 1:
                    solution += 'Primul numar este: ' + str(e) + '\n'
                else:
                    solution += 'Numarul al ' + str(self.k) + ' lea cel mai mic element este: ' + str(e) + '\n'
                solution += 'Se cauta numere mai mici decat numarul: ' + str(self.k) + ' si se ordoneaza: \n'
                final = []
                i = 0
                index = search_arr(temp, e)
                while i <= index:
                     final.append(temp[i])
                     i = i + 1
                solution += 'Ordonare completa. Primele ' + str(self.k) + ' elemente sunt: \n'
                solution += str(final);
                solution += '\nNumerele sortate sunt: ' + str(final);
                
        return solution
