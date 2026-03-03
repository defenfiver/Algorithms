def main():
    n = int(input())
    genes = input().split(" ")
    for i in range(n):
        genes[i] = int(genes[i])
    coolJeansBro = sorted(genes)
    if genes == coolJeansBro:
        print("yes")
        return
    counter = 0
    pos = []
    for i in range(n):
        if genes[i] != coolJeansBro[i]:
            counter += 1
            pos.append(i+1)
    if counter == 2:
        print("yes")
        print(f'swap {pos[0]} {pos[1]}')
        return
    if genes[::-1] == coolJeansBro:
        print("yes")
        print(f'reverse 1 {n}')
        return
    for i in range(n//2):
        reversey = genes[:i+1] + genes[n-i-2:i:-1] + genes[n-i-1:]
        if reversey == coolJeansBro:
            print("yes")
            print(f'reverse {i+2} {n-i-1}')
            return
    print("no")


main()
