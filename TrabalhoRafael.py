import tkinter as tk
from tkinter import simpledialog, messagebox
import networkx as nx

def criaGrafo():
    G = nx.Graph()
    G.add_edge('rio do sul', 'presidente getulio', weight=66)
    G.add_edge('rio do sul', 'ibirama', weight=22.5)
    G.add_edge('rio do sul', 'agronomica', weight=17.6)
    G.add_edge('rio do sul', 'lontras', weight=66)
    G.add_edge('rio do sul', 'laurentino', weight=30)
    G.add_edge('rio do sul', 'aurora', weight=20)
    G.add_edge('presidente getulio', 'laurentino', weight=11)
    G.add_edge('presidente getulio', 'lontras', weight=60)
    G.add_edge('presidente getulio', 'taio', weight=70)
    G.add_edge('presidente getulio', 'rio do oeste', weight=45)
    G.add_edge('lontras', 'agronomica', weight=22.5)
    G.add_edge('lontras', 'taio', weight=20)
    G.add_edge('lontras', 'rio do oeste', weight=45)
    G.add_edge('ibirama', 'aurora', weight=75)
    G.add_edge('ibirama', 'agronomica', weight=176)
    G.add_edge('ibirama', 'salete', weight=22)
    G.add_edge('aurora', 'anta gorda', weight=44)
    G.add_edge('aurora', 'braço do trambudo', weight=40)
    G.add_edge('laurentino', 'pouso redondo', weight=7.5)
    G.add_edge('itaqua', 'taio', weight=40)
    G.add_edge('itaqua', 'dalbergia', weight=45)
    G.add_edge('ituporanga', 'salete', weight=45)
    
    return G

def verificaCidade(graph, cidade):
    cidades = [node.lower() for node in graph.nodes]
    while cidade.lower() not in cidades:
        messagebox.showwarning("Aviso", "Essa cidade não existe, favor informar outro valor.")
        cidade = simpledialog.askstring("Input", "Informe a cidade novamente:")
    return cidade

def calculaCaminho(graph, start, end):
    path = nx.dijkstra_path(graph, source=start.lower(), target=end.lower(), weight='weight')
    cost = nx.dijkstra_path_length(graph, source=start.lower(), target=end.lower(), weight='weight')
    return path, cost

def main():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    graph = criaGrafo()

    while True:
        start = simpledialog.askstring("Input", "Diga a cidade Inicial:", parent=root)
        start = verificaCidade(graph, start)  # Verifica se a cidade inicial é válida
        end = simpledialog.askstring("Input", "Diga a cidade final:", parent=root)
        end = verificaCidade(graph, end)  # Verifica se a cidade final é válida
        
        path, cost = calculaCaminho(graph, start, end)
        caminho_lista = ' --> '.join(path)
        
        resultado = f"O caminho mais curto de {start} para {end} é {caminho_lista} com um custo de: {cost}."
        messagebox.showinfo("Resultado", resultado)
        
        answer = messagebox.askyesno("Query", "Quer calcular outro caminho?")
        if not answer:
            break

    root.mainloop()

if __name__ == "__main__":
    main()
