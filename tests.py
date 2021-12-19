import unittest
import program
import time


class TestCalculator(unittest.TestCase):

    def test_add(self):
        input = 'input.txt'

        program.write_file(input, [0, 1, -1, 10, 20])
        self.assertEqual(program.summa(input), 30)

        program.write_file(input, [10 ** 100, 10, 10])
        self.assertEqual(program.summa(input), 10 ** 100 + 10 + 10)

        program.write_file(input, [-10, 10, 0, 0, 0])
        self.assertEqual(program.summa(input), 0)

    def test_mult(self):
        input = 'input.txt'

        program.write_file(input, [0, 1, -1, 10, 20, 10 ** 100])
        self.assertEqual(program.multiplication(input), 0)

        program.write_file(input, [10 ** 100, 10, 10])
        self.assertEqual(program.multiplication(input), 10 ** 100 * 10 * 10)

        program.write_file(input, [1, -1, 1, -1, 1, -1, 100])
        self.assertEqual(program.multiplication(input), -100)

    def test_max(self):
        input = 'input.txt'

        program.write_file(input, [10 ** 100, -10 ** 100, 0, 1, -1])
        self.assertEqual(program.maximum(input), 10 ** 100)

        program.write_file(input, [1, 2, 3])
        self.assertEqual(program.maximum(input), 3)

        program.write_file(input, [1, -3, -5, 1, 1, -1, -1, -1])
        self.assertEqual(program.maximum(input), 1)

    def test_min(self):
        input = 'input.txt'

        program.write_file(input, [10 ** 100, -10 ** 100, 0, 1, -1])
        self.assertEqual(program.minimum(input), -10 ** 100)

        program.write_file(input, [1, 2, 3])
        self.assertEqual(program.minimum(input), 1)

        program.write_file(input, [1, 3, 5, 1, 1, -1, -1, -1])
        self.assertEqual(program.minimum(input), -1)

    def test_count_odd(self):
        input = 'input.txt'

        program.write_file(input, [1, 2, 3, 4, 5])
        self.assertEqual(program.count(input), 3)

        program.write_file(input, [-1, -2, -3, 1, 2, 3])
        self.assertEqual(program.count(input), 4)

    def test_time(self):
        input = 'input.txt'
        begin = time.time()

        program.write_file(input, [1, 2, 3, 4, 5])
        program.summa(input)
        program.multiplication(input)
        program.maximum(input)
        program.minimum(input)
        program.count(input)
        self.assertLess(time.time() - begin, 0.03)

        program.write_file(input, [i for i in range(100)])
        program.summa(input)
        program.multiplication(input)
        program.maximum(input)
        program.minimum(input)
        program.count(input)
        self.assertLess(time.time() - begin, 0.6)


if __name__ == "__main__":
    unittest.main()
print()
