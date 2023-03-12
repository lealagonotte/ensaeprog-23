
from graph import Graph, graph_from_file,  test_kruskal, temps_exec, temps_exec_kruskal,power_min_kruskal


data_path = "input/"
file_name = "network.01.in"

#g = graph_from_file(data_path + file_name)
#print(g)
import time
import random
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
    
def temps_exec_verif_1(G1, trajet, n=15) :
    G=graph_from_file(G1)
    trajets=open(trajet)
    line=trajets.readline().split()
    nb=int(line[0])
    t0=time.perf_counter()
    for i in range(0, nb) :         
        line=trajets.readline().split()                   
        (src, dest)=(int(line[0]), int(line[1]))        
        G.min_power(src, dest)
    t=time.perf_counter()-t0
       
    trajets.close()  
    print(t)  

#temps_exec("input/network.2.in", "input/routes.2.in")
#G="input/network.00.in"
#represente(G, 1, 2)

temps_exec_kruskal("input/network.2.in", "input/routes.2.in")




#question 2 : wikipedia le truc avec les dessins , pas cycle si pas dans les composantes_connexes

def test(trajet="input/routes.1.in", n=140) :
    
    trajets=open(trajet)
    line=trajets.readline().split()
    
    nb=int(line[0])
    i = 0
    
    traj=random.randint(1,nb)
    for k in range(1, traj-1) :
        trajets.readline()
    line=trajets.readline().split()
    print(nb,traj,line)
    trajets.close()

    return None
#test()
#print(test_kruskal())


