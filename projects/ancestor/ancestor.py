def earliest_ancestor(ancestors, starting_node):
    # create vertices dict to create graph
    vertices = {}
    # add each
    for pair in ancestors:
        if pair[1] not in vertices:
            vertices[pair[1]] = set()
        vertices[pair[1]].add(pair[0])
    print(vertices)
    # declare a visited set to take away any redundant stack calls
    visited = set()
    # visited lists holds tuple pairs,
    visited_list = []
    stack = []
    stack.append(starting_node)
    # level keeps track of what level of the tree we are on (depth)
    level = 0
    while len(stack) > 0:
        level += 1
        # pop the top off
        vertex = stack.pop()
        if vertex in visited:
            level -= 1
        if vertex not in visited:
            visited.add(vertex)
            # checks to see if vertices dict has the equivalent key
            # Further Clarification: Looping over a dictionary that doesn't have the correct key results in a ValueError
            # Further Further Clarification: We don't want that happen because it stops the script from finishing running
            latest_ancestor_vert = vertices.get(vertex)
            if latest_ancestor_vert:
                for ancestor in latest_ancestor_vert:
                    # adds all of the connected ancestor nodes to the stack
                    stack.append(ancestor)
                    # the next line is so we can keep a track of what level of the tree we are on
                    visited_list.append((level, ancestor))
    if len(visited_list) == 0:
        return -1
    elif len(visited_list) > 1 and visited_list[-2][0] == visited_list[-1][0]:
        return min(visited_list[-2][1], visited_list[-1][1])
    else:
        return visited_list[-1][1]
