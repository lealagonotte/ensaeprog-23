
import queue
import sys
sys.setrecursionlimit(100000)


class Graph:
    """    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------

    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.    """
    def __init__(self, nodes=[]):
        """       Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.        """

        self.nodes = nodes   #liste des étiquettes du graphe
        self.graph = dict([(n, []) for n in nodes])   #on représente le graphe par une liste d'adjacence : à chaque noeud on associe une liste qui contient les noeuds avec lesquels il est connecté, le power_min et la distance
        self.nb_nodes = len(nodes)
        self.nb_edges = 0    #nombre d'arretes  

    
    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"          

        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output    

   
    def add_edge(self, node1, node2, power_min, dist=1):
        """        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.
        Parameters: 
                ----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        #si node1 ou node2 n'est pas dans la liste des étiquettes, on le rajoute. On met à jour la variable self.nb_nodes
        if node1 not in self.graph :
            self.graph[node1]=[]
            self.nb_nodes +=1
            self.nodes.append(node1)
        if  node2 not in self.graph :
            self.graph[node2]=[]
            self.nb_nodes +=1
            self.nodes.append(node2)      
#On rajoute la nouvelle arrête du graphe en ajoutant le triplet à la liste associée à l'étiquette node1 puis à l'étiquette node2
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min,dist))
        #on met à jour le nombre d'arrête
        self.nb_edges += 1  


    def get_path_with_power(self, src, dest, power):
        """Renvoie un chemin possible entre src et dest si un camion de puissance power peut couvrir le trajet t=(src, dest), 
        None si ce n'est pas possible
        Paramètres : 
        -src : ville (étiquette) de laquelle on part
        -dest : ville (étiquette) vers laquelle on veut aller
        -power : puissance du camion qui veut réaliser ce trajet """

        #On fait un parcours en profondeur récursif 
        marquage = [False for i in range(self.nb_nodes)]   #on marque les sommets que l'on visite
        #initialement, on n'en a visité aucun
        pred = [-1 for i in range(self.nb_nodes)]   #le tableau des prédecesseurs sert à savoir par quel sommet on est passé juste avant 
        #il sera utile pour reconstruire le chemin par lequel on est passé
        def dfs_rec(s):
        #  on fait une fonction intermédiaire pour le parcours récursif  
            marquage[s-1]=True   #on marque le sommet s : on l'a visité
            for voisin in self.graph[s]: #on regarde les voisins de s
                (i, j, k)=voisin  #i : noeud voisin, j puissance minimale pour passer par l'arrête (s,i), k distance
                if not (marquage[i-1]) and j <= power:  #si on n'a pas déjà visité i et que le camion peut passer
                    marquage[i-1] = True
                    pred[i-1] = s  #le prédecesseur de i est s
                    dfs_rec(i)  #on récure
        dfs_rec(src)  #on fait le parcours à partir de la source
        if marquage[dest-1]==False :  #on n'a pas visité dest donc le chemin n'existe pas
            return None
#on utilise le tableau de prédecesseur pour reconstruire le chemin
        chemin = [dest]
        p = dest
        while p != src:
            p = pred[p-1]
            chemin.append(p)
        n = len(chemin)
        #le chemin est à l'envers donc on le retourne
        for i in range(n//2):            
            chemin[i], chemin[n-1-i] = chemin[n-1-i], chemin[i]
        return chemin                                
# complexité de l'algorithme : 
# la complexité est celle d'un parcours en profondeur 
# Grâce au marquage, on passe au plus 1 fois par chaque sommet. 
# Pour chaque sommet, on a une boucle for : on fait le nombre d'arrêtes dans lesquelles s est une extremité
#La complexité est donc O(V+E) avec V le nombre de sommets et E le nombre d'arrêtes de G

    def connected_components(self):
"""Résultat : Renvoie les composantes connexes du graphe"""
# on fait un parcours en profondeur récursif comme au-dessus
# on crée la liste qui contiendra les composantes connexes
        comp_connexe=[] 
        marquage = [False for i in range(0,self.nb_nodes)] # on procède comme au-dessus       

        def dfs_rec(s) :
            comp=[s] #comp sera la liste représentant la classe dont un représentant est s
            marquage[s-1]=True
            for i in self.graph[s] : # i est tuple (node2, power, dist)
                i=i[0] #on veut la deuxième extrémité de l'arrête : elle est dans la composante connexe de s
                if marquage[i-1]==False :
                    marquage[i-1]=True
                    comp+=dfs_rec(i) #on récure pour ajouter tous les sommets tels qu'il existe un chemin entre s et ce sommet
            return comp    #on renvoie la composante connexe représentée par s          
# on veut toutes les composantes connexes donc on a fini quand on a parcouru tout le graphe ie tous les sommets sont marqués
        for noeud in self.nodes :
            if marquage[noeud-1]==False :
                comp_connexe.append(dfs_rec(noeud))
        return comp_connexe    
#Concernant la complexité, on réalise 

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})        """

        return set(map(frozenset, self.connected_components()))
    

    def min_power(self, src, dest):
        """
        Should return path, min_power.
        """

        #il faut trouver une puissance qui marche
        #on teste avec des 2**n pour limiter la complexité
        #deja il faut voir si un chemin existe 
        #ou bien puissance infinie ou bien meme composante connexes
        power=float("inf")

        if self.get_path_with_power(src, dest, power) == None :
            return None #pas de chemin possible
        else :
            #il existe un chemin et une puissance minimale
            #on cherche alors une puissance et un entier n tel que 2**n marche, on sait alors que p min sera entre 2**n-1 et 2**n

            n=0
            while self.get_path_with_power(src, dest, 2**n) == None :
                n+=1
            #on fait la dico

            a=2**(n-1)
            b=2**n
            while b-a>1 :
                m=(a+b)//2
                if self.get_path_with_power(src, dest, m) == None :
                    a=m
                else :
                    b=m
        return (self.get_path_with_power(src, dest, b),b)



    def plus_court_chemin(self, src, dest, power) :
    #on fait une file de priorité
            f=queue.PriorityQueue()
            dist=[-1 for i in range(self.nb_nodes)]
            marquage = [False for i in range(self.nb_nodes)]
            pred=[-1 for i in range(self.nb_nodes)] 
            dist[src-1]=0
            marquage[src-1]=True  
            f.put(src, 0)
    
            while not f.empty() : 
                u=f.get()
                marquage[u-1]=True
                for voisin in self.graph[u] :
                    (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
                    if not (marquage[i-1]) and j<=power and (dist[i-1]==-1 or dist[i-1]>d+k):
                        marquage[i-1]=True
                        pred[i-1]=u
                        dist[i-1]=dist[u-1]+k
                        f.put(i, dist[u-1]+k)
                
        
            if marquage[dest-1]==False :
                return None
            chemin = [dest]
            p=dest
            while p != src :
                p=pred[p-1]
                chemin.append(p)
            n=len(chemin)
            for i in range(n//2) :     

                chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]
            return chemin
    def pas_cycle(self, arrete) :
        comp=self.connected_components()
        (a,b,c)=(arrete)
        for i in comp :
            if a in i and b in i :
                return False
        return True

    def kruskal(self) :
        dico=self.graph
       
        #trier en fonction de key sorted
        Gf=Graph([k for k in range(1,self.nb_nodes)])
        liste_arrete=[]
        for i in range (1,self.nb_nodes) :
            for d in dico[i] :
                (a,b,c)=d
                if i< a :
                    liste_arrete.append((i,a,b))
        
        liste_arrete=sorted(liste_arrete, key=lambda x : x[2])
        for arrete in liste_arrete :
            (i,a,b)=arrete
            if Gf.pas_cycle(arrete) :
                Gf.add_edge(i, a, b)
        return Gf


def graph_from_file(filename):

    """

    Reads a text file and returns the graph as an object of the Graph class.



    The file should have the following format: 

        The first line of the file is 'n m'

        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)

        The nodes (node1, node2) should be named 1..n

        All values are integers.



    Parameters: 

    -----------

    filename: str

        The name of the file



    Outputs: 

    -----------

    G: Graph

        An object of the class Graph with the graph from file_name.

    """

    f=open(filename)

    ligne=f.readline().split()

    nb_nodes=int(ligne[0])

    nb_edges=int(ligne[1])

    nodes=[i for i in range(1, nb_nodes +1)]

    G=Graph(nodes)

    for i in range(nb_edges) :

        line=f.readline().split()

        if len(line) == 4 :

            G.add_edge(int(line[0]), int(line[1]), int(line[2]), int(line[3]))

        else : 

            G.add_edge(int(line[0]), int(line[1]), int(line[2]), 1)

    f.close()

    return G    



#with open(filename, "r") as file:

       # n, m = map(int, file.readline().split())

       # g = Graph(range(1, n+1))

       # for _ in range(m):

          #  edge = list(map(int, file.readline().split()))

          #  if len(edge) == 3:

          #      node1, node2, power_min = edge

           #     g.add_edge(node1, node2, power_min) # will add dist=1 by default

          # elif len(edge) == 4:

            #    node1, node2, power_min, dist = edge

             #   g.add_edge(node1, node2, power_min, dist)

            #else:

              #  raise Exception("Format incorrect")

    #return g

 





#cout(n,m)=O(n+m), m sommets  n arretes complexité truc




import graphviz

def represente(G, src, dest, power=1) :
    graphe=graph_from_file(G)
    g=graphviz.Graph(filename='G', format='png', directory="delivery_network", engine='dot')
    chemin=graphe.get_path_with_power(src, dest, power )
    gf=open(G, "r")
    gf.readline()
    gf=gf.readlines()
    for i in range(0,len(gf)) :
         
        gf[i]=gf[i].split()
        if chemin != None and int(gf[i][0]) in chemin and int(gf[i][1]) in chemin :
            g.edge(gf[i][0], gf[i][1], color="green")
        else :
            g.edge(gf[i][0], gf[i][1], color="red")
    g.render()


#mettre des couleurs dans la 7


#grosse erreur à corriger
import time
import math
import random


#pour les tests soit on fait des nv graphes qui appoprtent des trucs soit on fait de nv tests
#def algo_kruskal(g) :



def test_kruskal() :
    G=Graph([k for k in range (1,5)])
    for k in range(1,5) :
        G.add_edge(k, k+1, k)
    G.add_edge(5, 1, 5)
    print (G)
    return(G.kruskal())
def power_min_kruskal(g, src, dest) :
    #on suppose g est couvrant
    #renvoie puissance minimale et chemin associé
   
        marquage = [False for i in range(self.nb_nodes)]
        pred=[-1 for i in range(self.nb_nodes) ]
        def dfs_rec(s) :            
            marquage[s-1]=True
            for voisin in self.graph[s] :
                (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
                if not (marquage[i-1]) :
                    marquage[i-1]=True
                    pred[i-1]=s
                    dfs_rec(i)
        dfs_rec(src)
        if marquage[dest-1]==False :
            return None
        chemin = [dest]
        power_min=0
        p=dest
        while p != src :
            p_old=p
            p=pred[p-1]
            chemin.append(p)
            bool=False
            i=0
            while not bool :
                (n1,n2,power,d)=g.graph[p_old][i]
                if n1==p :
                    bool=True
            power_min=max(power_min, power)
        n=len(chemin)
        for i in range(n//2) :
            
            chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]
        return (chemin, power_min)
                       
    

def temps_exec(G1, trajet, n=15) :
    G=graph_from_file(G1)
    
    trajets=open(trajet)
    line=trajets.readline().split()
    nb=int(line[0])
    moy=0
    i = 0
    trajets.close()

    while i < n :
        trajets=open(trajet)

        traj=random.randint(1,nb)
        for k in range(0, traj-1) :
            trajets.readline()
        
        line=trajets.readline().split()
                   
        (src, dest)=(int(line[0]), int(line[1]))        
        t0=time.perf_counter()
        G.min_power(src, dest)
        t=time.perf_counter()-t0
        moy+=t
        i+=1
        trajets.close()  
    print((moy/n)*float(nb)) 
    return((moy/n)*float(nb))

def temps_exec_kruskal(G1, trajet, n=15) :
    g=graph_from_file(G1)
    G=g.kruskal()
    trajets=open(trajet)
    line=trajets.readline().split()
    nb=int(line[0])
    moy=0
    i = 0
    trajets.close()
    while i < n :
        trajets=open(trajet)

        traj=random.randint(1,nb)
        for k in range(0, traj-1) :
            trajets.readline()
        
        line=trajets.readline().split()
                   
        (src, dest)=(int(line[0]), int(line[1]))        
        t0=time.perf_counter()
        power_min_kruskal(G,src, dest)
        t=time.perf_counter()-t0
        moy+=t
        i+=1
        trajets.close()  
    print((moy/n)*float(nb)) 
    return((moy/n)*float(nb))

