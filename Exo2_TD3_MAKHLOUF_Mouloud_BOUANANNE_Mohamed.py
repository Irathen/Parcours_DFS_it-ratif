

#def sommet
class Vertex:
    marked=False
    pre=None
    post=None
    neighbors=[]
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append((v))
            self.neighbors.sort()
    def set_marked():
        self.marked=True
    def set_pre(n):
        self.pre=n
    def set_post(n):
        self.post=n
    def is_marked(self):
        return self.marked==True
    def mark(self):
        self.marke=True
    
    

class Graph:
    vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
			# my YouTube video shows a silly for loop here, but this is a much faster way to do it
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
			
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))
    def print_graph_ord(self):
        for key in sorted(list(self.vertices.keys())):
            print(key +"=  Pre: "+ str(self.vertices[key].pre)+"  Post: "+str(self.vertices[key].post))
    def init_from_file(self,f):
        #Ajout des sommets dans le graphe g
        Gl=f.readline().split()
        for name in Gl:
         v=Vertex(name)
         self.add_vertex(v)
        #Remplissage des voisins de chaque sommets
        for i in f.readlines():
            arg=i.split('=')
            arg[0]=arg[0].strip()
            if len(arg)==2:
                list_neighbors=arg[1].split()
                for i in range(len(list_neighbors)):
                    list_neighbors[i]=list_neighbors[i].strip()
        
            else:
                print("erreur nombre d argument insuffisent")
            if arg[0] in self.vertices:
                for i in list_neighbors:
                    if i in self.vertices:
                        self.add_edge(arg[0],i)


f=open("Graphe.txt",'r')

#Creation du graphe
g = Graph()
g.init_from_file(f)

    
#Graphe final opertionnel   
print("Graphe construit avec la representation de liste d'adjacence")    
g.print_graph()
print("Sommets apres le parcours avec pre et post assignees")
#parcours iteratif DFS
time=1
P=[]
v=g.vertices["1"]
P.append(v)

while len(P) != 0:
    if  not v.is_marked():
        v.pre=time
        time+=1
        v.marked=True
        #print("v non marque")
        #print(v.name)
        """print(type(v.neighbors))
        print(type([1,3,5]))
        print(print([2,4,5].reverse()))
        print(v.neighbors.reverse())"""

        if len(v.neighbors)!=0:
            for i in v.neighbors[::-1]:
                if g.vertices[i].marked==False:
                    P.append(g.vertices[i])
        if len(P)>=1:
            v=P[-1]
    else:
        if v.post ==None:
            v.post=time
            time+=1
        v=P.pop()
        if len(P)>=1:
            v=P[-1]
        



g.print_graph_ord()



f.close()