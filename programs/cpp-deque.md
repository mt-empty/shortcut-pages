# C++ Deque

> Source: http://www.cplusplus.com/reference/deque/deque/

> Aliases: c++-double-ended-queue, cpp-double-ended-queue, c++-deque

$ Iterators
    `deque.begin()                 {{Returns an iterator pointing to the first element in the deque container}} 
    `deque.end()                   {{Returns an iterator referring to the past-the-end element in the deque container}} 
    `deque.rbegin()                {{Returns a reverse iterator pointing to the last element in the container}} 
    `deque.rend()                  {{Returns a reverse iterator pointing to the theoretical element preceding the first element in the deque container}} 
    `deque.cbegin()                {{Returns a const_iterator pointing to the first element in the container (C++ 11 only)}} 
    `deque.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `deque.crbegin()               {{Returns a const_reverse_iterator pointing to the last element in the container (C++11 only)}} 
    `deque.crend()                 {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the container (C++11 only)}} 

$ Capacity
    `deque.size()                  {{Returns the number of elements in the deque container}} 
    `deque.max_size()              {{Returns the maximum number of elements that the deque container can hold}} 
    `deque.resize()                {{Resizes the container so that it contains n elements}} 
    `deque.empty()                 {{Returns whether the deque container is empty}} 
    `deque.shrink_to_fit()         {{Requests the container to reduce its memory usage to fit its size (C++11 only)}} 

$ Element Access
    `dequei                        {{Returns a reference to the element at position n in the deque container}} 
    `deque.at(i)                   {{Returns a reference to the element at position n in the deque container object}} 
    `deque.front()                 {{Returns a reference to the first element in the deque container}} 
    `deque.back()                  {{Returns a reference to the last element in the container}} 

$ Modifiers
    `deque.assign(5, 'a')          {{Assigns new contents to the deque container, replacing its current contents, and modifying its size accordingly}} 
    `deque.push_back(x)            {{Adds a new element at the end of the deque container, after its current last element}} 
    `deque.push_front(x)           {{Inserts a new element at the beginning of the deque container, right before its current first element}} 
    `deque.pop_back()              {{Removes the last element in the deque container, effectively reducing the container size by one}} 
    `deque.pop_front()             {{Removes the first element in the deque container, effectively reducing its size by one}} 
    `deque.insert(it,10)           {{Inserts elements at the specified location in the container}} 
    `deque.erase (deque.begin()+5) {{Removes from the deque container either a single element (position) or a range of elements ([first,last))}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of x, which is another deque object containing elements of the same type}} 
    `deque.clear()                 {{Removes all elements from the deque (which are destroyed), leaving the container with a size of 0}} 
    `deque.emplace(it, x)          {{The container is extended by inserting a new element at position (C++11 only)}} 
    `deque.emplace_front(x)        {{Inserts a new element at the beginning of the deque, right before its current first element (C++11 only)}} 
    `deque.emplace_back(x)         {{Inserts a new element at the end of the deque, right after its current last element (C++11 only)}} 

$ Allocator
    `deque.get_allocator()         {{Returns a copy of the allocator object associated with the deque object}} 

$ Function Overloads
    `Operators: ==, !=, <, <=, >, >=
>                                  {{Performs the appropriate comparison operation between the deque containers lhs and rhs}} 
    `swap(x, y)                    {{Contents of container x are exchanged with those of y}} 

