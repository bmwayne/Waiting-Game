import time
import random

def waitinggame():
    target = random.randint(2,4)
    print("\n your target is {} seconds".format(target))
    print(input('-------- Press Enter to begin --------'))

    start = time.perf_counter()

    print(input('-------- Press Enter again to stop --------'))

    elapsed = time.perf_counter() - start

    if elapsed == target:
        print('You hit the spot!')
    elif elapsed < target:
        print('You were {0:.3f} seconds fast'.format(target - elapsed))
    elif elapsed > target:
        print('You were {0:.3f} seconds slow'.format(elapsed - target))

while True:
    waitinggame()
