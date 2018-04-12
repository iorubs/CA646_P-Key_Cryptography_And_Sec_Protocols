# El Gamal

### Practicals:

##### Practical 1. Implement the following routine:

```java
    Integer order(Integer, Integer∗, Integer)
    such that order(p, f, a) will return the order of a in the group Z*p
    where f is a list of the prime factors of p − 1. Ensure that your method
    works when f contains duplicates. For example, consider cases where p = 17.
```

##### Practical 2. Implement the following routine:

```java
    Integer findg(Integer, Integer∗)
    such that findg(p, f) will return a generator of Z∗p where p is a prime
    and f is a list of the prime factors of p − 1.
```

##### Practical 3. Implement the following routine:

```java
    (Integer, Integer) pair(Integer)
    such that pair(d) will return (p, a) containing a safe prime p with d bits and a generator a for Z∗p
```

##### Practical 4. A simple algorithm for finding log α^β is to compute α^0, α^1, α^2, ... until β is obtained.

```java
    Using this algorithm, implement the following routine:
    Integer log(Integer, Integer, Integer)
    such that log(p, a, x) will return log a^x in the cyclic group Z∗p where p is prime and a is a generator.
```

##### Practical 5. Implement ElGamal using the following routines:

```java
    (Integer, Integer, Integer, Integer) egKey(Integer)
    (Integer, Integer) egEnc(Integer, Integer, Integer, Integer)
    Integer egDec(Integer, Integer, Integer, Integer)

    such that:
      • egKey(s) will return a tuple (p, α, x, y) where p is a safe prime, α a generator, and x and y are the
      public and private components of the ElGamal key.
      • egEnc(p, α, y, m) will return (c1, c2)
      • egDec(p, x, c1, c2) will return m
```
