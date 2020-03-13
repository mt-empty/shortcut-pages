# OCaml

> Source: http://ocaml.org

$ Data Types
    `unit                          {{Void, takes only one value: ()}} 
    `int                           {{Integer of either 31 or 63 bits}} 
    `int32                         {{32 bit integer, like 32l}} 
    `int64                         {{64 bit integer, like 32L}} 
    `float                         {{Double precision float, 1.0}} 
    `bool                          {{Boolean, takes two values: true or false}} 
    `char                          {{Simple ASCII characters, like 'A'}} 
    `string                        {{A String of chars, like "hello"}} 
    `list                          {{Lists, like head :: tail or [ 1 ; 2 ; 3 ]}} 
    `array                         {{Arrays, like [| 1 ; 2 ; 3 |]}} 
    `tuple                         {{Tuples like (1, "foo", 'b')}} 

$ Imports - Namespaces
    `open Unix ;;                  {{Global Open}} 
    `let open Unix in <expr>       {{Local open}} 
    `Unix.(<expr>)                 {{Local open}} 

$ Modules
    `module M = struct ... end     {{Module definition}} 
    `module M: sig .. end= struct .. end
>                                  {{Module and singature}} 
    `module M = unix               {{Module renaming}} 
    `include M                     {{Include items from}} 
    `module type Sg = sig .. end   {{Signature definition}} 
    `module type Sg = module type of M
>                                  {{Signature of module}} 
    `let module M = struct .. end in ..
>                                  {{Local module}} 
    `let m = (module M : Sg)       {{first class module}} 
    `module M = (val m : Sg)       {{from first class module}} 
    `module Make(S: Sg) = struct .. end
>                                  {{functor}} 
    `module M = Make(M’)           {{functor application}} 

$ Looping
    `while cond do ... done;       {{While Loop}} 
    `for var = min_value to max_value do ... done;
>                                  {{For Loop}} 
    `for var = max_value downto min_value do ... done;
>                                  {{For Loop}} 

$ Functions
    `let func x = <expr>           {{function with one arg}} 
    `let rec func x = <expr>       {{recursive}} 
    `List.iter (fun x -> e) l      {{anonymous function}} 
    `let f (x : int) = expr        {{arg with a constrained type}} 

