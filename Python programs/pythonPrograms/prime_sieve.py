# Prime Number Generator (Sieve of Eratosthenes)
def sieve(n):
    primes = [True] * (n+1)
    primes[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

if __name__ == "__main__":
    n = int(input("Generate primes up to: "))
    print(sieve(n))
