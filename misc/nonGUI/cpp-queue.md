# C++ Queue

> Source: http://www.cplusplus.com/reference/queue/queue/

> Aliases: cpp-queues, cpp-queues-container

$ Member Functions
    `myqueue.empty()               {{Returns whether the queue is empty}} 
    `myqueue.size()                {{Returns the number of elements in the queue}} 
    `myqueue.front()               {{Returns a reference to the next element in the queue}} 
    `myqueue.back()                {{Returns a reference to the last element in the queue. This is the 'new' element in the queue}} 
    `myqueue.push(x)               {{Inserts a new element at the end of the queue, after its current last element}} 
    `myqueue.emplace(x)            {{Adds a new element at the end of the queue, after its current last element. This new element is constructed in place passing args as the arguments for its constructor (C++11 only)}} 
    `myqueue.pop()                 {{Removes the next element in the queue, effectively reducing its size by one}} 
    `foo.swap(bar)                 {{Exchanges the contents of the container adaptor (*this) by those of x (C++11 only)}} 

$ Function Overloads
    `Operator ==, !=, <, <=, >, >= {{Compares the contents of the underlying containers of two container adaptors. The comparison is done by applying the corresponding operator to the underlying containers}} 
    `swap(x, y)                    {{Exchanges the contents of x and y (C++11 only)}} 

$ Helper Classes
    `uses_allocator<std::queue>    {{Provides a transparent specialization of the std::uses_allocator type trait for std::queue: the container adaptor uses allocator if and only if the underlying container does (C++11 only)}} 

