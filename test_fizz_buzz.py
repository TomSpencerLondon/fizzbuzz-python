import unittest
from fizz_buzz import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    # def setUp(self):
    #     number = 1;
    #     fizz_buzz(number) = fizz_buzz(1);

    def test_it_should_be_default_value(self):
        self.assertEqual(1,fizz_buzz(1))
        self.assertEqual(2,fizz_buzz(2))

    def test_it_should_be_fizz(self):
        self.assertEqual("fizz",fizz_buzz(3))
        self.assertEqual("fizz",fizz_buzz(6))

    def test_it_should_be_buzz(self):
        self.assertEqual("buzz",fizz_buzz(5))
        self.assertEqual("buzz",fizz_buzz(10))

    def test_it_should_be_buzz(self):
        self.assertEqual("fizzbuzz",fizz_buzz(15))
        self.assertEqual("fizzbuzz",fizz_buzz(30))

if __name__ == '__main__':
    unittest.main()
