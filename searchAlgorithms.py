# Shlomi Ben-Shushan


import containers as ds


class SearchProblemInterface:
    """
    This is an example of how a Search Problem should look in order to use the following algorithms.
    A search problem should have a method for getting the start state, a method that gets a state and returns true if
    and only if it is a goal state, a method for gettings the successors states, and a method that gets and action and
    returns its cost.
    """

    def getStartState(self):
        raise "getStartState not defined"

    def isGoalState(self, state):
        raise "isGoalState not defined"


    def getSuccessors(self, state):
        raise "getSuccessors not defined"


    def getCostOfActions(self, actions):
        raise "getCostOfActions not defined"


class Node:
    """
    In Search Problems, every node in the Tree/Graph should contain a state and a path to it.
    """
    
    def __init__(self, state, path):
        self.state = state
        self.path = path


def nullHeuristic(state, problem=None):
    """
    A trivial heuristic. For better results in A* or other heuristic-based algorithm, you should implement and use a
    better heuristic function.
    """
    return 0


def DFS(problem):
    """
    Depth First Search algorithm deepens in the search-graph until it is no longer possible, then backtrack and deepens
    in another way, until there are no more paths left.
    """
    
    frontier = ds.Stack()  # Use Stack to implement LIFO.
    frontier.push((problem.getStartState(), []))
    closed_list = []  # Using Graph-Search to avoid re-checking states.
    while not frontier.isEmpty():
        state, solution = frontier.pop()
        if problem.isGoalState(state):
            return solution
        closed_list.append(state) 
        for child in problem.getSuccessors(state):  # Expand to the successors that hasn't been visited.
            if not child[0] in closed_list:  # Push successor that isn't int the closed_list to the frontier.
                frontier.push((child[0], solution + [child[1]]))
    return None


def BFS(problem):
    """
    Breadth First Search algorithm expand every node in depth i before it expands to depth i+1.
    """
    
    frontier = ds.Queue()  # Use Queue to implement FIFO.
    frontier.push((problem.getStartState(), []))
    closed_list = []  # Using Graph-Search to avoid re-checking states.
    while not frontier.isEmpty():
        state, solution = frontier.pop()
        if problem.isGoalState(state):
            return solution
        closed_list.append(state)
        for child in problem.getSuccessors(state):  # Expand to the successors that hasn't been visited.
            if not child[0] in closed_list:  # Push successor that isn't int the closed_list to the frontier.
                closed_list.append(child[0])
                frontier.push((child[0], solution + [child[1]]))
    return None


def UCS(problem):
    """
    Uniform Cost Search algorithm searches the node of least total cost first.
    """
    
    frontier = ds.PriorityQueue()  # Use PriorityQueue to prioritize the next state.
    frontier.push((problem.getStartState(), []) ,0)  # The first node contains the start_state, empty path and cost = 0.
    closed_list = []  # Using Graph-Search to avoid re-checking states.
    while not frontier.isEmpty():
        state, solution = frontier.pop()
        if problem.isGoalState(state):
            return solution
        if state not in closed_list:
            for child in problem.getSuccessors(state):  # Expand according to the lower cost (to "g" function).
                if child[0] not in closed_list:
                    new_state = (child[0], solution + [child[1]])
                    cost = problem.getCostOfActions(solution + [child[1]])
                    frontier.push(new_state, cost)
        closed_list.append(state)
    return None


def AStar(problem, heuristic=nullHeuristic):
    """
    A* Search algorithm searches the node that has the lowest combined cost and heuristic first.
    """
    
    s = problem.getStartState()
    frontier = ds.PriorityQueue()  # Use PriorityQueue to prioritize the next state.
    frontier.push((s, []), nullHeuristic(s, problem))  # The first node contains the start, empty path and an heuristic.
    closed_list = []  # Using Graph-Search to avoid re-checking states.
    while not frontier.isEmpty():
        state, solution = frontier.pop()
        if problem.isGoalState(state):
            return solution
        if state not in closed_list:
            for child in problem.getSuccessors(state):  # Expand according to the cost and heuristic.
                if child[0] not in closed_list:
                    new_state = (child[0], solution + [child[1]])
                    cost = problem.getCostOfActions(solution + [child[1]]) + heuristic(child[0], problem)
                    frontier.push(new_state, cost)
        closed_list.append(state)
    return solution
