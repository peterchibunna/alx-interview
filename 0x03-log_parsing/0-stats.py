#!/usr/bin/python3
"""
Module: 0x03. Log Parsing
"""
import sys


def print_stats(tf_size, s_codes):
    """Print the stats gathered
    """
    print('File size: {}'.format(tf_size), flush=True)
    for k, v in s_codes.items():
        if v > 0:
            print('{}: {}'.format(k, v), flush=True)


if __name__ == "__main__":
    total_file_size = 0
    status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }
    line_count = 0
    try:
        while True:

            for line in sys.stdin:
                line_count += 1
                # print(line_count)
                parts = line.split(' ')
                if len(parts) == 9:
                    file_size = parts[8]
                    total_file_size += int(file_size)
                    code = parts[7]
                    status_codes[code] += 1
                if line_count % 10 == 0:
                    print_stats(total_file_size, status_codes)
            # sys.stdin.flush()
            if line_count % 10 != 0:
                print_stats(total_file_size, status_codes)
            break
    except (KeyboardInterrupt, EOFError, StopIteration):
        print_stats(total_file_size, status_codes)
