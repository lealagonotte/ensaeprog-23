
from graph import Graph, graph_from_file, temps_calcul_naif, test_kruskal, temps_calcul_kruskal, power_min_kruskal, calcul_trajets_total

##test de la question 7##

#G="input/network.00.in"
#represente(G, 1, 2)




##Question 1 du tp2##
#print(temps_calcul_naif("input/network.1.in", "input/routes.1.in"))
#print(temps_calcul_naif("input/network.2.in", "input/routes.2.in"))
#en faisant le test plusieurs fois, sur route.1.in et le graphe 1, on observe que le temps est très court (0.02 secondes)
#Si on prend la route 2 et le graphe 2, on voit que le temps nécessaire est entre 30h et 50h. C'est beaucoup trop long!!


##test question4 du tp2
print(test_kruskal())



##question 5 du tp2##
#print(temps_calcul_kruskal("input/network.1.in", "input/routes.1.in"))
print(temps_calcul_kruskal("input/network.2.in", "input/routes.2.in"))
#print(temps_calcul_kruskal("input/network.3.in", "input/routes.3.in"))
#print(temps_calcul_kruskal("input/network.4.in", "input/routes.4.in"))
#print(temps_calcul_kruskal("input/network.5.in", "input/routes.5.in"))
#print(temps_calcul_kruskal("input/network.6.in", "input/routes.6.in"))
#print(temps_calcul_kruskal("input/network.7.in", "input/routes.7.in"))
#print(temps_calcul_kruskal("input/network.8.in", "input/routes.8.in"))
#print(temps_calcul_kruskal("input/network.9.in", "input/routes.9.in"))
#on trouve des temps beaucoup plus courts. Par exemple pour le premier, on trouve 0.002 sec
#pour le second, on trouve environ 3h
#pour le troisième, on trouve environ 20h
#pour le 5eme, 7h
#pour le dernier, on trouve environ 30h
#on trouve donc des temps bien plus courts!!

#print(calcul_trajets_total("input/network.2.in", "input/routes.2.in"))





