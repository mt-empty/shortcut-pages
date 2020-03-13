# Elm

> Source: https://github.com/izdi/elm-cheat-sheet

$ Hello World
    `import Html exposing (text)

main =
	&#34;hello world&#34; |> text
>                                  {{Basic Hello World Example}} 

$ Comments
    `-- Single line comment        {{Single line comment}} 
    `&#123;&#45;
 	Multi line comment
 &#45;&#125;
>                                  {{Multiline comment}} 

$ Modules
    `module Mymodule where         {{Defines a module, exports everything by default}} 
    `module Mymodule (Type, value) where
>                                  {{Exports only specified entities}} 

$ Importing
    `import String
import String as Str
>                                  {{Qualified imports}} 
    `import Mymodule exposing (..)
import Mymodule exposing ( Error )
import Mymodule exposing ( Error(..) )
import Mymodule exposing ( Error(Forbidden) )
>                                  {{Unqualified imports}} 

$ Compilation
    `elm make HelloWorld.elm -> index.html
>                                  {{Default compilation}} 
    `elm make HelloWorld.elm --output hw.js
>                                  {{Custom name}} 
    `elm make HelloWorld.elm MyModule.elm --output hw.js
>                                  {{Multiple files}} 
    `elm make HelloWorld.elm --warn
>                                  {{With warnings}} 
    `elm make HelloWorld.elm --output hw.html
>                                  {{To HTML}} 

