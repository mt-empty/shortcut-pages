# C++ Unordered Multiset

> Source: http://www.cplusplus.com/reference/unordered_set/unordered_multiset/

> Aliases: c++-unordered-multiset, cpp-unordered-multisets-container, c++-unordered-multisets-container, cpp-unordered-multisets, c++-unordered-multiset-container, cpp-unordered-multiset-container, c++-unordered-multisets

$ Capacity
    `myset.empty()                 {{Returns a bool value indicating whether the unordered_multiset container is empty, i.e. whether its size is 0}} 
    `myset.size()                  {{Returns the number of elements in the unordered_multiset container}} 
    `myset.max_size()              {{Returns the maximum number of elements that the unordered_multiset container can hold}} 

$ Iterators
    `myset.begin()                 {{Returns an iterator pointing to the first element in the unordered_multiset container or in one of its buckets}} 
    `myset.end()                   {{Returns an iterator pointing to the past-the-end element in the unordered_multiset container or in one of its buckets}} 
    `myset.cbegin()                {{Returns a const_iterator pointing to the first element in the unordered_multiset container or in one of its buckets}} 
    `myset.cend()                  {{Returns a const_iterator pointing to the past-the-end element in the unordered_multiset container or in one of its buckets}} 

$ Element Lookup
    `myset.find(k)                 {{Searches the container for an element with k as key and returns an iterator to it if found, otherwise it returns an iterator to unordered_multiset::end}} 
    `myset.count(k)                {{Searches the container for elements with a value of k and returns the number of elements found}} 
    `myset.equal_range(k)          {{Returns the bounds of a range that includes all the elements in the container that compare equal to k}} 

$ Modifiers
    `myset.emplace(k)              {{Inserts a new element in the unordered_multiset. This new element is constructed in place using args as the arguments for the element's constructor}} 
    `myset.emplace_hint(k)         {{Inserts a new element in the unordered_multiset. This new element is constructed in place using args as the arguments for the element's constructor. Position points to a location in the container suggested as a hint on where to start the search for its insertion point}} 
    `myset.insert(k)               {{Inserts new elements in the unordered_multiset}} 
    `myset.erase(k)                {{Removes from the unordered_multiset container either the elements whose value is k or a range of elements ([first,last))}} 
    `myset.clear()                 {{All the elements in the unordered_multiset container are dropped: their destructors are called, and they are removed from the container, leaving it with a size of 0}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of ums, which is another unordered_multiset object containing elements of the same type}} 

$ Buckets
    `myset.bucket_count()          {{Returns the number of buckets in the unordered_multiset container}} 
    `myset.max_bucket_count()      {{Returns the maximum number of buckets that the unordered_multiset container can have}} 
    `myset.bucket_size(n)          {{Returns the number of elements in bucket n}} 
    `myset.bucket(k)               {{Returns the bucket number where the elements with value k is located}} 

$ Hash Policy
    `myset.load_factor()           {{Returns the current load factor in the unordered_multiset container}} 
    `myset.max_load_factor()       {{Returns the current maximum load factor for the unordered_multiset container}} 
    `myset.max_load_factor(z)      {{Sets z as the new maximum load factor for the unordered_multiset container}} 
    `myset.rehash(n)               {{Sets the number of buckets in the container to n or more}} 
    `myset.reserve(n)              {{Sets the number of buckets in the container (bucket_count) to the most appropriate to contain at least n elements}} 

$ Observers
    `stringset::hasher fn = myset.hash_function()
>                                  {{Returns the hash function object used by the unordered_multiset container}} 
    `bool case_insensitive = myset.key_eq()('test', 'Test');
>                                  {{Returns the key equivalence comparison predicate used by the unordered_multiset container}} 
    `myset.get_allocator()         {{Returns the allocator object used to construct the container}} 

$ Non Member Function Overloads
    `Operator ==, !=               {{These overloaded global operator functions perform the appropriate equality or inequality comparison operation between the unordered_multiset containers lhs and rhs}} 
    `swap(first, second)           {{The contents of container `first` are exchanged with those of `second`. Both container objects must be of the same type (same template parameters), although sizes may differ}} 

