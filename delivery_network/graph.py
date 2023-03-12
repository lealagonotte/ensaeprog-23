
#cette classe UnionFind nous sera utile dans le td2, pour la question 3
#elle sert à manipuler les composantes connexes efficacement et facilement
class UnionFind(object):
    '''UnionFind Python class.'''
    def __init__(self, n):
        assert n > 0, "n doit être strictement positif"
        self.n = n
        # cahque sommet est son propre parent au début
        self.parent = [i for i in range(n)]
    
    def find(self, i):
        '''Find the parent of an element (e.g. the group it belongs to) and compress paths along the way.'''
        if self.parent[i] != i:
            # path compression on the way to finding the final parent 
            # (i.e. the element with a self loop)
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
     
    def is_connected(self, x, y):
        '''Check whether X and Y are connected, i.e. they have the same parent.'''
        if self.find(x) == self.find(y):
            return True
        else:
            return False
    
    def union(self, x, y):
        '''Unite the two elements by uniting their parents.'''
        xparent = self.find(x)
        yparent = self.find(y)
        if xparent != yparent:
            # if these elements are not yet in the same set,
            # we will set the y parent to the x parent
            self.parent[yparent]= xparent





import queue
import time
import math
import random
import graphviz
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

        self.nodes = nodes   #liste des sommets du graphe
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
        #si node1 ou node2 n'est pas dans la liste des sommets, on le rajoute. On met à jour la variable self.nb_nodes
        if node1 not in self.graph :
            self.graph[node1]=[]
            self.nb_nodes +=1
            self.nodes.append(node1)
        if  node2 not in self.graph :
            self.graph[node2]=[]
            self.nb_nodes +=1
            self.nodes.append(node2)      
#On rajoute la nouvelle arrête du graphe en ajoutant le triplet à la liste associée à le sommet node1 puis à le sommet node2
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
        comp_connexe = [] 
        marquage = [False for i in range(0,self.nb_nodes)]  # on procède comme au-dessus       

        def dfs_rec(s):
            comp = [s]  #comp sera la liste représentant la classe dont un représentant est s
            marquage[s-1] = True
            for i in self.graph[s]:  # i est tuple (node2, power, dist)
                i = i[0]  #on veut la deuxième extrémité de l'arrête : elle est dans la composante connexe de s
                if not(marquage[i-1]):
                    marquage[i-1] = True
                    comp += dfs_rec(i)  #on récure pour ajouter tous les sommets tels qu'il existe un chemin entre s et ce sommet
            return comp    #on renvoie la composante connexe représentée par s          
# on veut toutes les composantes connexes donc on a fini quand on a parcouru tout le graphe ie tous les sommets sont marqués
        for noeud in self.nodes :
            if marquage[noeud-1]==False :
                comp_connexe.append(dfs_rec(noeud))
        return comp_connexe    
