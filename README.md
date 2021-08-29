# cs50ai
CS50 AI solutions

## Week 0:
### Degrees
    `def shortest_path(source, target):
    # create a start node
    start = Node(source, None, None)

    # implement the frontier with first node is start
    frontier = []
    frontier.append(start)

    # implement empty explored list
    explored = []

    found = False
    # keep going through each node in frontier
    while len(frontier) > 0:
        # FIFO, pop the first node from the frontier
        person = frontier.pop(0)
        explored.append(person)
        # get the list of neighbors
        neighbors = neighbors_for_person(person.state)
        exist = False
        for state, action in neighbors:
            if state == target:
                end = Node(state, person, action)
                found = True
                break
            
            for item in explored:
                if item.state == state:
                    exist = True
                    break
            
            if not exist:
                new_node = Node(state, person, action)
                frontier.append(new_node)
    if not found:
        return None
    else:
        path = []
        path.append(end)
        while path[:-1].parent != None:
            path.append(path[:-1].parent)
        path.reverse()
        result = set()
        for node in path:
            result.add((node.state, node.action))
        return result

