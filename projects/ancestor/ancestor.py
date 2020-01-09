
def earliest_ancestor(ancestors, starting_node):
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
        for ancestor_node in ancestors[vertex]:
            stack.append(ancestor_node)
