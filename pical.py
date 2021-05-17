import random
import time
import math
import click
from multiprocessing import Pool

random.seed(time.time())

def rep(i):
    a = 0
    t = 0
    for _ in range(i):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x*x + y*y)
        t += 1
        if dist<= 1:
            a += 1
    return (a, t)

@click.command(help='Estimate Pi by throwing darts.')
@click.option('-t', '--threads', default=18, help='Number of threads.')
@click.option('-b', '--batch', default=100000, help='Batch size.')
def main(threads, batch):
    pool = Pool(threads)
    a = 0
    t = 0
    e = time.time()
    while True:
        res = [pool.apply_async(rep, (batch, )) for _ in range(1800)]
        for r in res:
            aa, tt= r.get()
            a += aa
            t += tt
            print("Estimated pi: {:.16f} time: {:8.2f} hit: {:20d} total: {:20d}".format(float(4 * a) / float(t), time.time() - e, a, t), end="\r", flush=True)

if __name__ == "__main__":
    main()