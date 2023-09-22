# Leo Quantization

Implement quantization operations in Leo, including $+ * /$, on quantized values.

## Description

Use quantized data in the zkML program in Leo and perform operations on quantized data. Choose fixed FP32 quantization, which is 32-bit floating-point quantization.

## Directory Structure
- quantization: Python FP32 quantization implement
- quantize: a Leo library that implements Float arithmetic operations

## Key Points

### FP32
FP32 uses 32 bits to represent a number: 1 bit for the sign, 8 bits for the exponent, and the remaining 23 bits for the significant figures. Although it provides high precision, the disadvantage of FP32 is its high computation and memory usage.

### Leo Language
Support u8, u16, u32, u64, u128, i8, i16, i32, i64, i128 numeric types, "Leo Quantization" convert Float values in ML/AI to integer values supported by Leo.

## Usage
```shell
# code clone
git clone https://github.com/storswiftlabs/leo-quantization.git
# Python
python -m unittest quantization/test_float.py
# Leo run
cd quantize
# Execute quantized arithmetic
leo run float_add
leo run float_sub
leo run float_mul
leo run float_div
# Change inputs data
vi inputs/quantize.in
```

## References

[1] Maxime Labonne. Introduction to Weight Quantization, https://towardsdatascience.com/introduction-to-weight-quantization-2494701b9c0c, 2023.

[2] LIU, Xuanming, et al. Evaluate and Guard the Wisdom of Crowds: Zero Knowledge Proofs for Crowdsourcing Truth Inference. arXiv preprint arXiv:2308.00985, 2023.

[3] Fixed-point arithmetic, https://en.wikipedia.org/wiki/Fixed-point_arithmetic#Operations

[4] zkTI, https://github.com/Blockchain-Research-Center/zkTI.
