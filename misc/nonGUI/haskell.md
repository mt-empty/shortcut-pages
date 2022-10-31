# Haskell

> Source: https://www.haskell.org/

> Aliases: haskell-language, hs

$ Data Types
    `1                             {{Integer}} 
    `1.42                          {{Float}} 
    `"abc"                         {{String}} 
    `'a'                           {{Char}} 
    `True                          {{Bool}} 
    `1, 2, 3                       {{[Int]}} 
    `(1, 4.2)                      {{(Int, Float)}} 

$ Basic Mathematical Operations
    `Num                           {{Basic numeric typeclass}} 
    `Integral                      {{Numeric typeclass including integral numbers}} 
    `Fractional                    {{Numeric typeclass including fractional numbers (supports real division)}} 
    `(+) :: Num a => a -> a -> a   {{Numeric addition}} 
    `(/) :: Fractional a => a -> a -> a
>                                  {{Division}} 
    `div :: Integral a => a -> a -> a
>                                  {{Integer division}} 

$ Comparators
    `A == B                        {{A is equal to B}} 
    `A /= B                        {{A is not equal to B}} 
    `A < B                         {{A is less than B}} 
    `A <= B                        {{A is less than or equal to B}} 
    `A > B                         {{A is greater than B}} 
    `A >= B                        {{A is greater than or equal to B}} 

$ IO
    `putStrLn "Hello!"             {{Prints the string "Hello!"}} 
    `getLine                       {{Reads the input}} 

$ Enumerations
    `start..stop                   {{Creates a list containing all values between start and stop}} 
    `start,next..stop              {{Same as above but with a different step}} 
    `start..                       {{Iterates from start to the maximum bound (if any)}} 

$ Lists
    `                              {{Empty list}} 
    `1, 2, 3 !! 1                  {{Returns the first element of the list}} 
    `1, 2 ++ 3, 4                  {{Joins the two lists together}} 
    `'A' : 'B', 'C'                {{Adds the letter A to the head of the list}} 
    `x + y | x <- 1,2, y <- 1..5   {{List comprehension}} 
    `x | x <- 1..10, x > 7         {{List comprehension with guards}} 

$ Tuples
    `fst : (a, b) -> a             {{Accesses the first element of a tuple (only works on pair)}} 
    `snd : (a, b) -> b             {{Accesses the second element of a tuple (only works on pair)}} 

$ Functions
    `f x y ...                     {{Calls a function with the given parameters}} 
    `func x y = x + y              {{Declaration of a simple function that adds two variables}} 
    `(\x y -> x + y) 2 3           {{Anonymous function that adds two variables}} 

$ Control Flow
    `if cond then x else y         {{If expression}} 

