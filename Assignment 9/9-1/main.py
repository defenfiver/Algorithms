bestSoFar = None
allSkills = None


class Person:
    def __init__(self, skills: list, number_skills: int, id: int):
        self.skills = skills
        self.known_skills = number_skills
        self.id = id

    def __str__(self):
        return f'{self.skills}'


class DecisionState:
    def __init__(self, undecided: list[Person], uncovered, inc=None, exc=None, ski_cov=None, cts=0):
        self.undecided = undecided
        self.skills_uncovered = list(uncovered)
        self.included = [] if inc is None else inc
        self.excluded = [] if exc is None else exc
        self.skills_covered = set() if ski_cov is None else set(ski_cov)
        self.size = cts

    def copy(self):
        return DecisionState(self.undecided[:], self.skills_uncovered[:], self.included[:], self.excluded[:], list(self.skills_covered)[:], self.size)

    def includePerson(self, person):
        self.undecided.remove(person)
        self.included.append(person)
        active_skills = person.skills
        for j in active_skills:
            if j in self.skills_uncovered:
                self.skills_uncovered.remove(j)
                self.skills_covered.add(j)
        self.size += 1
        return self

    def excludePerson(self, person):
        self.undecided.remove(person)
        self.excluded.append(person)
        return self

    def hypoIncludeAll(self):
        global allSkills
        tmp_skills = self.skills_covered.copy()
        for j in self.undecided:
            for k in j.skills:
                tmp_skills.add(k)
        if allSkills == tmp_skills:
            return True
        return False

    def hypoInclude(self, person):
        tmp = self.copy()
        return tmp.includePerson(person)


def subsetSimp(cur_state: DecisionState):
    unDec = cur_state.undecided[:]
    for j in unDec:  # If all the skills are already included, exclude that person
        if set(j.skills) <= set(cur_state.skills_covered):
            cur_state.excludePerson(j)

    unDec = cur_state.undecided[:]
    unDec.sort(key=lambda a: a.known_skills, reverse=True)
    for j in range(len(unDec)):  # If anyone is a subset of a person with more skills than them, exclude them
        if unDec[j] in cur_state.undecided:
            for k in unDec[j+1:]:
                if unDec[j].known_skills != k.known_skills:
                    if k in cur_state.undecided:
                        if set(k.skills) <= set(unDec[j].skills):
                            cur_state.excludePerson(k)
    return cur_state


def onlySimp(cur_state: DecisionState):
    unc = cur_state.skills_uncovered[:]
    for j in unc:
        if j in cur_state.skills_uncovered:
            count = 0
            toInc = None
            for k in cur_state.undecided:
                if count > 1:
                    break
                if j in k.skills:
                    count += 1
                    toInc = k
            if count == 1:
                cur_state.includePerson(toInc)
    return cur_state


def everySimp(cur_state: DecisionState):
    if len(cur_state.skills_uncovered) > 1:
        for j in range(len(cur_state.skills_uncovered)-1, -1, -1):
            count = 0
            for k in cur_state.undecided:
                if cur_state.skills_uncovered[j] in k.skills:
                    count += 1
            if count == len(cur_state.undecided):
                cur_state.skills_uncovered.pop(j)
    return cur_state


def pick_person(cur_state: DecisionState):
    return cur_state.undecided[0]


def solve(cur_state: DecisionState):
    global bestSoFar
    subsetSimp(cur_state)
    onlySimp(cur_state)
    everySimp(cur_state)
    team_size = cur_state.size

    if not cur_state.undecided or not cur_state.skills_uncovered:
        if not cur_state.skills_uncovered:
            if bestSoFar.size >= team_size:
                bestSoFar = cur_state
            return cur_state
        else:
            return None
    if team_size >= bestSoFar.size - 1:
        return bestSoFar
    if not cur_state.hypoIncludeAll():
        return None
    next_person = pick_person(cur_state)

    inc_state = cur_state.copy().includePerson(next_person)
    inc_solve = solve(inc_state)

    exc_state = cur_state.copy().excludePerson(next_person)
    exc_solve = solve(exc_state)

    if inc_solve is None and exc_solve is None:
        return None
    elif inc_solve is None:
        return exc_solve
    elif exc_solve is None:
        return inc_solve
    else:
        return inc_solve if inc_solve.size <= exc_solve.size else exc_solve


def approximate(cur_state: DecisionState):
    subsetSimp(cur_state)
    onlySimp(cur_state)
    everySimp(cur_state)
    for j in cur_state.undecided[:]:
        cur_state.includePerson(j)
    return cur_state


if __name__ == "__main__":
    num_candidates, num_skills = input().split(" ")
    num_candidates = int(num_candidates)
    num_skills = int(num_skills)
    all_skills = set(input().split(" "))
    allSkills = all_skills
    people = []
    for i in range(num_candidates):
        tmpX = int(input())
        tmpY = input().split(" ")
        if tmpX != 0:
            people.append(Person(tmpY, tmpX, i))

    init_state = DecisionState(people, all_skills)
    init_state.undecided.sort(key=lambda a: a.known_skills, reverse=True)
    bestSoFar = approximate(init_state.copy())
    sol = solve(init_state)
    print(sol.size)
