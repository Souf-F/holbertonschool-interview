# 🔺 Pascal's Triangle

## 📋 Overview

Module that generates Pascal's Triangle of n rows.

## 🎯 Objective

Create a data structure representing Pascal's Triangle where each element is the sum of the two elements above it.

## 📥 Input

An integer n representing the number of rows.

## 📤 Output

List of lists of integers representing Pascal's Triangle, empty list if n ≤ 0.

## 🔑 Concepts Used

### List of Lists
- 2D data structure to represent triangle
- Nested lists for each row

### Nested Loops
- Outer loop: iterate through rows
- Inner loop: calculate elements in each row

### Index Access
- Accessing previous row elements
- Building current row from previous row

### List Append
- Adding elements to current row
- Adding completed rows to triangle

### Mathematical Relationships
- Element = sum of two elements above
- Pattern recognition for triangle edges (always 1)

## ⚙️ How It Works

1. Validates n > 0
2. Initializes triangle with first row [1]
3. For each row i from 1 to n-1:
   - Start row with 1
   - For each internal position: add sum of two elements above
   - End row with 1
   - Add completed row to triangle
4. Returns complete triangle

## 💡 Logic

Pascal's Triangle property: Each element equals the sum of the two elements diagonally above it.

Edge elements (first and last) are always 1.

## ✅ Key Points

- Handles edge cases (n ≤ 0)
- Efficient by using previously calculated rows
- O(n²) time complexity
- O(n²) space complexity
- Correct index calculations for row access
