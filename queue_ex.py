class Queue:
    def __init__(self):
        self.bikes =[]
        self.cars =[]
        
    def enqueue(self,type,ele):
        self.type =type
        self.ele =ele
        if type =="car":
            self.cars.append(ele)
        elif type == "bike":
            self.bikes.append(ele)
        
    def dequeue(self,type):
        self.type =type
        if self.type =="bike":
            
            if len(self.bikes)==0:
                print("no bikes to delete")
            else:
                self.bikes.pop()
                
        else:
            if len(self.cars)==0:
                print("no cars to delete")
            else:
                self.cars.pop()
            
            
    def dequeueany(self):
        self.cars.pop()
        self.bikes.pop()
            
            
    def display(self):
        if len(self.bikes)==0:
            print("no bikes to display")
        else:
            print(self.bikes)
        if len(self.cars)==0:
            print("no cars to display")
        else:
            print(self.cars)
        print()
        
    def length_of_queue(self):
        print("length of cars-->",len(self.cars))
        print("length of bikes-->",len(self.bikes))
        
        
q=Queue()


while True:
    print("1.enqueue\n2.dequeue\n3.dequeueany\n4.display\n5.length")
    n=int(input("enter the number :"))
    print("-"*20)
    
    match n:
        case 1:
            t=input("enter type :")
            e=input("enter element :")
            q.enqueue(t,e)
        case 2:
            t=input("enter type :")
            q.dequeue(t)
        case 3:
            q.dequeueany()
        case 4:
            q.display()
        case 5:
            q.length_of_queue()
    print("-"*20)
            
            



