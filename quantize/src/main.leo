// The 'quantize' program.
program quantize.aleo {

// The 'quantize' program.
// It just support positive decimal operation.
// The number of digits in a positive decimal cannot exceed 2^{23}-1, that |positive decimal| < 2^{23}-1


    // ps: Floating-point numbers beyond BASE^23-1 are not currently considered
    struct Float{
        scale: u32, // scale, determines the sign of a floating-point number
        int_value: u64, // quantized value
    }

    // get max number in two i16 number
    function max_i16(a: u32, b: u32) -> u32{
        if(a>b){
            return a;
        }else{
            return b;
        }
    }

    function get_max_value(BASE: u64, MAXIMUM_BIT: u32) -> u64{
      let res: u64 = BASE**MAXIMUM_BIT-1u64;
      return res;
    }


    transition float_add (a: Float, b: Float) -> Float {
        let MAXIMUM_BIT: u32 = 23u32;
        let BASE: u64 = 2u64;
        let max_value: u64 = get_max_value(BASE, MAXIMUM_BIT);

        if(a.scale>=b.scale+MAXIMUM_BIT+2u32){
            return Float{scale: b.scale, int_value: b.int_value};
        }
        if(b.scale>=a.scale+MAXIMUM_BIT+2u32){
            return Float{scale: a.scale, int_value: a.int_value};
        }

        let max_scale: u32 = max_i16(a.scale, b.scale); // 26
        let a_value: u64 = a.int_value;
        let b_value: u64 = b.int_value;
        // magnify lower value to help addition operation
        if(a.scale < max_scale){
            let tmp: u64 = BASE.pow(max_scale-a.scale);
            a_value *= tmp;
        }else{
            let tmp: u64 = BASE.pow(max_scale-b.scale);
            b_value *= tmp;
        }
        let value: u64 = a_value+b_value;

        // form 0 to MAXIMUM_BIT*2
        for i :u32 in 0u32..46u32{
            if (value > max_value){
                max_scale -= 1u32;
                value /= BASE;
            }
        }
        return Float{scale: max_scale, int_value: value};
    }

    // float_sub just support a > b condition.
    transition float_sub (a: Float, b: Float) -> Float {
        let MAXIMUM_BIT: u32 = 23u32;
        let BASE: u64 = 2u64;
        let max_value: u64 = get_max_value(BASE, MAXIMUM_BIT);

        if(a.scale>=b.scale+MAXIMUM_BIT+2u32){
            return Float{scale: b.scale, int_value: b.int_value};
        }
        if(b.scale>=a.scale+MAXIMUM_BIT+2u32){
            return Float{scale: a.scale, int_value: a.int_value};
        }

        let max_scale: u32 = max_i16(a.scale, b.scale); // 26
        let a_value: u64 = a.int_value;
        let b_value: u64 = b.int_value;
        // magnify lower value to help addition operation
        if(a.scale < max_scale){
            let tmp: u64 = BASE.pow(max_scale-a.scale);
            a_value *= tmp;
        }else{
            let tmp: u64 = BASE.pow(max_scale-b.scale);
            b_value *= tmp;
        }
        let value: u64 = a_value-b_value;

        // form 0 to MAXIMUM_BIT*2
        for i :u32 in 0u32..46u32{
            if (value > max_value){
                max_scale -= 1u32;
                value /= BASE;
            }
        }
        return Float{scale: max_scale, int_value: value};
    }

    transition float_mul (a: Float, b: Float) -> Float {
        let MAXIMUM_BIT: u32 = 23u32;
        let BASE: u64 = 2u64;
        let max_value: u64 = get_max_value(BASE, MAXIMUM_BIT);

        let scale: u32 = a.scale + b.scale;
        let value: u64 = a.int_value * b.int_value;

        // form 0 to MAXIMUM_BIT*2
        for i :u32 in 0u32..46u32{
            if (value > max_value){
                scale -= 1u32;
                value /= BASE;
            }
        }
        return Float{scale: scale, int_value: value};
    }

    transition float_div (a: Float, b: Float) -> Float {
        let MAXIMUM_BIT: u32 = 23u32;
        let BASE: u64 = 2u64;
        let max_value: u64 = get_max_value(BASE, MAXIMUM_BIT);

        let scale: u32 = a.scale + MAXIMUM_BIT - b.scale;
        let value: u64 = a.int_value * max_value / b.int_value;

        // form 0 to MAXIMUM_BIT*2
        for i :u32 in 0u32..46u32{
            if (value > max_value){
                scale -= 1u32;
                value /= BASE;
            }
        }
        return Float{scale: scale, int_value: value};
    }
    
}


