import heapq

inps = int(input())
nodes = []
time = 0
for x in range(inps):
    e, le = input().split(" ")
    nodes.append((int(le), int(e)))
nodes.sort(key=lambda n: n[1], reverse=True)

current_time = nodes[-1][1]
queue = [nodes[-1]]
nodes.pop()
# Iterate over time, starting at node[0].enter
# as time goes on add all the items that happened while you iterated over the current
# add to min heap by length and do that one next repeat
while nodes or queue:
    current_node = heapq.heappop(queue)
    wait = 0
    if current_time > current_node[1]:
        wait = current_time - current_node[1]
    time += current_node[0] + wait
    current_time += current_node[0]

    while nodes and nodes[-1][1] <= current_time:
        heapq.heappush(queue, nodes[-1])
        nodes.pop()
    if not queue and nodes:
        current_time = nodes[-1][1]
        while nodes and nodes[-1][1] <= current_time:
            heapq.heappush(queue, nodes[-1])
            nodes.pop()

print(time//inps)
# for i in range(len(nodes)):
#     # Finds all available nodes
#     available_nodes = [x for x in nodes if x.enter <= last_time]
#     # Finds the shortest node that is available
#     mini = min(available_nodes, key=lambda n: n.length, default=None)
#     if not mini:  # If there isn't one currently known find the next received message
#         nodes.sort(key=lambda n: n.enter)
#
#         # Finds all nodes that arrive at the next time
#         next_available_nodes = [x for x in nodes if x.enter <= nodes[0].enter]
#         # Finds the shortest of those nodes
#         mini = min(next_available_nodes, key=lambda n: n.length)
#
#         last_time = mini.enter + mini.length
#         time_taken = mini.length
#     else:
#         time_taken = 0
#         # If the node arrived before the last time we did something
#         if mini.enter < last_time:
#             # Add the difference between when it arrived and when we started it
#             time_taken += last_time - mini.enter
#         time_taken += mini.length
#         last_time += time_taken
#     nodes.remove(mini)
#     times.append(time_taken)
# print(sum(times)//len(times))
