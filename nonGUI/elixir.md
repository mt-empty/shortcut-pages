# Elixir

> Source: http://elixir-lang.org/

$ Equality
    `===                           {{strict test for equality}} 
    `!==                           {{strict test for inequality}} 
    `and                           {{short-circuit operator for logical AND}} 
    `or                            {{short-circuit operator for logical OR}} 
    `not                           {{short-circuit operator for logical NOT}} 
    `xor                           {{short-circuit operator for exclusive OR}} 
    `==                            {{relaxed test for equality}} 
    `!=                            {{relaxed test for inequality}} 
    `&&                            {{relaxed operator for logical AND}} 
    `||                            {{relaxed operator for logical OR}} 
    `!                             {{relaxed operator for logical NOT}} 
    `>                             {{greater than}} 
    `>=                            {{greater than or equal to}} 
    `<                             {{less than}} 
    `<=                            {{less than or equal to}} 

$ Arithmetic
    `+                             {{plus}} 
    `-                             {{minus}} 
    `*                             {{multiply}} 
    `/                             {{divide}} 
    `div                           {{integer divide}} 
    `rem                           {{integer modulus}} 

$ Other Operators
    `++                            {{list addition (concat)}} 
    `--                            {{list subtraction}} 
    `in                            {{test for membership}} 
    `^term                         {{no reassign}} 
    `<>                            {{binary concatenation}} 

$ Types
    `2, 0xcafe, 0b100, 10_000      {{Integer}} 
    `1.0, 3.1415, 6.02e23          {{Float}} 
    `:foo, :me@home :elixir        {{Atom}} 
    `{:ok, 11, 'hi'}               {{Tuple}} 
    `[1, 2, 3], [head|tail]        {{List}} 
    `'abc'                         {{Character List}} 
    `[a: :foo, b: :bar]            {{Keyword List}} 
    `%{ key => value }             {{Map (no duplicates)}} 
    `<< 1, 2 >>, "string"          {{Binary}} 
    `true, false, nil              {{Boolean}} 
    `a..b                          {{Range}} 

$ Sigils
    `~S                            {{string (no interpolation)}} 
    `~s                            {{string (with interpolation)}} 
    `~C                            {{character list (no interpolation)}} 
    `~c                            {{character list (with interpolation)}} 
    `~R                            {{regex (no interpolation)}} 
    `~r                            {{regex (with interpolation)}} 
    `~W                            {{word list (no interpolation)}} 
    `~w                            {{word list (with interpolation)}} 

$ Example Functions
    `String.length/1               {{returns the number of Unicode graphemes}} 
    `Enum.member?/2                {{checks if value exists within a collection}} 
    `File.read!/1                  {{returns the contents of a file}} 
    `IO.puts/2                     {{outputs item(s) to a device}} 
    `String.jaro_distance/2        {{returns the jaro distance of two strings}} 
    `Map.new/0                     {{returns an empty map}} 
    `Map.put/3                     {{puts a new key and value into map}} 
    `Enum.random/1                 {{returns a random entry from a collection}} 
    `String.reverse/1              {{reverses a string}} 
    `:erlang.localtime/0           {{returns date / time tuple}} 
    `List.last/1                   {{returns a list's last element}} 
    `:timer.sleep/1                {{calls the Erlang timer module (milliseconds)}} 

