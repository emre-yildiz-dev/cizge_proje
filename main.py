from graph import Graph, GraphInputType
from graph_io import read_graph_from_file, write_graph_to_file
from graph_generators import (
    create_complete_graph,
    create_cycle_graph,
    create_wheel_graph,
    create_hypercube_graph,
    create_random_graph
)

def print_graph_info(graph: Graph, name: str = "Graph"):
    """Print detailed information about a graph"""
    print(f"\n=== {name} Information ===")
    print(f"Number of vertices: {len(graph.vertices)}")
    print(f"Isolated vertices: {graph.get_isolated_vertices()}")
    print(f"Pendant vertices: {graph.get_pendant_vertices()}")
    
    is_complete, is_cycle, is_wheel, is_hypercube = graph.determine_graph_type()
    print("\nGraph type:")
    if is_complete:
        print("- Complete graph")
    if is_cycle:
        print("- Cycle graph")
    if is_wheel:
        print("- Wheel graph")
    if is_hypercube:
        print("- Hypercube graph")
    if not any([is_complete, is_cycle, is_wheel, is_hypercube]):
        print("- None of the special types")
    
    is_bip, sets = graph.is_bipartite()
    if is_bip:
        set1, set2 = sets
        print("\nBipartite graph:")
        print(f"Set 1: {set1}")
        print(f"Set 2: {set2}")
        
        is_complete_bip, _ = graph.is_complete_bipartite()
        if is_complete_bip:
            print("(Complete bipartite)")
    else:
        print("\nNot a bipartite graph")
    
    is_conn, components = graph.is_connected()
    if is_conn:
        print("\nGraph is connected")
    else:
        print("\nGraph is not connected")
        print(f"Connected components: {components}")

def main():
    # Example 1: Read from file
    print("\n=== Example 1: Reading from file ===")
    print("Create a file named 'input_matrix.txt' with the following content:")
    print("""Matrix
M a b c d
a 0 1 0 1
b 1 0 1 1
c 0 1 0 0
d 1 1 0 0""")
    
    try:
        graph = read_graph_from_file("input_matrix.txt")
        print_graph_info(graph, "File Input Graph")
        
        # Save in both formats
        write_graph_to_file(graph, "output_matrix.txt", GraphInputType.MATRIX)
        write_graph_to_file(graph, "output_list.txt", GraphInputType.LIST)
        print("\nGraph has been saved in both matrix and list formats")
    except FileNotFoundError:
        print("Please create the input file first")
    
    # Example 2: Generate special graphs
    print("\n=== Example 2: Special Graphs ===")
    
    # Complete graph K5
    k5 = create_complete_graph(5)
    print_graph_info(k5, "K5 (Complete Graph)")
    
    # Cycle graph C6
    c6 = create_cycle_graph(6)
    print_graph_info(c6, "C6 (Cycle Graph)")
    
    # Wheel graph W7
    w7 = create_wheel_graph(7)
    print_graph_info(w7, "W7 (Wheel Graph)")
    
    # Hypercube Q3
    q3 = create_hypercube_graph(3)
    print_graph_info(q3, "Q3 (3-Cube Graph)")
    
    # Example 3: Random graph
    print("\n=== Example 3: Random Graph ===")
    random_graph = create_random_graph(6, 8)
    print_graph_info(random_graph, "Random Graph")

if __name__ == "__main__":
    main() 