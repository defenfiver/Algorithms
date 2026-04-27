import copy
"""
Tasks:
    Backtracking: Bookmarked?
    Bounding: Approximation made
    Profile Code: incomplete

Choice Tasks:
    Optimizations:
        includeOptimizations
            If a node has one neighbor include that neighbor and exclude that node
            If all of a nodes neighbors have been included, exclude that node
        initOptimizations
            If a node has no neighbors at the start, you don't have to include that node because it has no edges
        calc_next?: Choose the node with the most not included neighbors
    backtrack:
        "do": If one of the neighbors of a node has been excluded, you can't exclude that node



Potential Optimizations
x If a node only has one neighbor, include that neighbor, and exclude that node
x Remove nodes if they have no edges (If all of a nodes edges have been included, exclude that node)
x Removes edge that are already included
x Choose the next node that has the most edges
"""


# noinspection PyDefaultArgument
class ProblemState:
    def __init__(self, next_id=0, include_set=set(), exclude_set=set(), undecided=set()):
        self.next_id = next_id
        self.include_set = include_set
        self.exclude_set = exclude_set
        self.undecided = undecided

    def calc_next(self, graph: dict[int, set]):
        _max = -1
        _max_num = -1
        for x in self.undecided:
            if len(graph[x]) > _max:
                _max = len(graph[x])
                _max_num = x
        self.next_id = _max_num
        return _max_num


