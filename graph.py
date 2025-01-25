from dataclasses import dataclass
from typing import List, Dict, Set, Tuple, Optional
from enum import Enum

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
        graph = cls()
        # Implementation will be added
        return graph
    
    @classmethod
    def random_graph(cls, num_vertices: int, num_edges: int) -> 'Graph':
        """Create a random graph with given number of vertices and edges"""
        graph = cls()
        # Implementation will be added
        return graph
    
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
        if n < 1:
            raise ValueError("n must be >= 1")
        graph = cls()
        # Implementation will be added
        return graph
    
    @classmethod
    def create_cycle_graph(cls, n: int) -> 'Graph':
        """Create a cycle graph Cn"""
        if n < 3:
            raise ValueError("n must be >= 3")
        graph = cls()
        # Implementation will be added
        return graph
    
    @classmethod
    def create_wheel_graph(cls, n: int) -> 'Graph':
        """Create a wheel graph Wn"""
        if n < 3:
            raise ValueError("n must be >= 3")
        graph = cls()
        # Implementation will be added
        return graph
    
    @classmethod
    def create_hypercube_graph(cls, n: int) -> 'Graph':
        """Create an n-cube graph Qn"""
        if n < 1:
            raise ValueError("n must be >= 1")
        graph = cls()
        # Implementation will be added
        return graph
    
    def determine_graph_type(self) -> Tuple[bool, bool, bool, bool]:
        """Determine if graph is complete, cycle, wheel, or n-cube
        Returns tuple of (is_complete, is_cycle, is_wheel, is_hypercube)"""
        # Implementation will be added
        return (False, False, False, False)
    
    def is_bipartite(self) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
        """Check if graph is bipartite and return the two vertex sets if true"""
        # Implementation will be added
        return (False, None)
    
    def is_complete_bipartite(self) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
        """Check if graph is complete bipartite and return the two vertex sets if true"""
        # Implementation will be added
        return (False, None)
    
    def is_connected(self) -> Tuple[bool, Optional[List[Set[str]]]]:
        """Check if graph is connected and return connected components if not"""
        # Implementation will be added
        return (False, None)

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