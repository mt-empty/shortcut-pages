# C++ Bitset

> Source: http://www.cplusplus.com/reference/bitset/bitset/

> Aliases: cpp-bitset-container, c++-bitset, c++-bitset-container

$ Construct Bitset
    `std::bitset<4> foo            {{Constructs a bitset container object}} 

$ Bit Access
    `foo[pos]                      {{The function returns the value (or a reference) to the bit at position pos}} 
    `foo.count()                   {{Returns the number of bits in the bitset that are set}} 
    `foo.size()                    {{Returns the number of bits in the bitset}} 
    `foo.test(pos)                 {{Returns whether the bit at position pos is set (i.e., whether it is one)}} 
    `foo.any()                     {{Returns whether any of the bits is set (i.e., whether at least one bit in the bitset is set to one)}} 
    `foo.none()                    {{Returns whether none of the bits is set (i.e., whether all bits in the bitset have a value of zero)}} 
    `foo.all()                     {{Returns whether all of the bits in the bitset are set (to one) (C++11 only)}} 

$ Bit Operations
    `foo.set()                     {{Sets (to one) all bits in the bitset}} 
    `foo.set(pos)                  {{Sets val as the value for the bit at position pos}} 
    `foo.reset()                   {{Resets (to zero) all bits in the bitset}} 
    `foo.reset(pos)                {{Resets (to zero) the bit at position pos}} 
    `foo.flip()                    {{Flips all bits in the bitset}} 
    `foo.flip(pos)                 {{Flips the bit at position pos}} 

$ Bitset Operations
    `foo.to_string()               {{Returns a string representing the bits in the bitset}} 
    `foo.to_ulong()                {{Returns an unsigned long with the integer value that has the same bits set as the bitset}} 
    `foo.to_ullong()               {{Returns an unsigned long long with the integer value that has the same bits set as the bitset (C++11 only)}} 

$ Non Member Function Overloads
    `Operator &, |, ^, <<, >>      {{Performs the proper bitwise operation using the contents of the bitset}} 

