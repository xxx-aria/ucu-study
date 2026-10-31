"""
Graph: reading edges from a file, a dictionary representation of
an undirected graph, editing it and exporting it to the DOT format.
"""


def get_graph_from_file(filename: str) -> list[list[int]]:
    """
    Reads a graph from a specified file and returns a list of edges.
    The file should contain pairs of integers representing edges,
    with each edge formatted as "node1,node2" on a new line.
    For example:
        1,2
        3,4
        1,5

    Parameters:
    -----------
    filename: str
        The path to the file containing the graph edges in comma-separated format.

    Returns:
    --------
    list[list[int]]:
        A list of edges, where each edge is represented as a list of two integers.

    Example:
    --------
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
    ...                                  encoding='utf-8') as tmp:
    ...     _ = tmp.write('1,2\\n3,4\\n1,5\\n')
    >>> get_graph_from_file(tmp.name)
    [[1, 2], [3, 4], [1, 5]]
    >>> os.remove(tmp.name)
    """

    edges = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(',')
            if len(line) != 2:
                continue
            u, v = line
            edges.append([int(u), int(v)])
    return edges


def to_edge_dict(edge_list: list[list[int]]) -> dict[int, list[int]]:
    """
    Converts a graph from a list of edges to a dictionary representation.
    Each node maps to a list of adjacent nodes based on the edges provided.
    The list of adjacent nodes should be sorted in ascending order
    and contain no duplicates.

    Parameters:
    -----------
    edge_list : list[list[int]]
        A list of edges, where each edge is represented as a list of two integers.

    Returns:
    --------
    dict[int, list[int]]:
        A dictionary with nodes as keys and lists of adjacent nodes as values.

    Example:
    --------
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """

    graph = {}
    for u, v in edge_list:
        if u not in graph:
            graph[u] = set()
        if v not in graph:
            graph[v] = set()

        graph[u].add(v)
        graph[v].add(u)

    for node, neighs in graph.items():
        graph[node] = sorted(list(neighs))

    return graph


def is_edge_in_graph(graph: dict[int, list[int]], edge: tuple[int, int]) -> bool:
    """
    Checks if a given edge exists in the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to check.

    Returns:
    --------
    bool:
        True if the edge exists in the graph; False otherwise.

    Example:
    --------
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (4, 3))
    True
    """

    u, v = edge
    return u in graph and v in graph[u]


def add_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """
    Adds a new edge to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to add.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new edge included.

    Example:
    --------
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """

    u, v = edge
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

    return graph


def del_edge(graph: dict[int, list[int]], edge: tuple[int, int]) -> dict[int, list[int]]:
    """
    Removes an edge from the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    edge : tuple[int, int]
        A tuple representing the edge to remove.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified edge removed.

    Example:
    --------
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """

    u, v = edge

    try:
        graph[u].remove(v)
        graph[v].remove(u)
    except (ValueError, KeyError):
        pass

    return graph


def add_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """
    Adds a new node to the graph and returns the updated graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to add to the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the new node included.

    Example:
    --------
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """

    if node not in graph:
        graph[node] = []

    return graph


def del_node(graph: dict[int, list[int]], node: int) -> dict[int, list[int]]:
    """
    Deletes a node and all its incident edges from the graph.

    Parameters:
    -----------
    graph : dict[int, list[int]]
        A dictionary representation of the graph.
    node : int
        The node to delete from the graph.

    Returns:
    --------
    dict[int, list[int]]:
        The updated graph with the specified node and its edges removed.

    Example:
    --------
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """

    graph.pop(node, 0)
    for u in graph:
        if node in graph[u]:
            graph[u].remove(node)

    return graph


def convert_to_dot(filename: str) -> None:
    """
    Reads a file of edges, converts it into a directed graph in DOT format,
    and saves it as a file with the same name but with a .dot extension.

    This function allows for quick visualization and verification of
    graph functions by exporting them in a format that can be rendered as a graph.

    Parameters:
    -----------
    filename : str
        The name of the input file containing graph edges in "node1,node2" format,
        with one edge per line.

    Returns:
    --------
    None
        Saves the directed graph in DOT format to a file with the same
        name as the input file but with a .dot extension.
        Every edge "a,b" becomes two arcs: "a -> b" and "b -> a".

    Example:
    --------
    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False,
    ...                                  encoding='utf-8') as tmp:
    ...     _ = tmp.write('1,2\\n3,4\\n1,5\\n')
    >>> convert_to_dot(tmp.name)
    >>> dot_name = tmp.name[:-len('.txt')] + '.dot'
    >>> with open(dot_name, encoding='utf-8') as dot_file:
    ...     print(dot_file.read().strip())
    digraph {
    1 -> 2
    1 -> 5
    2 -> 1
    3 -> 4
    4 -> 3
    5 -> 1
    }
    >>> os.remove(tmp.name)
    >>> os.remove(dot_name)
    """

    graph = to_edge_dict(get_graph_from_file(filename))
    new_name = filename.split('.')[0]
    with open(new_name + '.dot', 'w', encoding='utf-8') as f:
        f.write('digraph {\n')
        for u in sorted(graph):
            for v in graph[u]:
                f.write(f'{u} -> {v}\n')
        f.write('}\n')


if __name__ == '__main__':
    import doctest

    print(doctest.testmod())
