import sys
import argparse

from prime import *

# --- Helper Function ---
# Validates arguments to be positive integers
def check_positive_int(value):
    try:
        if int(value) <= 0:
            raise argparse.ArgumentTypeError(f"Value must be a positive integer above 0")
    except TypeError:
        raise argparse.ArgumentTypeError(f"Value must be a positive integer above 0")
    return int(value)

# --- Main driver ---
# Uses argparse to determine which function to run and pass their values
# As well as provide help/documentation in using prime_gen.py
def driver(*args, **kwargs):
    parser = argparse.ArgumentParser(description=
    """
    prime_gen.py is a script that produces prime numbers by two different methods:
    range: finds all the prime numbers from 1 to limit (inclusive)
    digits: prints a set of random prime numbers of a certain digit size
    """)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--range', '-r', dest='range', metavar='LIMIT', type=check_positive_int, nargs=1, default=None,
                        help="""
                        Finds all the prime numbers from 1 up to LIMIT (inclusive).
                        For example: -r 10 would output 2, 3, 5, 7
                        """)
    group.add_argument('--digits', '-d', dest='digits', metavar=('DIGITS', 'SIZE'), type=check_positive_int, nargs=2, default=None,
                        help="""
                        Prints a prime number with DIGITS amount of digits, and will continue to find SIZE amount of prime numbers of that digit size. DIGITS and SIZE must be positive integers.
                        For example: -d 10 5 would print [7768103059, 6872570119, 2456328697, 1585648489, 1313618821]
                        """)

    args = parser.parse_args()

    if args.range:
        range_1_n(args.range[0])
    else:
        digit_size(args.digits[0], args.digits[1])

if __name__ == "__main__":
    driver(*sys.argv)
