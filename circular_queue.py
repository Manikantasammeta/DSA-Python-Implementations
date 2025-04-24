class Circle_Queue:
    def __init__(self,maxsize):
        self.maxsize =maxsize
        self.data = maxsize * [None]
        self.front =-1
        self.rare = -1
        
    def display(self):
        print(self.data)
        
    def isfull(self):
        if (self.front ==  0) and (self.rare+1 ==self.maxsize):
            return True
        elif  self.front ==self.rare+1:
            return True
        else:
            return False
        
    def isempy(self):
        if self.rare ==-1:
            return True
        else:
            return False
        
        
    def enqueue(self,n):
        if self.isfull():
            print("CQ is Full")
        else:
            if self.rare + 1 == self .maxsize:
                self.rare = 0
            else:
                self.rare +=1
                if self.front ==-1:
                    self.front+=1
            self.data[self.rare]=n
                    
    def peek(self):
        if self.isempy():
            print("CQ is empty")
        else:
            print(self.data[self.front])
            
            
    def dequeue(self):
        if self.isempy():
            return "no elements to delete"
        else:
            d = self.data[self.front]
            start = self.front
            if self.front ==self.rare:
                self.front =-1
                self.rare =-1
            elif self.front + 1== self.maxsize:
                self.front = 0
            else:
                self.front+=1
            self.data[start] =None
            return d
                
        
cq=Circle_Queue(5)
cq.display()
print(cq.isfull())
print(cq.dequeue())
cq.enqueue(10)
cq.display()
print(cq.isfull())
cq.enqueue(100)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.display()
print(cq.isfull())
cq.enqueue(40)
cq.dequeue()
cq.display()
print(cq.isfull())
cq.enqueue(90)
cq.display()
print(cq.isfull())
cq.enqueue(90)

