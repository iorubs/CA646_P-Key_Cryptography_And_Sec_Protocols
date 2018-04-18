from math import sqrt

# find i s.t. (a ** i % p) == x
def baby_steps_giant_steps(p, a, b, N=None):
    if N is None:
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
    return -1
