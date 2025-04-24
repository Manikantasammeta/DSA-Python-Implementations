class graph:
    def __init__(self):
        self.gdict={}
        
        
    def display(self):
        for i  in self.gdict:
            print(i,":",self.gdict[i])
        
    def addvertex(self,vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex]=[]
            
    def addedges(self,v1,v2):
        if v1 in self.gdict.keys() and v2 in self.gdict.keys():
            self.gdict[v1].append(v2)
            self.gdict[v2].append(v1)
            
      
    def deleteedge(self,v1,v2):
        if v1 in self.gdict.keys() and v2 in self.gdict.keys():
            self.gdict[v1].remove(v2)
            self.gdict[v2].remove(v1)
        
        
    def deletevertex(self,v1):
        if v1 in self.gdict.keys():
            for i in self.gdict.values():
                if v1 in i:
                    i.remove(v1)
            self.gdict.pop(v1)
            
                    
g=graph()
g.addvertex("A")
g.addvertex("B")
g.addvertex("C")
g.addvertex("D")
g.addvertex("E")
g.addvertex("F")
g.addvertex("G")
g.addedges("A","B")
g.addedges("B","D")
g.addedges("C","A")
g.addedges("D","C")
g.addedges("E","C")
g.addedges("E","F")
g.addedges("F","G")
g.addedges("F","D")
g.addedges("G","B")

g.display()
print()
g.display()
print()
g.deletevertex("A")
g.display()
