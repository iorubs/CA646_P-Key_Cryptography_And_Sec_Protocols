import hashlib
import sys
from secrets import randbelow
from rsa.practicals import expm, invm, gcd
from el_gamal.practicals import egKey


def addSimple(m, k, x):
    redundancy = ((1 << k) - 1) << m
    return x + redundancy


def removeSimple(m, k, x):
    redundancy = ((1 << k) - 1) << m
    return x - redundancy


def okSimple(m, k, x):
    redundancy = (1 << k) - 1
    return (x >> m) == redundancy


def rsaRecSignature(n, d, m, k):
    m_len = len(bin(m)[2:])
    return expm(n, addSimple(m_len, k, m), d)


def rsaRecRecovery(n, s, e, k):
    x = expm(n, s, e)
    m_len = len(bin(x)[2:]) - k
    return removeSimple(m_len, k, x)


def rsaRecVerification(m, n, s, e, k):
    return okSimple(len(bin(m)[2:]), k, expm(n, s, e))


def rsaRecValidate(m, n, s, e, k):
    rec_m = rsaRecRecovery(n, s, e, k)
    return rsaRecVerification(m, n, s, e, k) and m == rec_m


def rsaAppSignature(n, d, m):
    m = hashlib.sha1(str(m).encode('utf-8'))
    sha1 = int(m.hexdigest(), 16)
    return expm(n, sha1, d)


def rsaAppValidate(n, s, e, m):
    m = hashlib.sha1(str(m).encode('utf-8'))
    return int(m.hexdigest(), 16) == expm(n, s, e)


def addWeak(x):
    return (x << 8) + 0xFF


def removeWeak(x):
    return x >> 8


def okWeak(x):
    return (x & 0xFF) == 0xFF


def egSignature(p, m, a, x):
    # if m < 0 or m >= p - 1:
    #     raise Exception('m is outside range: 0 <= m < p-1')

    k = randbelow(p - 1)
    while k < 1 or gcd(k, p - 1) != 1:
        k = randbelow(p - 1)

    r = expm(p, a, k)
    s = invm(p - 1, k) * (m - x * r) % (p - 1)
    return (r, s)


def egVerification(p, m, a, r, s, y):
    if r < 1 or r > p - 1:
        return False

    v1 = (expm(p, y, r) * expm(p, r, s)) % p
    v2 = expm(p, a, m)
    return v1 == v2


def egSignatureSha1(p, m, a, x):
    sha1 = hashlib.sha1(str(m).encode('utf-8'))
    digest = int(sha1.hexdigest(), 16)
    return egSignature(p, digest, a, x)


def egVerificationSha1(p, m, a, r, s, y):
    sha1 = hashlib.sha1(str(m).encode('utf-8'))
    digest = int(sha1.hexdigest(), 16)
    return egVerification(p, digest, a, r, s, y)


def main():
    m = 27
    p, a, x, y = egKey(5)
    r, s = egSignature(p, m, a, x)
    print('ElGamal simple validation:', egVerification(p, m, a, r, s, y))

    m = "Some random stuff"
    r, s = egSignatureSha1(p, m, a, x)
    print('ElGamal sha1 validation:', egVerificationSha1(p, m, a, r, s, y))


if 'run_ds' in sys.argv:
    main()
