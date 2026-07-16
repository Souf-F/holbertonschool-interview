#!/usr/bin/python3

def isWinner(x, nums):
    """
    Determine who wins the most rounds of the Prime Game.

    Args:
        x (int): number of rounds
        nums (list): array of n values, one per round

    Returns:
        str: name of the player who won the most rounds ("Maria" or "Ben")
        None: if the winner cannot be determined
    """
    if x is None or nums is None or x <= 0 or len(nums) == 0:
        return None

    max_n = max(nums)
    if max_n < 2:
        sieve = []
    else:
        # Sieve of Eratosthenes up to max_n
        sieve = [True] * (max_n + 1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(max_n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, max_n + 1, i):
                    sieve[j] = False

    prime_count = [0] * (max_n + 1) if max_n >= 0 else []
    count = 0
    for i in range(max_n + 1):
        if i >= 2 and sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue
        primes_up_to_n = prime_count[n]
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
