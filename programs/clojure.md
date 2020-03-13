# Clojure

> Source: http://clojure.org/api/cheatsheet

> Aliases: clojurescript

$ Numbers
    `quot                          {{(quot n d) - Returns the quotient of dividing numerator n by denominator d}} 
    `mod                           {{(mod n d) - Returns the modulus of dividing numerator n by denominator d}} 
    `inc                           {{(inc x) - Returns a number one greater than x}} 
    `max                           {{(max x y & more) - Returns the greatest number argument}} 
    `rand                          {{(rand n) - Returns a random floating point number between 0 inclusive and n exclusive}} 
    `even?                         {{(even? n) - Returns true if n is an even number}} 
    `integer?                      {{(integer? n) - Returns true if n is an integer, false otherwise}} 

$ Strings
    `count                         {{(count x) - Returns the number of items in x}} 
    `subs                          {{(subs s start end) - Returns the substring of s beginning at start inclusive, and ending at end exclusive}} 
    `join                          {{(join coll) - Returns a string of all elements in coll, as returned by (seq coll), separated by an optional separator}} 
    `split                         {{(split s re limit) - Splits string on a regular expression. Optional argument limit is the maximum number of splits}} 
    `replace                       {{(replace s match replacement) - Replaces all instance of match with replacement in s}} 
    `blank?                        {{(blank? s) - True if s is nil, empty, or contains only whitespace}} 

$ Functions
    `defn                          {{Defines a function}} 
    `identity                      {{(identity x) - Returns its argument}} 
    `constantly                    {{(constantly x) - Returns a function that takes any number of arguments and always returns x}} 
    `comp                          {{(comp f1 f2 f3 & fs) - Takes a set of functions (fns) and returns a function that is the composition of those functions}} 
    `complement                    {{(complement f) - Takes a function f and returns a function that takes the same arguments as f}} 
    `memoize                       {{Returns a memoized version of a referentially transparent function}} 
    `apply                         {{(apply f args) - Applies function f to the argument list formed by prepending intervening arguments to args}} 
    `cond->                        {{(cond-> expr & clauses) - Takes an expression and a set of test/form pairs}} 
    `some->                        {{When expr is not nil, threads it into the first form (via ->)}} 

$ Lists
    `list                          {{(list & items) - Creates a new list containing items}} 
    `peek                          {{(peek coll) - Returns the first element of a list; same as first.}} 
    `cons                          {{(cons x coll) - Returns a new sequence where x is the first element and coll is the rest}} 
    `conj                          {{Returns a new collection with the xs added to coll}} 
    `pop                           {{(pop coll) - For a list, returns a new list without the first item}} 

$ Vectors
    `vector                        {{(vector & args) - Creates a new vector containing args}} 
    `assoc                         {{(assoc coll k v) - When applied to a map, returns a new map that contains the mapping of key(s) to val(s)}} 
    `subvec                        {{(subvec v start end) - Returns a persistent vector of the items in v from start inclusive to end exclusive}} 
    `replace                       {{(replace smap coll) - Given a map of replacement pairs smap and a vector/collection coll, returns a vector/seq with any elements = to a key in smap replaced with the corresponding val in smap}} 
    `mapv                          {{(mapv f coll) - Returns a vector consisting of the result of applying f to the set of first items of each coll, followed by applying f to the set of second items in each coll, until any one of the colls is exhausted}} 
    `filterv                       {{Returns a vector of the items in coll for which (pred item) returns true}} 
    `reduce-kv                     {{Reduces an associative collection}} 

