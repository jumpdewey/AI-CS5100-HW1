# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    visited = set()
    stack = util.Stack()
    stack.push((problem.getStartState(), []))
    while stack:
        (vertex, path) = stack.pop()
        visited.add(vertex)
        if problem.isGoalState(vertex):
            return path
        for (succ, dire, _) in problem.getSuccessors(vertex):
            if succ not in visited:
                stack.push((succ, path + [dire]))

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    visited = set()
    q = util.Queue()
    q.push((problem.getStartState(), []))
    while q:
        (vertex, path) = q.pop()
        if visited.__contains__(vertex):
            continue
        visited.add(vertex)
        if problem.isGoalState(vertex):
            return path
        for (succ, dire, _) in problem.getSuccessors(vertex):
            if succ not in visited:
                q.push((succ, path + [dire]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = set()
    pq = util.PriorityQueue()
    costmap = {}
    path = {}
    start = problem.getStartState()
    pq.push(start, 0)
    costmap[start] = 0
    path[start] = []
    while pq:
        vertex = pq.pop()
        visited.add(vertex)
        if problem.isGoalState(vertex):
            return path[vertex]
        for (succ, dire, cost) in problem.getSuccessors(vertex):
            if succ not in visited:
                newCost = costmap.get(vertex) + cost
                pq.update(succ, newCost)
                if costmap.get(succ) == None or costmap.get(succ) > newCost:
                    path[succ] = path[vertex] + [dire]
                    costmap[succ] = newCost



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    closelist = set()
    pq = util.PriorityQueue()
    priorityMap = {}
    path = {}
    startstate = problem.getStartState()
    pq.push(startstate, 0)
    priorityMap[startstate] = 0
    path[startstate] = []
    while pq:
        vertex = pq.pop()
        closelist.add(vertex)
        if problem.isGoalState(vertex):
            return path[vertex]
        for (succ, dire, cost) in problem.getSuccessors(vertex):
            if succ not in closelist:
                if succ in priorityMap and priorityMap[succ] < cost + priorityMap[vertex]:
                    continue
                newCost = priorityMap.get(vertex) + cost + heuristic(succ, problem)
                pq.update(succ, newCost)
                priorityMap[succ] = priorityMap.get(vertex) + cost
                path[succ] = path[vertex] + [dire]


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
