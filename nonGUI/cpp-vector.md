# C++ Vector

> Source: http://www.cplusplus.com/reference/vector/vector/

> Aliases: cpp-vectors

$ Iterators
    `myvector.begin()              {{Returns an iterator pointing to the first element in the vector}} 
    `myvector.end()                {{Returns an iterator referring to the past-the-end element in the vector container}} 
    `myvector.rbegin()             {{Returns a reverse iterator pointing to the last element in the vector}} 
    `myvector.rend()               {{Returns a reverse iterator pointing to the theoretical element preceding the first element in the vector}} 
    `myvector.cbegin()             {{Returns a const_iterator pointing to the first element in the container (C++ 11 Only)}} 
    `myvector.cend()               {{Returns a const_iterator pointing to the past-the-end element in the container (C++ 11 Only)}} 
    `myvector.crbegin()            {{Returns a const_reverse_iterator to the reverse beginning of the sequence (C++ 11 Only)}} 
    `myvector.crend()              {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the container (C++ 11 Only)}} 

$ Capacity
    `myvector.size()               {{Returns the number of elements in the vector}} 
    `myvector.max_size()           {{Returns the maximum number of elements that the vector can hold}} 
    `myvector.resize()             {{Resizes the container so that it contains n elements}} 
    `myvector.capacity()           {{Returns the size of the storage space currently allocated for the vector}} 
    `myvector.empty()              {{Returns whether the vector is empty}} 
    `myvector.reserve()            {{Requests that the vector capacity be at least enough to contain n elements}} 
    `myvector.shrink_to_fit()      {{Requests the container to reduce its capacity to fit its size (C++ 11 Only)}} 

$ Element Access
    `myvectorn                     {{Returns a reference to the element at position n in the vector container}} 
    `myvector.at(n)                {{Returns a reference to the element at position n in the vector}} 
    `myvector.front()              {{Returns a reference to the first element in the vector}} 
    `myvector.back()               {{Returns a reference to the last element in the vector}} 
    `myvector.data()               {{Returns a direct pointer to the memory array used internally by the vector to store its owned elements (C++ 11 Only)}} 

$ Modifiers
    `myvector.assign(n, v)         {{Assigns new contents to the vector, replacing its current contents, and modifying its size accordingly}} 
    `myvector.push_back(v)         {{Adds a new element at the end of the vector, after its current last element}} 
    `myvector.pop_back()           {{ Removes the last element in the vector, effectively reducing the container size by one}} 
    `myvector.insert(it, n, v)     {{The vector is extended by inserting new elements before the element at the specified position}} 
    `myvector.erase(myvector.begin() + n)
>                                  {{Removes from the vector either a single element (position) or a range of elements ([first, last])}} 
    `myvector.swap(x)              {{Exchanges the content of the container by the content of x, which is another vector object of the same type}} 
    `myvector.clear()              {{Removes all elements from the vector (which are destroyed), leaving the container with a size of 0}} 
    `myvector.emplace(myvector.begin() + 1, n)
>                                  {{The container is extended by inserting a new element at position (C++ 11 Only)}} 
    `myvector.emplace_back(n)      {{Inserts a new element at the end of the vector, right after its current last element (C++ 11 Only)}} 

$ Allocator
    `myvector.get_allocator()      {{Returns a copy of the allocator object associated with the vector}} 

