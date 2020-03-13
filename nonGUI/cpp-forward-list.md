# C++ Forward List

> Source: http://www.cplusplus.com/reference/forward_list/forward_list/

> Aliases: cpp-forward_list, c++-forward_list, c++-forward-list-library, c++-forward-list

$ Iterators
    `mylist.before_begin()         {{Returns an iterator pointing to the position before the first element in the container}} 
    `mylist.begin()                {{Returns an iterator pointing to the first element in the forward_list container}} 
    `mylist.end()                  {{Returns an iterator referring to the past-the-end element in the forward_list container}} 
    `mylist.cbefore_begin()        {{Returns a const_iterator pointing to the position before the first element in the container}} 
    `mylist.cbegin()               {{Returns a const_iterator pointing to the first element in the container}} 
    `mylist.cend()                 {{Returns a const_iterator pointing to the past-the-end element in the forward_list container}} 

$ Capacity
    `mylist.empty()                {{Returns a bool value indicating whether the forward_list container is empty}} 
    `mylist.max_size()             {{Returns the maximum number of elements that the forward_list container can hold}} 

$ Element Access
    `mylist.front()                {{Returns a reference to the first element in the forward_list container}} 

$ Modifiers
    `mylist.assign(4, 15)          {{Assigns new contents to the forward_list container, replacing its current contents, and modifying its size accordingly}} 
    `mylist.emplace_front(10, 'a') {{Inserts a new element at the beginning of the forward_list, right before its current first element}} 
    `mylist.push_front(x)          {{Inserts a new element at the beginning of the forward_list, right before its current first element}} 
    `mylist.pop_front()            {{Removes the first element in the forward_list container, effectively reducing its size by one}} 
    `mylist.emplace_after( it, 100, 'x')
>                                  {{Container is extended by inserting a new element after the element at position. This new element is constructed in place using args as the arguments for its construction}} 
    `mylist.insert_after( it, 2, 20)
>                                  {{Container is extended by inserting new elements after the element at position}} 
    `mylist.erase_after(it)        {{Removes from the forward_list container either a single element (the one after position) or a range of elements}} 
    `first.swap(second)            {{Exchanges the content of the container by the content of fwdlst, which is another forward_list object of the same type}} 
    `mylist.resize(3)              {{Resizes the container to contain n elements}} 
    `mylist.clear()                {{Removes all elements from the forward_list container (which are destroyed), and leaving the container with a size of 0}} 

$ Operations
    `first.splice_after(first.before_begin(), second, second.begin())
>                                  {{Transfers elements from fwdlst into the container inserting them after the element pointed by position}} 
    `mylist.remove(20)             {{Removes from the container all the elements that compare equal to val}} 
    `mylist.remove_if(is_odd_object)
>                                  {{Removes from the container all the elements for which Predicate pred returns true}} 
    `mylist.unique()               {{Removes all but the first element from every consecutive group of equal elements in the container}} 
    `first.merge(second)           {{Merges x into the forward_list by transferring all of its elements at their respective ordered positions into the container}} 
    `mylist.sort(std::greater<int>())
>                                  {{Sorts the elements in the forward_list, altering their position within the container}} 
    `mylist.reverse()              {{Reverses the order of the elements in the forward_list container}} 

$ Observers
    `mylist.get_allocator()        {{Returns a copy of the allocator object associated with the container}} 

$ Function Overloads
    `Operators: ==, !=, <, <=, >, >=
>                                  {{Performs the appropriate comparison operation between the forward_list containers lhs and rhs}} 
    `swap(x, y)                    {{Contents of container x are exchanged with those of y. Both container objects must be of the same type}} 

