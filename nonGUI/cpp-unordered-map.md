# C++ Unordered Map

> Source: http://www.cplusplus.com/reference/unordered_map/unordered_map/

> Aliases: cpp-unordered-maps-container, cpp-unordered-map-container, c++-unordered-maps-container, cpp-unordered-maps, c++-unordered-maps, c++-unordered-map, c++-unordered-map-container

$ Capacity
    `umap.empty()                  {{Returns a bool value indicating whether the unordered_map container is empty, i.e. whether its size is 0}} 
    `umap.size()                   {{Returns the number of elements in the unordered_map container}} 
    `umap.max_size()               {{Returns the maximum number of elements that the unordered_map container can hold}} 

$ Iterators
    `umap.begin()                  {{Returns an iterator pointing to the first element in the unordered_map container or in one of its buckets}} 
    `umap.end()                    {{Returns an iterator pointing to the past-the-end element in the unordered_map container or in one of its buckets}} 
    `umap.cbegin()                 {{Returns a const_iterator pointing to the first element in the unordered_map container or in one of its buckets}} 
    `umap.cend()                   {{Returns a const_iterator pointing to the past-the-end element in the unordered_map container or in one of its buckets}} 

$ Element Access
    `umap[k]                       {{If k matches the key of an element in the container, the function returns a reference to its mapped value; If k does not match the key of any element in the container, the function inserts a new element with that key and returns a reference to its mapped value}} 
    `umap.at(k)                    {{Returns a reference to the mapped value of the element with key k in the unordered_map}} 

$ Element Lookup
    `umap.find(k)                  {{Searches the container for an element with k as key and returns an iterator to it if found, otherwise it returns an iterator to unordered_map::end}} 
    `umap.count(k)                 {{Searches the container for elements whose key is k and returns the number of elements found}} 
    `umap.equal_range(k)           {{Returns the bounds of a range that includes all the elements in the container with a key that compares equal to k}} 

$ Modifiers
    `umap.emplace(k, v)            {{Inserts a new element in the unordered_map if its key is unique}} 
    `umap.emplace_hint(k, v)       {{Inserts a new element in the unordered_map if its key is unique with hint}} 
    `umap.insert({k, v})           {{Inserts new elements in the unordered_map}} 
    `umap.erase(k)                 {{Removes from the unordered_map container either a single element or a range of elements ([first,last))}} 
    `umap.clear()                  {{All the elements in the unordered_map container are dropped: their destructors are called, and they are removed from the container, leaving it with a size of 0}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of second, which is another unordered_map object containing elements of the same type}} 

$ Buckets
    `umap.bucket_count()           {{Returns the number of buckets in the unordered_map container}} 
    `umap.max_bucket_count()       {{Returns the maximum number of buckets that the unordered_map container can have}} 
    `umap.bucket_size(n)           {{Returns the number of elements in bucket n}} 
    `umap.bucket(k)                {{Returns the bucket number where the element with key k is located}} 

$ Hash Policy
    `umap.load_factor()            {{Returns the current load factor in the unordered_map container}} 
    `umap.max_load_factor()        {{Returns the current maximum load factor for the unordered_map container}} 
    `umap.max_load_factor(z)       {{Sets z as the new maximum load factor for the unordered_map container}} 
    `umap.rehash(n)                {{Sets the number of buckets in the container to n or more}} 
    `umap.reserve(n)               {{Sets the number of buckets in the container (bucket_count) to the most appropriate to contain at least n elements}} 

$ Observers
    `stringmap::hasher fn = umap.hash_function()
>                                  {{Returns the hash function object used by the unordered_map container}} 
    `bool case_insensitive = umap.key_eq()('test', 'TEST')
>                                  {{Returns the key equivalence comparison predicate used by the unordered_map container}} 
    `umap.get_allocator()          {{Returns the allocator object used to construct the container}} 

$ Non Member Function Overloads
    `Operator ==, !=               {{These overloaded global operator functions perform the appropriate equality or inequality comparison operation between the unordered_map containers lhs and rhs}} 
    `swap(first, second)           {{The contents of container lhs are exchanged with those of rhs}} 

