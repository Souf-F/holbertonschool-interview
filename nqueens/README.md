---

## 📈 Complexity

| Metric | Value |
|--------|-------|
| **Time Complexity** | O(N!) |
| **Space Complexity** | O(N) |
| **N=4** | 2 solutions |
| **N=8** | 92 solutions |
| **N=10** | 724 solutions |

---

## 💻 Code Structure

```python
is_safe(board, row, col, n)
├─ Checks if queen placement is valid
├─ Checks column conflicts
└─ Checks diagonal conflicts

solve_nqueens(board, row, n, solutions)
├─ Recursive backtracking function
├─ Base case: all queens placed
└─ Recursive case: try each column

nqueens(n)
├─ Initialize empty board
└─ Call solve_nqueens()

main()
├─ Validate input
└─ Print solutions
```

---

## 🧪 Testing

```bash
# Valid cases
./0-nqueens.py 4
./0-nqueens.py 8

# Error cases
./0-nqueens.py        # Missing argument
./0-nqueens.py abc    # Not a number
./0-nqueens.py 3      # N too small
./0-nqueens.py -5     # Negative number
```

---

## ✅ Requirements

- Python 3.4.3+
- Ubuntu 14.04 LTS
- PEP 8 compliant
- Only `sys` module allowed
- File must be executable

---

## 🎓 Key Concepts

### Backtracking
Solving a problem by trying all possible solutions, abandoning paths that fail early.

### Board Representation
Array where `board[i] = column_position` of queen in row i.

### Diagonal Check
Two queens are on same diagonal if:
- `abs(row1 - row2) == abs(col1 - col2)`

---

## 📚 Resources

- [N Queens Problem - Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
- [Backtracking Algorithm](https://en.wikipedia.org/wiki/Backtracking)
- [Queen Movement - Chess Rules](https://en.wikipedia.org/wiki/Queen_(chess))

---

**Difficulty:** Amateur  
**Author:** Holberton School  
**Last Updated:** 2026-06-17
