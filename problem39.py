from problem import Problem
import random


class Problem39(Problem):
    def __init__(self):
        statement = ""
        
#marime_vector=6 pentru exemplul din cerinta
#vector=[59, 32, 35, 74, 16, 25] pentru exemplul din cerinta
        
        marime_vector=random.randint(7, 10)
        vector = [None] * marime_vector

        #vector=random.sample(range(7, 10), marime_vector)
        for i in range(0, marime_vector):
            vector[i] = random.randint(1,100)
    
    
        statement = "Construiti un hash folosind valorile: "
        statement += str(vector[0])
        for i in range(1, marime_vector):
            statement += ","
            statement +=str(vector[i])
        statement +="\n"
        statement +="a). liste simplu inlantuite: h(x) = x % 7 \n"
        statement +="b). open adressing (linear probing): h(x, i) = (x + i) % 10 \n"
        statement +="c). quadratic probing: h(x, i) = (x + 3 * i^2 + 0 * i) % 17 \n"
        statement +="d). double hashing: h(x, i) = (x % 5 + i * (x % 7 + 1)) % 17 \n"
        
        
        data = vector
        super().__init__(statement, data)
        

    
    def solve(self):
        Capacitate=17
        vector = self.data
        marime_vector=len(vector)
        self.ht = HashTable()
        for i in range(0,marime_vector): 
            self.ht.inserare(vector[i],vector[i])
        solution = "a) Liste simplu inlantuite:\n"
        for i in range(0,7):   
            solution += self.ht.afisare(i)
        self.ht.compartimente = [None]*Capacitate    
        
        for i in range(0,marime_vector): 
            self.ht.inserare2(vector[i])
        solution += "\n"
        solution += "b) Linear probing:\n"
        for i in range(0,17):   
            solution += self.ht.afisare2(i)
  
        self.ht.compartimente = [None]*Capacitate
        for i in range(0,marime_vector): 
            self.ht.inserare3(vector[i])
        solution += "\n"
        solution += "c) Quadratic probing:\n"
        for i in range(0,17):   
            solution += self.ht.afisare2(i)
            
        self.ht.compartimente = [None]*Capacitate
        for i in range(0,marime_vector): 
            self.ht.inserare4(vector[i])
        solution += "\n"
        solution += "d) Double hashing:\n"
        for i in range(0,17):   
            solution += self.ht.afisare2(i)    
            
        return solution
    

  

            
class Nod:
	def __init__(self, cheie, valoarenod):
		self.cheie = cheie
		self.valoarenod = valoarenod
		self.next = None
    
class HashTable:
    
	# Initializam hash table-ul
    def __init__(self):
        Capacitate=17                     
        ht=Problem39()
        vector=ht.data
        self.capacitate = Capacitate
        self.compartimente = [None]*self.capacitate
        self.marime_vector=len(vector)
        self.vizitat=[0] * self.marime_vector
       # super().__init__(vizitat,marime_vector)
	# Generam index-ul pentru cheia data
    def hasha(self, cheie):
	    valoare = cheie % 7
	    return valoare
    
    def hashb(self, cheie,i):
	    valoare = (cheie + i) % 10
	    return valoare
    
    def hashc(self, cheie,i):
	    valoare = (cheie + 3 *i*i) % 17
	    return valoare
    
    def hashd(self, cheie,i):
        valoare = (cheie % 5 + (i * (cheie % 7 + 1))) % 17
        return valoare

	
    def inserare(self, cheie, valoarenod):
		# Apelam functia care calculeaza index-ul pentru cheia data
	    index = self.hasha(cheie)
		# Mergem la nodul corespunzator
	    nod = self.compartimente[index]
		# Daca "compartimentul" este gol creaza un nod il adauga si returneaza
	    if nod is None:
		    self.compartimente[index] = Nod(cheie, valoarenod)
		    return
		# Altfel il adauga la finalul listei inlantuite corespunzatoare index-ului
	    prev = nod
	    while nod is not None:
		    prev = nod
		    nod = nod.next
		
	    prev.next = Nod(cheie, valoarenod)
        
        
        
    def inserare2(self, cheie):
        k=0
        index = self.hashb(cheie,k)
        
        if self.compartimente[index] is None:
            self.compartimente[index]=cheie              
        else:
            while self.compartimente[index] is not None:
                k+=1
                index = self.hashb(cheie,k)
            self.compartimente[index]=cheie  
            
            
    def inserare3(self, cheie):
        k=0
        index = self.hashc(cheie,k)
        
        if self.compartimente[index] is None:
            self.compartimente[index]=cheie              
        else:
            while self.compartimente[index] is not None:
                k+=1
                index = self.hashc(cheie,k)
            self.compartimente[index]=cheie 
    
    
    def inserare4(self, cheie):
        k=0
        index = self.hashd(cheie,k)
        
        if self.compartimente[index] is None:
            self.compartimente[index]=cheie              
        else:
            while self.compartimente[index] is not None:
                k+=1
                index = self.hashd(cheie,k)
            self.compartimente[index]=cheie 
        
        
    def afisare(self,i):  
        solution =  str(i)+":"
        nod = self.compartimente[i]
        while nod is not None:
            solution += str(nod.valoarenod) + " "
            self.vizitat[i] += 1
            nod = nod.next
        solution += "\n"
        return solution
    

    def afisare2(self,i):        
        if self.compartimente[i] is not None:
            solution = "h[" +str(i)+"] = "
            solution += str(self.compartimente[i])
            solution += "\n"
            return solution	 
        else:
            solution=""
            return solution
                      
        