# noinspection PyUnboundLocalVariable
class Solver:

    def __init__(self):
        self.N = 0
        self.M = 0
        self.graph = None
        self.best = None
        self.Load()

    def Load(self):
        self.N, self.M = map(int, input().split(" "))
        self.graph = {vertex_id: set() for vertex_id in range(self.N)}
        for _ in range(self.M):
            a, b = map(int, input().split(" "))
            # Add edge between a <---> b
            self.graph[a].add(b)
            self.graph[b].add(a)

        # Update best to a "worst-case" scenario:
        # We know we *could* solve the problem by building a toll station in every
        # star system, so initialize best to N
        self.best = self.N
        # print(self.graph)

    def TestValid(self, state: ProblemState, graph=None):
        if graph is None:
            graph = self.graph
        for system_id in range(self.N):
            # If system has a station, all of its hyper relays have a toll station.
            if system_id in state.include_set:
                continue
            # Otherwise, we need to check that all hyper relays connected to this system have a toll station on the other end.
            for conn_id in graph[system_id]:
                if conn_id not in state.include_set:
                    return False
        return True

    @staticmethod
    def IncludeSystem(state: ProblemState, system_id: int, graph: dict[int, set]):
        state.include_set.add(system_id)
        keys = graph[system_id]
        for i in keys:
            graph[i].discard(system_id)
        state.undecided.discard(system_id)

    @staticmethod
    def ExcludeSystem(state: ProblemState, system_id: int):
        state.exclude_set.add(system_id)
        state.undecided.discard(system_id)

    def Approximate(self, state: ProblemState):
        graph = copy.deepcopy(self.graph)
        while not self.TestValid(state, graph):
            _next = state.calc_next(graph)
            self.IncludeSystem(state, _next, graph)
            self.includeOptimizations(state, graph)
        return len(state.include_set)

    def initOptimizations(self, state: ProblemState, graph: dict[int, set]):

        # Optimizations that can only be run once, at the start
        cop_Undecided = copy.deepcopy(state.undecided)
        for i in cop_Undecided:
            if i in state.undecided:
                if len(graph[i]) == 0:
                    self.ExcludeSystem(state, i)
                    # print(f'{i} is a loser')

    def includeOptimizations(self, state: ProblemState, graph: dict[int, set]):
        # Optimizations that should be run every time a node is included
        changing = 2
        while changing > 0:
            changing -= 1
            cop_Undecided = copy.deepcopy(state.undecided)
            for i in cop_Undecided:
                if i in state.undecided:
                    length = len(graph[i])
                    # If i has one neighbor, include neighbor and exclude i
                    if length == 1:
                        # # A trick I found here https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
                        neighbor = None
                        for neighbor in graph[i]:
                            break
                        self.IncludeSystem(state, neighbor, graph)
                        self.ExcludeSystem(state, i)
                        changing = 1
                        # print(f' optimized {neighbor}, {graph}')
                    # If all of i's neighbors have been included exclude i
                    elif length == 0:
                        self.ExcludeSystem(state, i)
                        changing = 1
                        # print(f' opti-excluded {i}')

    # Entry point to running the solver
    def Solve(self):
        # Build initial problem state
        initial_state = ProblemState(0, include_set=set(), exclude_set=set(), undecided=set([x for x in range(self.N)]))

        # Create a copy of the graph, so self.graph stays unchanged
        graph = copy.deepcopy(self.graph)

        # Run optimizations, if somehow valid return
        self.initOptimizations(initial_state, graph)
        # self.includeOptimizations(initial_state, graph) This is what caused incorrectness not entirely sure why
        if self.TestValid(initial_state):
            return max(len(initial_state.include_set), self.best)

        # Update best with the optimizations
        self.best = self.Approximate(copy.deepcopy(initial_state))
        cur_system = initial_state.calc_next(graph)

        do = True
        # if a neighbor of the node has already been excluded you can't exclude the node so you can skip it
        for i in graph[cur_system]:
            if i in initial_state.exclude_set:
                do = False
                break
        if do:
            new_graph = copy.deepcopy(graph)
            exc_state = copy.deepcopy(initial_state)

        # Try including the current system under consideration
        self.IncludeSystem(initial_state, cur_system, graph)
        initial_state.calc_next(graph)
        self.includeOptimizations(initial_state, graph)
        self.Branch(initial_state, graph)

        if do:
            # Try excluding the current system under consideration
            self.ExcludeSystem(exc_state, cur_system)
            for x in copy.deepcopy(new_graph[cur_system]):
                self.IncludeSystem(exc_state, x, new_graph)
            self.includeOptimizations(exc_state, new_graph)
            exc_state.calc_next(new_graph)
            # print(f'Excluding {cur_system}')
            self.Branch(exc_state, new_graph)

        return self.best

    def Branch(self, state: ProblemState, graph: dict[int, set]):
        # Current count of systems with stations
        num_stations = len(state.include_set)
        # Is this a valid solution?
        valid_sol = self.TestValid(state)
        # If so, if better than best, update best and bail out of this branch.
        if valid_sol and num_stations < self.best:
            self.best = num_stations
            return
        # If this solution is worse or equal to the best, we don't need to try it
        if num_stations >= self.best:
            return
        # If this solution could only be as good as the best
        if len(state.undecided) == 1 and num_stations + 1 == self.best:
            return
        # Not a solution. If next_id is not valid, return.
        if state.calc_next(graph) == -1:
            return
        # If we're here, next_id is valid, and we don't yet have a solution on this branch.
        cur_system = state.next_id

        do = True
        # if a neighbor of the node has already been excluded you can't exclude the node so you can skip it
        for i in graph[cur_system]:
            if i in state.exclude_set:
                do = False
        if do:
            new_graph = copy.deepcopy(graph)
            exc_state = copy.deepcopy(state)

        # Try including the current system under consideration
        self.IncludeSystem(state, cur_system, graph)
        state.calc_next(graph)
        # print(f'Including {cur_system}')
        self.includeOptimizations(state, graph)
        self.Branch(state, graph)

        if do:
            # Try excluding the current system under consideration
            self.ExcludeSystem(exc_state, cur_system)
            for x in copy.deepcopy(new_graph[cur_system]):
                self.IncludeSystem(exc_state, x, new_graph)
            self.includeOptimizations(exc_state, new_graph)
            exc_state.calc_next(new_graph)
            # print(f'Excluding {cur_system}')
            self.Branch(exc_state, new_graph)


if __name__ == "__main__":
    solver = Solver()
    print(solver.Solve())
