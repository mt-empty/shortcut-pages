# C++ Unordered Set

> Source: http://www.cplusplus.com/reference/unordered_set/unordered_set/

> Aliases: c++-unordered-sets, c++-unordered-set-container, cpp-unordered-set-container, cpp-unordered-sets, c++-unordered-sets-container, cpp-unordered-sets-container, c++-unordered-set

$ Capacity
    `myset.empty()                 {{Returns a bool value indicating whether the unordered_set container is empty, i.e. whether its size is 0}} 
    `myset.size()                  {{Returns the number of elements in the unordered_set container}} 
    `myset.max_size()              {{Returns the maximum number of elements that the unordered_set container can hold}} 

$ Iterators
    `myset.begin()                 {{Returns an iterator pointing to the first element in the unordered_set container or in one of its buckets}} 
    `myset.end()                   {{Returns an iterator pointing to the past-the-end element in the unordered_set container or in one of its buckets}} 
    `myset.cbegin()                {{Returns a const_iterator pointing to the first element in the unordered_set container or in one of its buckets}} 
    `myset.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the unordered_set container or in one of its buckets}} 

$ Element Lookup
    `myset.find(k)                 {{Searches the container for an element with k as value and returns an iterator to it if found, otherwise it returns an iterator to unordered_set::end (the element past the end of the container)}} 
    `myset.count(k)                {{Searches the container for elements with a value of k and returns the number of elements found. Because unordered_set containers do not allow for duplicate values, this means that the function actually returns 1 if an element with that value exists in the container, and zero otherwise}} 
    `myset.equal_range(k)          {{Returns the bounds of a range that includes all the elements that compare equal to k. In unordered_set containers, where keys are unique, the range will include one element at most}} 

$ Modifiers
    `myset.emplace(k)              {{Inserts a new element in the unordered_set if its value is unique. This new element is constructed in place using args as the arguments for the element's constructor}} 
    `myset.emplace_hint(k)         {{Inserts a new element in the unordered_set if its value is unique. This new element is constructed in place using args as the arguments for the element's constructor. position points to a location in the container suggested as a hint on where to start the search for its insertion point}} 
    `myset.insert(k)               {{Inserts new elements in the unordered_set}} 
    `myset.erase(k)                {{Removes from the unordered_set container either a single element or a range of elements ([first,last))}} 
    `myset.clear()                 {{All the elements in the unordered_set container are dropped: their destructors are called, and they are removed from the container, leaving it with a size of 0}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of `second`, which is another unordered_set object containing elements of the same type}} 

$ Buckets
    `myset.bucket_count()          {{Returns the number of buckets in the unordered_set container}} 
    `myset.max_bucket_count()      {{Returns the maximum number of buckets that the unordered_set container can have}} 
    `myset.bucket_size(n)          {{Returns the number of elements in bucket n}} 
    `myset.bucket(k)               {{Returns the bucket number where the element with value k is located}} 

$ Hash Policy
    `myset.load_factor()           {{Returns the current load factor in the unordered_set container}} 
    `myset.max_load_factor()       {{Returns the current maximum load factor for the unordered_set container}} 
    `myset.max_load_factor(z)      {{Sets z as the new maximum load factor for the unordered_set container}} 
    `myset.rehash(n)               {{Sets the number of buckets in the container to n or more}} 
    `myset.reserve(n)              {{Sets the number of buckets in the container (bucket_count) to the most appropriate to contain at least n elements}} 

$ Observers
    `stringset::hasher fn = myset.hash_function()
>                                  {{Returns the hash function object used by the unordered_set container}} 
    `bool case_insensitive = myset.key_eq()('test', 'Test');
>                                  {{Returns the key equivalence comparison predicate used by the unordered_set container}} 
    `myset.get_allocator()         {{Returns the allocator object used to construct the container}} 

$ Non Member Function Overloads
    `Operator ==, !=               {{These overloaded global operator functions perform the appropriate equality or inequality comparison operation between the unordered_set containers lhs and rhs}} 
    `swap(first, second)           {{The contents of container `first` are exchanged with those of `second`. Both container objects must be of the same type}} 

