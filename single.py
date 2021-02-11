import sys
import random
import time


def dice(n=1): return list(map(lambda _: random.randrange(6)+1, [None]*n))


start = time.time()
total = int(sys.argv[1]) if len(sys.argv) == 2 else 10

data = list(map(dice, [5] * total))
print("{0:,} dices thrown ({1}sec)".format(
    total, round((time.time()-start), 3)))

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
