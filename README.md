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

### Tic Tac Toe (using Minimax with alpha beta pruning)
    def minimax(board):
        """
        This method uses minimax with alpha beta pruning to optimize the running time
        Returns the optimal action for the current player on the board.
        """
        b = copy.deepcopy(board)  # Deep copy the board to test moves
        if player(board) == X:
            move, val = max_val_pruning(b, 0, -math.inf, math.inf)
        else:
            move, val = min_val_pruning(b, 0, -math.inf, math.inf)
        return move


    def max_val_pruning(board, depth, alpha, beta):
        """
        :param board: the board
        :param depth: depth of the search tree
        :param alpha: alpha value
        :param beta: beta value
        :return: move and value of that move
        """
        if terminal(board):  # If the game is ended
            val = utility(board)  # Get the score
            if val == -100:
                return None, val + depth  # As the depth increase, the value for O win increase
            elif val == 100:
                return None, val - depth  # AS the depth increase, the value for X win decrease
            else:
                return None, val
    
        val = - math.inf  # Set the initial value for the best value
        move = None
        # For each possible action on the board
        for a in actions(board):
            # Get the move (temp, won't be used) and value for the given action
            m, v = min_val_pruning(result(copy.deepcopy(board), a), depth + 1, alpha, beta)
            # Case the value for the given action if greater than the best value
            if v > val:
                val = v  # Set the new best value
                move = a  # Set the best move
                alpha = max(alpha, val)  # Set the alpha value
            # Random choose between actions that have the same value as the best value
            # So the AI won't move the same way in the same scenario
            elif v == val and bool(random.getrandbits(1)):
                move = a
            # Stop exploring if the best value of this action is greater than beta value
            if val > beta:
                return move, val
        return move, val


    def min_val_pruning(board, depth, alpha, beta):
        if terminal(board):
            val = utility(board)
            if val == -100:
                return None, val + depth
            elif val == 100:
                return None, val - depth
            else:
                return None, val
        val = math.inf
        move = None
        for a in actions(board):
            m, v = max_val_pruning(result(copy.deepcopy(board), a), depth + 1, alpha, beta)
            if v < val:
                val = v
                move = a
                beta = min(beta, val)
            elif v == val and bool(random.getrandbits(1)):
                move = a
            if val < alpha:
                return move, val
        return move, val