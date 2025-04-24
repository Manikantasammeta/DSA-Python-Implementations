class node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prvc = None
class Circular_DoubleLL:
    def __init__(self):
        self.head =None
        
    def insert_at_first(self,val):
        newnode =node(val)
        # temp =self.head
        if self.head is None:
            self.head =newnode
            newnode.next =self.head
            newnode.prvc =self.head
        else:
            temp =self.head 
            while temp.next!=self.head:
                temp =temp.next
            temp.next=newnode
            newnode.next=self.head
            newnode.prvc =temp
            self.head.prvc=newnode
            self.head=newnode
            
            
            
    def insert_at_last(self,val):
        newnode = node(val)
        if self.head is None:
            self.head =newnode
            newnode.next =self.head
            newnode.prvc =self.head
        else:
            temp =self.head
            while temp.next != self.head:
                temp=temp.next
            temp.next=newnode
            newnode.prvc =temp
            self.head.prvc = newnode
            newnode.next =self.head
        
    def display(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp =self.head
            while temp:
                print(temp.data,end=" <==> ")
                temp =temp.next
                if temp == self.head:
                    break
            print()
            
    def length_of_cdll(self):
        if self.head is None:
            print("no elements to idspaly")
        else:
            temp =self.head
            cnt=0
            while temp:
                cnt+=1
                temp =temp.next
                if temp ==self.head:
                    break
        return cnt
                
            
    def insert_at_loc(self,val,loc):
        newnode =node(val)
        self.loc =loc
        if loc <=0:
            print("loc must be grater then Zero")
        elif loc >= self.length_of_cdll():
            print("the loc must be less then ",self.length_of_cdll())
        elif loc ==1:
            self.insert_at_first(val)
        elif self.head is None:
            self.head =newnode
            newnode.next =self.head
            newnode.prvc =self.head
        else:
            temp =self.head
            cnt =1
            while temp !=None and cnt<loc-1:
                temp=temp.next
                cnt+=1
            newnode.prvc =temp
            newnode.next=temp.next
            temp.next=newnode
            newnode.next.prvc =newnode
            
    def delete_at_last(self):
        if self.head is None:
            print("no elements to delete")
        else:
            temp =self.head
            while temp.next.next!=self.head:
                temp= temp.next
            self.head.prvc =temp
            temp.next =self.head 
            
    def delete_at_first(self):
        if self.head is None:
            print("no elements to display")
        else: 
            temp = self.head
            while temp.next!=self.head:
                temp= temp.next
            self.head=self.head.next
            self.head.prvc =temp
            temp.next =self.head
            
    def delete_at_loc(self,loc):
        if self.head is None:
            # self.loc=loc
            print("no elements to delete")
        elif loc < 0:
            print("loc is grater then zero")
        elif loc > self.length_of_cdll():
            print("loc is must be less then",self.length_of_cdll())
        elif loc==1:
            self.delete_at_first()
        elif loc==self.length_of_cdll():
            self.delete_at_last()
        else:
            temp =self.head
            cnt=1
            while temp != None and cnt<loc-1:
                cnt+=1
                temp= temp.next
            temp.next=temp.next.next
            temp.next.prvc =temp
             
c=Circular_DoubleLL()

while True:
    print("1.insert_at_first\n2.insert_at_last\n3.insert_at_loc\n4.Display\n5.length\n6.delete_at_first\n7.delete_at_last\n8.delete_at_loc")
    n=int(input("Enter the number :"))
    print("-"*20)
    match n:
        case 1:
            n=int(input("enter the element :"))
            c.insert_at_first(n)
        case 2:
            n=int(input("enter the element :"))
            c.insert_at_last(n)
        case 3:
            n=int(input("enter the element :"))
            loc=int(input("enter the loc :"))
            c.insert_at_loc(n,loc)
        case 4:
            c.display()
        case 5:
            print("the length of the CDLL-->",c.length_of_cdll())
        case 6:
            c.delete_at_first()
        case 7:
            c.delete_at_last()
        case 8:
            n=int(input("enter the loc :"))
            c.delete_at_loc(n)
    print("-"*20)
        