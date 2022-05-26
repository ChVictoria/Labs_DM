import networkx as nx
import pylab as plt
from tkinter import *

g = nx.DiGraph()
g.add_edge(0, 1, weight=5)
g.add_edge(0, 2, weight=-6)
g.add_edge(1, 2, weight=7)
g.add_edge(2, 1, weight=-2)
g.add_edge(1, 3, weight=4)
g.add_edge(2, 3, weight=6)


def myfunc1(elem):
    return elem != s


def myfunc2(elem):
    return u == elem[0]


def myfunc3(u, v):
    if d[v] > d[u] + g[u][v]['weight']:
        d[v] = d[u] + g[u][v]['weight']
        P[v].clear()
        P[v].extend(P[u][:len(P[u]) - 1])
        P[v].append(u)
        P[v].append(v)


M0 = set()
M2 = set()
P = dict()
M11 = []
M12 = []
d = []
s = 0
h = 3
for u in g.nodes():
    d.append(float("inf"))
    P[u] = []
d[s] = 0

M11.append(s)
for u in [i for i in filter(myfunc1, g.nodes())]:
    M2.add(u)
while len(M11) != 0 or len(M12) != 0:
    u = M11.pop() if len(M12) == 0 else M12.pop()
    for v in [k for j, k in filter(myfunc2, g.edges())]:
        if v in M2:
            M11.append(v)
            M2.remove(v)
            myfunc3(u, v)
        elif v in M11 or v in M12:
            myfunc3(u, v)
        elif v in M0 and d[v] > d[u] + g[u][v]['weight']:
            M12.append(v)
            M0.remove(v)
            d[v] = d[u] + g[u][v]['weight']
            P[v].clear()
            P[v].extend(P[u][:len(P[u]) - 1])
            P[v].append(u)
            P[v].append(v)
    M0.add(u)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw(g, arrows=True, pos=nx.circular_layout(g), with_labels=True)
pos = nx.circular_layout(g)
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels,label_pos=0.3)
plt.savefig(r'graph.png')
plt.close()
nx.draw(g, arrows=True, pos=nx.circular_layout(g), with_labels=True)
pos = nx.circular_layout(g)
my_edge_list = [(P[h][i - 1], P[h][i]) for i in range(1, len(P[h]))]
print("P = ", P)
print("d = ", d)
nx.draw_networkx_edges(g, edgelist=my_edge_list, pos=nx.circular_layout(g), arrows=True, edge_color='r',
                       nodelist=g.nodes())
nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=labels,label_pos=0.3)
plt.savefig(r'subgraph.png')
root = Tk()
root.title("Алгоритм Левіта")
l1 = Label(root, text="Граф", font=("Times", 16))
l2 = Label(root, text="Найкоротший шлях від вершини " + str(s) + " до вершини " + str(h), font=("Times", 16))
p = PhotoImage(file='graph.png')
iml = Label(root, image=p)
p1 = PhotoImage(file='subgraph.png')
iml1 = Label(root, image=p1)
l1.pack()
iml.pack()
l2.pack()
iml1.pack()
root.mainloop()
