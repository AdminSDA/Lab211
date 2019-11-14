from problem import Problem
import random
from random import randint
 
def numar(x,stack):
     stack.append(x); #O(n)
 
def p(arr,stack):
     arr.append(stack.pop()); #O(n)
     

def p1(stack,x,vec):
     vec.append(stack.pop(x));
 
class Problem3(Problem):
    def __init__(self):
        statement = '3. Primiti o stiva. Operatii: \n'
        statement += 'numar -> se inseaza numarul in stiva \n'
        statement += 'P -> se extrage un numar din stiva si se afiseaza \n'
        statement += 'Introduceti in stiva urmatoarele numere: ' 
        
       
        data=[];
        n=randint(3, 99);  
        for i in range (1, n):
          data.append(randint(1, 99));
        statement += 'si determinati operatiile pentru care se afiseaza: '
        stack = data;
        i=1;
        n=len(stack);
        if n <= 3:
               k=randint(1,3);
          else:
               k=randint(int(n/2), n-3);
        contor=e=k;
        vec=[];
        while(i<n):
                  p1(stack,contor,vec);
                  if(i<e):
                      contor-=1;
                  i+=1;
                                                       
        p1(stack,contor-1,vec);
        
        statement += str(vec);
        statement += "\n"
        super().__init__(statement, data)
       
    def solve(self):
          solution = 'Vom parcurge vectorul\n'
          n = len(self.data); 
          data1=self.data;
          stack = [];
          arr = [];
          ok = 0; #ok := verifica daca s-a citit pana la k (k actioneaza ca un separator)
          i = 0;
          contor = 1;
          k=self.k
          n = n-1;
          solution +='Se va folosi raportul ' + str(int(k/n*100)) + '% si ' + str(int((n-k)/n*100)) + '% \n'
          solution +='Operatiile folosite sunt: \n'
          while i <= n:
                      if i <= k:
                            if ok == 0:
                                   e = self.data[i]
                                   numar(e,stack)
                                   solution += 'numar(' + str(e) + ')\n'
                                   if i == k:
                                              ok = 1;
                                              i = 1;
                                   else:
                                        i = i + 1;
                                        contor += 1;
                                       
                            elif contor-i != 0:
                                    e=data1[contor-i]
                                    solution += 'p()\n'
                                    p(arr,stack);
                                    i = i + 1;
                                    contor = contor - 1;
                                       
                            if ok == 1 & contor == 1:
                                    contor = k + 1;
                                   
                      else:
                            if contor == n:
                                break;
                            e = self.data[contor];
                            numar(e,stack);
                            solution+='numar('+str(e)+')\n'
                            solution+='p()\n'
                           
                            p(arr,stack);
                            contor = contor + 1;
                            i = i + 1;
                               
          solution+='p()\n'  
          p(arr,stack);
          return solution
