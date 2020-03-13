# Groovy

> Source: http://www.groovy-lang.org/syntax.html

$ Type List
    `java.lang.String              {{Strings}} 
    `java.lang.Character           {{Single Unicode Character}} 
    `java.lang.Boolean             {{Boolean type}} 
    `java.lang.Byte                {{Eight-bit integer}} 
    `java.lang.Integer             {{32-bit integer}} 
    `java.lang.Float               {{32-bit floating point number}} 
    `java.lang.Double              {{64-bit doulbe precision floating point number}} 
    `java.math.BigDecimal          {{Uncapped floating point number}} 
    `java.util.List                {{Contain values of any type}} 
    `java.util.Map                 {{No need for quotes}} 

$ Operators
    `Addition                      {{a.plus(b)}} 
    `Subtraction                   {{a.minus(b)}} 
    `Multiplication                {{a.multipy(b)}} 
    `Division                      {{a.div(b)}} 
    `Modulo Operator               {{a.mod(b)}} 
    `Power-of Operator             {{a.power(b)}} 
    `Logical AND                   {{a.and(b)}} 
    `a in b                        {{b.isCase(a)}} 
    `Shift Left                    {{a.leftShift(b)}} 
    `Shift Right                   {{a.rightShift(b)}} 
    `Increment                     {{a.next()}} 
    `Decrement                     {{a.previous()}} 

$ Comparison Operators
    `a == b                        {{Value based equality}} 
    `a != b                        {{Value based inequality}} 
    `a < b                         {{Less than}} 
    `a <= b                        {{Less than or equal}} 
    `a <=> b                       {{Compare}} 
    `a =~ b                        {{Regex pattern match}} 
    `a?.b                          {{Null-safe navigation}} 
    `a ?: b                        {{Elvis operator}} 

$ Truth Condition
    `String                        {{False if empty or null}} 
    `Number                        {{False if zero or null}} 
    `Collection                    {{False if zero or null}} 
    `Map                           {{False if zero or null}} 
    `Matcher (=~)                  {{False if no match found}} 

$ Loops
    `for (<var> in <value>) ...    {{Basic for loop}} 
    `for (int i = 0; i < 10;   i += 2) ...
>                                  {{For loop similar to java}} 
    `while (<expr>) ...            {{Basic while loop}} 

