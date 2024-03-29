import sys
from secrets import randbelow
from rsa.practicals import expm, prime, fermat


def order(p, f, a):
    t = p - 1
    for pi in f:
        if expm(p, a, t // pi) == 1:
            t = t // pi

    return t


def findg(p, f):
    g = randbelow(p)
    while g < 1 or order(p, f, g) != p - 1:
        g = randbelow(p)

    return g


def pair(d):
    q = prime(d - 1)
    p = 2 * q + 1
    while len(bin(q)[2:]) < d - 1 or not fermat(p, 100):
        q = prime(d - 1)
        p = 2 * q + 1

    return (p, findg(p, [2, q]))


# find i s.t. (a ** i % p) == x
def log(p, a, x):
    i = 0
    while expm(p, a, i) != x:
        i += 1

    return i


def egKey(s):
    p, a = pair(s)
    x = randbelow(p - 1)
    while x < 1:
        x = randbelow(p - 1)

    y = expm(p, a, x)
    return (p, a, x, y)


def egEnc(p, a, y, m):
    if m < 0 or m >= p:
        raise Exception('m is outside range: 0 <= m < p')

    k = randbelow(p - 1)
    while k < 1:
        k = randbelow(p - 1)

    c1 = expm(p, a, k)
    c2 = m * expm(p, y, k) % p

    return (c1, c2)


def egDec(p, x, c1, c2):
    return expm(p, c1, (p - 1 - x)) * c2 % p


def main():
    m = 50
    p, a, x, y = egKey(100)
    print(f'message: {m}')
    c1, c2 = egEnc(p, a, y, m)
    print(f'encrypt: c1 {c1}, c2 {c2}')
    print("decrypt: ", egDec(p, x, c1, c2))


if 'run_eg' in sys.argv:
    main()
