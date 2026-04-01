import numpy
from testInput import testInput
import cProfile


def blend():
    # x = int(input())
    x = 10000
    nums, inputs = [], []
    # for i in range(x):
    #     tmp = input().split(" ")
    #     inputs.append([tmp[0], int(tmp[1])])
    tmpInput = testInput().split("\n")
    for i in range(x):
        tmp = tmpInput[i].split(" ")
        inputs.append([tmp[0], int(tmp[1])])

    for i in range(x):
        num = inputs[i]
        action = num[0]
        item = num[1]
        if action == "a":
            nums.append(item)
            med = numpy.median(nums)
            imed = int(med)
            if imed == med:
                med = imed
            print(med)
        elif action == "r":
            if item not in nums:
                print("Wrong!")
            else:
                nums.remove(item)
                if not nums:
                    print("Wrong!")
                else:
                    med = numpy.median(nums)
                    imed = int(med)
                    if imed == med:
                        med = imed
                    print(med)


cProfile.run('blend()')
