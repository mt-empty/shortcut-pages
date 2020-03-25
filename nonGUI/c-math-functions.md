# C Math Functions

> Source: http://www.gnu.org/software/libc/manual/html_mono/libc.html

> Aliases: c-mathematics-functions, math.h

$ Trignometric Functions
    `double sin (double x)         {{Returns the sine of x, where x is given in radians. The return value is in the range -1 to 1}} 
    `double cos (double x)         {{Returns the cosine of x, where x is given in radians. The return value is in the range -1 to 1}} 
    `double tan (double x)         {{Returns the tangent of x, where x is given in radians}} 
    `void sincos (double x, double *sinx, double *cosx)
>                                  {{Returns the sine of x in *sinx and the cosine of x in *cos, where x is given in radians}} 

$ Inverse Trignometric Functions
    `double asin (double x)        {{Returns the arc sine of x in radians. The return value is in the range -pi/2 to pi/2}} 
    `double acos (double x)        {{Returns the arc cosine of x in radians. The return value is in the range 0 to pi}} 
    `double atan (double x)        {{Returns the arc tangent of x in radians. The return is in the range -pi/2 to pi/2}} 
    `double atan2 (double y, double x)
>                                  {{Returns the arc tangent in radians of y/x based on the signs of both values to determine the correct quadrant. The return value is given in radians and is in the range -pi to pi, inclusive}} 

$ Exponentiation and Logarithms
    `double exp (double x)         {{Returns the value of e raised to the xth power}} 
    `double exp2 (double x)        {{Returns the value of 2 raised to the xth power}} 
    `double exp10 (double x)       {{Returns the value of 10 raised to the xth power}} 
    `double log (double x)         {{Returns the natural logarithm (base-e logarithm) of x}} 
    `double log2 (double x)        {{Returns the natural logarithm (base-2 logarithm) of x}} 
    `double log10 (double x)       {{Returns the common logarithm (base-10 logarithm) of x}} 
    `double pow (double x, double y)
>                                  {{Returns x raised to the power of y}} 
    `double sqrt (double x)        {{Returns the square root of x}} 
    `double cbrt (double x)        {{Returns the cube root of x}} 

$ Hyperbolic Functions
    `double sinh (double x)        {{Returns the hyperbolic sine of x}} 
    `double cosh (double x)        {{Returns the hyperbolic cosine of x}} 
    `double tanh (double x)        {{Returns the hyperbolic tangent of x}} 
    `double asinh (double x)       {{Returns the inverse hyperbolic sine of x}} 
    `double acosh (double x)       {{Returns the inverse hyperbolic cosine of x}} 
    `double atanh (double x)       {{Returns the inverse hyperbolic tangent of x}} 

$ Rounding Functions
    `double ceil (double x)        {{Rounds x upwards to the nearest integer, returning that value as a double}} 
    `double floor (double x)       {{Rounds x downwards to the nearest integer, returning that value as a double}} 
    `double trunc (double x)       {{Round x towards zero to the nearest integer (returned in floating-point format)}} 
    `double rint (double x)        {{Round x to an integer value according to the current rounding mode}} 
    `double nearbyint (double x)   {{Returns the same value as the rint functions, but do not raise the inexact exception if x is not an integer}} 
    `double round (double x)       {{Similar to rint, but they round halfway cases away from zero instead of to the nearest integer (or other current rounding mode)}} 
    `double modf (double value, double *integer-part)
>                                  {{Breaks the argument value into an integer part and a fractional part (between -1 and 1, exclusive). Their sum equals value}} 

$ Remainder Functions
    `double fmod (double numerator, double denominator)
>                                  {{Computes the remainder from the division of numerator by denominator}} 
    `double drem (double numerator, double denominator)
>                                  {{Like fmod except it rounds the internal quotient n to the nearest integer instead of towards zero to an integer}} 
    `double remainder (double numerator, double denominator)
>                                  {{Another name for drem}} 

$ Normalization Functions
    `double frexp (double value, int *exponent)
>                                  {{To split the number value into a normalized fraction and an exponent}} 
    `double ldexp (double value, int exponent)
>                                  {{Returns the result of multiplying the floating-point number value by 2 raised to the power exponent}} 

$ Absolute Value
    `double fabs (double number)   {{Returns the absolute value of the floating-point number number}} 

