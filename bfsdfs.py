class Queue:
    def __init__(self):
        self.buffer = []
    def enqueue(self, element):
        self.buffer.insert(0,element)
    def dequeue(self):
        return self.buffer.pop()
    def size(self):
        return len(self.buffer)
    def isEmpty(self):
        return self.buffer == []
    def show(self):
        print self.buffer


def BFS(graph,root,target):
    q = Queue()
    visited = []
    q.enqueue(root)
    path = 0
    while not q.isEmpty():
        v = q.dequeue()
        if v == target:
           return visited
        elif v not in visited:
            for edge in graph[v]:
                if v not in visited:
                    q.enqueue(edge)
            visited.append(v)
    return visited


def dfs(graph,start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)
    return path

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}

print(BFS(graph,1,7))
print(dfs(graph,2))
