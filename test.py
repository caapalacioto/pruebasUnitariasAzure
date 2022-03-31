import suma
import unittest

class TestMyModule(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(suma.sum(5, 7), 12)
    def test_sum_negative(self):
        self.assertEqual(suma.sum(-5, -7), 12)
    def test_sum_cero(self):
        self.assertEqual(suma.sum(0, 0), 0)
    def test_sum_strin(self):
        self.assertRaises(TypeError, suma.sum, 0, 'a')


if __name__ == '__main__':
    unittest.main()