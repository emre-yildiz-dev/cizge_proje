from dataclasses import dataclass
from typing import List, Dict, Set, Tuple, Optional
from enum import Enum
from collections import deque

class GraphInputType(Enum):
    MATRIX = "Matrix"
    LIST = "List"

@dataclass
class Vertex:
    """Represents a vertex in the graph"""
    label: str
    neighbors: Set[str] = None
    
    def __post_init__(self):
        if self.neighbors is None:
            self.neighbors = set()

@dataclass
class Graph:
    """Main graph class that handles all operations"""
    vertices: Dict[str, Vertex]
    input_type: GraphInputType
    
    def __init__(self):
        self.vertices = {}
        self.input_type = None
    
    @classmethod
    def from_file(cls, filename: str) -> 'Graph':
        """Create a graph from a file input"""
        from graph_io import read_graph_from_file
        return read_graph_from_file(filename)
    
    @classmethod
    def random_graph(cls, num_vertices: int, num_edges: int) -> 'Graph':
        """Create a random graph with given number of vertices and edges"""
        from graph_generators import create_random_graph
        return create_random_graph(num_vertices, num_edges)
    
    def to_adjacency_matrix(self) -> List[List[int]]:
        """Convert graph to adjacency matrix representation"""
        vertices_list = sorted(self.vertices.keys())
        size = len(vertices_list)
        matrix = [[0] * size for _ in range(size)]
        
        for i, v1 in enumerate(vertices_list):
            for j, v2 in enumerate(vertices_list):
                if v2 in self.vertices[v1].neighbors:
                    matrix[i][j] = 1
        
        return matrix
    
    def to_adjacency_list(self) -> Dict[str, Set[str]]:
        """Convert graph to adjacency list representation"""
        return {v: self.vertices[v].neighbors for v in self.vertices}
    
    def get_isolated_vertices(self) -> Set[str]:
        """Return set of isolated vertices"""
        return {v for v, vertex in self.vertices.items() if not vertex.neighbors}
    
    def get_pendant_vertices(self) -> Set[str]:
        """Return set of pendant vertices (vertices with degree 1)"""
        return {v for v, vertex in self.vertices.items() if len(vertex.neighbors) == 1}
    
    @classmethod
    def create_complete_graph(cls, n: int) -> 'Graph':
        """Create a complete graph Kn"""
        from graph_generators import create_complete_graph
        return create_complete_graph(n)
    
    @classmethod
    def create_cycle_graph(cls, n: int) -> 'Graph':
        """Create a cycle graph Cn"""
        from graph_generators import create_cycle_graph
        return create_cycle_graph(n)
    
    @classmethod
    def create_wheel_graph(cls, n: int) -> 'Graph':
        """Create a wheel graph Wn"""
        from graph_generators import create_wheel_graph
        return create_wheel_graph(n)
    
    @classmethod
    def create_hypercube_graph(cls, n: int) -> 'Graph':
        """Create an n-cube graph Qn"""
        from graph_generators import create_hypercube_graph
        return create_hypercube_graph(n)
    
    def determine_graph_type(self) -> Tuple[bool, bool, bool, bool]:
        """Determine if graph is complete, cycle, wheel, or n-cube
        Returns tuple of (is_complete, is_cycle, is_wheel, is_hypercube)"""
        n = len(self.vertices)
        if n == 0:
            return False, False, False, False
        
        # Check if complete
        is_complete = all(len(v.neighbors) == n-1 for v in self.vertices.values())
        
        # Check if cycle
        is_cycle = (n >= 3 and 
                   all(len(v.neighbors) == 2 for v in self.vertices.values()) and
                   len(self._find_connected_components()) == 1)
        
        # Check if wheel
        if n >= 4:
            # Find potential center (vertex with degree n-1)
            center_candidates = [v for v, data in self.vertices.items() 
                              if len(data.neighbors) == n-1]
            if len(center_candidates) == 1:
                center = center_candidates[0]
                # Remove center and check if remaining graph is a cycle
                remaining_vertices = set(self.vertices.keys()) - {center}
                is_wheel = all(len(self.vertices[v].neighbors - {center}) == 2 
                             for v in remaining_vertices)
            else:
                is_wheel = False
        else:
            is_wheel = False
        
        # Check if hypercube
        # All vertices must have same degree, which must be log2(n)
        from math import log2
        if n > 0 and n & (n-1) == 0:  # n is power of 2
            degree = int(log2(n))
            is_hypercube = all(len(v.neighbors) == degree for v in self.vertices.values())
        else:
            is_hypercube = False
        
        return is_complete, is_cycle, is_wheel, is_hypercube
    
    def _find_connected_components(self) -> List[Set[str]]:
        """Find all connected components in the graph using BFS"""
        components = []
        unvisited = set(self.vertices.keys())
        
        while unvisited:
            # Start a new component
            start = next(iter(unvisited))
            component = set()
            queue = deque([start])
            
            # BFS
            while queue:
                vertex = queue.popleft()
                if vertex in unvisited:
                    component.add(vertex)
                    unvisited.remove(vertex)
                    queue.extend(n for n in self.vertices[vertex].neighbors if n in unvisited)
            
            components.append(component)
        
        return components
    
    def is_bipartite(self) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
        """Check if graph is bipartite and return the two vertex sets if true"""
        if not self.vertices:
            return True, (set(), set())
        
        colors = {}  # vertex -> color (0 or 1)
        
        def try_color_component(start: str) -> bool:
            queue = deque([(start, 0)])
            
            while queue:
                vertex, color = queue.popleft()
                
                if vertex in colors:
                    if colors[vertex] != color:
                        return False
                    continue
                    
                colors[vertex] = color
                next_color = 1 - color
                
                for neighbor in self.vertices[vertex].neighbors:
                    queue.append((neighbor, next_color))
            
            return True
        
        # Try to color each component
        for vertex in self.vertices:
            if vertex not in colors:
                if not try_color_component(vertex):
                    return False, None
        
        # If we get here, the graph is bipartite
        set0 = {v for v, c in colors.items() if c == 0}
        set1 = {v for v, c in colors.items() if c == 1}
        return True, (set0, set1)
    
    def is_complete_bipartite(self) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
        """Check if graph is complete bipartite and return the two vertex sets if true"""
        # First check if it's bipartite
        is_bip, sets = self.is_bipartite()
        if not is_bip or not sets:
            return False, None
        
        set1, set2 = sets
        
        # Check if every vertex in set1 is connected to all vertices in set2
        for v1 in set1:
            if len(self.vertices[v1].neighbors) != len(set2):
                return False, None
            if not set2.issubset(self.vertices[v1].neighbors):
                return False, None
        
        # Check if every vertex in set2 is connected to all vertices in set1
        for v2 in set2:
            if len(self.vertices[v2].neighbors) != len(set1):
                return False, None
            if not set1.issubset(self.vertices[v2].neighbors):
                return False, None
        
        return True, (set1, set2)
    
    def is_connected(self) -> Tuple[bool, Optional[List[Set[str]]]]:
        """Check if graph is connected and return connected components if not"""
        components = self._find_connected_components()
        return len(components) == 1, components if len(components) > 1 else None

@dataclass
class GraphStats:
    """Class to hold basic graph statistics"""
    num_vertices: int
    num_edges: int
    vertex_degrees: Dict[str, int]
    
    @classmethod
    def from_graph(cls, graph: Graph) -> 'GraphStats':
        num_vertices = len(graph.vertices)
        vertex_degrees = {v: len(vertex.neighbors) for v, vertex in graph.vertices.items()}
        num_edges = sum(vertex_degrees.values()) // 2
        return cls(num_vertices, num_edges, vertex_degrees) 