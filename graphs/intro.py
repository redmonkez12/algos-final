import networkx as nx

G = nx.Graph()
G.add_node("A2")
G.add_nodes_from(["A3", "A4", "A5"])
G.add_edge("A2", "A3")
G.add_edges_from([("A3", "A4"), ("A4", "A5")])

for i in range(2, 6):
    G.add_edge("B{}".format(i), "C{}".format(i))
    if 2 < i < 5:
        G.add_edge("B{}".format(i), "B{}".format(i + 1))
    if i < 5:
        G.add_edge("C{}".format(i), "C{}".format(i + 1))

print(G.number_of_nodes(), "nodes.")
print(G.number_of_edges(), "edges.")


class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")

        val = self.top.value

        self.top = self.top.next

        return val

