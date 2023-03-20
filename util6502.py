# Simple 6502 Emulator
# (CC-BY) R Mark Adams, Ph.D. 2023

# Utilities for the programs to use

def getopts(argv):
    """ Returns the options from the command-line arguments

    :param argv: The normal sys.argv result
    :return: A dictionary of the command-line options (i.e. the '-<?>' and the following word

    NOTE:
        If the -<?> is followed by another -<?>, it will return a '' for the option content.  It will also
        do this id the -<?> is the last argument on the command line.
    """
    opts = {}
    while argv:
        if argv[0][0] == '-':
            if len(argv) > 1:
                if argv[1][0] != '-':
                    opts[argv[0]] = argv[1]
                else:
                    opts[argv[0]] = ''
            else:
              opts[argv[0]] = ''
        argv = argv[1:]
    return opts

def set_bit(v, index, x):
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value.

    :param v: number to set the bit of
    :param index: the bit to set in <v>
    :param x: the bit-value to set (1 if truth-y, 0 otherwise)
    :return: <v> with the bit set as above

    Usage:
    >>> set_bit(7, 3, 1)
    15
    >>> set_bit(set_bit(7, 1, 0), 3, 1)
    13
    """
    mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
    v &= ~mask          # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask         # If x was True, set the bit indicated by the mask.
    return v            # Return the result, we're done.

def testBit(int_type, offset):
    """ testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.

    Usage:
    >>> set_bit(7, 3, 1)
    15
    >>> bool(testBit(4,1))
    False
    >>> bool(testBit(4,2))
    True
    """
    mask = 1 << offset
    return(int_type & mask)

# def setBit(int_type, offset):
#     """ setBit() returns an integer with the bit at 'offset' set to 1."""
#     mask = 1 << offset
#     return(int_type | mask)

def clearBit(int_type, offset):
    """ clearBit() returns an integer with the bit at 'offset' cleared.

    >>> clearBit(7, 1)
    5
    """
    mask = ~(1 << offset)
    return(int_type & mask)

def toggleBit(int_type, offset):
    """toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0."""
    mask = 1 << offset
    return(int_type ^ mask)