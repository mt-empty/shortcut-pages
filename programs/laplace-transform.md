# Laplace Transform

> Source: http://tutorial.math.lamar.edu/pdf/Laplace_Table.pdf

> Aliases: laplace-rules, laplace-transforms, laplace-transform-table, laplace, laplace-identities, laplace-table

$ Common Transforms
    `L( 1 )                        {{1 / s}} 
    `L( t^n )                      {{( n! ) / [ s^( n+1 ) ]}} 
    `L( e^( at ) )                 {{1 / ( s-a )}} 
    `L( sin( at ) )                {{a / [ ( s^2 ) + ( a^2 ) ]}} 
    `L( cos( at ) )                {{s / [ ( s^2 ) + ( a^2 ) ]}} 
    `L( tsin( at ) )               {{( 2as ) / [ [ ( s^2 ) + ( a^2 ) ]^2 ]}} 
    `L( tcos( at ) )               {{[ ( s^2 ) - ( a^2 ) ] / [ [ ( s^2 ) + ( a^2 ) ]^2 ]}} 
    `L( sinh( at ) )               {{a / [ ( s^2 ) - ( a^2 ) ]}} 
    `L( cosh( at ) )               {{s / [ ( s^2 ) - ( a^2 ) ]}} 
    `L(  e^( at ) sin( bt ) )      {{b / [ [ ( s-a )^2 ] + ( b^2 ) ]}} 
    `L(  e^( at ) cos( bt ) )      {{( s-a ) / [ [ ( s-a )^2 ] + ( b^2 ) ]}} 
    `L(  e^( at ) sinh( bt ) )     {{b / [ [ ( s-a )^2 ] - ( b^2 ) ]}} 
    `L(  e^( at ) cosh( bt ) )     {{( s-a ) / [ [ ( s-a )^2 ] - ( b^2 ) ]}} 
    `L(  t^n  e^( at )  )          {{( n! ) / [ ( s-a )^( n+1 ) ]}} 

$ Identities
    `F(s)                          {{L{ f(t) }}} 
    `f(t)                          {{(L^-1){ F(s) }}} 

