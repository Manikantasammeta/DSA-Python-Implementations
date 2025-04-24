class NODE:
    def __init__(self,data):
        self.data =data
        self.next = None
        
class single_linkedlist:
    def __init__(self):
        self.head =None
        
         
    #insert at  first
    def inser_at_first(self,n):
        new_node =NODE(n)
        new_node.next = self.head
        self.head = new_node
                    
    #inser at last
    def insert_at_last(self,n):
        New_node = NODE(n)
        if self.head is not None:
            temp = self.head
            
            while temp.next:       #if the node is not NONE the this loop willbe Executed
                temp =temp.next
            temp.next = New_node
            
        else:
            self .head = New_node
            
            
    def insert_at_loc(self,val,loc):
        new_node =NODE(val)
        if loc<=0:
            print("Enter the location Grater then 0")
        elif loc == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            c =1
            while temp != None and c < loc -1:
                temp = temp.next
                c+=1
            new_node.next = temp.next
            temp.next =new_node
            
            
    # delete at first
           
    def delete_at_front(self):
        if self.head is None:
            print('no elements')
        else:
            temp =self.head
            self.head =temp.next
            temp.next =None
                
        
    # delete at last        
    def delete_at_last(self):
        if self.head  is None:
            print("No elements to delete")
        else:
            temp =self.head
            while temp.next.next:
                temp =temp.next
            temp.next =None     
            
            
            
    #delete at location
    def delete_at_loc(self,loc):
        if self.head is None:
            print("No elements to delete")
        elif loc <=0:
            print("enter the loc grater then 0")
        elif loc == 1:
            temp =self.head
            self.head =temp.next
            temp.next =None
        else:
            temp =self.head
            c=1
            while temp !=None and c <loc -1:
                temp = temp.next
                c+=1

            temp.next =temp.next.next
            
                
            
            
    def display(self):
        if self.head is None:
            print("Single linkedlist Empty ")
        else:
            temp =self.head
            while temp !=None:
                print(temp.data,end=" --> ")
                temp =temp.next
            print()
            
            
    def len_of_sl(self):
        if self.head is None:
            print("No elements present")
        else:
            temp = self.head
            c =0
            while temp != None:
                c+=1
                temp = temp.next
            print(c)
              
        
sl =single_linkedlist()


while True:
    print("Enter\n1.Insert element at Firest\n2.Insert element a last\n3.Insert element at location\n4.Delete at at Firest\n5.Delete at Last\n6.Delete at Location\n7.Display elements\n8.Lenth of elements")
    n=int(input("enter number"))
    match n:
        case 1:
            val=int(input("Enter the element:"))
            sl.inser_at_first(val)
        case 2:
            val=int(input("Enter the element:"))
            sl.insert_at_last(val)
        case 3:
            val=int(input("Enter the element:"))
            ele=int(input("Enter the loc:"))
            sl.insert_at_loc(val,ele)
        case 4:
            sl.delete_at_front()
        case 5:
            sl.delete_at_last
        case 6:
            val=int(input("Enter the loc:"))
            sl.delete_at_loc(val)
        case 7:
            sl.display()
        case 8:
            sl.len_of_sl()
    print("*"*30)   
