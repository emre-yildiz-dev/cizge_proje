import unittest
from graph import Graph, GraphInputType, Vertex
from graph_generators import (
    create_complete_graph,
    create_cycle_graph,
    create_wheel_graph,
    create_hypercube_graph,
    create_random_graph
)

class TestGraphCreation(unittest.TestCase):
    def test_complete_graph(self):
        g = create_complete_graph(4)
        self.assertEqual(len(g.vertices), 4)
        for v in g.vertices.values():
            self.assertEqual(len(v.neighbors), 3)
        is_complete, _, _, _ = g.determine_graph_type()
        self.assertTrue(is_complete)
    
    def test_cycle_graph(self):
        g = create_cycle_graph(5)
        self.assertEqual(len(g.vertices), 5)
        for v in g.vertices.values():
            self.assertEqual(len(v.neighbors), 2)
        _, is_cycle, _, _ = g.determine_graph_type()
        self.assertTrue(is_cycle)
    
    def test_wheel_graph(self):
        g = create_wheel_graph(5)  # 4 outer vertices + 1 center
        self.assertEqual(len(g.vertices), 5)
        # Check center vertex has degree n-1
        center = chr(ord('a') + 4)  # Last vertex is center
        self.assertEqual(len(g.vertices[center].neighbors), 4)
        _, _, is_wheel, _ = g.determine_graph_type()
        self.assertTrue(is_wheel)
    
    def test_hypercube_graph(self):
        g = create_hypercube_graph(3)  # 3-cube (8 vertices)
        self.assertEqual(len(g.vertices), 8)
        for v in g.vertices.values():
            self.assertEqual(len(v.neighbors), 3)
        _, _, _, is_hypercube = g.determine_graph_type()
        self.assertTrue(is_hypercube)
    
    def test_random_graph(self):
        g = create_random_graph(5, 6)
        self.assertEqual(len(g.vertices), 5)
        total_edges = sum(len(v.neighbors) for v in g.vertices.values()) // 2
        self.assertEqual(total_edges, 6)

class TestGraphProperties(unittest.TestCase):
    def setUp(self):
        self.g = Graph()
        # Create a simple graph
        #   a -- b -- c
        #   |         |
        #   d         e
        #   |
        #   f    g
        vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        edges = [('a','b'), ('b','c'), ('a','d'), ('c','e'), ('d','f')]
        
        for v in vertices:
            self.g.vertices[v] = Vertex(v)
        for v1, v2 in edges:
            self.g.vertices[v1].neighbors.add(v2)
            self.g.vertices[v2].neighbors.add(v1)
    
    def test_isolated_vertices(self):
        isolated = self.g.get_isolated_vertices()
        self.assertEqual(isolated, {'g'})
    
    def test_pendant_vertices(self):
        pendant = self.g.get_pendant_vertices()
        self.assertEqual(pendant, {'e', 'f'})
    
    def test_connected_components(self):
        is_connected, components = self.g.is_connected()
        self.assertFalse(is_connected)
        self.assertEqual(len(components), 2)  # Main component and isolated vertex 'g'
    
    def test_bipartite(self):
        is_bip, sets = self.g.is_bipartite()
        self.assertTrue(is_bip)
        set1, set2 = sets
        # Check no edges within same set
        for v1 in set1:
            for v2 in self.g.vertices[v1].neighbors:
                self.assertIn(v2, set2)

def create_test_files():
    """Create test input files"""
    # Matrix format
    matrix_content = """Matrix
M a b c d
a 0 1 0 1
b 1 0 1 1
c 0 1 0 0
d 1 1 0 0"""
    
    with open("test_matrix.txt", "w") as f:
        f.write(matrix_content)
    
    # List format
    list_content = """List
a b d
b a c d
c b
d a b"""
    
    with open("test_list.txt", "w") as f:
        f.write(list_content)

if __name__ == '__main__':
    create_test_files()
    unittest.main() 