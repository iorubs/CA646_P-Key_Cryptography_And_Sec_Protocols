# RSA

### Practicals:

##### Practical 1. Use Euclid’s algorithm to implement the routine:

```java
    Integer gcd(Integer, Integer)
```

##### Practical 2. Use the Extended Euclidean Algorithm to implement the routine:

```java
    (Integer, Integer, Integer) gcde(Integer, Integer)
    where a call gcde(a, b) of this routine should return a tuple (g, x, y) of three integers such that:
    	• g = gcd(a, b)
    	• a × x + b × y = g
```

##### Practical 3. Implement the following routine:

```java
    Integer invm(Integer, Integer)
    such that invm(m, a) computes the inverse of a modulo m.
    	• Note that this routine will not always produce a result.
    	• If your programming language supports exceptions, then you should throw an exception if the
    inverse of a modulo m does not exist
```

##### Practical 4. Implement the following routine:

```java
    Integer divm(Integer, Integer, Integer)
    such that divm(m, a, b) computes ab^−1 mod m if it exists.
```

##### Practical 5. Using the square-and-multiply algorithm, implement the following routine:

```java
    Integer expm(Integer, Integer, Integer)
    such that expm(m, a, k) computes a^k modulo m.
```

##### Practical 6. Implement the following routine:

```java
    Integer∗ factors(Integer)
    such that factors(x) will return a list of integer values that are the factors of x. Note that if a prime p has a power e > 0 in the factorization of x, then p should appear e times in the result.
```

##### Practical 7. Implement the following routine:

```java
    Integer phi(Integer)
    such that phi(n) will return φ(n).
```

##### Practical 8. Implement the following routine:

```java
    Boolean fermat(Integer, Integer)
    such that fermat(x, t) will use Fermat’s algorithm to determine if x is prime
```

##### Practical 9. Implement the following routine:

```java
    Integer prime(Integer)
    such that prime(d) will use Fermat’s algorithm to generate a d-bit prime.
```

##### Practical 10. Implement the following routine:

```java
    Integer∗ efactors(Integer)
    that will determine the prime factors of an integer value n that is the product of two primes. This function should use a more efficient algorithm than trial division and should be capable of factoring numbers such as 709138557871512933443.
```

##### Practical 11. Implement RSA as the following routines:

```java
    (Integer, Integer, Integer) rsaKey(Integer)
    Integer rsaEnc(Integer, Integer, Integer)
    Integer rsaDec(Integer, Integer, Integer)
    such that:
    	• rsaKey(s) will generate an RSA key-pair (n,e,d) where n is an s-bit modulus
    	• rsaEnc(n, e, m) will return E(n,e)(m)
    	• rsaDec(n, d, c) will return D(n,d)(c)
```

##### Practical 12. Using efactors(), implement a routine:

```java
    String ecrack(Integer, Integer, Integer∗)
    such that ecrack(n, e, c) will decrypt an integer produced by rsaEnc() with the public key (n, e) without having access to the private exponent.
```
