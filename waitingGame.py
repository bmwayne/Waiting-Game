import time
import random

def waitinggame():
    target = random.randint(2,4)
    print("\n your target is {} seconds".format(target))
    print(input('-------- Press Enter to begin --------'))

    start = time.perf_counter()

    print(input('-------- Press Enter again to stop --------'))

    elapsed = time.perf_counter() - start