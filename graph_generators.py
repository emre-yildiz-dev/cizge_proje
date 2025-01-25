from typing import List
from itertools import combinations
from graph import Graph, Vertex

def create_complete_graph(n: int) -> Graph:
    """Create a complete graph Kn"""
    graph = Graph()
    
    # Create vertices
    vertices = [chr(ord('a') + i) for i in range(n)]
    for v in vertices:
        graph.vertices[v] = Vertex(v)
        
    # Add edges between all pairs of vertices
    for v1, v2 in combinations(vertices, 2):
        graph.vertices[v1].neighbors.add(v2)
        graph.vertices[v2].neighbors.add(v1)
        
    return graph

def create_cycle_graph(n: int) -> Graph:
    """Create a cycle graph Cn"""
    graph = Graph()
    
    # Create vertices
    vertices = [chr(ord('a') + i) for i in range(n)]
    for v in vertices:
        graph.vertices[v] = Vertex(v)
        
    # Add edges to form a cycle
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        graph.vertices[v1].neighbors.add(v2)
        graph.vertices[v2].neighbors.add(v1)
        
    return graph

def create_wheel_graph(n: int) -> Graph:
    """Create a wheel graph Wn"""
    # First create a cycle graph with n-1 vertices
    graph = create_cycle_graph(n - 1)
    
    # Add center vertex
    center = chr(ord('a') + n - 1)
    graph.vertices[center] = Vertex(center)
    
    # Connect center to all other vertices
    for v in graph.vertices:
        if v != center:
            graph.vertices[v].neighbors.add(center)
            graph.vertices[center].neighbors.add(v)
            
    return graph

def create_hypercube_graph(n: int) -> Graph:
    """Create an n-cube graph Qn"""
    graph = Graph()
    
    # Generate binary strings of length n
    def generate_binary_strings(length: int) -> List[str]:
        if length == 0:
            return ['']
        smaller = generate_binary_strings(length - 1)
        return [s + '0' for s in smaller] + [s + '1' for s in smaller]
    
    # Create vertices (using binary strings as labels)
    vertices = generate_binary_strings(n)
    for v in vertices:
        graph.vertices[v] = Vertex(v)
    
    # Add edges between vertices that differ in exactly one bit
    for v1 in vertices:
        for v2 in vertices:
            if sum(c1 != c2 for c1, c2 in zip(v1, v2)) == 1:
                graph.vertices[v1].neighbors.add(v2)
                graph.vertices[v2].neighbors.add(v1)
                
    return graph

def create_random_graph(num_vertices: int, num_edges: int) -> Graph:
    """Create a random graph with given number of vertices and edges"""
    if num_vertices < 1:
        raise ValueError("Number of vertices must be positive")
        
    max_edges = (num_vertices * (num_vertices - 1)) // 2
    if num_edges > max_edges:
        raise ValueError(f"Too many edges. Maximum possible edges for {num_vertices} vertices is {max_edges}")
    
    graph = Graph()
    
    # Create vertices
    vertices = [chr(ord('a') + i) for i in range(num_vertices)]
    for v in vertices:
        graph.vertices[v] = Vertex(v)
    
    # Add random edges
    possible_edges = list(combinations(vertices, 2))
    import random
    selected_edges = random.sample(possible_edges, num_edges)
    
    for v1, v2 in selected_edges:
        graph.vertices[v1].neighbors.add(v2)
        graph.vertices[v2].neighbors.add(v1)
        
    return graph 