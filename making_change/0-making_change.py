#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
        coins: List of coin denominations
        total: Target amount

    Returns:
        Fewest number of coins needed, or -1 if impossible
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                if dp[amount - coin] != float('inf'):
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]
