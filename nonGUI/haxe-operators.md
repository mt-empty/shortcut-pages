# Haxe

> Source: http://haxe.org/manual/types-numeric-operators.html

> Aliases: haxe-ops, haxelang-ops, haxelang-operators

$ Arithmetic
    `++                            {{increment (unary, post- & pre-fix)}} 
    `--                            {{decrement (unary, post- & pre-fix)}} 
    `+                             {{addition}} 
    `-                             {{substract}} 
    `-                             {{negate an expression (unary, prefix)}} 
    `/                             {{divide}} 
    `*                             {{multiply}} 
    `%                             {{modulo}} 

$ Bitwise
    `~                             {{bitwise negation (unary, prefix)}} 
    `<<                            {{left bit shift}} 
    `>>                            {{right bit shift}} 
    `>>>                           {{right unsigned bit shift}} 
    `|                             {{bitwise OR}} 
    `&                             {{bitwise AND}} 
    `^                             {{bitwise XOR}} 

$ Comparison
    `==                            {{equality}} 
    `!=                            {{inequality}} 
    `>                             {{greater than}} 
    `<                             {{less than}} 
    `>=                            {{greater than or equal to}} 
    `<=                            {{less than or equal to}} 

$ Conditional
    `&&                            {{logical AND}} 
    `||                            {{logical OR}} 
    `!                             {{logical NOT, inverts the boolean. (unary, prefix)}} 
    `?:                            {{ternary operator. e.g. `condition ? then_expr : else_expr`}} 

$ Assignment
    `=                             {{assign}} 
    `+=                            {{addition assignment}} 
    `-=                            {{subtraction assignment}} 
    `*=                            {{multiplication assignment}} 
    `/=                            {{division assignment}} 
    `%=                            {{modulo assignment}} 

$ Bitwise Assignment
    `<<=                           {{bitwise left shift assignment}} 
    `>>=                           {{bitwise right shift assignment}} 
    `>>>=                          {{right unsigned bitwise shift assignment}} 
    `|=                            {{bitwise OR assignment}} 
    `&=                            {{bitwise AND assignment}} 
    `^=                            {{bitwise XOR assignment}} 

$ Extra
    `=>                            {{Extractor in the Pattern Matching expressions}} 
    `=>                            {{Separator in the key-value pare of short Map expression. e.g. `[key => value]`}} 
    `...                           {{Iterator, e.g. `0...42` creates an Iterator<Int> from 0 to 41.}} 
    `!                             {{nothing, unless defined on an abstract. (unary, postfix)}} 
    `=>                            {{nothing, unless defined on an abstract. (unary, postfix)}} 
    `||=                           {{nothing, unless defined on an abstract.}} 
    `&&=                           {{nothing, unless defined on an abstract.}} 

