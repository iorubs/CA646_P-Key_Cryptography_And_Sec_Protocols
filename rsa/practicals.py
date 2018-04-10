# -*- coding: utf-8 -*-

import sys
from math import sqrt
from secrets import randbelow


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def gcde(a, b):
    if b == 0:
        return (a, 1, 0)

    g, x, y = gcde(b, a % b)
    return (g, y, x - (a // b) * y)


def invm(m, a):
    g, x, _ = gcde(a, m)

    if g != 1:
        raise Exception(f'Inverse of {a} modulo {m} does not exist!')

    return x % m


def divm(m, a, b):
    return (invm(m, b) * a) % m


def expm(m, a, k):
    y = 1
    # Skip 0b at the start of bin numbers
    for x in bin(k)[2:]:
        y = (y * y) % m

        if x == '1':
            y = (y * a) % m

    return y


def factors(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return factors(i) + factors(x // i)

    return [x]


def phi(n):
    coprimes = 0
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            coprimes += 1
    return coprimes


def randint(n, m):
    if n >= m:
        raise Exception('n must be smaller than m')

    rand = randbelow(m)
    while rand < n:
        rand = randbelow(m)

    return rand


def fermat(n, t):
    if n <= 1:
        return False
    elif n < 3:
        return True

    for i in range(0, t):
        a = randint(2, n - 1)
        if expm(n, a, n - 1) != 1:
            return False

    return True


def prime(d):
    p = randint(1 << (d - 1), 1 << d)
    while not fermat(p, 100):
        p = randint(1 << (d - 1), 1 << d)

    return p


def efactors(n):
    def f(x):
        return x**2 + 1

    x = randint(0, n)
    y = x
    d = 1
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(abs(x-y), n)

    return d


def rsaKey(s):
    p = prime(s // 2)
    q = prime(s // 2)
    while q == p:
        q = prime(s // 2)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = randint(2, phi_n)
    while gcd(e, phi_n) != 1:
        e = randint(2, phi_n)

    d = invm(phi_n, e)

    return (n, e, d)


def rsaEnc(n, e, m):
    return expm(n, m, e)


def rsaDec(n, d, c):
    return expm(n, c, d)


def ecrack(n, e, c):
    p = efactors(n)
    q = n // p
    d = invm((p - 1) * (q - 1), e)
    return rsaDec(n, d, c)


def main():
    # Increase recursion limit if needed.
    sys.setrecursionlimit(2000)

    print('Max word size:', sys.maxsize, 'bits.')
    print('Recursion limit', sys.getrecursionlimit())

    m = 27
    s = 2000
    print('Message:', m, 'Modulus length:', s)

    n, e, d = rsaKey(s)
    print('Modulus:', n, '\nExponent e:', e, '\nExponent d:', d)

    c = rsaEnc(n, e, m)
    print('Cyphertext:', c)

    print('Decryption result: ', rsaDec(n, d, c))


if 'run_rsa' in sys.argv:
    main()
