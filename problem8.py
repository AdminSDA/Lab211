#Echipa 1, Grupa 211, Problema 8
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
        n = random.randint(1, l)  #Pt. subpunctul c)
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
        solution = '\nSubpunctul a)\n'
        solution += '\n>>>>>>>>>>>>>>>>>>> Aplicam ' + str(p1) + ' pasi din Insertion Sort <<<<<<<<<<<<<<<<<<<<\n'
        solution += str(sir)
        solution += '\nSetam un marker ce delimiteaza elementele sortate de cele nesortate.\n'
        solution += '\nConsideram primul element ca fiind sortat.'
        solution += '\nSelectam primul element nesortat.'
        solution += '\n' + str(sir) + '\n'
        
        for i in range(1, p1+1):
            solution += '\nPASUL: '+ str(i) +'\n' 
            cp_i = i  
            solution += '\tElementul curent este: ' + str(sir[i]) 
            solution += '\nIncercam sa gasim pozitia corecta a lui ' + str(sir[i]) +  '\n' 
            while cp_i:
                
                if sir[cp_i] < sir[cp_i - 1]:
                    solution += '\nComparam ' + str(sir[cp_i]) + ' cu ' + str(sir[cp_i - 1])
                    solution += '\n\tDaca ' + str(sir[cp_i]) + ' este mai mic ' + str(sir[cp_i - 1]) + ' facem interschimbarea.\n'
                    sir[cp_i], sir[cp_i - 1] = sir[cp_i - 1], sir[cp_i]
                    cp_i -= 1
                    solution += str (sir) + '\n'
                else:
                    solution += '\nCele doua elemente sunt asezate corect.\n' + str(sir[0:i+1]) +  str(sir[i+1:l]) + '\n'
                    break
            
        solution = '\n>>>>>>>>>>>>>>>>>>> Aplicam ' + str(p2) + ' pasi din Bubble Sort <<<<<<<<<<<<<<<<<<<<\n'
        solution += str(sir)
        for j in range(1, p2+1):
            modif = True
            solution +='\nPASUL : ' + str(j) + '\n'
            while modif:
                modif=False
                for i in range(0, l-1):
                    
                    if sir[i] > sir[i+1]:
                        solution += str(sir[i]) + ' > ' + str(sir[i+1]) + ' facem interschimbarea.\n'
                        sir[i], sir[i+1] = sir[i+1], sir[i]
                        modif = True
            solution += '\t' + str(sir[0:l-j]) + str(sir[l-j:l]) + '\n'

    
        return solution, sir
#=================================================================B===============================================================================
    def solve_b(self):
        sir_b = self.data[0]
        p3 = self.data[3]
        p4 = self.data[4]
        l = self.data[6]  
        sir = [x for x in sir_b]
        solution = '\nSubpunctul b)' + '\n'
        solution += str(sir)
        solution += '\n>>>>>>>>>>>>>>>>>>> Aplicam ' + str(p3) + ' pasi din algoritmul de sortare prin selectia maximului <<<<<<<<<<<<<<<<<<<<\n'
        for i in range(0, p3):
            solution +=  '\n PASUL: ' + str(i+1)  
            poz_max = i
            elem_max = sir[i]
            solution += '\nCautam pozitia pe care se afla elementul maxim si salvam si valoarea elementului maxim'
            
            for j in range(i, l):
                if sir[j] > elem_max:
                    solution += '\n' + str(sir[j]) + ' > ' + str(elem_max)
                    poz_max=j
                    elem_max=sir[j]
            
            solution += '\n Interschimbam elementele ' + str(sir[i]) + ' si ' + str(sir[poz_max]) + '.'
            sir[i], sir[poz_max] = sir[poz_max], sir[i]
            
            solution += '\n' + str(sir)


        solution += '\n >>>>>>>>>>>>>>>>>>> Aplicam ' + str(p4) + ' pasi din algoritmul de sortare prin  selectia minimului <<<<<<<<<<<<<<<<<<<<\n'
        solution += str(sir)
        for i in range(0, p4):
            solution += '\n PASUL: ' + str(i+1) 
            poz_min = i
            elem_min = sir[i]
            solution += '\nCautam pozitia pe care se afla elementul minim si salvam si valoarea elementului minim'
            
            for j in range(i, l):
                if sir[j] < elem_min:
                    solution += '\n' + str(sir[j]) + ' < ' + str(elem_min)
                    poz_min = j
                    elem_min = sir[j]
            solution += '\n Interschimbam elementele ' + str(sir[i]) + ' si ' + str(sir[poz_min]) +'.\n'
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            solution += str(sir)
        
        cerinta = self.statement
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
                self.solution1 += '\nInterschimbam ' + str(sir[i]) + ' cu '+ str(sir[j])
                sir[i], sir[j] = sir[j], sir[i]
            
            
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
        solution += str(sir_nou)
        solution += '\nAplicam algoritmul de sortare prin insertie' 
        solution += '\nSetam un marker ce delimiteaza elementele sortate de cele nesortate.\n'
        solution += '\nConsideram primul element ca fiind sortat.'
        solution += '\nSelectam primul element nesortat.'
        solution += str(sir)

        for i in range(0, l):
            solution +=  '\nPASUL ' + str(i+1) + ':'
            cp_i = i  
            solution += '\tElementul curent este: ' + str(sir_nou[i]) 
            solution += '\nIncercam sa gasim pozitia corecta a lui ' + str(sir_nou[i]) + '\n' 
            while cp_i:
                if sir_nou[cp_i] < sir_nou[cp_i - 1]:
                    solution += '\nComparam ' + str(sir_nou[cp_i]) + ' cu ' + str(sir_nou[cp_i - 1])
                    solution += '\n\tDaca ' + str(sir_nou[cp_i]) + ' este mai mic ' + str(sir_nou[cp_i - 1]) + ' facem interschimbarea.\n'
                    sir_nou[cp_i-1], sir_nou[cp_i] = sir_nou[cp_i], sir_nou[cp_i-1]
                    cp_i -= 1
                else:
                    solution += '\nAm gasit pozitia corecta, deci ne oprim.\n' 

                    break
            solution += str(sir) + '\n'


        solution += '\nAplicam algoritmul de sortare prin selectia minimului\n'
        solution += str(sir)
        for i in range(0, l):
            solution += '\nPASUL ' + str(i+1) +  ':'
            poz_min = i
            elem_min = sir[i]
            solution += '\nCautam pozitia pe care se afla elementul minim si salvam si valoarea elementului minim'
            for j in range(i+1, l):
                if sir[j] < elem_min:
                    solution += '\n' + str(sir[j]) + ' < ' + str(elem_min)
                    poz_min = j
                    elem_min = sir[j]
            solution += '\n Interschimbam elementele ' + str(sir[i]) + ' si ' + str(sir[poz_min]) +'.\n'
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            
            solution += str(sir) + '\n'

        return solution, sir
    
    def solve(self):
        solve_a = self.solve_a()
        solve_b = self.solve_b()
        solve_c = self.solve_c()
        solve_d = self.solve_d()
        return solve_a + solve_b + solve_c + solve_d
    
    
