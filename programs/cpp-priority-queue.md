# C++ Priority Queue

> Source: http://www.cplusplus.com/reference/queue/priority_queue/

> Aliases: cpp-priority-queues-container, c++-priority-queue, c++-priority-queue-container, cpp-priority-queues

$ Member Functions
    `mypq.empty()                  {{Returns whether the priority_queue is empty}} 
    `mypq.size()                   {{Returns the number of elements in the priority_queue}} 
    `mypq.top()                    {{Returns a constant reference to the top element in the priority_queue}} 
    `mypq.push(x)                  {{Inserts a new element in the priority_queue. The content of this new element is initialized to val}} 
    `mypq.emplace(x)               {{Adds a new element to the priority_queue. This new element is constructed in place passing args as the arguments for its constructor (C++11 only)}} 
    `mypq.pop()                    {{Removes the element on top of the priority_queue, effectively reducing its size by one. The element removed is the one with the highest value}} 
    `foo.swap(bar)                 {{Exchanges the contents of the container adaptor by those of x, swapping both the underlying container value and their comparison function using the corresponding swap non-member functions (C++11 only)}} 

$ Function Overloads
    `swap(x, y)                    {{Exchanges the contents of x and y (C++11 only)}} 

$ Helper Classes
    `uses_allocator<std::queue>    {{Provides a transparent specialization of the std::uses_allocator type trait for std::priority_queue, the container adaptor uses allocator if and only if the underlying container does (C++11 only)}} 

