import unittest


def fizzbuzz(number):
    if number == 3:
        return 'fizz'


class FizzBuzzTest(unittest.TestCase):
    def test_should_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')


unittest.main()
