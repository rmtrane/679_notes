#!/usr/bin/env python

import math
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help = "total number of items to choose from")
parser.add_argument("-k", type=int, help = "number of items to choose")
parser.add_argument("--log", action="store_true", help = "returns the log binomial coefficient")
parser.add_argument("--test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

def logfactorial(n, k = 0):
    '''Takes an integer n and calculates log(n!) = log(1) + log(2) + ... + log(n)

    >>> logfactorial(1)
    0.0
    >>> round(logfactorial(10),5)
    15.10441
    '''

    assert int(n) == n, 'Error: input should be an integer -- it is not!'
    assert n > 0, 'Error: input should be positive!'

    if k != None:
        assert int(k) == k, 'Error: input k should be an integer'
        assert k >= 0, 'Error: input k should be positive'

    result=0

    for i in range(k+1, n+1):
        result += math.log(i)

    return(result)


def choose(n,k, log = False):
    '''Takes two positive integers, n and k, and calculates n choose k.

    >>> choose(5,1)
    5
    >>> choose(5,3)
    10
    >>> choose(5,10)
    0
    '''

    assert int(n) == n, 'Error: inputs should be an integer -- n it is not!'
    assert n > 0, 'Error: inputs should be positive -- n is not'
    assert int(k) == k, 'Error: inputs should be an integer -- k is not!'
    assert n > 0, 'Error: input should be positive -- k is not'

    if n < k:
        return(0)
    else:
        result = logfactorial(n,k) - logfactorial(n-k)

    if not log:
        result = round(math.exp(result))

    return(result)

if not args.test and __name__ == '__main__':
    if args.n<=0:
        raise Exception("argument -n must be positive")
    if args.k<0:
        raise Exception("argument -k must be 0 positive")

if __name__ == '__main__':
    if args.test:
        print("Testing the module...")
        import doctest
        doctest.testmod()
        print("DONE!")
    else:
        print(choose(args.n, args.k, args.log))
