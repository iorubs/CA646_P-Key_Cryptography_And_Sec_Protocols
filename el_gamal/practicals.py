from secrets import randbelow
from rsa.practicals import factors, expm, prime, fermat


def order(p, f, a):
    t = p - 1
    for pi in f:
        if expm(p, a, t // pi) == 1:
            t = t // pi

    return t


def findg(p, f):
    g = randbelow(p)
    while g == 0 or order(p, f, g) != p - 1:
        g = randbelow(p)

    return g


def pair(d):
    q = prime(d)
    p = 2 * q + 1
    while len(bin(q)[2:]) < d // 2 or not fermat(p, 100):
        q = prime(d // 2)
        p = 2 * q + 1

    return (p, findg(p, [2, q]))

def log(p, a, x):
    i = 0
    log = a ** 0
    while log < x:

print(pair(20))
