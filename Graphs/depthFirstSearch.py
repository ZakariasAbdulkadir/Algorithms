# Vertex: Node Edges: Connection line
class Node:
    def __init_(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
    
    # O(v + e) | O(v) spacez
    def DFS(self, array):
        array.append(self.name)
        for child in self.children:
            child.DFS(array)
        return array