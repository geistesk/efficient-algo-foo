#!/usr/bin/env python

from typing import List, NamedTuple, Set, Tuple, TypeVar


# Our nodes are generics and edges are a tuple of nodes.
Node = TypeVar('Node')
Edge = Tuple[Node, Node]


class Graph(NamedTuple):
    'Undirected graph with nodes and edges'
    nodes: List[Node]
    edges: List[Edge]


def depth_first_search(graph: Graph, ele: Node, root: Node = None) -> bool:
    'Depth first search in graph for ele.'

    visited: Set[Node] = set()
    s: Node = root if root is not None else graph.nodes[0]

    def dfs(node: Node) -> bool:
        if node == ele:
            return True

        visited.add(node)

        neighbors_l: List[Node] = [m for (m, n) in graph.edges if n == node]
        neighbors_r: List[Node] = [n for (m, n) in graph.edges if m == node]
        neighbors: List[Node] = [
          n for n in set(neighbors_l).union(neighbors_r) if n not in visited]

        for n in neighbors:
            if dfs(n):
                return True
        return False

    return dfs(s)


if __name__ == '__main__':
    graph = Graph([1, 2, 3, 7], [(1, 2), (1, 7), (2, 3), (3, 7)])
    print(depth_first_search(graph, 1, root=3))
