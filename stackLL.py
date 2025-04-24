class node:
    def __init__(self,data):
        self.data =data
        self.next = None


class stacklinkedlist:
    def __init__(self):
        self.head =None
        
        
    def push(self,val):
        newnode = node(val)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head= newnode
        
        
    def display(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp =self.head
            while temp!=None:
                print(temp.data,end=" ")
                
                temp =temp.next
                
            print()
            
    def peek_ele(self):
        if self.head is None:
            print("no emements to dispaly")
        else:
            print("the peek element is-->",self.head.data)
            
            
    def min_ele(self):
        if self.head is None:
            print("no elements to display")
        else:
            min_ele =self.head.data
            temp =self.head
            while temp:
                if min_ele > temp.data:
                    min_ele =temp.data
                temp= temp.next
            print("min element-->",min_ele)
            
    def pop(self):
        if self.head is None:
            print("no elements to dispaly")
        else:
            self.head = self.head.next
            
s=stacklinkedlist()
s.push(10)
s.push(20)
s.push(1)

s.display()
s.push(66)
s.display()
s.peek_ele()
s.min_ele()
s.display()
s.pop()
s.display()