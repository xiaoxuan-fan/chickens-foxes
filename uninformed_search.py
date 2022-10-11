# Author: Xiaoxuan
# Date: 10/2/2022
# Purpose: Implement BFS, DFS, IDS
from collections import deque
from SearchSolution import SearchSolution


# wrap state in a node
class SearchNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent


# given a node, find its way back to the start node
def backchain(node):
    path = [node.state]
    while node.parent:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


# memoizing breadth-first search
def bfs_search(search_problem):
    solution = SearchSolution(search_problem, "BFS")
    start_node = SearchNode(search_problem.start_state)
    visited = set()
    frontier = deque()

    frontier.append(start_node)
    visited.add(start_node.state)
    while frontier:
        node = frontier.popleft()
        state = node.state

        if search_problem.goal_test(state):
            path = backchain(node)
            solution.path += path
            return solution

        children = search_problem.get_successors(state)
        for child in children:
            if child not in visited:
                visited.add(child)
                solution.nodes_visited += 1
                frontier.append(SearchNode(child, node))

    return solution


# path-checking depth-first search
def dfs_search(search_problem, depth_limit=100, node=None, solution=None):
    # If no node object is given, create a new search from the start state
    if node is None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

    state = node.state
    solution.nodes_visited += 1
    solution.path.append(state)

    if search_problem.goal_test(state):
        return solution

    if len(solution.path) <= depth_limit:
        children = search_problem.get_successors(state)
        for child in children:
            if child in solution.path:  # linear time
                continue
            solution = dfs_search(search_problem, depth_limit, SearchNode(child, node), solution)
            if search_problem.goal_test(solution.path[-1]):
                return solution

    solution.path.pop()
    return solution


# iterative deepening (DFS with increasing depth limit)
def ids_search(search_problem, depth_limit=100):
    node = SearchNode(search_problem.start_state)
    solution = SearchSolution(search_problem, "IDS")
    depth = 0

    while depth < depth_limit:
        solution = dfs_search(search_problem, depth, node, solution)
        if solution.path:
            return solution
        depth += 1

    return solution
