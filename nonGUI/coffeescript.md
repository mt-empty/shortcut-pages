# CoffeeScript Cheat Sheet

> Source: http://coffeescript.org

> Aliases: coffee-script

$ Usage
    `coffee src/file.coffee        {{Run CoffeeScript file}} 
    `coffee -c -o output/ src/     {{Compile files from src to output}} 
    `coffee -e "console.log 'Hello World'"
>                                  {{Evaluate CoffeeScript code}} 
    `coffee --join output/all.js --compile src/*.coffee
>                                  {{Concatenate the source CoffeeScript before compiling}} 
    `coffee                        {{Start Read-eval-print loop}} 
    `coffee --output output/ -cw src/
>                                  {{Watch directory src for changes}} 

$ Variables
    `language = 'CoffeeScript'     {{Initialize a variable}} 

$ Functions
    `hello = -> console.log "Hello"
>                                  {{Define function}} 
    `hello()                       {{Call function}} 
    `sum = (a, b) -> a + b         {{Define function with args}} 
    `sum 1, 2                      {{Call function with args}} 
    `sum_multiply = (a, b) -> [a + b, a * b]
>                                  {{Define function}} 
    `[sum, multiply ] = sum_multiply 1, 2
>                                  {{Call function}} 
    `myFunc = (param = 'default') -> console.log param
>                                  {{Define function with default param}} 
    `otherFunc = (first, other...) -> console.log other
>                                  {{Define function}} 
    `otherFunc myArray...          {{call function with array as arguments}} 

$ Arrays
    `array = [1, 2, 3, 4]          {{Array with numbers from 1 to 4}} 
    `array = [1..4]                {{Array with numbers from 1 to 4}} 
    `array = [1...5]               {{Array with numbers from 1 to 4}} 
    `array1 = array[1..3]          {{Create new array from three items from array}} 
    `array[1..3] = [3, 2, 1]       {{Change three items of array}} 
    `ground_coffee.reverse()       {{Reverse elements in array}} 
    `Math.max [12, 32, 5]...       {{Max element of array}} 
    `[1, 2].concat [3, 4, 5]       {{Concatenating arrays}} 

$ Operators and aliases
    `this, @                       {{this}} 
    `is                            {{===}} 
    `isnt                          {{!==}} 
    `not                           {{!}} 
    `and                           {{&&}} 
    `or                            {{||}} 
    `true, yes, on                 {{true}} 
    `false, no, off                {{false}} 
    `of                            {{in}} 
    `in                            {{find element in array (No JS equivalent)}} 
    `?                             {{Existential operator: returns true unless value is 'null' or 'undefined'}} 
    `a ** b                        {{Math.pow(a, b)}} 
    `a // b                        {{Math.floor(a / b)}} 
    `a %% b                        {{(a % b + b) % b}} 

