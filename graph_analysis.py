from typing import Set, List, Tuple, Optional
from collections import deque
from graph import Graph

def find_connected_components(graph: Graph) -> List[Set[str]]:
    """Find all connected components in the graph using BFS"""
    components = []
    unvisited = set(graph.vertices.keys())
    
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
                queue.extend(n for n in graph.vertices[vertex].neighbors if n in unvisited)
        
        components.append(component)
    
    return components

def is_bipartite(graph: Graph) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
    """Check if graph is bipartite and return the two vertex sets if true"""
    if not graph.vertices:
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
            
            for neighbor in graph.vertices[vertex].neighbors:
                queue.append((neighbor, next_color))
        
        return True
    
    # Try to color each component
    for vertex in graph.vertices:
        if vertex not in colors:
            if not try_color_component(vertex):
                return False, None
    
    # If we get here, the graph is bipartite
    set0 = {v for v, c in colors.items() if c == 0}
    set1 = {v for v, c in colors.items() if c == 1}
    return True, (set0, set1)

def is_complete_bipartite(graph: Graph) -> Tuple[bool, Optional[Tuple[Set[str], Set[str]]]]:
    """Check if graph is complete bipartite and return the two vertex sets if true"""
    # First check if it's bipartite
    is_bip, sets = is_bipartite(graph)
    if not is_bip or not sets:
        return False, None
    
    set1, set2 = sets
    
    # Check if every vertex in set1 is connected to all vertices in set2
    for v1 in set1:
        if len(graph.vertices[v1].neighbors) != len(set2):
            return False, None
        if not set2.issubset(graph.vertices[v1].neighbors):
            return False, None
    
    # Check if every vertex in set2 is connected to all vertices in set1
    for v2 in set2:
        if len(graph.vertices[v2].neighbors) != len(set1):
            return False, None
        if not set1.issubset(graph.vertices[v2].neighbors):
            return False, None
    
    return True, (set1, set2)

def determine_graph_type(graph: Graph) -> Tuple[bool, bool, bool, bool]:
    """Determine if graph is complete, cycle, wheel, or n-cube
    Returns tuple of (is_complete, is_cycle, is_wheel, is_hypercube)"""
    n = len(graph.vertices)
    if n == 0:
        return False, False, False, False
    
    # Check if complete
    is_complete = all(len(v.neighbors) == n-1 for v in graph.vertices.values())
    
    # Check if cycle
    is_cycle = (n >= 3 and 
                all(len(v.neighbors) == 2 for v in graph.vertices.values()) and
                len(find_connected_components(graph)) == 1)
    
    # Check if wheel
    if n >= 4:
        # Find potential center (vertex with degree n-1)
        center_candidates = [v for v, data in graph.vertices.items() 
                           if len(data.neighbors) == n-1]
        if len(center_candidates) == 1:
            center = center_candidates[0]
            # Remove center and check if remaining graph is a cycle
            remaining_vertices = set(graph.vertices.keys()) - {center}
            is_wheel = all(len(graph.vertices[v].neighbors - {center}) == 2 
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
        is_hypercube = all(len(v.neighbors) == degree for v in graph.vertices.values())
    else:
        is_hypercube = False
    
    return is_complete, is_cycle, is_wheel, is_hypercube 