# Neko Built-ins

> Source: http://nekovm.org/doc/view/builtins

> Aliases: neko-built-ins, neko-builtin-functions, neko-operations, neko-functions, neko-built-in-functions

$ Array
    `array $array(any*)            {{Create an array from a list of values}} 
    `array $amake(n:int)           {{Create an array of size n}} 
    `array $acopy(array)           {{Make a copy of an array}} 
    `int $asize(array)             {{Return the size of an array}} 
    `array $asub(array, p:int, l:int)
>                                  {{Return l elements starting at position p of an array. An error occurs if out of array bounds}} 
    `array $ablit(dst:array, dst_pos:int, src:array, src_pos:int, len:int)
>                                  {{Copy len elements from src_pos of src to dst_pos of dst. An error occurs if out of arrays bounds}} 
    `array $aconcat(array array)   {{Build a single array from several ones}} 

$ String
    `string $string(any)           {{Convert any value to a string. This will make a copy of string}} 
    `string $smake(n:int)          {{Return an uninitialized string of size n}} 
    `int $ssize(string)            {{Return the size of a string}} 
    `string $scopy(string)         {{Make a copy of a string}} 
    `string $ssub(string, p:int, l:int)
>                                  {{Return l chars starting at position p of a string. An error occurs if out of string bounds}} 
    `int? $sget(string, n:int)     {{Return the nth char of a string or null if out of bounds}} 
    `int? $sset(string, n:int, c:int)
>                                  {{Set the nth char of a string to (c & 255). Returns the char set or null if out of bounds}} 
    `void $sblit(dst:string, dst_pos:int, src:string, src_pos:int, len:int)
>                                  {{Copy len chars from src_pos of src to dst_pos of dst. An error occurs if out of strings bounds}} 
    `int $sfind(src:string, pos:int, pat:string)
>                                  {{Return the first position starting at `pos` in `src` where `pat` was found. Return `null` if not found. Error if `pos` is outside `src` bounds}} 

$ Object
    `object $new(object?)          {{Return a copy of the object or a new object if `null`}} 
    `any $objget(o:any, f:int)     {{Return the field f of o or null if doesn't exists or o is not an object}} 
    `any $objset(o:any, f:int, v:any)
>                                  {{Set the field `f` of `o` to `v` and return v if `o` is an object or `null` if not}} 
    `any $objcall(o:any, f:int, args:array)
>                                  {{Call the field `f` of `o` with `args` and return the value or `null` is `o` is not an object}} 
    `bool $objfield(o:any, f:int)  {{Return true if `o` is an object which have field `f`}} 
    `bool $objremove(o:object, f:int)
>                                  {{Remove the field `f` from object `o`. Return `true` on success}} 
    `int array $objfields(o:object)
>                                  {{Return all fields of the object}} 
    `int $hash(string)             {{Return the hashed value of a field name}} 
    `string $field(int)            {{Reverse the hashed value of a field name. Return `null` on failure}} 
    `void $objsetproto(o:object, proto:object?)
>                                  {{Set the prototype of the object}} 
    `object? $objgetproto(o:object)
>                                  {{Get the prototype of the object}} 

$ Function
    `int $nargs(function)          {{Return the number of arguments of a function. If the function have a variable number of arguments, it returns -1}} 
    `any $call(f:function, this:any, args:array)
>                                  {{Call `f` with `this` context and `args` arguments}} 
    `function $closure(function, any*)
>                                  {{Build a closure by applying a given number of arguments to a function}} 
    `any $apply(function, any*)    {{Apply the function to several arguments. Return a function asking for more arguments or the function result if more args needed}} 
    `function $varargs(f:function:1)
>                                  {{Return a variable argument function that, when called, will callback `f` with the array of arguments}} 

$ Number
    `int $iadd(any, any)           {{Add two integers}} 
    `int $isub(any, any)           {{Subtract two integers}} 
    `int $imult(any, any)          {{Multiply two integers}} 
    `int $idiv(any, any)           {{Divide two integers. An error occurs if division by 0}} 
    `bool $isnan(any)              {{Return if a value is the float `NaN`}} 
    `bool $isinfinite(any)         {{Return if a value is the float `+Infinite`}} 
    `int? $int(any)                {{Convert the value to the corresponding integer or return `null`}} 
    `float? $float(any)            {{Convert the value to the corresponding float or return `null`}} 

$ Abstract
    `'kind $getkind('abstract)     {{Returns the kind value of the abstract}} 
    `bool $iskind(any, 'kind)      {{Tells if a value is of the given kind}} 

$ Hashtable
    `int $hkey(any)                {{Return the hash of any value}} 
    `'hash $hnew(s:int)            {{Create an hashtable with s slots}} 
    `void $hresize('hash, int)     {{Resize an hashtable}} 
    `any $hget('hash, k:any, cmp:function:2?)
>                                  {{Look for the value bound to the key `k` in the hashtable. Use the comparison function `cmp` or `$compare` if `null`. Return `null` if no value is found}} 
    `bool $hmem('hash, k:any, cmp:function:2?)
>                                  {{Look for the value bound to the key `k` in the hashtable. Use the comparison function `cmp` or `$compare` if `null`. Return `true` if such value exists, `false` either}} 
    `bool $hremove('hash, k:any, cmp:function:2?)
>                                  {{Look for the value bound to the key `k` in the hashtable. Use the comparison function `cmp` or `$compare` if `null`. Return `true` if such value exists and remove it from the hash, `false` either}} 
    `bool $hset('hash, k:any, v:any, cmp:function:2?)
>                                  {{Set the value bound to key `k` to `v` or add it to the hashtable if not found. Return true if the value was added to the hashtable}} 
    `void $hadd('hash, k:any, v:any)
>                                  {{Add the value `v` with key `k` to the hashtable. Previous binding is masked but not removed}} 
    `void $hiter('hash, f:function:2)
>                                  {{Call the function `f` with every key and value in the hashtable}} 
    `int $hcount('hash)            {{Return the number of elements in the hashtable}} 
    `int $hsize('hash)             {{Return the size of the hashtable}} 

$ Other
    `void $print(any*)             {{Can print any value}} 
    `any $throw(any)               {{Throw any value as an exception. Never returns}} 
    `any $rethrow(any)             {{Throw any value as an exception while keeping previous exception stack. Never returns}} 
    `bool $istrue(v:any)           {{Return `true` if `v` is not `false`, not `null` and not `0`}} 
    `bool $not(any)                {{Return `true` if `v` is `false` or `null` or `0`}} 
    `int $typeof(any)              {{Return the type of a value. The builtin types are defined as integers from `0` to `8`. See "RTTI"}} 
    `int? $compare(any, any)       {{Compare two values and return 1, -1 or 0. Return null if comparison is not possible}} 
    `int $pcompare(any, any)       {{Physically compare two values. Same as `$compare` for integers}} 
    `array $excstack()             {{Return the stack between the place the last exception was raised and the place it was catched}} 
    `array $callstack()            {{Return the current callstack. Same format as `$excstack`}} 
    `int $version()                {{Return the version of Neko: 135 means 1.3.5}} 
    `void $setresolver(function:2?)
>                                  {{Set a function to callback with object and field id when an object field is not found}} 

