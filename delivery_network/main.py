
from graph import UnionFind
from graph import Graph, graph_from_file, temps_calcul_kruskal, power_min_kruskal, represente, dfs_initial, calcul_trajets_total, test_q4

### test q4
print(test_q4())

##test de la question 7##



"""G="input/network.00.in"
represente(G, 1, 2)
represente(G, 8, 6)

G1="input/network.01.in"
represente(G1, 1, 3) 
represente(G1, 7, 3) #renvoie bien none car 7 et 3 ne sont pas des composantes connectées """



"""
#TEST MÉTHODE FIND
uf = UnionFind(10)
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)
uf.union(6, 7)
uf.union(8, 9)

# Expecting 1
print(uf.find(0))
# Expecting 1
print(uf.find(1))
# Expecting 3
print(uf.find(2))
# Expecting 3
print(uf.find(3))
# Expecting 5
print(uf.find(4))
# Expecting 5
print(uf.find(5))
# Expecting 7
print(uf.find(6))
# Expecting 7
print(uf.find(7))
# Expecting 9
print(uf.find(8))
# Expecting 9
print(uf.find(9))


## FIN DU TEST DE LA MÉTHODE FIND 
"""




##Question 1 du tp2##
#print(temps_calcul_naif("input/network.1.in", "input/routes.1.in"))
#print(temps_calcul_naif("input/network.2.in", "input/routes.2.in"))
#en faisant le test plusieurs fois, sur route.1.in et le graphe 1, on observe que le temps est très court (0.02 secondes)
#Si on prend la route 2 et le graphe 2, on voit que le temps nécessaire est entre 30h et 40h. C'est beaucoup trop long!!


##test question4 du tp2
#print(test_kruskal())

#g=(graph_from_file("input/network.1.in").kruskal())
#print(dfs_initial(g))



g=(graph_from_file("input/network.1.in").kruskal())
print(power_min_kruskal(g, 11, 6, dfs_initial(g)))
##question 5 du tp2##
"""print(temps_calcul_kruskal("input/network.1.in", "input/routes.1.in"))
print(temps_calcul_kruskal("input/network.2.in", "input/routes.2.in"))
print(temps_calcul_kruskal("input/network.3.in", "input/routes.3.in"))
print(temps_calcul_kruskal("input/network.4.in", "input/routes.4.in"))
print(temps_calcul_kruskal("input/network.5.in", "input/routes.5.in"))
print(temps_calcul_kruskal("input/network.6.in", "input/routes.6.in"))
print(temps_calcul_kruskal("input/network.7.in", "input/routes.7.in"))
print(temps_calcul_kruskal("input/network.8.in", "input/routes.8.in"))
print(temps_calcul_kruskal("input/network.9.in", "input/routes.9.in"))
print(temps_calcul_kruskal("input/network.10.in", "input/routes.10.in"))"""

#on trouve des temps beaucoup plus courts. Par exemple pour le premier, on trouve 0.002 sec
#pour le second, on trouve environ 3h
#pour le troisième, on trouve environ 20h
#pour le 5eme, 7h
#pour le dernier, on trouve environ 30h
#on trouve donc des temps bien plus courts!!

#print(calcul_trajets_total("input/network.2.in", "input/routes.2.in"))


##Question 16
#for i in range (1,11) :
    #print(calcul_trajets_total(i))