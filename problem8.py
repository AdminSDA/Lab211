#Echipa 1, Grupa 211, Problema 8
import random 
from random import sample
from problem import Problem

class bcolors:
    PURPLE = '\033[95m'
    CYAN = '\033[96m' #TURCOAZ
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class Problem8(Problem):
    def __init__(self):
        statement = "Se da sirul "
        l = random.randint(5, 15) #l = lungimea sirului
        v = sample(range(1, 100), l)
        statement += str(v)
        statement += "\nRezolvati urmatoarele cerinte:\n"
        p1 = random.randint(2, l)
        p2 = random.randint(2, l)
        p3 = random.randint(2, l)
        p4 = random.randint(2, l)
        n = random.randint(1, l)  #Pt. subpunctul c)
        statement += "\na) aplicati "
        statement += str(p1)
        statement += " pasi din algoritmul de sortare prin insertie urmat de "
        statement += str(p2)
        statement += " pasi din algoritmul de sortare prin metoda bulelor;\n"
        statement += "\nb) aplicati "
        statement += str(p3)
        statement += " pasi din algoritmul de sortare prin selectia maximului urmat de "
        statement += str(p4)
        statement += " pasi din algoritmul de sortare prin selectia minimului;\n"
        statement += "\nc) ce elemente ar putea fi considerate pivoti a. i. la finalul unei partitionari a algoritmului Quicksort sa avem primele "
        statement += str(n)
        statement += " elemente sortate si specificati partitionarea folosita (Hoare/Lomuto/etc...);\n"
        statement += "\nd) exemplificati sortarea sirului folosind Insertion Sort si Selection Sort (minim).\n"
        data = [v, p1, p2, p3, p4, n, l]
        self.solution1 =""
        super().__init__(statement, data)
#======================================================================A==========================================================================   
    def solve_a(self):
        sir_a = self.data[0]
        p1 = self.data[1]
        p2 = self.data[2]
        l = self.data[6]
        sir = [x for x in sir_a]
        solution = bcolors.BOLD + bcolors.UNDERLINE + "\nSubpunctul a)" + bcolors.ENDC + "\n"
        solution += "\n>>>>>>>>>>>>>>>>>>> Aplicam " + str(p1) + " pasi din " + bcolors.UNDERLINE + bcolors.PURPLE + "Insertion Sort " + bcolors.ENDC + "<<<<<<<<<<<<<<<<<<<<\n"
        solution += str(sir)
        solution += "\nSetam un marker ce delimiteaza elementele sortate de cele nesortate.\n"
        solution += "\nConsideram primul element ca fiind sortat."
        solution += "\nSelectam primul element nesortat."
        solution += "\n" + bcolors.PURPLE + str(sir[0:1]) + bcolors.ENDC + str(sir[1:l]) + "\n"
        
        for i in range(1, p1+1):
            solution += bcolors.PURPLE + "\nPASUL: "+ str(i) +"\n" + bcolors.ENDC
            cp_i = i  
            solution += "\tElementul curent este: " + str(sir[i]) 
            solution += "\nIncercam sa gasim pozitia corecta a lui " + str(sir[i]) +  "\n" 
            while cp_i:
                
                if sir[cp_i] < sir[cp_i - 1]:
                    solution += "\nComparam " + str(sir[cp_i]) + " cu " + str(sir[cp_i - 1])
                    solution += "\n\tDaca " + str(sir[cp_i]) + " este mai mic " + str(sir[cp_i - 1]) + " facem interschimbarea.\n"
                    sir[cp_i], sir[cp_i - 1] = sir[cp_i - 1], sir[cp_i]
                    cp_i -= 1
                    solution +=  bcolors.PURPLE + str(sir[0:i+1]) + bcolors.ENDC + str(sir[i+1:l]) + "\n"
                else:
                    solution += "\nCele doua elemente sunt asezate corect.\n" + bcolors.PURPLE + str(sir[0:i+1]) + bcolors.ENDC + str(sir[i+1:l]) + "\n"
                    break
            
            
        
        solution += "\n>>>>>>>>>>>>>>>>>>> Aplicam " + str(p2) + " pasi din " + bcolors.UNDERLINE + bcolors.CYAN + "Bubble Sort" + bcolors.ENDC + " <<<<<<<<<<<<<<<<<<<<\n"
        solution += str(sir)
        for j in range(0, p2+1):
            modif = True
            solution += "\nParcurgem vectorul "+ bcolors.CYAN + "\nPASUL : "+str(j)+ bcolors.ENDC + "\n"
            while modif:
                modif=False
                for i in range(0, l-1):
                    solution += "\nComparam elementele doua cate doua.\n"
                    if sir[i] > sir[i+1]:
                        solution += "\nDaca cele doua elemente sunt asezate gresit, facem interschimbarea.\n"
                        sir[i], sir[i+1] = sir[i+1], sir[i]
                        modif = True
            solution += "\t" + str(sir[0:l-j]) + bcolors.CYAN + str(sir[l-j:l]) + bcolors.ENDC + "\n"
        cerinta = self.statement
        return cerinta, solution, sir
