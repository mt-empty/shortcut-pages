# Arduino

> Source: https://www.arduino.cc/en/Reference/HomePage

> Aliases: arduino-ide

$ General Structure
    `setup()                       {{Run code once at beginning of program}} 
    `loop()                        {{Loop code continuously}} 
    `#define constantName value    {{Replace all references to constantName with value at compile time}} 
    `#include library              {{Include library in sketch and access its functions}} 

$ Constants
    `HIGH / LOW                    {{Pin input or output voltage is high or low}} 
    `true / false                  {{Boolean values}} 
    `INPUT / INPUT_PULLUP / OUTPUT {{Configure pin to sample voltage or provide current to other circuits}} 
    `LED_BUILTIN                   {{Pin where built-in LED is connected}} 

$ Control Structures
    `if (expression A) {do thing A}
>                                  {{Do thing A if expression A is true}} 
    `else if (expression B) {do thing B}
>                                  {{Do thing B if expression A is false and expression B is true}} 
    `else {do thing C}             {{Do thing C if all the above "if" and "else if" blocks are false}} 
    `for(int x = 0; x < 100; x++){println(x)}
>                                  {{Set x to 0, then while x is less than 100, print X and increment x by 1}} 
    `while(statement){expression}  {{Keep doing expression while statement is true}} 
    `do{statement}while(expression);
>                                  {{Like while loop, except expression is evaluated after statement runs once}} 
    `switch (var) {case 1: statement A break; case 2: statement B break; default: statement C break}
>                                  {{Run statement A, B or C depending on whether var is 1, 2 or a different value}} 
    `break;                        {{Exit a for, while, do while loop or switch statement}} 
    `continue;                     {{Skip rest of current iteration of for, while, or do while loop, start next iteration}} 
    `return value;                 {{Terminate the function and optionally return value to the function that called it}} 
    `goto label;                   {{Send the program flow to `label:`}} 

$ Comments
    `// stuff                      {{Single-line comment}} 
    `&#47;* many things */         {{Multi-line comment}} 

$ Comparison Operators
    `==                            {{Equals}} 
    `!=                            {{Is not equal to}} 
    `<                             {{Less than}} 
    `>                             {{Greater than}} 
    `<=                            {{Less than or equal to}} 
    `>=                            {{Greater than or equal to}} 

$ Boolean Operators
    `&&                            {{And}} 
    `||                            {{Or}} 
    `!                             {{Not}} 

$ Bitwise Operators
    `&                             {{And}} 
    `|                             {{Or}} 
    `^                             {{Xor}} 
    `~                             {{Not}} 
    `<<                            {{Bitshift left}} 
    `>>                            {{Bitshift right}} 

$ Compound Operators
    `x ++                          {{x = x + 1}} 
    `x --                          {{x = x - 1}} 
    `x += y                        {{x = x + y}} 
    `x -= y                        {{x = x - y}} 
    `x *= y                        {{x = x * y}} 
    `x /= y                        {{x = x / y}} 
    `x %= y                        {{x = the remainder of x / y}} 
    `x &= y                        {{x = x & y}} 
    `x |= y                        {{x = x | y}} 

$ I/O
    `pinMode(pin, mode)            {{Set pin to either INPUT, OUTPUT, or INPUT_PULLUP}} 
    `digitalWrite(pin, value)      {{Set pin to either HIGH or LOW}} 
    `digitalRead(pin)              {{Read value of pin, which will be HIGH or LOW}} 
    `analogReference(type)         {{Configure refence voltage used for analog input}} 
    `analogRead(pin)               {{Return input voltage of pin as integer between 0 and 1023}} 
    `analogWrite(pin, value)       {{Output PWM wave to pin with duty cycle of value (between 0 and 255)}} 

$ Time
    `millis()                      {{Return milliseconds since program started}} 
    `micros()                      {{Return microseconds since program started}} 
    `delay(n)                      {{Pause program for n milliseconds}} 
    `delayMicroseconds(n)          {{Pause program for n microseconds}} 

$ Math
    `min(x, y)                     {{Return the smaller of x or y}} 
    `max(x, y)                     {{Return the greater of x or y}} 
    `abs(x)                        {{Absolute value of x}} 
    `constrain(x, a, b)            {{Limit x to the range a-b, return a or b if x is too small or too large}} 
    `map(value, fromLow, fromHigh, toLow, toHigh)
>                                  {{Map value from one range of numbers to another}} 
    `pow(a, x)                     {{Calculate a to the power of x}} 
    `sqrt(x)                       {{Square root of x}} 
    `sin(x) / cos(x) / tan(x)      {{Sine, cosine and tangent of x}} 
    `randomSeed(x)                 {{Start the pseudo-random number generator at point x}} 
    `random(min, max)              {{Generate a pseudo-random number between min (inclusive) and max (exclusive)}} 

