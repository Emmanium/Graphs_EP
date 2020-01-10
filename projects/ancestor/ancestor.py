def earliest_ancestor(ancestors, starting_node):
    # create vertices dict to create graph
    vertices = {}
    # add each
    for pair in ancestors:
        if pair[0] not in vertices:
            vertices[pair[0]] = set()
        if pair[1] not in vertices:
            vertices[pair[1]] = set()
        vertices[pair[0]].add(pair[1])
        vertices[pair[1]].add(pair[0])
    # establish visited cache, use a set
    visited = set()
    stack = []
    stack.append(starting_node)
    while len(stack) > 0:
        # pop the top off
        vertex = stack.pop()
        # if it hasn't been visited
        if vertex not in visited:
            # print and add it to visited
            print(vertex)
            visited.add(vertex)
        # add all of its neighbors to the stack
        for ancestor_node in vertices[vertex]:
            stack.append(ancestor_node)
