import unittest

from ..float import new, Float, dequantization, get_float_list


class TestQuantization(unittest.TestCase):

    def test_float_quantization(self):
        f = Float(0.1)
        dequantized_value = dequantization(f.scale, f.value)
        decimal_places = len(str(f.real_value).split('.')[1])
        tran_number = round(dequantized_value, decimal_places)
        print(f.real_value, tran_number)
        self.assertEqual(f.real_value, tran_number)

    def test_float_quantization_max_value(self):
        f = Float(83886070)
        print(f)
        dequantized_value = dequantization(f.scale, f.value)
        print(dequantized_value)
        self.assertNotEqual(f.real_value, int(dequantized_value))

    def test_float_quantization_over(self):
        f = Float(0.0000000654321)
        print(f)
        dequantized_value = dequantization(f.scale, f.value)
        # Get real_value decimal places
        decimal_places = len(str(f.real_value).split('.')[1])
        tran_number = round(dequantized_value, decimal_places)
        print(tran_number)

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

    def test_leo_res_dequantization(self):
        f = Float(0.1)
        print(f)
        f = Float(0.2)
        print(f)
        dequantized_value_add = dequantization(24, 5033163) # 0.1+0.2 = 0.3
        print("dequantized_value_add", dequantized_value_add)
        dequantized_value_sub = dequantization(26, 6710885) # 0.2-0.1 = 0.1
        print("dequantized_value_sub", dequantized_value_sub)
        dequantized_value_mul = dequantization(28, 5368706) # 0.1*0.2 = 0.02
        print("dequantized_value_mul", dequantized_value_mul)
        dequantized_value_div = dequantization(24, 8388607) # 0.1/0.2 = 0.5
        print("dequantized_value_div",dequantized_value_div)

    def test_get_float_list(self):
        real_value_list = [0.1, 0.2, 0.3, 0.12, 0.14999999, 0.9999999]
        scale_list, value_list = get_float_list(real_value_list)
        print("scale_list", scale_list)
        print("value_list", value_list)
        self.assertEqual([26, 25, 24, 26, 25, 23], scale_list)
        self.assertEqual([6710885, 6710885, 5033164, 8053062, 5033163, 8388606], value_list)
