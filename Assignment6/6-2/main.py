class Node:
    def __init__(self, enter, length):
        self.enter = int(enter)
        self.length = int(length)

    def __str__(self):
        return f'e: {self.enter}, l: {self.length}'


inps = int(input())
nodes = []
times = []
for x in range(inps):
    e, le = input().split(" ")
    nodes.append(Node(e, le))
nodes.sort(key=lambda n: n.enter)
last = 0
for i in range(len(nodes)):
    # Finds the shortest message that is currently known
    mini = min([x for x in nodes if x.enter <= last], key=lambda n: n.length, default=None)
    if not mini:  # If there isn't one currently known find the next received message
        nodes.sort(key=lambda n: n.enter)
        mini = min([x for x in nodes if x.enter <= nodes[0].enter], key=lambda n: n.length, default=None)
        last = mini.enter
    time_taken = 0
    if mini.enter < last:
        time_taken += last - mini.enter
    time_taken += mini.length
    last += time_taken
    nodes.remove(mini)
    times.append(time_taken)
print(sum(times)//len(times))
