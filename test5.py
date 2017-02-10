def print_asterisks(num):
    print ''.join('*' for i in xrange(num))

def histogram(s):
    map(print_asterisks, s)

def main():
    # Test inputs
    print histogram([14,47,15])


if __name__ == "__main__":
    import sys
    sys.exit(main())