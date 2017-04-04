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
    if type(n) != type(1):
        return "Invalid Data Type"

    solution = []
    for i in range(0, n + 1):
        if prime_test(i, solution):
            solution.append(i)
    return solution



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
    '''
    Unit test for prime_numbers
    Test Strategy: egde cases : 0, 1
                   special case : range(0,2)
                   negtives ranges : any int that's negative range(0, negative_n)
                   positive ranges : any int that's postive range(0, postive n)
    coverage : selctive choose to cover major areas not full catesian
    '''
    def test_negative_range(self):
        self.assertEqual([], prime_numbers(-17))
        self.assertEqual([], prime_numbers(-1))

    def test_postive_range(self):
        self.assertEqual([2,3,5,7], prime_numbers(9))
        self.assertEqual([2,3,5,7], prime_numbers(8))
        self.assertEqual([2,3,5,7,11,13,17,19], prime_numbers(19))

    def test_special_case(self):
        self.assertEqual([2], prime_numbers(2))

    def test_data_type(self):
        self.assertEqual("Invalid Data Type", prime_numbers([]))

    def test_edge_case(self):
        self.assertEqual([], prime_numbers(0))
        self.assertEqual([], prime_numbers(1))
unittest.main()
