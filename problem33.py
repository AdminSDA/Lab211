class nod:
    def __init__(self, val):   #initializarea nodului
        self.value = val
        self.st = None
        self.dr = None
        self.h = 1
    def insert(self, data):     #inseram cate un element in bst
        if self.value == data:
            return False
        elif self.value > data:
            if self.st:
                return self.st.insert(data)
            else:
                self.st = nod(data)
                return True
        else:
            if self.dr:
                return self.dr.insert(data)
            else:
                self.dr = nod(data)
                return True
    def height(self):       #tinem cont de inaltime, ca sa putem aplica apoi rotirile
        if self.st and self.dr:
            return 1 + max(self.st.height(), self.dr.height())
        elif self.st:
            return 1 + self.st.height()
        elif self.dr:
            return 1 + self.dr.height()
        else:
            return 1
    def inorder(self):      #facem si o parcurgere
        if self:
            if self.st:
                self.st.inorder()
            print (str(self.value))
            if self.dr:
                self.dr.inorder()
class BST:
    def __init__(self):
        self.r = None
    def insert(self,data):
        if self.r:
            return self.r.insert(data)
        else:
            self.r = nod(data)
            return True
    def height(self):
        if self.r:
            return self.r.height()
        else:
            return 0
    def balance(self, r):       #functie de verificat balansul
        if not r:
            return 0
        return self.height(r.st) - self.height(r.dr)

    def LR(self, b):        #rotire stanga
        a = b.dr
        S1 = a.st
        a.st = b
        b.dr = S1
        b.h = 1 + max(self.height(b.st), self.height(b.dr))
        a.h = 1 + max(self.height(a.st), self.height(a.dr))
        return a

    def RR(self, b):        #rotire dreapta
        a = b.st
        S2 = a.dr
        a.dr = b
        b.st = S2
        b.h = 1 + max(self.height(b.st), self.height(b.dr))
        a.h = 1 + max(self.height(a.st), self.height(a.dr))
        return a

    def inorder(self):
        print("INORDER")
        self.r.inorder()


bst = BST()

r = None
nums = [7, 5, 4, 3, 1, 2, 6, 9]
for num in nums:
    r = bst.insert(num)

# Nu am mai avut timp sa translatez din c++ in py, a ramas de asamblat toate functiile si de afisat procedural rotirile.