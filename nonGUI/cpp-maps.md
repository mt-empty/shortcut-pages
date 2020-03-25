# C++ Map

> Source: http://www.cplusplus.com/reference/map/map/

> Aliases: cpp-map

$ Iterators
    `mymap.begin()                 {{Returns an iterator referring to the first element in the map container}} 
    `mymap.end()                   {{Returns an iterator referring to the past-the-end element in the map container}} 
    `mymap.rbegin()                {{Returns a reverse iterator pointing to the last element in the container}} 
    `mymap.rend()                  {{Returns a reverse iterator pointing to the theoretical element right before the first element in the map container}} 
    `mymap.cbegin()                {{Returns a const_iterator pointing to the first element in the container (C++11 only)}} 
    `mymap.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `mymap.crbegin()               {{Returns a const_reverse_iterator pointing to the last element in the container (C++11 only)}} 
    `mymap.crend()                 {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the container (C++11 only)}} 

$ Capacity
    `mymap.size()                  {{Returns the number of elements in the map container}} 
    `mymap.max_size()              {{Returns the maximum number of elements that the map container can hold}} 
    `mymap.empty()                 {{Returns whether the map container is empty}} 

$ Element Access
    `mymapi                        {{Returns a reference to the value that is mapped to a key equivalent to key, performing an insertion if such key does not already exist}} 
    `mymap.at(k)                   {{Returns a reference to the mapped value of the element identified with key k (C++11 only)}} 

$ Modifiers
    `mymap.insert(std::pair<char,int>(k, v))
>                                  {{Inserts element(s) into the container, if the container doesn't already contain an element with an equivalent key}} 
    `mymap.erase(it)               {{Removes from the map container either a single element or a range of elements}} 
    `y.swap(x)                     {{Exchanges the content of the container by the content of x, which is another map of the same type}} 
    `mymap.clear()                 {{Removes all elements from the map container (which are destroyed), leaving the container with a size of 0}} 
    `mymap.emplace(k, v)           {{Inserts a new element in the map if its key is unique. This new element is constructed in place using args as the arguments for the construction of a value_type  (C++11 only)}} 
    `mymap.emplace_hint(it, k, v)  {{Inserts a new element in the map if its key is unique, with a hint on the insertion position. This new element is constructed in place using args as the arguments for the construction of a value_type (C++11 only)}} 

$ Observers
    `mymap.key_comp()              {{Returns a copy of the comparison object used by the container to compare keys}} 
    `mymap.value_comp()            {{Returns a comparison object that can be used to compare two elements to get whether the key of the first one goes before the second}} 

$ Operations
    `mymap.find(k)                 {{Searches the container for an element with a key equivalent to k and returns an iterator to it if found, otherwise it returns an iterator to map::end}} 
    `mymap.count(k)                {{Searches the container for elements with a key equivalent to k and returns the number of matches}} 
    `mymap.lower_bound(k)          {{Returns an iterator pointing to the first element in the container whose key is not considered to go before k}} 
    `mymap.upper_bound(k)          {{Returns an iterator pointing to the first element in the container whose key is considered to go after k}} 
    `mymap.equal_range(k)          {{Returns the bounds of a range that includes all the elements in the container which have a key equivalent to k}} 

$ Allocator
    `mymap.get_allocator()         {{Returns a copy of the allocator object associated with the map}} 

