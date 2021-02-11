import sys
import random
import time
import itertools
from multiprocessing import Pool


def dice(n=1): return list(map(lambda _: random.randrange(6)+1, [None]*n))
def flatten(ls): return list(itertools.chain.from_iterable(ls))
def throw5(n): return list(map(dice, [5]*int(n)))


if __name__ == '__main__':
    start = time.time()
    total = int(sys.argv[1]) if len(sys.argv) >= 2 else 10

    NUM_THREADS = int(sys.argv[2]) if len(sys.argv) == 3 else 2
    params = [total/NUM_THREADS] * NUM_THREADS
    with Pool(processes=NUM_THREADS) as p:
        results = p.map(func=throw5, iterable=params)

    data = flatten(results)
    print("{0:,} dices thrown with {1} threads ({2}sec)".format(
        total, NUM_THREADS, round((time.time()-start), 3)))

    count = 0
    dist = {}
    start = time.time()
    for line in data:
        hs = "_".join(map(str, line))
        p = dist.get(hs)
        dist[hs] = 0 if p is None else p+1
        sl = sorted(line)
        matched = sl == [1, 1, 2, 2, 4]
        count += 1 if matched else 0
    t = round(time.time()-start, 3)
    print("{0}/{1}={2} ({3}sec)".format(count,
                                        total, count/total, t))
    print(len(dist))
