"""
I had a difficult time figuring out a possible solution so,
Idea for puzzle solution from https://math.stackexchange.com/questions/351500/find-the-poisoned-pie
"""


def generate_mapping(s: int, p: int):
    """
    Return a dictionary mapping of which pies you test with each poison test stick.
    Test sticks are labeled: stick-0, stick-1, stick-2, stick-3, ..., stick-s
    Pies are labeled 0 : 999

    For this problem, s will always = 10, and p will always = 1000
    """
    # This example return is correctly formatted but will not ensure that you
    # identify the poisoned pie.
    # E.g., in this example, you use stick-0 to test pies 0 and 10.
    s0, s1, s2, s3, s4, s5, s6, s7, s8, s9 = [], [], [], [], [], [], [], [], [], []
    for i in range(p):
        x = (format(i, '010b'))
        if x[9] == "1":
            s0.append(i)
        if x[8] == "1":
            s1.append(i)
        if x[7] == "1":
            s2.append(i)
        if x[6] == "1":
            s3.append(i)
        if x[5] == "1":
            s4.append(i)
        if x[4] == "1":
            s5.append(i)
        if x[3] == "1":
            s6.append(i)
        if x[2] == "1":
            s7.append(i)
        if x[1] == "1":
            s8.append(i)
        if x[0] == "1":
            s9.append(i)
    return {
        "stick-0": s0,
        "stick-1": s1,
        "stick-2": s2,
        "stick-3": s3,
        "stick-4": s4,
        "stick-5": s5,
        "stick-6": s6,
        "stick-7": s7,
        "stick-8": s8,
        "stick-9": s9
    }


def solve(positive_tests: list, test_mapping: dict):
    """
    Returns the id of the poisoned pie.
    - positive_tests: list of poison tests that have a positive indicator
    - test_mapping: the test mapping that you gave in your generate_mapping function.
    """
    p = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    for i in positive_tests:
        if i == "stick-0":
            p[9] = "1"
        if i == "stick-1":
            p[8] = "1"
        if i == "stick-2":
            p[7] = "1"
        if i == "stick-3":
            p[6] = "1"
        if i == "stick-4":
            p[5] = "1"
        if i == "stick-5":
            p[4] = "1"
        if i == "stick-6":
            p[3] = "1"
        if i == "stick-7":
            p[2] = "1"
        if i == "stick-8":
            p[1] = "1"
        if i == "stick-9":
            p[0] = "1"
    poisoned = "".join(p)
    return int(poisoned, 2)
