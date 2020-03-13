# C++ List

> Source: http://www.cplusplus.com/reference/forward_list/forward_list/

> Aliases: cpp-<list>-library, c++-list-library, c++-lists, c++-<list>, c++-list

$ Iterators
    `mylist.begin()                {{Returns an iterator pointing to the first element in the list container}} 
    `mylist.end()                  {{Returns an iterator referring to the past-the-end element in the list container}} 
    `mylist.rbegin()               {{Returns a reverse iterator pointing to the last element in the container}} 
    `mylist.rend()                 {{Returns a reverse iterator pointing to the theoretical element preceding the first element in the list container}} 
    `mylist.cbegin()               {{Returns a const_iterator pointing to the first element in the container (C++11 only)}} 
    `mylist.cend()                 {{Returns a const_iterator pointing to the past-the-end element in the container (C++11 only)}} 
    `mylist.crbegin()              {{Returns a const_reverse_iterator pointing to the last element in the container (C++11 only)}} 
    `mylist.crend()                {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the container (C++11 only)}} 

$ Capacity
    `mylist.size()                 {{Returns the number of elements in the list container}} 
    `mylist.max_size()             {{Returns the maximum number of elements that the list container can hold}} 
    `mylist.empty()                {{Returns whether the list container is empty}} 

$ Element Access
    `mylist.front()                {{Returns a reference to the first element in the list container}} 
    `mylist.back()                 {{Returns a reference to the last element in the list container}} 

$ Modifiers
    `mylist.assign(size, value)    {{Assigns new contents to the list container, replacing its current contents, and modifying its size accordingly}} 
    `mylist.push_back(x)           {{Adds a new element at the end of the list container, after its current last element}} 
    `mylist.push_front(x)          {{Inserts a new element at the beginning of the list, right before its current first element}} 
    `mylist.pop_back()             {{Removes the last element in the list container, effectively reducing the container size by one}} 
    `mylist.pop_front()            {{Removes the first element in the list container, effectively reducing its size by one}} 
    `mylist.insert(it, x)          {{Container is extended by inserting new elements before the element at the specified position}} 
    `mylist.erase(it)              {{Removes from the list container either a single element (position) or a range of elements}} 
    `x.swap(y)                     {{Exchanges the content of the container by the content of x, which is another list of the same type}} 
    `mylist.clear()                {{Removes all elements from the list container (which are destroyed), and leaving the container with a size of 0}} 
    `mylist.resize()               {{Resizes the container so that it contains n elements}} 
    `mylist.emplace(it, x)         {{The container is extended by inserting a new element at position (C++11 only)}} 
    `mylist.emplace_back(x)        {{Inserts a new element at the end of the list, right after its current last element (C++11 only)}} 
    `mylist.emplace_front(x)       {{Inserts a new element at the beginning of the list, right before its current first element (C++11 only)}} 

$ Operations
    `x.splice(it, y)               {{Transfers elements from x into the container, inserting them at position}} 
    `mylist.remove(x)              {{Removes from the container all the elements that compare equal to val}} 
    `mylist.remove_if(single_digit)
>                                  {{Removes from the container all the elements for which Predicate pred returns true}} 
    `mylist.unique()               {{Removes all but the first element from every consecutive group of equal elements in the container}} 
    `x.merge(y)                    {{Merges x into the list by transferring all of its elements at their respective ordered positions into the container}} 
    `mylist.sort()                 {{Sorts the elements in the list, altering their position within the container}} 
    `mylist.reverse()              {{Reverses the order of the elements in the list container}} 

$ Observers
    `mylist.get_allocator()        {{Returns a copy of the allocator object associated with the list container}} 

$ Non-Member Function Overloads
    `Operator ==, !=, <, <=, >, >= {{Performs the appropriate comparison operation between the list containers lhs and rhs}} 
    `x.swap(y)                     {{Contents of container x are exchanged with those of y}} 

