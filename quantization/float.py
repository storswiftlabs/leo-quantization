_BASE = 2
_MAXIMUM_BIT = 23 # Float 23bit, Double is 52bit
_MINIMUM_BASE_POW = 256


def get_maximum_value():
    return pow(_BASE, _MAXIMUM_BIT) - 1


def get_minimum_value():
    return 0


max_value: int = get_maximum_value()


class Float:
    # quantize [0.0, 1.0] to [0, max_value]
    scale: int  # scale, determines the sign of a floating-point number
    value: int  # quantized value uint
    real_value: float  # origin float value

    def __init__(self, real_value: float):
        self.real_value = real_value
        self.scale = 0
        self.value = 1

        while real_value < 1:
            real_value *= _BASE
            self.scale += 1
        if self.scale >= _MAXIMUM_BIT:
            self.value = 0;
            self.scale = _MINIMUM_BASE_POW
            return

        # Start with the largest possible scale
        self.scale += _MAXIMUM_BIT
        self.value = int(real_value * max_value)

        # If value is too large, decrease scale
        while self.value > max_value:
            self.scale -= 1
            self.value = int(self.value / _BASE)

    def __str__(self):
        return f'scale: {self.scale}, value: {self.value}, real_value: {self.real_value}'


def dequantization(scale, value):
    value /= pow(_BASE, scale)
    return value


def new(scale: int, value: int, real_value: float):
    """
    Description: 已知scale和zero_point情况下，构造Float object
    """
    f = Float(real_value)
    f.scale = scale
    f.value = value
    f.real_value = real_value
    return f


if __name__ == '__main__':
    pass
