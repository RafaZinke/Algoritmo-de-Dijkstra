import tkinter as tk
from tkinter import simpledialog
import networkx as nx


def create_graph():
    G = nx.Graph()
    G.add_edge('Rio do Sul', 'Presidente Getulio', weight=66)
    G.add_edge('Rio do Sul', 'Ibirama', weight=22.5)
    G.add_edge('Rio do Sul', 'Agronomica', weight=17.6)
    G.add_edge('Rio do Sul', 'Lontras', weight=66)
    G.add_edge('Rio do Sul', 'Laurentino', weight=30)
    G.add_edge('Rio do Sul', 'Aurora', weight=20)
    G.add_edge('Aurora', 'Anta Gorda', weight=44)

    return G

def calculate_path(graph, start, end):
    path = nx.dijkstra_path(graph, source=start, target=end, weight='weight')
    cost = nx.dijkstra_path_length(graph, source=start, target=end, weight='weight')
    return path, cost

def main():
    root = tk.Tk()
    graph = create_graph()

    while True:
        start = simpledialog.askstring("Input", "Diga a cidade Inicial:", parent=root)
        end = simpledialog.askstring("Input", "Diga a cidade final:", parent=root)
        path, cost = calculate_path(graph, start, end)
        
        result_text = f"O caminho mais curto {start} para {end} é {path} Com um custo de: {cost}."
        tk.messagebox.showinfo("Resultado:", result_text)
        
        answer = tk.messagebox.askyesno("Query", "Quer calcular outro Caminho?")
        if not answer:
            break

    root.mainloop()

if __name__ == "__main__":
    main()
