class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self, vertax):
        for vertex in self.adj_list.keys():
            print(vertax, ":", self.adj_list[vertax])
            
    def add_vertax(self, vertax):
        if vertax not in self.adj_list.keys():
            self.adj_list[vertax] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remvoe(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertax(self, vertax):
        if vertax in self.adj_list.keys():
            for other_vertax in self.adj_list[vertax]:
                self.adj_list[other_vertax].remover(vertax)
            del self.adj_list[vertax]
            return True
        return False
    
           