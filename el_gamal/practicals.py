import sys
from secrets import randbelow
from rsa.practicals import expm, prime, fermat
from math import sqrt


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
        q = prime(d)
        p = 2 * q + 1

    return (p, findg(p, [2, q]))


def log(p, a, x):
    s = 1
    for i in range(0, p):
        s = (s * a) % p
        if s == x:
            return i + 1
    return -1


def baby_steps_giant_steps(p, a, b, N=None):
    if not N:
        N = 1 + int(sqrt(p))

    # Baby step table
    baby_steps = {}
    baby_step = 1
    for r in range(N + 1):
        baby_steps[baby_step] = r
        baby_step = baby_step * a % p

    # Giant steps
    giant_stride = pow(a, (p-2) * N, p)
    giant_step = b
    for q in range(N + 1):
        if giant_step in baby_steps:
            return q * N + baby_steps[giant_step]
        else:
            giant_step = giant_step * giant_stride % p
    return "No Match"


def egKey(s):
    p, a = pair(s)
    x = randbelow(p - 1)
    while x < 1:
        x = randbelow(p - 1)

    y = expm(p, a, x)
    return (p, a, x, y)


def egEnc(p, a, y, m):
    k = randbelow(p - 1)
    while k < 1:
        k = randbelow(p - 1)

    c1 = expm(p, a, k)
    c2 = m * expm(p, y, k)

    return (c1, c2)


def egDec(p, x, c1, c2):
    return (c1 ** (p - 1 - x)) * c2 % p


def main():
    # print(log(p, g, 2))
    # print(baby_steps_giant_steps(p, g, 2))
    m = 27
    p, a, x, y = egKey(10)
    print(f'message: {m}')
    c1, c2 = egEnc(p, a, y, m)
    print(f'encrypt: c1 {c1}, c2 {c2}')
    print("decrypt: ", egDec(p, x, c1, c2))


if 'run_eg' in sys.argv:
    main()
