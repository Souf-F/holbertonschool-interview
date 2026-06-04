# 📊 Log Parsing

## 📋 Overview

Script that reads logs from stdin and displays statistics every 10 lines or on interruption (Ctrl+C).

## 🎯 Objective

Process a continuous stream of logs, validate format, extract relevant data and display cumulative metrics.

## 📥 Input

Logs in format: `<IP> - [<date>] "GET /projects/260 HTTP/1.1" <code> <size>`

Non-compliant lines are ignored.

## 📤 Output

**Every 10 valid lines:**
- Total file size
- Number of occurrences by status code (200, 301, 400, 401, 403, 404, 405, 500)
- Codes sorted in ascending order

## 🔑 Concepts Used

### Stdin/Stdout
- Reading from standard input continuously
- Writing to standard output

### Regular Expressions
- Format validation
- Extraction of capture groups (code and size)

### Dictionaries
- Storage of counters by status code
- Dynamic code management

### Exception Handling
- Try/Except to catch KeyboardInterrupt (Ctrl+C)
- Display stats before exit

### Loops and Conditionals
- Iteration over stdin
- Modulo to determine every 10th line

### Sorting
- Display codes in ascending order

## ⚙️ How It Works

1. Reads each line from stdin
2. Validates format with regex
3. If valid: extracts code and size
4. Accumulates data
5. Every 10 lines: displays statistics
6. On Ctrl+C: displays final statistics

## 📦 Dependencies

- `sys` - Access to stdin/stdout
- `re` - Regular expressions

## ✅ Key Points

- Executable script directly
- Not executed when imported
- Graceful interrupt handling
- Filtering of invalid codes
- Cumulative statistics
