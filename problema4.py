
from problem import Problem

class Problem4(Problem):
    def __init__(self):
        
        import random

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
        
        data=[array,k]

        super().__init__(statement, data)

    def solve(self):

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
            #def afisare(self):
                #solution+=self.array)

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
            #def afisare(self):
                #solution+=self.array)

        def print_state(queue, stack):
             stack_str = "\n\tStiva\t\t"
             if len(stack.array) != 0:
                for elem in stack.array:
                    stack_str += (str(elem)+ " ")
                stack_str += "(varf)"
             else:
                stack_str += "Stiva este goala.\n"
             queue_str = "\n\tCoada 1\t\t"
             if len(queue.array) != 0:
                for elem in queue.array:
                    queue_str += (str(elem) + " ")
                    queue_str += "<--"
             else:
                queue_str += "Coada este goala.\n"
             stack_str+=queue_str
             stack_str+="\n\tCoada 2\t\tCoada este goala.\n"
             return stack_str

        q = Queue([])
        s = Stack([])
        array = self.data[0]
        n = len(array)
        k = self.data[1]

        solution=" "

        for i in range (0, n):
            s.push(array[i])
        solution+=self.statement
        solution+="-------- Rezolvare --------\n\nAvem initial:"
        solution+=str(print_state(q, s))

        if s.top() != k:
            solution+="\n____________________________________________________\n"
            solution+="\nVom introduce in coada 1 toate elementele de pe stiva,"
            solution+="ce se afla deasupra elementului de scos\n"
            while s.top()!=k:
                q.push(s.top())
                solution+="\nAplicam operatia P " + str(s.top())+"\n"
                s.pop()  #am bagat prima jumate in coada
                solution+=str(print_state(q, s))
            solution+="\n______________________________________\n"
            solution+="\nVom scoate elementul cerut de pe stiva\n"
            solution+="\nAplicam operatia S " + str(s.top())
            s.pop()
            print_state(q, s)
            if s.length() != 0:
                solution+="\n______________________________________________________\n"
                solution+="\nIntroducem in coada 1 toate elementele ramase pe stiva\n"
            while s.length() != 0:
                q.push(s.top())
                solution+="\nAplicam operatia P " + str(s.top())
                s.pop() #am bagat a 2a jum in coada
                solution+=str(print_state(q, s))
            solution+="\n"
            solution+="\n______________________________________________________\n"
            solution+="\nIntroducem toate elementele din coada 1, in ordine, pe stiva\n"
            while q.length() != 0:
                s.push(q.top()) #am bagat toata coada in stiva
                solution+="\nAplicam operatia I_1 " + str(s.top())
                q.pop()
                solution+=str(print_state(q, s))
            solution+="\n"
            solution+="\n_______________________________________________\n"
            solution+="\nScoatem toate elementele de pe stiva, in ordine"
            solution+="si le introducem in coada 1\n"
            while s.length() != 0: #am bagat toata stiva in coada
                q.push(s.top())
                solution+="\nAplicam operatia P " + str(s.top())+"\n"
                s.pop()
                solution+=str(print_state(q, s))
            solution+="\n"
            solution+="\n______________________________________________________\n"
            solution+="\nIntroducem toate elementele din coada 1, in ordine, pe stiva\n"
            while q.length() != 0:
                s.push(q.top()) #am bagat toata coada in stiva
                solution+="\nAplicam operatia I_1 " + str(s.top())
                q.pop()
                solution+=str(print_state(q, s))
            solution+="\n"
        else:
            solution+="\n___________________________________________\n"
            solution+="\nElementul de scos se afla in varful stivei,"
            solution+="deci vom aplica operatia S " + str(s.top()) + "\n"
            s.pop()
            solution+=str(print_state(q, s))

        
        return solution
