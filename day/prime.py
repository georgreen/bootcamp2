import math
def prime_test(n, primeList = []):
    '''
    input: n integer
    output: boolean True if prime false otherwise
    '''
    if n < 2:
       return False
    for prime in primeList:
        if n % prime == 0:
            return False
        if math.sqrt(n) < prime:
            break
    return True

def prime_numbers(n):
    '''
    input: n integer
    output: a list, containing prime numbers in range(0,n)
    '''
    pass

    
import unittest
class test_prime_test(unittest.TestCase):
    pass

class test_prime_numbers(unittest.TestCase):
    pass
