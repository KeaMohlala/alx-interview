#!/usr/bin/python3

def isWinner(x, nums):
    # Helper function to generate a list of prime numbers up to n
    def sieve_of_eratosthenes(n):
        is_prime = [True] * (n + 1)
        p = 2
        primes = []
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
        return primes

    # Maximum number in nums to generate primes only once
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes available up to n
        prime_count = sum(1 for p in primes if p <= n)

        # If prime_count is odd, Maria wins; if even, Ben wins
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
