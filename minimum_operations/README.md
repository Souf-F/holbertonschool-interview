# 📝 Minimum Operations

## 📋 Overview

Module that calculates the minimum number of operations (Copy All and Paste) needed to obtain exactly n characters H in a file.

## 🎯 Objective

Find the minimum number of operations to go from 1 character H to n characters H using only Copy All and Paste.

## 📥 Input

An integer n representing the desired number of H characters.

## 📤 Output

Minimum number of operations, or 0 if impossible (n ≤ 1).

## 🔑 Concepts Used

### Prime Factorization
- Decomposition of a number into prime factors
- Identification of successive divisors

### Greedy Algorithm
- Attempt with smallest divisor first
- Optimization through repeated division

### Nested Loops
- Outer loop: iteration over divisors
- Inner loop: division by same divisor while possible

### Modulo and Integer Division
- Divisibility check with modulo
- Euclidean division with //

### Algorithm Optimization
- Progressive problem reduction
- Accumulation of minimum operations

## ⚙️ How It Works

1. Validates that n > 1
2. Initializes operations counter to 0
3. Starts with divisor 2
4. While n > 1:
   - If divisor divides n: add divisor to operations and divide n
   - Else: try next divisor
5. Returns total operations

## 💡 Logic

Each prime factor p represents p operations (1 Copy All + p-1 Paste) to multiply by p.

Sum of all prime factors = minimum number of operations.

## ✅ Key Points

- Handles edge cases (n ≤ 1)
- No unnecessary calculations through division
- O(√n) complexity
- Mathematical approach based on number theory
