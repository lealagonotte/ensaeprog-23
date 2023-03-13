"""teste la fonction kruskal"""
import sys 
sys.path.append("delivery_network")

from graph import Graph
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

    

if __name__ == '__main__':
    unittest.main()
