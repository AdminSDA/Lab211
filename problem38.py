import random;
import string;   
import Problem from problem
 
def random_char(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
 
       
class NTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def __str__(self):
        return '%s_%s' % (self.left, self.right)  
       
def return_all(key1, key2, c1, c2):
   
        if type(key1) is NTree:
             key11 = str(key1);
             key1 = key11;
        if type(key2) is NTree:
             key21 = str(key2);
             key2 = key21;
             
             
        if(key1.count('D')>=1 and key2 == 'A'):
            if c2 < c1:
                 return 'A'
            else:
                    return 'B'
                   
        if(key1.count('C')>=1 and key2 == 'A'):
            if c2 < c1:
                 return 'A'
            else:
                     return 'B'            
                     
                     
        if(key1 == 'A' and key2.count('D')>=1):
            if c1 < c2:
                 return 'A'
            else:
                    return 'B'
                 
                 
        if(key1 == 'A' and key2.count('C')>=1):
            if c1 < c2:
                 return 'A'
            else:
                    return 'B'
         
        if(key1.count('A')>=1 and key1.count('B')>=1 and key1.count('C')>=1 and key2=='E'):
                if c1 < c2:
                    return 'B'
       
                   
        if(key2.count('A')>=1 and key2.count('B')>=1 and key2.count('C')>=1 and key1=='E'):
                 if c2 > c1:
                    return 'B'  
                    
        if(key1.count('D')>=1 and key1.count('B')>=1 and key1.count('C')>=1 and key2=='E'):
                if c1 < c2:
                    return 'B'
       
                   
        if(key2.count('D')>=1 and key2.count('B')>=1 and key2.count('C')>=1 and key1=='E'):
                 if c2 > c1:
                    return 'B'    
                
        if(key1.count('B')>=1 and key1.count('C')>=2 and key2=='E'):
                if c1 < c2:
                    return 'B'
       
                   
        if(key2.count('B')>=1 and key2.count('C')>=2 and key1=='E'):
                 if c2 > c1:
                    return 'B'  
                    
        if(key1.count('B')>=1 and key1.count('D')>=2 and key2=='E'):
                if c1 < c2:
                    return 'B'
       
                   
        if(key2.count('B')>=1 and key2.count('D')>=2 and key1=='E'):
                 if c2 > c1:
                    return 'B'              
                   
        if(key1.count('A')>=1 and key2 == 'E'):
            if c2 < c1:
                 return 'C'
            else:
                    return 'B'           
        
        if(key1.count('C')>=1 and key2 == 'E'):
            if c2 < c1:
                 return 'C'
            else:
                    return 'B'
                   
        if(key1.count('D')>=1 and key2 == 'E'):
            if c2 < c1:
                 return 'C'
            else:
                    return 'B' 
             
             
        if(key2.count('A')>=1 and key1 == 'E'):
            if c1 < c2:
                 return 'C'
            else:
                    return 'B'           
        
        if(key2.count('C')>=1 and key1 == 'E'):
            if c1 < c2:
                 return 'C'
            else:
                    return 'B'
                   
        if(key2.count('D')>=1 and key1 == 'E'):
            if c1 < c2:
                 return 'C'
            else:
                    return 'B'    
         
                   
        else:
            return 'C'            
 
class Problem38(Problem):
    def __init__(self):
        statement = "Alegeti pentru fiecare propozitie, care dintre afirmatiile A, B, sau C se potriveste cel mai bine:\n"
        statement+= "A. Adevarat, indiferent de mesaje.\n"
        statement+= "B. Fals, indiferent de mesaje.\n"
        statement+= "C. Depinde de mesaj.\n"
        statement+= "Frecventa literei A este strict mai mica decat frecventa literei B. (C.)\n"
        statement+="Frecventa literei C este mai mare sau egala cu frecventa literei A. (A.)\n"
        statement+="Frecventa literei D este strict mai mare decat frecventa literei A. (A.)\n"
        statement+="Frecventa literei D este mai mare sau egala cu suma frecventelor lui A, B si C. (C.) (A, B, C = 1, D = 2).\n"
        statement+="Frecventa literei E este strict mai mica decat suma frecventelor literelor A, B si C. (B.)\n"
        y = random.randint(5, 20);
        data = random_char(y);
        data = data + " "
        data += random_char(random.randint(5,20));
        data = data + " "
        data += random_char(random.randint(5,20));
        data = data + " "
        data += random_char(random.randint(5,20));
        statement+="Propozita este " + data +" \n";
        super().__init__(statement, data)
       
    def solve(self):
        solution="Ca idee, folosim algoritmul lui Huffman si implementam arborele binar\n"
        solution+="Selectam literele A,B,C,D,E din propozitie si stabilim ca orice litera este adevarata\n"
        solution+="Vectorul selectat este:\n"
        letters="ABCDE"
        nodes=[];
        i = 0;
        e = len(self.data);
        data = self.data;
        while i < 5:
            if data.count(letters[i]) != 0:
                nodes.append((letters[i], data.count(letters[i]), "A"));
     
            i = i + 1;
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        solution+=str(nodes) + '\n';
        returned_key=0;
        while len(nodes) >= 2:
            e = nodes[-1]
            f = nodes[-2]
            (key1, a, b) = e;
            (key2, a1, b1) = f;
            nodes = nodes[:-2]
            returned_key = return_all(key1, key2, b, b1);
            node = NTree(key1, key2);
            nodes.append((node, a + a1, returned_key))
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
           
        if(returned_key == 'A'):
                solution+="Adevarat, indiferent de propozite\n";
   
        if(returned_key == 'B'):
                solution+="Fals, indiferent de propozite\n'";
 
        if(returned_key == 'C'):
                solution+='In functie de propozitie\n';
                
        return solution;
