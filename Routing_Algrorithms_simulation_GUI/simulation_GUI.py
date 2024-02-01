""" Author: MHD Kamal Rushdi
    Student ID: 150210907
    Date: 2023-01-08
    Description: This program is a network routing simulator that uses the Link State Routing and Distance Vector Routing algorithms
        to find the shortest path between two nodes in a network topology"""

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, simpledialog
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time
from tabulate import tabulate

class RoutingSimulator:
    def __init__(self, num_nodes):                      
        self.num_nodes = num_nodes
        self.graph = self.generate_random_topology()

    def generate_random_topology(self):
        connected = False                                   
        while not connected:                                
            G = nx.erdos_renyi_graph(self.num_nodes, 0.4)
            connected = nx.is_connected(G)
        for i, j in G.edges():                              
            G[i][j]['weight'] = random.randint(1, 10)
        return G

    def link_state_routing(self):
        return nx.shortest_path(self.graph, weight='weight', method='dijkstra')

    def distance_vector_routing(self):
        return nx.shortest_path(self.graph, weight='weight', method='bellman-ford')

    def print_routing_table(self, algorithm_name, results):
        print(f"\nRouting Table ({algorithm_name}):")
        headers = [f"Node {i}" for i in range(self.num_nodes)]
        table_data = []

        for src in range(self.num_nodes):
            row = [f"Node {src}"]
            for dest in range(self.num_nodes):
                if src != dest:
                    path = results[src][dest]
                    cost = sum(self.graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
                    row.append(f"Cost: {cost}, Path: {path}")
                else:
                    row.append("-")
            table_data.append(row)

        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

        for src in range(self.num_nodes):
            for dest in range(self.num_nodes):
                if src != dest:
                    path = results[src][dest]
                    cost = sum(self.graph[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1))
                    hops = len(path) - 1
                    delay = cost * 2 + hops * 3
                    print(f"Path from Node {src} to Node {dest}: Total Cost={cost}, Hop Count={hops}, Total Delay={delay} us")

    def get_shortest_path(self, source, target, method='dijkstra'):
        if method == 'dijkstra':
            return nx.shortest_path(self.graph, source=source, target=target, weight='weight', method='dijkstra')
        else:
            return nx.shortest_path(self.graph, source=source, target=target, weight='weight', method='bellman-ford')
class RoutingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Network Routing Simulator")
        self.geometry("1000x800")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.simulator = None
        self.create_widgets()

    def create_widgets(self):
        self.generate_button = ttk.Button(self, text="Generate Graph", command=self.generate_graph)
        self.generate_button.pack()

        self.run_simulation_button = ttk.Button(self, text="Run Simulation", command=self.run_simulation)
        self.run_simulation_button.pack()

        self.highlight_path_button = ttk.Button(self, text="Highlight Shortest Path", command=self.highlight_shortest_path)
        self.highlight_path_button.pack()

        self.algorithm_choice = tk.IntVar(value=1)
        self.radio1 = ttk.Radiobutton(self, text="Link State Routing", variable=self.algorithm_choice, value=1)
        self.radio1.pack()
        self.radio2 = ttk.Radiobutton(self, text="Distance Vector Routing", variable=self.algorithm_choice, value=2)
        self.radio2.pack()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.output_note = ttk.Label(self, text="Note: Simulation results are displayed in the terminal.", font=('Arial', 12), foreground="Navy")
        self.output_note.pack()
        self.output_note = ttk.Label(self, text="Make sure the terminal is large enough to fit the table and try small graph 6 nodes or less", font=('Arial', 12), foreground="Navy")
        self.output_note.pack()

        self.canvas_frame = ttk.Frame(self)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        self.canvas = None

    def generate_graph(self):
        num_nodes = simpledialog.askinteger("Input", "Enter number of nodes:", parent=self, minvalue=2, maxvalue=20)
        if num_nodes is not None:
            self.simulator = RoutingSimulator(num_nodes)
            self.display_graph(self.simulator.graph)

    def display_graph(self, G, highlight_path=None):
        if self.canvas:
           self.canvas.get_tk_widget().destroy()
           plt.close()  # Close the existing figure

        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='lightblue', edge_color='grey', width=1, node_size=500)

        edge_labels = {(i, j): G[i][j]['weight'] for i, j in G.edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        if highlight_path:
            edges_in_path = [(highlight_path[n], highlight_path[n + 1]) for n in range(len(highlight_path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    def on_close(self):
        """ Custom close function to properly terminate the application. """
        plt.close()  # Close the matplotlib figure
        self.destroy()  # Close the Tkinter window

    def run_simulation(self):
        if not self.simulator:
            messagebox.showinfo("Information", "Please generate the graph first")
            return

        algorithm = "Link State Routing" if self.algorithm_choice.get() == 1 else "Distance Vector Routing"
        start_time = time.perf_counter()
        results = self.simulator.link_state_routing() if self.algorithm_choice.get() == 1 else self.simulator.distance_vector_routing()
        elapsed_time = (time.perf_counter() - start_time) * 1000

        print(f"{algorithm}:")
        self.simulator.print_routing_table(algorithm, results)
        print(f"Time elapsed for {algorithm}: {elapsed_time:.6f} ms\n")

         
    def highlight_shortest_path(self):
        if not self.simulator:
            messagebox.showinfo("Information", "Please generate the graph first")
            return

        source = simpledialog.askinteger("Input", "Enter source node:", parent=self, minvalue=0, maxvalue=self.simulator.num_nodes - 1)
        target = simpledialog.askinteger("Input", "Enter target node:", parent=self, minvalue=0, maxvalue=self.simulator.num_nodes - 1)

        if source is None or target is None:
            return

        shortest_path = self.simulator.get_shortest_path(source, target)
        self.display_graph(self.simulator.graph, highlight_path=shortest_path)

if __name__ == "__main__":
    app = RoutingApp()
    app.mainloop()
