class stack:
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
            
    def push(self,n):
        if self.isfull():
            return "Stack is full"
        else:
            self.data.append(n)
        
    def pop(self):
        if self.isempty():
            print("Stack is empyt")
        else:
            self.data.pop()
            
    def peek(self):
        print(self.data[-1])
    
    def display(self):
        print(self.data)
        
    def len_of_stack(self):
        print(len(self.data))
    
s=stack(5)


while True:
    print("1.push\n2.pop\n3.display\n4.peek\n5.isempty\n6.isfull\n7.len_os_Stack\n")
    opt=int(input("enter the operation  :"))
    match opt:
        case 1:
            val=input("enter element to insert:")
            s.push(val)
        case 2:
            print("removed element from stack",s.pop())
        case 3:
            s.display()
        case 4:
            print("top element of stack",s.peek())
        case 5:
            print("Is the stack is empty:",s.isempty())
        case 6:
            print("Is the stack is Full",s.isfull())
        case 7:
            print("length of the stack is",s.len_of_stack())
        case _:
            exit()
        



