#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determines the winner of a prime number game between Maria and Ben.

    In this game, given a set of consecutive integers starting from 1 up to n, 
    Maria and Ben take turns choosing a prime number from the set and removing 
    it and its multiples. Maria always plays first. The player who cannot make a 
    move loses. Both players play optimally.

    Args:
        x (int): The number of rounds played.
        nums (List[int]): An array of integers where each element n represents the 
                          upper limit of the set of consecutive integers (1 to n) for that round.

    Returns:
        str or None: The name of the player ('Maria' or 'Ben') who won the most rounds. 
                     If there is a tie, returns None.

    Example:
        >>> isWinner(3, [4, 5, 1])
        'Ben'
    
    Notes:
        - This function assumes that `n` (the upper limit in `nums`) will not exceed 10,000.
        - Both players play optimally, meaning they will always make moves that maximize their chance of winning.

    """
    # Helper function to generate a list of prime numbers up to n
    def sieve_of_eratosthenes(n):
        """
        Generates all prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.

        Args:
            n (int): The upper limit up to which primes are generated.

        Returns:
            List[int]: A list of prime numbers up to the number n.
        
        Example:
            >>> sieve_of_eratosthenes(10)
            [2, 3, 5, 7]
        """
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
