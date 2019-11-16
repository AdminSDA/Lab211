#Echipa 1, Grupa 211, Problema 8
#Buican Laura Andreea, Pintilie Sabina Maria, Silaghi Tudor Adrian 
import random 
from random import sample
from problem import Problem

class Problem8(Problem):
    def __init__(self):
        statement = 'Se da sirul '
        l = random.randint(5, 10) #l = lungimea sirului
        v = sample(range(1, 100), l)
        statement += str(v)
        statement += '\nRezolvati urmatoarele cerinte:\n'
        p1 = random.randint(1, 4)
        p2 = random.randint(2, 4)
        p3 = random.randint(2, 4)
        p4 = random.randint(2, 4)
        n = random.randint(1, 5)  #Pt. subpunctul c)
        statement += '\na) aplicati '
        statement += str(p1)
        statement += ' pasi din algoritmul de sortare prin insertie urmat de '
        statement += str(p2)
        statement += ' pasi din algoritmul de sortare prin metoda bulelor;\n'
        statement += '\nb) aplicati '
        statement += str(p3)
        statement += ' pasi din algoritmul de sortare prin selectia maximului urmat de '
        statement += str(p4)
        statement += ' pasi din algoritmul de sortare prin selectia minimului;\n'
        statement += '\nc) ce elemente ar putea fi considerate pivoti a. i. la finalul unei partitionari a algoritmului Quicksort sa avem primele '
        statement += str(n)
        statement += ' elemente sortate si specificati partitionarea folosita (Hoare/Lomuto/etc...);\n'
        statement += '\nd) exemplificati sortarea sirului folosind Insertion Sort si Selection Sort (minim).\n'
        data = [v, p1, p2, p3, p4, n, l]
        self.solution1 =''
        super().__init__(statement, data)
#======================================================================A==========================================================================   
    def solve_a(self):
        sir_a = self.data[0]
        p1 = self.data[1]
        p2 = self.data[2]
        l = self.data[6]
        sir = [x for x in sir_a]
        solution = 'Subpuctul a)\n'
        solution += 'INSERTION SORT: \n'
        
        for i in range(1, p1+1):
            solution += '\nPASUL '+ str(i) +':\n' 
            cp_i = i  
            while cp_i:
                if sir[cp_i] < sir[cp_i - 1]:
                    sir[cp_i], sir[cp_i - 1] = sir[cp_i - 1], sir[cp_i]
                    cp_i -= 1
                    solution += str(sir) + '\n'
                else:
                    break

            solution += str(sir) + '\n'
            
        solution += '\nBUBBLE SORT: \n'
        for j in range(1, p2+1):
            modif = True
            solution +='\nPASUL ' + str(j) + ':\n'
            while modif:
                modif=False
                for i in range(0, l-1): 
                    if sir[i] > sir[i+1]:
                        sir[i], sir[i+1] = sir[i+1], sir[i]
                        modif = True
            solution += str(sir)

    
        return solution, sir
#=================================================================B===============================================================================
    def solve_b(self):
        sir_b = self.data[0]
        p3 = self.data[3]
        p4 = self.data[4]
        l = self.data[6]  
        sir = [x for x in sir_b]
        solution = '\nSubpunctul b)\n'
        solution += 'SELECTIA MAXIMULUI:'
        for i in range(0, p3):
            solution +=  '\n PASUL ' + str(i+1) + ':' 
            poz_max = i
            elem_max = sir[i]
            for j in range(i, l):
                if sir[j] > elem_max:
                    poz_max=j
                    elem_max=sir[j]
            solution += '\n' + str(sir) + ':'


        solution += '\nSELECTIA MINIMULUI:\n'
        for i in range(0, p4):
            solution += '\n PASUL ' + str(i+1) + ':\n'
            poz_min = i
            elem_min = sir[i]
            for j in range(i, l):
                if sir[j] < elem_min:
                    poz_min = j
                    elem_min = sir[j]
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            solution += str(sir)

        return solution, sir
#======================================================================C=========================================================================
    # C 
    def partition(self,sir,low,high): 
        i = low         # cel mai la stanga element
        j = high          # cel mai la dreapta element
        pivot = sir[random.randint(low,high)]
        poz_pivot = sir.index(pivot)
        l=len(sir)
        pas = 0
    
        self.solution1 += '\nPivot: ' + str(pivot) + '\n'

        while i < j:  
            pas += 1
            if sir[i] < pivot: 
                i = i + 1 
            elif sir[j] > pivot:
                j = j -1
            else:
                sir[i], sir[j] = sir[j], sir[i]
        self.solution1 += str(sir) + '\n'
            
        return j

    def quickSort(self,sir,low,high,n): 
        if low < high: 
            poz_pivot = Problem8.partition(self,sir,low,high) 

            Problem8.quickSort(self,sir, low, poz_pivot - 1, n) 
           
            if poz_pivot < n-1:
                Problem8.quickSort(self,sir, poz_pivot + 1, high, n) 

    def solve_c(self):
        sir = self.data[0]
        n = self.data[5]
        l = self.data[6]
        self.solution1 += '\nSubpunctul c)\n'
        Problem8.quickSort(self,sir,0,l-1,n) 
        self.solution1 += '\nFolosim partitionarea Hoare\n'
        
        cerinta = self.statement
        return self.solution1, sir

 #===========================================================D===================================================================================   
    def solve_d(self):
        sir = self.data[0]
        sir_nou = [x for x in sir]
        l = self.data[6]

        solution = '\nSubpunctul d)\n'
        solution += 'INSERTION SORT:'

        for i in range(0, l):
            solution +=  '\nPASUL ' + str(i+1) + ':\n'
            cp_i = i  
            while cp_i:
                if sir_nou[cp_i] < sir_nou[cp_i - 1]:
                    sir_nou[cp_i-1], sir_nou[cp_i] = sir_nou[cp_i], sir_nou[cp_i-1]
                    cp_i -= 1
                else:
                    break
            solution += str(sir) + '\n'

        solution += '\nSELECTION SORT: \n'
        for i in range(0, l):
            solution += '\nPASUL ' + str(i+1) +  ':\n'
            poz_min = i
            elem_min = sir[i]
            for j in range(i+1, l):
                if sir[j] < elem_min:
                    poz_min = j
                    elem_min = sir[j]
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            
            solution += str(sir) + '\n'

        return solution, sir
    
    def solve(self):
        solve_a = self.solve_a()
        solve_b = self.solve_b()
        solve_c = self.solve_c()
        solve_d = self.solve_d()
        return solve_a + solve_b + solve_c + solve_d
