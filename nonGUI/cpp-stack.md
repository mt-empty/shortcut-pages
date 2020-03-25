# C++ Stack

> Source: http://www.cplusplus.com/reference/stack/stack/

$ Member Functions
    `mystack.empty()               {{Returns whether the stack is empty: i.e. whether its size is zero}} 
    `mystack.size()                {{Returns the number of elements in the stack}} 
    `mystack.top()                 {{Returns a reference to the top element in the stack}} 
    `mystack.push(n)               {{Inserts a new element at the top of the stack, above its current top element}} 
    `mystack.emplace(x)            {{Adds a new element at the top of the stack, above its current top element (C++11 only)}} 
    `mystack.pop()                 {{Removes the element on top of the stack, effectively reducing its size by one}} 
    `y.swap(x)                     {{Exchanges the contents of the container adaptor (*this) by those of x (C++11 only)}} 

$ Non-member Function Overloads
    `Operator ==, !=, <, <=, >, >= {{Compares the contents of the underlying containers of two container adaptors}} 
    `swap(x, y)                    {{Exchanges the contents of x and y (C++11 only)}} 

$ Non-member Class Specializations
    `uses_allocator<stack>         {{Provides a transparent specialization of the std::uses_allocator type trait for std::stack: the container adaptor uses allocator if and only if the underlying container does (C++11 only)}} 

