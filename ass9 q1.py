%%writefile checkprime.py

'''
No modules required for this check
'''
def prime(number):
    '''
    Check prime number function
    '''
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return "Not a prime number"
        else:
            return "Prime number"
    else:
        return "Not a prime number"

%%writefile testcheckprime.py

'''
Import required modules
'''
import unittest
from problem1 import prime


class TestPrime(unittest.TestCase):
    '''
    create a class named TestPrime to write tests for our function
    '''

    def test_not_prime(self):
        '''
        This is to test if our function is reporting non prime numbers correctly
        '''
        non_prime = 15
        self.assertEqual(prime(non_prime), "Not a prime number")

    def test_prime(self):
        '''
        This is to test if our function is reporting prime numbers correctly
        '''
        prime_number = 47
        result = prime(prime_number)
        self.assertEqual(result, "Prime number")

if __name__ == "__main__":
    unittest.main()
In [ ]:
python testcheckprime.py
In [ ]:
pylint checkprime.py
pylint testcheckprime.py