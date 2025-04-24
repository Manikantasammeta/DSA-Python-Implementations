class node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Circular_linked_list:
    
    def __init__(self,):
        self.head =None
        
     #inserting at last   
    def insert_at_last(self,val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            new_node.next= self.head
        else:
            temp= self.head
            while temp.next!= self.head:
                temp =temp.next
                
            temp.next=new_node
            new_node.next = self.head
            
     #display       
    def display(self):
        if self.head is None:
            print("No elements to display")
        else:
            temp =self.head
            while temp:
                print(temp.data,end=" --> ")
                temp =temp.next
                if temp == self.head:
                    break
            print()
            
    #length of Cll     
    def len_of_cll(self):
        if self.head is None:
            print("no elelments to display")
        else:
            temp =self.head
            c=0
            while temp:
                c+=1
                temp=temp.next
                if temp ==self.head:
                    break
            return c
                 
    #inserting at first
    def insert_at_first(self,val):
        new_node =node(val)
        if self.head  is None:
            self.head =new_node
            new_node =self.head
        else:
            temp= self.head
            while temp.next !=self.head:
                temp = temp.next
            temp.next= new_node
            new_node.next=self.head
            self.head =new_node
        
        
    def inser_at_loc(self,n,loc):
        self.loc=loc
        self.n=n
        new_node = node(n)
        if self.loc<=0:
            print("enter the loc grater then 0")
        elif loc> self.len_of_cll():
            print("eneter the loc less then ",self.len_of_cll())
        elif self.head is None:
            self.head =new_node
            new_node =self.head
            
        elif loc == self.len_of_cll():
            self.insert_at_last(n)
            
        else:
            temp =self.head
            cnt =1
            while temp.next!= None and cnt<loc-1:
                temp =temp.next
                cnt +=1
            new_node.next =temp.next
            temp.next = new_node
            
    def delete_at_last(self):
        if self.head is None:
            print("no elements to delete")
        else:
            temp =self.head
            while temp.next.next !=self.head:
                temp= temp.next
            temp.next =self.head
            
    def delete_at_first(self):
        if self.head is None:
            print("no elements to delete")
    
            
        else:
            
            temp =self.head
            if temp.next== self.head:
                self.head= None
                exit
            else:
                a=temp.next
                while temp.next!=self.head:
                    temp =temp.next  
                temp.next= a
                self.head =a
            
            
    def delete_at_loc(self,loc):
        self.loc =loc
        if self.head is None:
            print("no elements to delete")
        elif loc <=0:
            print("enter loc greter then 0")
        elif loc > self.len_of_cll():
            print("enter loc less then",self.len_of_cll())
        elif self.len_of_cll()==1:
            self.head == None
        elif loc == self.len_of_cll():
            self.delete_at_last()
        else:
            temp =self.head
            cnt =1
            while cnt<loc-1:
                cnt+=1
                temp=temp.next
        
            temp.next= temp.next.next
            
            
            
    
        
        
        
        
        
            
               
                
        
s=Circular_linked_list()
s.insert_at_last(10)
s.display()
print("Length of Circular_linked_list -->",s.len_of_cll())
s.delete_at_first()
s.display()
print("Length of Circular_linked_list -->",s.len_of_cll())


s.insert_at_last(20)
s.insert_at_first(40)

s.insert_at_last(30)

s.display()
print("Length of Circular_linked_list -->",s.len_of_cll())
s.delete_at_first()
s.display()
# s.inser_at_loc(50,3)
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())
# s.display()

# s.inser_at_loc(90,5)
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())
# s.inser_at_loc(80,5)
# s.display()
# s.delete_at_last()
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())
# s.delete_at_first()
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())
# s.delete_at_loc(2)
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())
# s.insert_at_last(999)
# s.display()
# print("Length of Circular_linked_list -->",s.len_of_cll())



