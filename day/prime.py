import math
def prime_test(n, primeList = []):
    '''
    input: n integer
    output: boolean True if prime false otherwise
    '''
    if n < 2:
       return False
    elif n == 2:
       return True

    for prime in primeList:
        if n % prime == 0:
            return False
        if int(math.sqrt(n)) < prime:
            return True
    return False

def prime_numbers(n):
    '''
    input: n integer
    output: a list, containing prime numbers in range(0,n)
    '''
    pass


import unittest
class test_prime_test(unittest.TestCase):
    '''
    Unit test for prime_test
    Test Strategy: egde cases : 0, 1
                   special case : 2
                   negtives : any int that's negative
                   positive : any int that's postive
    coverage : selctive choose to cover major areas not full catesian
    '''
    def test_less_than_two(self):
        '''
        test edge case 1
        '''
        self.assertEqual(False, prime_test(1))

    def test_zero(self):
        '''
        test edge case 0
        '''
        self.assertEqual(False, prime_test(0))

    def test_two(self):
        '''
        test edge case 2
        '''
        self.assertEqual(True, prime_test(2,))

    def test_postive_numbers(self):
        '''
        test postive numbers
        '''
        self.assertEqual(False, prime_test(8, [2,3,5,7]))
        self.assertEqual(True, prime_test(7, [2,3,5]))

    def test_negative_numbers(self):
        '''
        test negative numbers
        '''
        self.assertEqual(False, prime_test(-1))
        self.assertEqual(False, prime_test(-37))




class test_prime_numbers(unittest.TestCase):
    pass

unittest.main()
