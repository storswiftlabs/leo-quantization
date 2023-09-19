import unittest

from quantization.float import new, Float, dequantization


class TestQuantization(unittest.TestCase):

    def test_float_quantization(self):
        f = Float(0.1)
        print(f)

    def test_float_dequantization(self):
        scale = 26
        value = 6710885
        real_value = 0.1
        dequantized_value = dequantization(scale, value)

        # Get real_value decimal places
        decimal_places = len(str(real_value).split('.')[1])
        tran_number = round(dequantized_value, decimal_places)
        print(tran_number)
        assert tran_number, real_value

    def test_new_float_normal(self):
        scale = 4
        value = 2
        real_value = 0.1
        f = new(scale, value, real_value)
        print(f)
        print(dequantization(scale, value))

    def test_new_float_no_zero_point(self):
        scale = 2
        value = 2
        real_value = 0.1
        f = new(scale, value, real_value)
        print(f)
