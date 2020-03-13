# C++ Multimap

> Source: http://www.cplusplus.com/reference/map/multimap/

> Aliases: c++-multimaps, c++-multimap

$ Iterators
    `mymultimap.begin()            {{Returns an iterator referring to the first element in the multimap container}} 
    `mymultimap.end()              {{Returns an iterator referring to the past-the-end element in the multimap container}} 
    `mymultimap.rbegin()           {{Returns a reverse iterator pointing to the last element in the container}} 
    `mymultimap.rend()             {{Returns a reverse iterator pointing to the theoretical element right before the first element in the multimap container}} 
    `mymultimap.cbegin()           {{Returns a const_iterator pointing to the first element in the container (C++11 only)}} 
    `mymultimap.cend()             {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `mymultimap.crbegin()          {{Returns a const_reverse_iterator pointing to the last element in the container (C++11 only)}} 
    `mymultimap.crend()            {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the container (C++11 only)}} 

$ Capacity
    `mymultimap.size()             {{Returns the number of elements in the multimap container}} 
    `mymultimap.max_size()         {{Returns the maximum number of elements that the multimap container can hold}} 
    `mymultimap.empty()            {{Returns whether the multimap container is empty}} 

$ Modifiers
    `mymultimap.insert(pair<char,int>(k, v))
>                                  {{Extends the container by inserting new elements, effectively increasing the container size by the number of elements inserted}} 
    `mymultimap.erase(it)          {{Removes elements from the multimap container}} 
    `y.swap(x)                     {{Exchanges the content of the container by the content of x, which is another multimap of the same type}} 
    `mymultimap.clear()            {{Removes all elements from the multimap container (which are destroyed), leaving the container with a size of 0}} 
    `mymultimap.emplace(k, v)      {{Inserts a new element in the multimap. This new element is constructed in place using args as the arguments for the construction of a value_type (C++11 only)}} 
    `mymap.emplace_hint(it, k, v)  {{Inserts a new element in the multimap, with a hint on the insertion position. This new element is constructed in place using args as the arguments for the construction of a value_type (C++11 only)}} 

$ Observers
    `mymultimap.key_comp()         {{Returns a copy of the comparison object used by the container to compare keys}} 
    `mymap.value_comp()            {{Returns a comparison object that can be used to compare two elements to get whether the key of the first one goes before the second}} 

$ Operations
    `mymultimap.find(k)            {{Searches the container for an element with a key equivalent to k and returns an iterator to it if found, otherwise it returns an iterator to multimap::end}} 
    `mymultimap.count(k)           {{Searches the container for elements with a key equivalent to k and returns the number of matches}} 
    `mymultimap.lower_bound(k)     {{Returns an iterator pointing to the first element in the container whose key is not considered to go before k}} 
    `mymultimap.upper_bound(k)     {{Returns an iterator pointing to the first element in the container whose key is considered to go after k}} 
    `mymap.equal_range(k)          {{Returns the bounds of a range that includes all the elements in the container which have a key equivalent to k}} 

$ Allocator
    `mymultimap.get_allocator()    {{Returns a copy of the allocator object associated with the multimap}} 

