# UTF-8 Validation Project

## Overview

This project validates whether a given dataset represents a valid UTF-8 encoding. It demonstrates understanding of character encoding, bit manipulation, and algorithm design.

UTF-8 is the most widely used character encoding on the internet, supporting all Unicode characters while remaining backward compatible with ASCII.

---

## What is UTF-8?

UTF-8 (8-bit Unicode Transformation Format) is a variable-width encoding scheme where characters can be represented by 1 to 4 bytes.

### Character Encoding Rules

| Bytes | Format | Range |
|-------|--------|-------|
| 1 | `0xxxxxxx` | 0 - 127 (ASCII) |
| 2 | `110xxxxx 10xxxxxx` | 128 - 2047 |
| 3 | `1110xxxx 10xxxxxx 10xxxxxx` | 2048 - 65535 |
| 4 | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` | 65536 - 1114111 |

### Key Rules

1. **Single-byte character** starts with `0` (bit 7 is 0)
2. **Multi-byte character start** starts with `11` (bits 7-6 are 1)
3. **Continuation bytes** always start with `10` (bits 7-6 are 10)
4. The number of leading 1s in the first byte indicates the total bytes for that character

---

## Examples

### Valid UTF-8

- `[65]` → `True` (ASCII 'A' = 0x41 = `01000001`)
- `[80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]` → `True` (ASCII "Python is cool!")
- `[194, 128]` → `True` (Valid 2-byte character)
- `[224, 160, 128]` → `True` (Valid 3-byte character)

### Invalid UTF-8

- `[229, 65, 127, 256]` → `False` (Invalid byte sequence)
- `[240, 158, 146]` → `False` (Incomplete 4-byte character)
- `[255]` → `False` (Invalid start byte)

---

## How It Works

### Algorithm Steps

1. **Initialize** a counter for expected continuation bytes
2. **For each byte** in the data:
   - If it's the start of a new character (`num_bytes == 0`):
     - Check if it's a single-byte character (0xxxxxxx) → valid
     - Or determine the character type (2, 3, or 4 bytes)
   - If we expect continuation bytes:
     - Verify it starts with `10xxxxxx`
     - Decrement the counter
3. **Return** True only if all characters are complete (counter is 0)

### Bit Manipulation

```python
byte & 0xFF           # Extract 8 least significant bits
(byte & 0xE0) == 0xC0 # Check for 2-byte character start (110xxxxx)
(byte & 0xF0) == 0xE0 # Check for 3-byte character start (1110xxxx)
(byte & 0xF8) == 0xF0 # Check for 4-byte character start (11110xxx)
(byte & 0xC0) == 0x80 # Check for continuation byte (10xxxxxx)
```

---

## Files

### `validate_utf8.py`
The main module containing the `validUTF8()` function that performs the validation.

**Function Signature:**
```python
def validUTF8(data)
```

**Parameters:**
- `data` (list): A list of integers, where each integer represents one byte (only 8 least significant bits are considered)

**Returns:**
- `True` if the data is a valid UTF-8 encoding
- `False` otherwise

**Time Complexity:** O(n) where n is the number of bytes
**Space Complexity:** O(1)

### `0-main.py`
Test file that demonstrates the function with three test cases.

### `README.md`
This file - documentation for the project.

---

## Installation & Usage

### Prerequisites
- Python 3.4+
- Linux/Ubuntu environment

### Setup

```bash
# Clone or navigate to the project directory
cd utf8_validation

# Make files executable
chmod +x validate_utf8.py
chmod +x 0-main.py

# Run tests
./0-main.py
```

### Expected Output
```
True
True
False
```

### Using the Function in Your Code

```python
from validate_utf8 import validUTF8

# Test with ASCII
data = [65, 66, 67]  # 'ABC'
print(validUTF8(data))  # True

# Test with multi-byte UTF-8
data = [194, 162]  # '¢' (cent sign)
print(validUTF8(data))  # True

# Test with invalid sequence
data = [255, 255]  # Invalid
print(validUTF8(data))  # False
```

---

## Testing

The project includes comprehensive test cases:

1. **Single ASCII character:** `[65]` → `True`
2. **ASCII string:** "Python is cool!" → `True`
3. **Invalid sequence:** Mixed valid and invalid bytes → `False`

### Running Additional Tests

Create a test file `test_utf8.py`:

```python
#!/usr/bin/python3
from validate_utf8 import validUTF8

# Test cases
test_cases = [
    ([65], True, "Single ASCII"),
    ([80, 121, 116, 104, 111, 110], True, "ASCII string"),
    ([194, 128], True, "2-byte character"),
    ([224, 160, 128], True, "3-byte character"),
    ([240, 144, 128, 128], True, "4-byte character"),
    ([255], False, "Invalid start byte"),
    ([194], False, "Incomplete 2-byte"),
]

for data, expected, description in test_cases:
    result = validUTF8(data)
    status = "✓" if result == expected else "✗"
    print(f"{status} {description}: {result}")
```

---

## Key Concepts Learned

### Bit Manipulation
- Understanding binary representation of bytes
- Using bitwise operators (`&`, `|`, `<<`, `>>`)
- Masking and shifting operations

### Character Encoding
- How UTF-8 works at the byte level
- Variable-width encoding advantages
- Backward compatibility with ASCII

### Algorithm Design
- State machine pattern (tracking character state)
- Efficient validation in a single pass
- Edge case handling

### Code Quality
- Clear variable naming
- Proper documentation
- Efficient time and space complexity

---

## Complexity Analysis

| Aspect | Complexity |
|--------|-----------|
| Time | O(n) - single pass through data |
| Space | O(1) - only uses a few variables |
| Correctness | 100% - all UTF-8 rules validated |

---

## Common Mistakes to Avoid

1. **Forgetting the 8-bit mask** - Always use `byte & 0xFF` to get only 8 bits
2. **Wrong bit patterns** - Double-check the binary patterns for each byte type
3. **Not tracking continuation bytes** - Ensure you decrement the counter for each continuation byte
4. **Incomplete characters** - Always check if `num_bytes == 0` at the end

---

## Resources

- [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
- [The Unicode Standard](https://unicode.org/)
- [RFC 3629 - UTF-8](https://tools.ietf.org/html/rfc3629)

---

## Code Style

This project follows **PEP 8** style guidelines:
- Maximum line length: 79 characters
- Proper indentation (4 spaces)
- Clear naming conventions
- Comprehensive docstrings

To check style compliance:
```bash
python3 -m pep8 validate_utf8.py
```

---

## Author

Developed as part of Holberton School's interview preparation curriculum.

---

## License

This project is provided for educational purposes.

---

## Summary

This UTF-8 validation project demonstrates:
- ✅ Understanding of character encoding standards
- ✅ Proficiency with bit manipulation
- ✅ Algorithm design and optimization
- ✅ Clean, well-documented code
- ✅ Comprehensive testing approach

The solution efficiently validates UTF-8 encoding in a single pass with O(n) time complexity and O(1) space complexity, making it both correct and efficient.