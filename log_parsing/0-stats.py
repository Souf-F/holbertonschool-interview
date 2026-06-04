#!/usr/bin/python3
"""
Log parsing script that reads stdin and computes metrics.
"""

import sys
import re


def print_stats(file_size, status_codes):
    """Print statistics."""
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


def main():
    """Main function that processes log lines from stdin."""
    line_count = 0
    file_size = 0
    status_codes = {}

    pattern = (
        r'^\d+\.\d+\.\d+\.\d+ - \[.*?\] '
        r'"GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}

    try:
        for line in sys.stdin:
            match = re.match(pattern, line.strip())

            if match:
                code = int(match.group(1))
                size = int(match.group(2))

                if code in valid_codes:
                    file_size += size
                    status_codes[code] = status_codes.get(code, 0) + 1
                    line_count += 1

                    if line_count % 10 == 0:
                        print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
