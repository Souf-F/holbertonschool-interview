# Island Perimeter
 
A short technical interview project (Holberton School) focused on grid traversal algorithms in Python.
 
## Description
 
This project implements a function that calculates the perimeter of an island described in a 2D grid, where `0` represents water and `1` represents land.
 
## Requirements
 
- Editors: `vi`, `vim`, `emacs`
- Interpreted on Ubuntu 14.04 LTS with `python3` (3.4.3)
- Files start with `#!/usr/bin/python3` and end with a new line
- Code follows `PEP 8` style
- No imports allowed
- All modules and functions are documented
- All files are executable
## Task
 
### 0. Island Perimeter
 
`0-island_perimeter.py` — contains `island_perimeter(grid)`, which returns the perimeter of the island in `grid`.
 
**Rules for the grid:**
- Rectangular, width/height ≤ 100
- Fully surrounded by water
- Exactly one island (or none)
- No lakes inside the island
**Example:**
```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
island_perimeter(grid)  # 12
```
 
## Author
 
Soufiane Filali — [Souf-F](https://github.com/Souf-F)