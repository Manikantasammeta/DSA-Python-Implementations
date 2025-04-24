class Queue:
    def __init__(self,maxsize):
        self.maxsize =maxsize
        self.data = []
    
    
    def isfull(self):
        if len(self.data)==self.maxsize:
            return  True
        else:
            return False
        
    def isempty(self):
        if len(self.data )==0:
            return True
        else:
            return False   
            
    def enqueue(self,n):
        if self.isfull():
            print("Queue is full")
        else:
            self.data.append(n)
         
    def dequeue(self):
        if self.isempty():
            print("Queue is empyt")
        else:
            self.data.pop()
            
    def peek(self):
        
        print(self.data[-1])
    
    def display(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.data)
        
    def len_of_queue(self):
        print(len(self.data))
    
q=Queue(5)
while True:
    print("1.Check Queue is full\n2.Check Queue is Empty\n3.EnQueue Element to Queue\n4.Dequeue Element from Queue\n5.Peek Element of Queue\n6.Display Elements of Queue\n7.length of Queue")
    n=int(input("enter the number :"))
    
    match n:
        
        case 1:
            print("-"*20)
            print("the queue is full-->",q.isfull())
        case 2:
            print("the queue is empty-->",q.isempty())
        case 3:
            v=int(input("enter the value :"))
            q.enqueue(v)
        case 4:
            q.dequeue()
        case 5:
            q.peek()
        case 6:
            q.display()
        case 7:
            q.display()
        case _:
            print("none")
    print("-"*20)
    print("-"*20)
    
    