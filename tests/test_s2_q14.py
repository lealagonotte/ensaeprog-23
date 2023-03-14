# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import graph_from_file, power_min_kruskal, dfs_initial
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in").kruskal()
        self.assertEqual(power_min_kruskal(g, 1, 4, dfs_initial(g))[1], 11)
        self.assertEqual(power_min_kruskal(g, 2, 4, dfs_initial(g))[1], 10)

    def test_network1(self):

        g = graph_from_file("input/network.04.in").kruskal()
        self.assertEqual(power_min_kruskal(g, 1, 4, dfs_initial(g))[1], 4)

if __name__ == '__main__':
    unittest.main()
