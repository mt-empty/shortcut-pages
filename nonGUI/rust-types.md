# Rust Types

> Source: https://doc.rust-lang.org/stable/reference.html#types

> Aliases: rust-objects, rust-object-types

$ Primitive Types
    `bool                          {{Boolean, True or False}} 

$ Machine Types
    `u8                            {{Unsigned integer in the range of [0, 2^8 - 1]}} 
    `u16                           {{Unsigned integer in the range of [0, 2^16 - 1]}} 
    `u32                           {{Unsigned integer in the range of [0, 2^32 - 1]}} 
    `u64                           {{Unsigned integer in the range of [0, 2^64 - 1]}} 
    `i8                            {{Signed integer in the range of [-(2^7), 2^7 - 1]}} 
    `i16                           {{Signed integer in the range of [-(2^15), 2^15 - 1]}} 
    `i32                           {{Signed integer in the range of [[-(2^31), 2^31 - 1]}} 
    `i64                           {{Signed integer in the range of [-(2^63), 2^63 - 1]}} 
    `f32                           {{The 32-bit floating point type}} 
    `f64                           {{The 64-bit floating point type}} 

$ Machine-dependent Integer Types
    `usize                         {{Unsigned integer type with the same number of bits as the platform's pointer type}} 
    `isize                         {{Signed integer type with the same number of bits as the platform's pointer type}} 

$ Textual Types
    `char                          {{A Unicode scalar value (i.e. a code point that is not a surrogate), represented as a 32-bit unsigned word in the 0x0000 to 0xD7FF or 0xE000 to 0x10FFFF range}} 
    `str                           {{Unicode string, represented as an array of 8-bit unsigned bytes holding a sequence of UTF-8 code points}} 

$ Tuple Types
    `tuple                         {{Tuple types and values are denoted by listing the types or values of their elements, respectively, in a parenthesized, comma-separated list}} 

$ Array and Slice Types
    `array                         {{An array has a fixed size, and can be allocated on either the stack or the heap}} 
    `slice                         {{A slice is a 'view' into an array. It doesn't own the data it points to, it borrows it}} 
    `vector                        {{A dynamic or ‘growable’ array, implemented as a standard library type}} 

$ Structure Types
    `struct                        {{The memory layout of a struct is undefined by default to allow for compiler optimizations like field reordering, but it can be fixed with the #[repr(...)] attribute}} 
    `tuple struct                  {{Just like a structure type, except that the fields are anonymous}} 
    `unit-like struct              {{Like a structure type, except that it has no fields. The one value constructed by the associated structure expression is the only value that inhabits such a type}} 

$ Enumerated Types
    `enumerated type               {{A nominal, heterogeneous disjoint union type, denoted by the name of an enum item}} 
    `enum item                     {{Declares both the type and a number of variant constructors, each of which is independently named and takes an optional tuple of arguments}} 

$ Pointer Types
    `reference (&)                 {{Point to memory owned by some other value}} 
    `raw (*)                       {{Pointers without safety or liveness guarantees}} 

$ Closure Types
    `FnOnce                        {{It can be called once and closure called as FnOnce can move out values from its environment}} 
    `FnMut                         {{It can be called multiple times as mutable and closure called as FnMut can mutate values from its environment}} 
    `Fn                            {{It can be called multiple times through a shared reference and closure called as Fn can neither move out from nor mutate values from its environment}} 

