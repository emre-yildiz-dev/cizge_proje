# Graph Theory Project

This project implements various graph theory concepts in Python, including graph creation, analysis, and manipulation.

## Project Structure

- `graph.py`: Core graph data structures and classes
- `graph_io.py`: File input/output operations
- `graph_generators.py`: Special graph generation functions
- `graph_analysis.py`: Graph analysis algorithms
- `main.py`: Main script to demonstrate functionality
- `test_graphs.py`: Unit tests

## Requirements

- Python 3.7 or higher
- No external dependencies required

## Running the Project

1. Clone the repository
2. Create an input graph file (example below)
3. Run the main script:

```bash
python main.py
```

The main script demonstrates:
- Reading graphs from files
- Creating special graphs (complete, cycle, wheel, hypercube)
- Analyzing graph properties
- Saving graphs in different formats

### Example Input File (Matrix Format)

Create a file named `input_matrix.txt` with the following content:

```
Matrix
M a b c d
a 0 1 0 1
b 1 0 1 1
c 0 1 0 0
d 1 1 0 0
```

### Example Input File (List Format)

Alternative format in `input_list.txt`:

```
List
a b d
b a c d
c b
d a b
```

## Running Tests

Run the unit tests with:

```bash
python test_graphs.py
```

The tests will:
1. Create test input files automatically
2. Test all graph creation functions
3. Test graph properties and algorithms
4. Verify file I/O operations

## Features

1. Graph Input/Output
   - Adjacency matrix format
   - Adjacency list format

2. Graph Generation
   - Complete graphs (Kn)
   - Cycle graphs (Cn)
   - Wheel graphs (Wn)
   - Hypercube graphs (Qn)
   - Random graphs

3. Graph Analysis
   - Isolated vertices
   - Pendant vertices
   - Graph type detection
   - Bipartite checking
   - Connected components

## Example Usage

```python
from graph import Graph
from graph_generators import create_complete_graph

# Create a complete graph with 5 vertices
g = create_complete_graph(5)

# Check if it's bipartite
is_bipartite, sets = g.is_bipartite()

# Find isolated vertices
isolated = g.get_isolated_vertices()

# Save to file
from graph_io import write_graph_to_file
write_graph_to_file(g, "output.txt", GraphInputType.MATRIX)
``` 