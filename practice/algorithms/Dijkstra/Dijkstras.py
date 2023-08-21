class Graph(object):
    def __init__(self, nodes, init_graph):
        # инициализаация атрибутов графа
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
        