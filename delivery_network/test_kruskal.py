"""teste la fonction kruskal"""
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        G=Graph([k for k in range (1,5)]) 
        test=Graph([k for k in range (1,5)])
        for k in range(1,5) :
            G.add_edge(k, k+1, k)
            test.add_edge(k,k+1,k)
        G.add_edge(5, 1, 5)
        kruskal=G.kruskal()        
        self.assertEqual(kruskal.graph, test.graph)


    def test_network1(self):
        G=graph_from_file("input/network.00.in")
        k=G.kruskal()
        self.assertEqual(k.nb_nodes-1, k.nb_edges)
        self.assertEqual(len(k.connected_components()),1) #le graphe est connexe et E=V-1
    
    def test_network2(self):
        G=graph_from_file("input/network.03.in")
        k=G.kruskal()
        prev=Graph(k.nodes) #on le calcule à la main
        prev.add_edge(2, 3, 4)
        prev.add_edge(3, 4, 4)
        prev.add_edge(2, 1, 10)
        self.assertEqual(prev.graph, k.graph)



    

if __name__ == '__main__':
    unittest.main()