#=================================================================B===============================================================================
    def solve_b(self):
        sir_b = self.data[0]
        p3 = self.data[3]
        p4 = self.data[4]
        l = self.data[6]  
        sir = [x for x in sir_b]
        solution = bcolors.BOLD + bcolors.UNDERLINE + "\nSubpunctul b)" + bcolors.ENDC + "\n"
        solution += str(sir)
        solution += "\n>>>>>>>>>>>>>>>>>>> Aplicam " + str(p3) + " pasi din algoritmul de sortare prin " + bcolors.RED + bcolors.UNDERLINE + "selectia maximului" + bcolors.ENDC + " <<<<<<<<<<<<<<<<<<<<\n"
        for i in range(0, p3):
            solution += bcolors.RED + "\n PASUL: " + str(i+1) + bcolors.ENDC
            poz_max = i
            elem_max = sir[i]
            solution += "\nCautam pozitia pe care se afla elementul maxim si salvam si valoarea elementului maxim"
            
            for j in range(i, l):
                if sir[j] > elem_max:
                    solution += "\n" + str(sir[j]) + " > " + str(elem_max)
                    poz_max=j
                    elem_max=sir[j]
            
            solution += "\n Interschimbam elementele " + str(sir[i]) + " si " + str(sir[poz_max]) + "."
            sir[i], sir[poz_max] = sir[poz_max], sir[i]
            
            solution += "\n" + bcolors.RED + str(sir[0:i+1]) + bcolors.ENDC + str(sir[i+1:l]) + "\n"


        solution += "\n >>>>>>>>>>>>>>>>>>> Aplicam " + str(p4) + " pasi din algoritmul de sortare prin " + bcolors.YELLOW + bcolors.UNDERLINE + "selectia minimului" + bcolors.ENDC + "<<<<<<<<<<<<<<<<<<<<\n"
        solution += str(sir)
        for i in range(0, p4):
            solution += bcolors.YELLOW + "\n PASUL: " + str(i+1) + bcolors.ENDC
            poz_min = i
            elem_min = sir[i]
            solution += "\nCautam pozitia pe care se afla elementul minim si salvam si valoarea elementului minim"
            
            for j in range(i, l):
                if sir[j] < elem_min:
                    solution += "\n" + str(sir[j]) + " < " + str(elem_min)
                    poz_min = j
                    elem_min = sir[j]
            solution += "\n Interschimbam elementele " + str(sir[i]) + " si " + str(sir[poz_min]) +".\n"
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            solution += bcolors.YELLOW + str(sir[0:i+1]) + bcolors.ENDC + str(sir[i+1:l]) + "\n"
        
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
    
        self.solution1 += "\n" + bcolors.RED + "Pivot: " + str(pivot) + bcolors.ENDC + "\n"
        self.solution1 += str(sir[:poz_pivot]) + bcolors.RED + str(sir[poz_pivot]) + bcolors.ENDC + str(sir[poz_pivot+1:])
        
        while i < j:
            #incrementare i daca e mai mic  
            pas += 1
            self.solution1 += "\n" + bcolors.UNDERLINE + "Pasul : " + str(pas) + bcolors.ENDC
            if sir[i] < pivot:
                self.solution1 += "\nIncrementam " + str(sir[i]) + " < " + str(pivot)
                i = i + 1 
            elif sir[j] > pivot:
                self.solution1 += "\nDecrementam " + str(sir[j]) + " > " + str(pivot)
                j = j -1
                #self.solution1 += "\n" + str(sir) + "\n"
            else:
                self.solution1 += "\nInterschimbam " + str(sir[i]) + " cu "+ str(sir[j])
                sir[i], sir[j] = sir[j], sir[i]
            if i == j:
                self.solution1 += "\n"+ str(sir[:i]) + bcolors.RED + str(sir[i]) + bcolors.ENDC  + str(sir[i+1:]) + "\n"
            else:
                self.solution1 += "\n"+ str(sir[:i]) + bcolors.YELLOW + str(sir[i]) + bcolors.ENDC  + str(sir[i+1:j]) +bcolors.YELLOW + str(sir[j]) + bcolors.ENDC + str(sir[j+1:]) + "\n"
        return j

    def quickSort(self,sir,low,high,n): 
        if low < high: 
            poz_pivot = Problem8.partition(self,sir,low,high) 
            
            # sortam partea initiala intotdeauna
            Problem8.quickSort(self,sir, low, poz_pivot - 1, n) 
           
            #sortam doar daca poz_pivot +1 < nr elemente dorite
            if poz_pivot < n-1:
                Problem8.quickSort(self,sir, poz_pivot + 1, high, n) 

    def solve_c(self):
        sir = self.data[0]
        n = self.data[5]
        l = self.data[6]
        self.solution1 += bcolors.BOLD + bcolors.UNDERLINE + "\nSubpunctul c)" + bcolors.ENDC + "\n"
        while not self.verifica_sortarea(sir, l-1):
            Problem8.quickSort(self,sir,0,l-1,n) 
        self.solution1 += "\nFolosim partitionarea Hoare\n"
        #solution = str(sir)
        cerinta = self.statement
        return cerinta, self.solution1

 #===========================================================D===================================================================================   
    def solve_d(self):
        sir = self.data[0]
        sir_nou = [x for x in sir]
        l = self.data[6]

        solution = bcolors.BOLD + bcolors.UNDERLINE + "\nSubpunctul d)" + bcolors.ENDC + "\n"
        solution += str(sir_nou)
        solution += "\nAplicam algoritmul de " + bcolors.BLUE + bcolors.UNDERLINE + "sortare prin insertie" + bcolors.ENDC
        solution += "\nSetam un marker ce delimiteaza elementele sortate de cele nesortate.\n"
        solution += "\nConsideram primul element ca fiind sortat."
        solution += "\nSelectam primul element nesortat."
        solution += "\n" +bcolors.BLUE + str(sir_nou[0:1]) + bcolors.ENDC + str(sir_nou[1:l]) + '\n'

        for i in range(0, l):
            solution += bcolors.BLUE + "\nPASUL " + str(i+1) + bcolors.ENDC + ":"
            cp_i = i  
            solution += "\tElementul curent este: " + str(sir_nou[i]) 
            solution += "\nIncercam sa gasim pozitia corecta a lui " + str(sir_nou[i]) + "\n" 
            while cp_i:
                if sir_nou[cp_i] < sir_nou[cp_i - 1]:
                    solution += "\nComparam " + str(sir_nou[cp_i]) + " cu " + str(sir_nou[cp_i - 1])
                    solution += "\n\tDaca " + str(sir_nou[cp_i]) + " este mai mic " + str(sir_nou[cp_i - 1]) + " facem interschimbarea.\n"
                    sir_nou[cp_i-1], sir_nou[cp_i] = sir_nou[cp_i], sir_nou[cp_i-1]
                    cp_i -= 1
                else:
                    solution += "\nAm gasit pozitia corecta, deci ne oprim.\n" #+ bcolors.BLUE + str(sir_nou[0:i]) + bcolors.ENDC + str(sir_nou[i:l-1]) + "\n"

                    break
            solution += bcolors.BLUE + str(sir_nou[0:i+2]) + bcolors.ENDC + str(sir_nou[i+2:l]) +"\n"


        solution += "\nAplicam algoritmul de " + bcolors.GREEN + bcolors.UNDERLINE + "sortare prin selectia minimului" + bcolors.ENDC + "\n"
        solution += str(sir)
        for i in range(0, l):
            solution += bcolors.GREEN + "\nPASUL " + str(i+1) + bcolors.ENDC + ":"
            poz_min = i
            elem_min = sir[i]
            solution += "\nCautam pozitia pe care se afla elementul minim si salvam si valoarea elementului minim"
            for j in range(i+1, l):
                if sir[j] < elem_min:
                    solution += "\n" + str(sir[j]) + " < " + str(elem_min)
                    poz_min = j
                    elem_min = sir[j]
            solution += "\n Interschimbam elementele " + str(sir[i]) + " si " + str(sir[poz_min]) +".\n"
            sir[i], sir[poz_min] = sir[poz_min], sir[i]
            
            solution += bcolors.GREEN + str(sir[0:i+1]) + bcolors.ENDC + str(sir[i+1:l]) + "\n"

        return solution, sir
    
    
    def verifica_sortarea(self, sir, pivot):
        for i in range(pivot):
            if sir[i] > sir[i+1]:
                return False
        return True
    def solve(self):
        test_probl = Problem8()
        de_printat = test_probl.solve_a() 
        de_printat += test_probl.solve_b() 
        de_printat += test_probl.solve_c() 
        de_printat += test_probl.solve_d() 
        # [print(x) for x in de_printat]
        return de_printat
    


