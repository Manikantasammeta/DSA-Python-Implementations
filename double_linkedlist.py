class node:
    def __init__(self,data):
        self.prce = None
        self.data =data
        self.next =None
        
        
class Double_linked_list:
    
    def __init__(self):
        self.head =None
    
    def display(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp =self.head
            while temp!= None:
                print(temp.data,end="<==>")
                temp = temp.next
            print()
                
                
                
                
    def insert_at_last(self,val):
        newnode =node(val)
        
        if self.head is None:
            self.head=newnode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prce= temp
            
    def length_of_Cll(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp =self.head
            c= 0
            while temp:
                c+=1
                temp =temp.next
            return c
        
            
            
    def insert_at_first(self,val):
        newnode =node(val)
        if self.head is None:
            self.head =newnode
        else:
            temp =self.head
            newnode.next=self.head
            self.head.prce =newnode
            self.head =newnode
                       
                     
                     
    def inser_at_loc(self,val,loc):
        newnode =node(val)
        if self.head is None:
            newnode=self.head
        else:
            temp =self.head
            cnt=1
            while cnt<loc-1:
                cnt+=1
                temp =temp.next
            newnode.next = temp.next
            temp.next=newnode
            newnode.prce =temp
            
    def delete_at_last(self):
        if self.head is None:
            print("no elements to dielete")
        else:
            temp =self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            
            
            
    def delete_at_first(self):
        if self.head is None:
            print("no elements to display")
        else:
            temp =self.head
            self.head=temp.next
            self.head.prce = None
                 
    def delete_at_loc(self,loc):
        if self.head is None:
            print("no elements to delete")
        elif loc ==1:
            self.delete_at_first()
        elif loc == self.length_of_Cll():
            self.delete_at_last()
        
        else:
            temp = self.head
            cnt =1
            while temp!=None and cnt<loc-1:
                cnt+=1
                temp=temp.next
            temp.next=temp.next.next
            temp.next.prvc =temp
                
                       
d=Double_linked_list()  
d.insert_at_first(10)
d.insert_at_first(70)
d.insert_at_first(90)
d.insert_at_first(100)
d.insert_at_last(20)
d.insert_at_last(30)
d.display()
d.delete_at_loc(6)
d.display()


