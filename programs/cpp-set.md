# C++ Set

> Source: http://www.cplusplus.com/reference/set/set/

> Aliases: cpp-sets, c++-sets, cpp-set-container, c++-set-container, c++-set

$ Iterators
    `myset.begin()                 {{Returns an iterator referring to the first element in the set container}} 
    `myset.end()                   {{Returns an iterator referring to the past-the-end element in the set container}} 
    `myset.rbegin()                {{Returns a reverse iterator pointing to the last element in the container}} 
    `myset.rend()                  {{Returns a reverse iterator pointing to the theoretical element right before the first element in the set container}} 
    `myset.cbegin()                {{Returns a const_iterator pointing to the first element in the container (C++11 only)}} 
    `myset.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `myset.crbegin()               {{Returns a const_reverse_iterator pointing to the last element in the container (C++11 only)}} 
    `myset.crend()                 {{Returns a const_reverse_iterator pointing to the element that would theoretically precede the first element in the container (C++11 only)}} 

$ Capacity
    `myset.empty()                 {{Returns whether the set container is empty}} 
    `myset.size()                  {{Returns the number of elements in the set container}} 
    `myset.max_size()              {{Returns the maximum number of elements that the set container can hold}} 

$ Modifiers
    `myset.insert(x)               {{Extends the container by inserting new elements, effectively increasing the container size by the number of elements inserted}} 
    `myset.erase(it)               {{Removes from the set container either a single element or a range of elements}} 
    `x.swap(y)                     {{Exchanges the content of the container by the content of x, which is another set of the same type}} 
    `myset.clear()                 {{Removes all elements from the set container (which are destroyed), leaving the container with a size of 0}} 
    `myset.emplace(x)              {{Inserts a new element in the set, if unique (C++11 only)}} 
    `myset.emplace_hint(it, x)     {{Inserts a new element in the set, if unique, with a hint on the insertion position (C++11 only)}} 

$ Observers
    `std::set<int>::key_compare mycomp = myset.key_comp()
>                                  {{Returns a copy of the comparison object used by the container}} 
    `std::set<int>::value_compare mycomp = myset.value_comp()
>                                  {{Returns a copy of the comparison object used by the container}} 

$ Operations
    `myset.find(x)                 {{Searches the container for an element equivalent to x and returns an iterator to it if found, otherwise it returns an iterator to set::end}} 
    `myset.count(x)                {{Searches the container for elements equivalent to x and returns the number of matches}} 
    `myset.lower_bound(x)          {{Returns an iterator pointing to the first element in the container which is not considered to go before x}} 
    `myset.upper_bound(x)          {{Returns an iterator pointing to the first element in the container which is considered to go after x}} 
    `myset.equal_range(x)          {{Returns the bounds of a range that includes all the elements in the container that are equivalent to x}} 

$ Allocator
    `myset.get_allocator()         {{Returns a copy of the allocator object associated with the set}} 

