# Network Routing Simulator

## Overview
This program is a Network Routing Simulator that supports both Link State Routing and Distance Vector Routing algorithms. It provides a visual representation of network graphs and allows users to interactively simulate routing algorithms.

## Prerequisites
Before running the program, ensure that all Python dependencies are installed. This includes:

- Python 3.x
- NetworkX
- Matplotlib
- Tkinter

You can install these packages using pip


## How to Use
Follow these steps to use the program:

1. **Run the Program**: Start the program from your Python environment.
2. **Generate the Graph**: Click on the "Generate Graph" button. It's recommended to use fewer than 6 nodes for clearer output, though the program supports up to 20 nodes.
3. **Select the Algorithm**: Choose the routing algorithm (Link State or Distance Vector) using the radio buttons provided.
4. **Highlight Shortest Path**: Click on the "Highlight Shortest Path" button and select the source and destination nodes to visualize the shortest path on the graph.
5. **Run Simulation**: Click on the "Run Simulation" button to execute the selected routing algorithm. The output will be displayed in the terminal.

## Notes
- The simulation results, including path details and performance metrics, will be printed in the terminal.
- It will show both costs and path for each node in the forwarding tables
- It will also show the remaining parameters such as hop count and transmission delay line by line below the table
- Finally, it will show total time elapsed in ms in the last line.
- Ensure you highlight a path before running the simulation. Running the simulation without highlighting a path may lead to improper functioning and may require restarting the program.
- You can switch between Link State Routing and Distance Vector Routing by changing the selection in the radio buttons.
- Highlighting the shortest path may change the orientation of the graph for visual clarity, but the underlying graph structure remains unchanged.

## Troubleshooting
If the program does not respond or behaves unexpectedly:
- Ensure that all prerequisites are correctly installed.
- Try restarting the program and following the steps in the given order.
- Check for any error messages in the terminal, which can provide insights into any issues.

