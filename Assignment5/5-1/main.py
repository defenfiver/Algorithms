class Node:
    def __init__(self, _energy, _n_cost, id_num):
        self.id_num = id_num
        self.energy = _energy
        self.n_cost = _n_cost
        self.next = None


def main():
    for j in range(x):
        current = nodes[j]
        starter = current.id_num
        power = 0
        init = True
        while current.id_num != starter or init:
            power += current.energy
            if power >= current.n_cost:
                power -= current.n_cost
                current = current.next
                init = False
            else:
                break
        if not init and current.id_num == starter:
            return starter


x = int(input())
nodes = []
for i in range(x):
    num = input().split(" ")
    energy = int(num[0])
    n_cost = int(num[1])
    nodes.append(Node(energy, n_cost, i))

for i in range(x):
    if i == x-1:
        nodes[i].next = nodes[0]
    else:
        nodes[i].next = nodes[i + 1]

print(main())