#Concernant la complexité, au pire on fait nb_sommets parcours en profondeur. Or on a analysé la complexité du parcours ne profondeur au-dessus
#Ainsi, la complexité au pire est O(V(V+E))

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})        """

        return set(map(frozenset, self.connected_components()))
    

    def min_power(self, src, dest):
        """
        Résulat : Renvoie la puissance minimale d'un camion pouvant couvrir le trajet (src, dest)
        Paramètres :
        Src : sommet duquel on part
        Dest : sommet auquel on veut arriver        """
       # on commence par regarder si un chemin existe. 
       # Pour cela, on regarde si get_path_wit_power renvoie un chemin quand power = +inf.
        power=float("inf")
        # Si elle n'en renvoie pas, alors il n'existe de chemin entre src et dest et donc on ne peut pas trouver de puissance minimale
        if self.get_path_with_power(src, dest, power) == None :
            return None 
        else :
            # Sinon, il existe un chemin et une puissance minimale
            # on cherche alors une puissance et donc un entier n tel que 2**n convienne 
            # on sait alors que la puissance minimale sera entre 2**n-1 et 2**n
            n=0
            while self.get_path_with_power(src, dest, 2**n) == None : #la puissance est trop faible, donc on l'augmente
                n+=1
            # On fait une recherche dichotomique entre 2**(n-1) et 2**n
            a=2**(n-1)
            b=2**n
            while b-a>1 : #a et b sont des entiers
                m=(a+b)//2
                if self.get_path_with_power(src, dest, m) == None : #si il n'y a pas de chemin pour powe=m, on cherche entre m et b
                    a=m
                else : #Sinon entre a et m
                    b=m
        # à la fin de la boucle, on a ou bien b=a+1 donc power =b ou bien a=b donc power=b
        return (self.get_path_with_power(src, dest, b),b) #On renvoie la puissance minimale et le chemin associé à cette puissance
#Complexité : Pour trouver un n tel que 2**n soit une puissance possible, on a une complexité logarithmique en power_min 
# en effet : k=2**n equivaut à n=log_2(k)
#Ensuite, la recherche dichotomique a une complexité en O(log(2**(n-1))=O(n-1)=O(log(k)). 
#En effet, d=2**n-2**(n-1)=2**(n-1). On divise par 2 la longueur de l'intervalle à chaque tour et 2**(n-1)/2**l=1 équivaut à l*log(2)=(n-1)log(2)
#donc l=n-1=O(log(k))
#Conclusion : la complexité est logarithmique en la puissance minimale

##Question 5##
    def plus_court_chemin(self, src, dest, power) :
    #on va utiliser une file de priorité pour sortir d'abord les éléments avec une distance plus petite
    # on utilise l'algorithme de Dijkstra, qui se rapproche d'un parcours en largeur
            f=queue.PriorityQueue()
            dist=[-1 for i in range(self.nb_nodes)] #tableau pour stocker les distances
            marquage = [False for i in range(self.nb_nodes)] #tableau de marquage
            pred=[-1 for i in range(self.nb_nodes)] #tableau des prédecesseurs
            #initialisation
            dist[src-1]=0
            marquage[src-1]=True  
            f.put(src, 0)
        #on continue tant que la file n'est pas vide
            while not f.empty() : 
                u=f.get() #on sort l'élément avec la plus grande priorité
                marquage[u-1]=True
                for voisin in self.graph[u] :
                    (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
                    if not (marquage[i-1]) and j<=power and (dist[i-1]==-1 or dist[i-1]>d+k): #on modifie si la distance est plus petite qu'avant
                        marquage[i-1]=True
                        pred[i-1]=u
                        dist[i-1]=dist[u-1]+k
                        f.put(i, dist[u-1]+k)               
        #comme dans la question 3, on reconstruit un chemin
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
##Question 2 du td 2##

    

    def kruskal(self) :
        """Renvoie un arbre couvrant de poids minimal de self"""
        #on utilise la class unionfind qui se trouve au début de la page
        uf=UnionFind(self.nb_nodes) #créationd'une structure Union Find
        dico=self.graph             
        Gf=Graph([k for k in range(1,self.nb_nodes)]) #on crée notre nouveau graphe
        liste_arrete=[] #on va stocker toutes les listes d'arrêtes dans un tableau
        for i in range (1,self.nb_nodes) :
            for d in dico[i] : #on parcourt chaque liste associée au sommet i
                (a,b,c)=d #a=node2, b=power, c=dist
                if i< a : #on ajoute les arrêtes seulement une fois dans liste_arrete
                    liste_arrete.append((i,a,b))
        
        liste_arrete=sorted(liste_arrete, key=lambda x : x[2]) #on trie la liste des arrêtes en fonction de leur power
        for arrete in liste_arrete :
            (i,a,b)=arrete
            #On ne crée pas de cycles en rajoutant l'arrete (s1,s2) lorsque les deux sommets s1 et s2 ne sont pas dans la même composante connexe
            #si ils sont dans la même composante connexe alors en rajoutant l'arrête, on crée un cycle car alors deux chemins joignent ces sommets
            if not uf.is_connected(i-1,a-1) : #si i et a ne sont pas dans les mêmes composantes connexes
                Gf.add_edge(i, a, b) #on rajoute l'arrête dans le nouveau graphe
                uf.union(i-1,a-1) # les deux sommets i et a sont maintenant dans la même composante connexe
        return Gf
    #complexité de Kruskal :
    #On fait une première boucle pour créer liste_arrete, la complexité est en O(nb_nodes)
    #Ensuite, on trie la liste, dans le meilleur des cas la complexité sera en O(nlog(n)) avec n le nombre d'arrete du graphe
    #Enfin, on fait une boucle. Il y a n tours. Chaque tour de boucle a une complexité constante car add_edge se fait en temps constant, de meme que union et is_connected avec la structure Union find
    #POur conclure, la complexité de la fonction est O(nb_nodes + nb_edges(log(nb_edges)))



##question 1##
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
    f=open(filename) #on ouvre le fichier qui s'appelle f
    ligne=f.readline().split() #on lit la première ligne, split permet d'avoir une liste de str
    #on sait que les éléments de la première ligne correspondent à nb_nodes et nb_edges
    nb_nodes=int(ligne[0]) 
    nb_edges=int(ligne[1])
    nodes=[i for i in range(1, nb_nodes +1)]
    G=Graph(nodes) #on crée le graphe associé
    #on va lire les lignes et ajouter les arrêtes au fur et à mesure
    for i in range(nb_edges) :
        line=f.readline().split() #on lit la ligne
        #on crée les arrêtes
        if len(line) == 4 :
            G.add_edge(int(line[0]), int(line[1]), int(line[2]), int(line[3]))
        else : 
            G.add_edge(int(line[0]), int(line[1]), int(line[2]), 1)
        #si il n'y a pas de 4ème élément dans la ligne, on met une distance égal à 1 par défaut
    f.close() #on ferme le fichier
    return G    

#version du corrigé

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

##Question 7##

def represente(G, src, dest, power=20) :
    """Résultat : Crée une image PNG qui est une représentation graphique du graphe de G, ainsi que du chemin associé trouvé"""
    graphe=graph_from_file(G) #on crée le graphe avec la class Graph associé à G
    g=graphviz.Graph(filename='G', format='png', directory="delivery_network", engine='dot') #on crée un graphe Graphviz
    chemin=graphe.get_path_with_power(src, dest, power ) #on trouve un chemin associé à la puissance power,
    #on aurait pu ne pas mettre power dans les variables et utiliser la fonction min_power
    gf=open(G, "r") 
    gf.readline() #on lit la première ligne car elle n'est pas utili
    gf=gf.readlines() #on lit toutes les lignes
    for i in range(0,len(gf)) :
         
        gf[i]=gf[i].split()
        if chemin != None and int(gf[i][0]) in chemin and int(gf[i][1]) in chemin :
            g.edge(gf[i][0], gf[i][1], color="green")
        else :
            g.edge(gf[i][0], gf[i][1])
    
    print(chemin)
    if chemin is not None : 
        for node in chemin : 
            g.node(str(node), color = 'blue')
    g.render()
                       
    
##question 1 du td2###
def temps_calcul_naif(G1, trajet, n=15) :
    """Renvoie le temps nécessaire pour calculer la puissance minimale sur l'ensemble des trajets.
    Pramamètres :
    -G1 : type str, nom du fichier du graphe
    -trajet : type str, nom du fichier où on pioche les trajets
    -n : indique le nombre de trajets où l'on fait réellement le calcul"""
    G=graph_from_file(G1)    #on convertit en Graph G1
    trajets=open(trajet) #on ouvre le fichier trajet
    line=trajets.readline().split() #on lit la première ligne
    nb=int(line[0]) #nb = nombre de trajets dans trajet
    #initialisation
    moy=0
    i = 0
    trajets.close() #on ferme pour recommencer au début
    while i < n : #on fait le calcul n fois
        trajets=open(trajet)
        traj=random.randint(1,nb) #on tire un nombre aléatoire pour savoir sur quel trajet on fait le calcul
        for k in range(0, traj-1) : #on avance dans le fichier jusqu'à être à la bonne ligne
            trajets.readline()        
        line=trajets.readline().split() #on stocke cette ligne                   
        (src, dest)=(int(line[0]), int(line[1]))        #on a ainsi src et dest
        t0=time.perf_counter() #on regarde le temps qu'il est
        G.min_power(src, dest) #on fait le calcul
        t=time.perf_counter()-t0 #on regarde le temps qu'on a mis
        moy+=t #on ajoute à moy ce temps pour trouver la moyenne des temps
        i+=1
        trajets.close()  #on ferme pour reprendre la lecture au début
    #print((moy/n)*float(nb)) 
    return((moy/n)*float(nb)) #on retourne le temps moyen*nb de trajet ce qui donne le temps total qu'on mettrait si on faisait le calcul pour tous les trajets


