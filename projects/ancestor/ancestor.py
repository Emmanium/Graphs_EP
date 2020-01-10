def earliest_ancestor(ancestors, starting_node):
    # create vertices dict to create graph
    vertices = {}
    # add each
    for pair in ancestors:
        if pair[1] not in vertices:
            vertices[pair[1]] = set()
        vertices[pair[1]].add(pair[0])
    print(vertices)
    # establish visited cache, use a set
    visited = set()
    visited_list = []
    stack = []
    stack.append(starting_node)
    while len(stack) > 0:
        # pop the top off
        vertex = stack.pop()
        # if it hasn't been visited
        if vertex not in visited:
            # print and add it to visited
            visited.add(vertex)
            visited_list.append(vertex)
            # add all of its neighbors to the stack
            print(vertex)
            latest_ancestor = vertices.get(vertex)
            if latest_ancestor:
                for ancestor in latest_ancestor:
                    stack.append(ancestor)
    if len(visited_list) == 1:
        return -1
    else:
        return visited_list[-1]
