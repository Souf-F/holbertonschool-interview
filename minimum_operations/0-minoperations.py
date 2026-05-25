#!/usr/bin/python3
"""
Module pour calculer le nombre minimum d'opérations
nécessaires pour obtenir n caractères H dans un fichier.
"""


def minOperations(n):
    """
    Calcule le nombre minimum d'opérations (Copy All et Paste)
    pour obtenir exactement n caractères H.

    Args:
        n (int): Le nombre de caractères H souhaité

    Returns:
        int: Le nombre minimum d'opérations, ou 0 si impossible
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
