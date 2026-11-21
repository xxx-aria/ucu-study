"""
Модуль notes_link: граф зв'язків між нотатками у стилі Obsidian.
"""


def build_graph_from_note(note_path: str, graph: dict | None = None) -> dict:
    """
    Build the graph of all notes reachable from the note at note_path.

    A link to a note looks like [[name]] and means a link to the file
    name.md in the same folder. The result is a dictionary
    {note name: sorted list of unique names it links to}.
    Notes without links are not keys of the dictionary.
    A link to a note that does not exist is kept, but not followed.
    If graph is given, the new notes are added to it.
    The function must call itself.
    """
    if graph is None:
        graph = {}
    note_name = note_path.split('/')[-1][:-3]
    try:
        with open(note_path, mode='r', encoding='utf-8') as note:
            for line in note:
                if '[[' in line and ']]' in line:
                    linked_notes = [x.split(']]')[-2] for x in line.split('[[') if ']]' in x]
                    linked_notes = list(filter(lambda x: x != '', linked_notes))
                    for linked_note in linked_notes:
                        new_note_path = note_path[: -len(note_name + '.md')] + linked_note + '.md'
                        new_note_name = linked_note.split('/')[-1]
                        if note_name not in graph:
                            graph[note_name] = []
                        if new_note_name not in graph[note_name]:
                            graph[note_name].append(new_note_name)
                            graph[note_name].sort()
                        if new_note_name not in graph:
                            build_graph_from_note(new_note_path, graph)
    except FileNotFoundError:
        pass
    return graph


def convert_to_dot(graph: dict) -> None:
    """
    Write the graph to the file graph.dot in the DOT format:
    the line 'digraph {', then one line 'note -> link' for every link
    (notes in sorted order, links in the order of their list), then '}'.
    """
    with open('graph.dot', mode='w', encoding='utf-8') as f:
        f.write('digraph {\n')
        for note in sorted(graph):
            for linked_note in sorted(graph[note]):
                f.write(f'{note} -> {linked_note}\n')
        f.write('}\n')
