class Trees:
    def __init__(self,data):
        self.prev =None
        self.data= data
        self.next =None
        
    #inserting elements
    def inserting(self,val):
        if self.data:
            if val<self.data:
                if self.prev is None:
                    self.prev=Trees(val)
                else:
                    self.prev.inserting(val)
                    
            elif val>self.data:
                if self.next is None:
                    self.next =Trees(val)
                else:
                    self.next.inserting(val)
        else:
            self.data =val
   
    #display   
    def dis(self):
        if self.prev:
            self.prev.dis()
        print(self.data,end="->")
        if self.next:
            self.next.dis()
        
        
    #pre order
    def pre_order(self,root):
        if root:
            print(root.data,end="->")   
            self.pre_order(root.prev)
            self.pre_order(root.next)
            
    #in order
    def in_order(self,root):
        if root:
            self.in_order(root.prev)
            print(root.data,end="->")
            self.in_order(root.next)
            
            
    def post_order(self,root):
        if root:
            self.post_order(root.prev)
            self.post_order(root.next)
            print(root.data,end="->")
            
    def level_order(self,root):
        if root:
            print(root.data,end=" ")
            self.level_order(root)
            
    def Searching_val(self,val):
        if val<self.data:
            if self.prev is None:
                return "value not found"
            return self.prev.Searching_val(val)
        elif val>self.data:
            if self.next is None:
                return " value not found"
            else:
                self.next.Searching_val(val)
        else:
            return "value found"
                
                
    def height_o_tree(self,root):
        self.r=0
        self.l=0
        if root:
            self.r+=1
            self.height_o_tree(root.prev)
        elif root:
            self.r+=1
            self.height_o_tree(root.next)
            
        return max(self.r,self.l)
        
    
                   
t=Trees(15)
t.inserting(19)
t.inserting(9)
t.inserting(6)
t.inserting(12)
t.inserting(17)
t.inserting(20)
t.inserting(4)
t.inserting(7)
t.dis()
print()
print("PRE--ORDER")
t.pre_order(t)
print()
print("IN--ORDER")
t.in_order(t)
print()
print("POST--ORDER")
t.post_order(t)
print()

print(t.Searching_val(23))
print()
print(t.height_o_tree(t))

