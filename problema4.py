import random

class Stack:
   def __init__(self, array):
       self.array = array
   def top(self):
      return self.array[len(self.array)-1]
   def pop(self):
       self.array = self.array[0:(len(self.array) - 1)]
   def push(self, element):
       self.array.append(element)
   def length(self):
       return len(self.array)
   def afisare(self):
       print self.array

class Queue:
   def __init__(self, array):
       self.array = array
   def top(self):
       return self.array[0]
   def pop(self):
       self.array=self.array[1:(len(self.array))]
   def push(self, element):
     self.array.append(element)
   def length(self):
       return len(self.array)
   def afisare(self):
       print self.array

class Problem4:
   def __init__(self, statement, count, array,k):
       self.statement = statement
       self.count = count
       self.array = array
       self.k = k

def generate():
   count = random.randint(1, 10)
   array = random.sample(range(1, 12), count)
   k = random.choice(array)
   statement = "Avand elementele " # in functie de count, array
   for elem in array:
    statement += (str(elem) + " ")
   statement += "intr-o stiva ("
   statement += str(array[-1])
   statement += " este ultimul el. inserat), gasiti o"
   statement += " succesiune de mutari a.i. sa stergeti el. "
   statement += str(k)
   statement += " din stiva avand la dispozitie 2 cozi si operatiile:"
   statement += "\nP -> se extrage un el. din stiva, se introduce in prima coada"
   statement += "\nS -> se sterge un el. din stiva"
   statement += "\n1 -> se extrage un el. din coada 1 se introduce in coada 2"
   statement += "\n2 -> se extrage un el. din coada 2 se introduce in coada 1"
   statement += "\nI_1 -> se extrage un el din coada 1 si se introduce in stiva"
   statement += "\nI_2 -> se extrage un el din coada 2 si se introduce in stiva\n\n"
   return Problem4(statement, count, array,k)

def print_state(queue, stack):
  stack_str = "\tStiva\t\t"
  if len(stack.array) != 0:
    for elem in stack.array:
      stack_str += (str(elem)+ " ")
    stack_str += "(varf)"
  else:
    stack_str += "Stiva este goala."
  queue_str = "\tCoada 1\t\t"
  if len(queue.array) != 0:
    for elem in queue.array:
      queue_str += (str(elem) + " ")
    queue_str += "<--"
  else:
    queue_str += "Coada este goala."
  print stack_str
  print queue_str
  print "\tCoada 2\t\tCoada este goala."

pb = generate()
q = Queue([])
s = Stack([])
array = pb.array
n = pb.count
k = pb.k
array = pb.array
n = pb.count
k = pb.k

for i in range (0, n):
    s.push(array[i])
print pb.statement
print "-------- Rezolvare --------\n\nAvem initial:"
print_state(q, s)

if s.top() != k:
    print "\n____________________________________________________"
    print "Vom introduce in coada 1 toate elementele de pe stiva,"
    print "ce se afla deasupra elementului de scos\n"
    while s.top()!=k:
        q.push(s.top())
        print "\nAplicam operatia P " + str(s.top())
        s.pop()  #am bagat prima jumate in coada
        print_state(q, s)
    print "______________________________________"
    print "Vom scoate elementul cerut de pe stiva"
    print "\nAplicam operatia S " + str(s.top())
    s.pop()
    print_state(q, s)
    if s.length() != 0:
        print "______________________________________________________"
        print "Introducem in coada 1 toate elementele ramase pe stiva"
    while s.length() != 0:
        q.push(s.top())
        print "\nAplicam operatia P " + str(s.top())
        s.pop() #am bagat a 2a jum in coada
        print_state(q, s)
    print "\n"
    print "______________________________________________________"
    print "Introducem toate elementele din coada 1, in ordine, pe stiva\n"
    while q.length() != 0:
        s.push(q.top()) #am bagat toata coada in stiva
        print "\nAplicam operatia I_1 " + str(s.top())
        q.pop()
        print_state(q, s)
    print "\n"
    print "_______________________________________________"
    print "Scoatem toate elementele de pe stiva, in ordine"
    print "si le introducem in coada 1\n"
    while s.length() != 0: #am bagat toata stiva in coada
        q.push(s.top())
        print "\nAplicam operatia P " + str(s.top())
        s.pop()
        print_state(q, s)
    print "\n"
    print "______________________________________________________"
    print "Introducem toate elementele din coada 1, in ordine, pe stiva\n"
    while q.length() != 0:
        s.push(q.top()) #am bagat toata coada in stiva
        print "\nAplicam operatia I_1 " + str(s.top())
        q.pop()
        print_state(q, s)
    print "\n"
else:
    print "\n___________________________________________"
    print "Elementul de scos se afla in varful stivei,"
    print "deci vom aplica operatia S " + str(s.top()) + "\n"
    s.pop()
    print_state(q, s)