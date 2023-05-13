#!/usr/bin/python3
"""
Module: 0x03. Log Parsing
"""
import re
import sys


def print_stats(tf_size, s_codes):
    """Print the stats gathered
    """
    print('File size: {}'.format(tf_size), flush=True)
    for status_code in sorted(s_codes.keys()):
        count = s_codes.get(status_code, 0)
        if count > 0:
            print('{}: {}'.format(status_code, count), flush=True)


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

    patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    try:
        while True:
            for line in sys.stdin:
                line_count += 1
                log_fmt = '{}\\-{}{}{}{}\\s*'.format(
                    patterns[0], patterns[1],
                    patterns[2], patterns[3],
                    patterns[4])
                resp_match = re.fullmatch(log_fmt, line)
                if resp_match is not None:
                    code = resp_match.group('status_code')
                    file_size = int(resp_match.group('file_size'))
                    # print(line_count)
                    # parts = line.split(' ')
                    # if len(parts) == 9:
                    #     file_size = parts[8]
                    total_file_size += int(file_size)
                    # code = parts[7]
                    status_codes[code] += 1
                if line_count % 10 == 0:
                    print_stats(total_file_size, status_codes)
            # sys.stdin.flush()
            if line_count % 10 != 0:
                print_stats(total_file_size, status_codes)
            break
    except (KeyboardInterrupt, EOFError, StopIteration):
        print_stats(total_file_size, status_codes)
    if line_count == 0:
        print_stats(total_file_size, status_codes)
