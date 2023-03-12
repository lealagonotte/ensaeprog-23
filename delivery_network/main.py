
from graph import Graph, graph_from_file, temps_calcul_naif, test_kruskal, temps_exec_kruskal, power_min_kruskal

##test de la question 7##

#G="input/network.00.in"
#represente(G, 1, 2)




##Question 1 du tp2##
#print(temps_calcul_naif("input/network.1.in", "input/routes.1.in"))
#print(temps_calcul_naif("input/network.2.in", "input/routes.2.in"))
#en faisant le test plusieurs fois, sur route.1.in et le graphe 1, on observe que le temps est très court (moins de 1 seconde)
#Si on prend la route 2 et le graphe 2, on voit que le temps nécessaire est entre 30h et 50h. C'est beaucoup trop long!!






temps_exec_kruskal("input/network.1.in", "input/routes.1.in")




#question 2 : wikipedia le truc avec les dessins , pas cycle si pas dans les composantes_connexes


#test()
#print(test_kruskal())


