from typing import List, Dict, Set, Tuple
from graph import Graph, GraphInputType, Vertex

def read_graph_from_file(filename: str) -> Graph:
    """Read graph from a file in either Matrix or List format"""
    graph = Graph()
    
    with open(filename, 'r') as f:
        # Read input type
        input_type = f.readline().strip()
        graph.input_type = GraphInputType(input_type)
        
        if graph.input_type == GraphInputType.MATRIX:
            # Read vertex labels
            labels = f.readline().strip().split()
            if labels[0] == 'M':  # Skip the M character
                labels = labels[1:]
            
            # Create vertices
            for label in labels:
                graph.vertices[label] = Vertex(label)
            
            # Read adjacency matrix
            for i, line in enumerate(f):
                row = line.strip().split()
                current_vertex = labels[i]
                for j, value in enumerate(row[1:]):  # Skip the vertex label
                    if value == '1':
                        graph.vertices[current_vertex].neighbors.add(labels[j])
                        
        else:  # List format
            for line in f:
                vertices = line.strip().split()
                if not vertices:
                    continue
                    
                current_vertex = vertices[0]
                if current_vertex not in graph.vertices:
                    graph.vertices[current_vertex] = Vertex(current_vertex)
                
                # Add neighbors
                for neighbor in vertices[1:]:
                    if neighbor not in graph.vertices:
                        graph.vertices[neighbor] = Vertex(neighbor)
                    graph.vertices[current_vertex].neighbors.add(neighbor)
    
    return graph

def write_graph_to_file(graph: Graph, filename: str, output_type: GraphInputType) -> None:
    """Write graph to a file in either Matrix or List format"""
    with open(filename, 'w') as f:
        f.write(output_type.value + '\n')
        
        if output_type == GraphInputType.MATRIX:
            # Write vertex labels
            vertices = sorted(graph.vertices.keys())
            f.write('M ' + ' '.join(vertices) + '\n')
            
            # Write matrix
            for v1 in vertices:
                row = [v1]  # Start with vertex label
                for v2 in vertices:
                    row.append('1' if v2 in graph.vertices[v1].neighbors else '0')
                f.write('\t'.join(row) + '\n')
                
        else:  # List format
            # Write adjacency list
            for vertex in sorted(graph.vertices.keys()):
                neighbors = sorted(graph.vertices[vertex].neighbors)
                if neighbors:
                    f.write(f"{vertex}\t{' '.join(neighbors)}\n")
                else:
                    f.write(f"{vertex}\n") 