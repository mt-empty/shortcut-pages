# C++ Unordered Multimap

> Source: http://www.cplusplus.com/reference/unordered_map/unordered_multimap/

> Aliases: cpp-unordered-multimaps, cpp-unordered-multimap-container, cpp-unordered-multimaps-container

$ Capacity
    `myumm.empty()                 {{Returns a bool value indicating whether the unordered_multimap container is empty, i.e. whether its size is 0}} 
    `myumm.size()                  {{Returns the number of elements in the unordered_multimap container}} 
    `myumm.max_size()              {{Returns the maximum number of elements that the unordered_multimap container can hold}} 

$ Iterators
    `myumm.begin()                 {{Returns an iterator pointing to the first element in the unordered_multimap container or in one of its buckets}} 
    `myumm.end()                   {{Returns an iterator pointing to the past-the-end element in the unordered_multimap container or in one of its buckets}} 
    `myumm.cbegin()                {{Returns a const_iterator pointing to the first element in the unordered_multimap container or in one of its buckets}} 
    `myumm.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the unordered_multimap container or in one of its buckets}} 

$ Element Lookup
    `myumm.find(k)                 {{Searches the container for an element with k as key and returns an iterator to it if found, otherwise it returns an iterator to unordered_multimap::end}} 
    `myumm.count(k)                {{Searches the container for elements whose key is k and returns the number of elements found}} 
    `myumm.equal_range(k)          {{Returns the bounds of a range that includes all the elements in the container with a key that compares equal to k}} 

$ Modifiers
    `myumm.emplace(k, v)           {{Inserts a new element in the unordered_multimap}} 
    `myumm.emplace_hint(k, v)      {{Inserts a new element in the unordered_multimap container with hint}} 
    `myumm.insert({k, v})          {{Inserts new elements in the unordered_multimap}} 
    `myumm.erase(k)                {{Removes from the unordered_multimap container either the elements whose key is k or those in a range ([first,last))}} 
    `myumm.clear()                 {{All the elements in the unordered_multimap container are dropped: their destructors are called, and they are removed from the container, leaving it with a size of 0}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of umm, which is another unordered_multimap object containing elements of the same type}} 

$ Buckets
    `myumm.bucket_count()          {{Returns the number of buckets in the unordered_multimap container}} 
    `myumm.max_bucket_count()      {{Returns the maximum number of buckets that the unordered_multimap container can have}} 
    `myumm.bucket_size(n)          {{Returns the number of elements in bucket n}} 
    `myumm.bucket(k)               {{Returns the bucket number where the elements with key k are located}} 

$ Hash Policy
    `myumm.load_factor()           {{Returns the current load factor in the unordered_multimap container}} 
    `myumm.max_load_factor()       {{Returns the current maximum load factor for the unordered_multimap container}} 
    `myumm.max_load_factor(z)      {{Sets z as the new maximum load factor for the unordered_multimap container}} 
    `myumm.rehash(n)               {{Sets the number of buckets in the container to n or more}} 
    `myumm.reserve(n)              {{Sets the number of buckets in the container (bucket_count) to the most appropriate to contain at least n elements}} 

$ Observers
    `stringmap::hasher fn = myumm.hash_function()
>                                  {{Returns the hash function object used by the unordered_multimap container}} 
    `bool case_insensitive = myumm.key_eq()('test', 'TEST')
>                                  {{Returns the key equivalence comparison predicate used by the unordered_multimap container}} 
    `myumm.get_allocator()         {{Returns the allocator object used to construct the container}} 

$ Non Member Function Overloads
    `Operator ==, !=               {{These overloaded global operator functions perform the appropriate equality or inequality comparison operation between the unordered_multimap containers lhs and rhs}} 
    `swap(first, second)           {{The contents of container lhs are exchanged with those of rhs}} 