##Question 5 du td2##

def power_min_kruskal(g, src, dest) :
    """Renvoie  pour un trajet t=(src, dest) et g un arbre couvrant, la puissance minimale (et un chemin associé) d'un camion pouvant couvrir ce trajet"""
    # Prérequis : on suppose g est couvrant de poids minimal. 
    # Ainsi, si le chemin entre src et dest existe, il est unique
    #on fait un parcours comme on a déjà fait précedemment
    marquage = [False for i in range(g.nb_nodes)]
    pred=[-1 for i in range(g.nb_nodes)]
    def dfs_rec(s) :            
        marquage[s-1]=True
        for voisin in g.graph[s] :
            (i,j,k)=voisin #i : noeud voisin, j puissance minimale, k distance
            if not (marquage[i-1]) :
                marquage[i-1]=True
                pred[i-1]=(s,j) #on stocke des couples dans le tableau de prédecesseurs pour avoir accès à la puissance de l'arrête (s,i) plus simplement
                dfs_rec(i)
    dfs_rec(src)
    if marquage[dest-1]==False :
        return None
    chemin = [dest]
    #on va calculer la puissance minimale nécessaire.
    #Pour cela, on construit le chemin pour aller de src à dest et on regarde le power de chaque arrête
    #la puissance minimale vaut le max de ces puissances    
    p=dest
    power_min=0
    while p != src :
        (p, power)=pred[p-1] #on prend le couple
        chemin.append(p)        
        power_min=max(power_min, power) #on regarde si power > power_min, auquel cas il faut augmenter la puissance minimale pour passer
    n=len(chemin)
    for i in range(n//2) :            
        chemin[i],chemin[n-1-i]=chemin[n-1-i], chemin[i]
    return (chemin, power_min)

def temps_calcul_kruskal(G1, trajet, n=15) :
    """Renvoie le temps nécessaire pour calculer la puissance minimale sur l'ensemble des trajets en utilisant l'algorithme de Kruskal.
    Pramamètres :
    -G1 : type str, nom du fichier du graphe
    -trajet : type str, nom du fichier où on pioche les trajets
    -n : indique le nombre de trajets où l'on fait réellement le calcul"""
    #même principe que pour temps_calcul_naif sauf qu'on passe par l'arbre de Kruskal, pour les explications voir au-dessus
    g=graph_from_file(G1)
    G=g.kruskal() #on prend l'arbre de Kruskal
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
   
    return((moy/n)*float(nb))

#la complexité de kruskal est O(nb_nodes + nb_edges(log(nb_edges)))
#on a une boucle while qui fait n tours
#Chaque tour a une complexité en O(1)
#La complexité totale est donc O(nb_nodes + nb_edges(log(nb_edges))) car n <<nb_nodes et << nb_edges

##Tests##
#Ici, se trouvent tous les tests

def test_kruskal() :
    """Teste la fonction kruskal avec un graphe qui est un cycle. Le résultat obtenu doit être le même graphe sans la dernière arrête"""
    G=Graph([k for k in range (1,5)]) 
    for k in range(1,5) :
        G.add_edge(k, k+1, k)
    G.add_edge(5, 1, 5)
    
    return(G.kruskal())
#Le résultat obtenu est bien le graphe qu'on voulait avoir 