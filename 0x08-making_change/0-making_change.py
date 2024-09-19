#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given amount total
"""

def makeChange(coins, total):
    """
    Function to determine the fewest number of coins needed to meet total
    :param coins: List of the values of the coins in your possession
    :param total: The total amount
    :return: Fewest number of coins needed to meet the total, or -1 if total
             can't be met
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)
    
    count = 0
    for coin in coins:
        if total == 0:
            break
        # Get the number of coins of this denomination
        num_coins = total // coin
        count += num_coins
        # Decrease the total by the value of the coins used
        total -= num_coins * coin

    # If the total is not zero, it means we couldn't meet the total
    if total != 0:
        return -1

    return count
