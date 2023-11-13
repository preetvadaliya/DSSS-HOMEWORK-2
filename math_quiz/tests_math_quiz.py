import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        # Test if the random operator is one of '+', '-', or '*'
        for _ in range(1000):  # Test a large number of random values
            rand_operator = generate_random_operator()
            self.assertTrue(rand_operator in {'+', '-', '*'})

    def test_perform_operation(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
            # Add more test cases as needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_operation(num1, num2, operator)

            # Test if the generated problem and answer match the expected values
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
