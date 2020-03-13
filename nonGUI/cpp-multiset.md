# C++ Multiset

> Source: http://www.cplusplus.com/reference/set/multiset/

> Aliases: c++-multiset, cpp-multiset-container, cpp-multisets, c++-multiset-container, c++-multisets

$ Iterators
    `mymultiset.begin()            {{Returns an iterator referring to the first element in the multiset container}} 
    `mymultiset.end()              {{Returns an iterator referring to the past-the-end element in the multiset container}} 
    `mymultiset.rbegin()           {{Returns a reverse iterator pointing to the last element in the container (i.e., its reverse beginning)}} 
    `mymultiset.rend()             {{Returns a reverse iterator pointing to the theoretical element right before the first element in the multiset container}} 
    `mymultiset.cbegin()           {{Returns a const_iterator pointing to the first element in the container (C++11 only)}} 
    `mymultiset.cend()             {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `mymultiset.crbegin()          {{Returns a const_reverse_iterator pointing to the last element in the container (i.e., its reverse beginning) (C++11 only)}} 
    `mymultiset.crend()            {{Returns a const_reverse_iterator pointing to the element that would theoretically precede the first element in the container (C++11 only)}} 

$ Capacity
    `mymultiset.empty()            {{Returns whether the multiset container is empty (i.e. whether its size is 0)}} 
    `mymultiset.size()             {{Returns the number of elements in the multiset container}} 
    `mymultiset.max_size()         {{Returns the maximum number of elements that the multiset container can hold}} 

$ Modifiers
    `mymultiset.insert(x)          {{Extends the container by inserting new elements, effectively increasing the container size by the number of elements inserted}} 
    `mymultiset.erase(it)          {{Removes elements from the multiset container}} 
    `x.swap(y)                     {{Exchanges the content of the container by the content of x, which is another multiset of the same type}} 
    `mymultiset.clear()            {{Removes all elements from the multiset container (which are destroyed), leaving the container with a size of 0}} 
    `mymultiset.emplace(x)         {{Inserts a new element in the multiset (C++11 only)}} 
    `mymultiset.emplace_hint(it, x)
>                                  {{Inserts a new element in the multiset, with a hint on the insertion position (C++11 only)}} 

$ Observers
    `std::multiset<int>::key_compare mycomp = mymultiset.key_comp()
>                                  {{Returns a copy of the comparison object used by the container}} 
    `std::multiset<int>::value_compare mycomp = mymultiset.value_comp()
>                                  {{Returns a copy of the comparison object used by the container}} 

$ Operations
    `mymultiset.find(x)            {{Searches the container for an element equivalent to x and returns an iterator to it if found, otherwise it returns an iterator to multiset::end}} 
    `mymultiset.count(x)           {{Searches the container for elements equivalent to x and returns the number of matches}} 
    `mymultiset.lower_bound(x)     {{Returns an iterator pointing to the first element in the container which is not considered to go before x}} 
    `mymultiset.upper_bound(x)     {{Returns an iterator pointing to the first element in the container which is considered to go after x}} 
    `mymultiset.equal_range(x)     {{Returns the bounds of a range that includes all the elements in the container that are equivalent to x}} 

$ Allocator
    `mymultiset.get_allocator()    {{Returns a copy of the allocator object associated with the multiset}} 

