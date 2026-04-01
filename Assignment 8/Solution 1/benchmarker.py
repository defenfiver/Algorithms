from old import blend as old
from new import blend as new
import timeit

print("It started")
oldTime = timeit.timeit(old, number=100)
print(f'The new solution took {oldTime} seconds ({oldTime/100} per)')

newTime = timeit.timeit(new, number=100)
print(f'The new solution took {newTime} seconds ({newTime/100} per)')
