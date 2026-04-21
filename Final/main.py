import copy
"""
Tasks:
    Backtracking: incomplete
    Bounding: incomplete
    Profile Code: incomplete

Choice Tasks:
    Optimizations:
        includeOptimizations
            If a node has one neighbor include that neighbor and exclude that node
            If all of a nodes neighbors have been included, exclude that node
        calc_next?: Choose the node with the most not included neighbors
        


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

    def TestValid(self, state: ProblemState):
        for system_id in range(self.N):
            # If system has a station, all of its hyper relays have a toll station.
            if system_id in state.include_set:
                continue
            # Otherwise, we need to check that all hyper relays connected to this system have a toll station on the other end.
            for conn_id in self.graph[system_id]:
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

    def includeOptimizations(self, state: ProblemState, graph: dict[int, set]):
        # Optimizations that should be run every time a node is included
        changing = 2
        while changing <= 0:
            changing -= 1
            for i in copy.deepcopy(state.undecided):
                if i in state.undecided:
                    length = len(graph[i])
                    # If i has one neighbor, include neighbor and exclude i
                    if length == 1:
                        # A trick I found here https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
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

    # Entry point to running the solver
    def Solve(self):
        # Build initial problem state
        initial_state = ProblemState(0, undecided=set([x for x in range(self.N)]))

        # Create a copy of the graph, so self.graph stays unchanged
        graph = copy.deepcopy(self.graph)

        # Run optimizations, if valid return
        self.includeOptimizations(initial_state, graph)
        if self.TestValid(initial_state):
            return len(initial_state.include_set)

        # Update best with the optimizations
        self.best = self.best - len(initial_state.exclude_set)

        cur_system = initial_state.calc_next(graph)

        new_graph = copy.deepcopy(graph)
        # Try including the current system under consideration
        inc_state = copy.deepcopy(initial_state)
        self.IncludeSystem(inc_state, cur_system, graph)
        inc_state.calc_next(graph)
        # print(f'Including {cur_system}')
        self.includeOptimizations(inc_state, graph)
        self.Branch(inc_state, graph)

        # Try excluding the current system under consideration
        self.ExcludeSystem(initial_state, cur_system)
        initial_state.calc_next(new_graph)
        # print(f'Excluding {cur_system}')
        self.Branch(initial_state, new_graph)

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
        # Not a solution. If next_id is not valid, return.
        if state.calc_next(graph) == -1:
            return
        # If we're here, next_id is valid, and we don't yet have a solution on this branch.
        cur_system = state.next_id

        # print(graph)
        new_graph = copy.deepcopy(graph)
        # Try including the current system under consideration
        inc_state = copy.deepcopy(state)
        self.IncludeSystem(inc_state, cur_system, graph)
        inc_state.calc_next(graph)
        # print(f'Including {cur_system}')
        self.includeOptimizations(inc_state, graph)
        self.Branch(inc_state, graph)

        # Try excluding the current system under consideration
        self.ExcludeSystem(state, cur_system)
        state.calc_next(new_graph)
        # print(f'Excluding {cur_system}')
        self.Branch(state, new_graph)


if __name__ == "__main__":
    solver = Solver()
    result = solver.Solve()
    print(result)
