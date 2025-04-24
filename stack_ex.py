# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)                        #factorial
# print(fact(int(input("enter a number: "))))

# enter a number: 5
# 120


# def nat(n,s=0):
#     if n>0:
#         return nat(n=n-1,s=s+n)                                 #sum of natural numbers
#     return s

       
# print(nat(int(input("enter a number :"))))

# enter a number :10
# 55



# def ss(n):
#     if n==0:
#         return 0                                      #sum of given number
#     else:
#         return n%10 +ss(n//10)
 
 
  
# print(ss(int(input("enter :"))))

# enter :5432
# 14



# l=[1,[2,[3],4],5,6,[7,[8],[9],10]]
# l1=[]
# def fun(l):
# 	for i in l:
#             if type(i)!=list:
#                     l1.append(i)													 #with out useing bulit-in methods
#             else:
#                  fun(i)

# fun(l)
# print(l1)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def pall(s):
#      if len(s)<=0:
#           return "it is pallindrome" 
#      elif s[0]!=s[-1]:
#           return "it is not a pallendrome"                                    #pallindrome 
#      else: return pall(s[1:-1])

# while True:
#      print(pall(input("enter str: ")))
     
     
# enter str: mani
# it is not a pallendrome
# enter str: maam
# it is pallindrome
# enter str:  
# it is pallindrome
# enter str: level
# it is pallindrome



# def ll(l1,sum=0,product=1):
#      if len(l1)==0:
#           return f"sumof list:{sum}\nproduct:{product}"                            #sum and product of list elements
#      else:
#           return ll(l1[1:],sum+l1[0],product*(l1[0]))
     
# print(ll([1,2,3,4,5,6,7,8]))

# sumof list:36
# product:40320




# def num(n):
#      if n<5:
#           print(n,end=" ")
#           num(n+1)
#           print(n,end=" ")
          
# num(1)

# 1 2 3 4 4 3 2 1 


# n=[1,[2],[3,4,7],[8,9],10]
# def fun(k,l1=[]):
#     if len(k)>0:
#         if type(k[0])==list:
#             l1.extend(k[0])
#             return fun(k[1::])                           #converting the multi dimensional to single dimensional
#         elif type(k[0])==int:
#             l1.append(k[0])
#             return fun(k[1::])
            
#     return l1
# print(fun(n))

# [1, 2, 3, 4, 7, 8, 9, 10]


class stack:
    def __init__(self,maxsize):
        self.maxsize =maxsize
        self.data = []
    
    def push(self,val):
        if len(self.data)>0 and len(self.data[-1])<self.maxsize:
            self.data[-1].append(val)
        else:
            self.data.append([val])
            
            
    def display(self):
        print(self.data)
        
        
    def pop(self):
        if len(self.data) ==0:
            return None
        if len(self.data) and len(self.data[-1])==0:
            return self.data.pop()
        if len(self.data[-1]):
            self.data.pop(-1)
        
        else:
            return self.data[-1].pop()
        
        
        
    def pop_at(self,stacknum):
        if stacknum>len(self.data):
            print("the loc must be less then",len(self.data))
        elif len(self.data[stacknum])>0:
            return self.data[stacknum].pop()
        
        
s=stack(3)
s.push(5)
s.push(3)
s.push(7)
s.push(8)
s.push(9)
s.push(0)
s.push(5)
s.display()
s.pop()
s.display()
s.pop_at(0)
s.display()
        
