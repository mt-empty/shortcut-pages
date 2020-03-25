# C++ Arrays

> Source: http://www.cplusplus.com/reference/array/array/

$ Iterators
    `arr.begin()                   {{Returns an iterator pointing to the first element in the array container}} 
    `arr.end()                     {{Returns an iterator pointing to the past-the-end element in the array container}} 
    `arr.rbegin()                  {{Returns a reverse iterator pointing to the last element in the array container}} 
    `arr.rend()                    {{Returns a reverse iterator pointing to the theoretical element preceding the first element in the array}} 
    `arr.cbegin()                  {{Returns a const_iterator pointing to the first element in the array container}} 
    `arr.cend()                    {{Returns a const_iterator pointing to the past-the-end element in the array container}} 
    `arr.crbegin()                 {{Returns a const_reverse_iterator pointing to the last element in the array container}} 
    `arr.crend()                   {{Returns a const_reverse_iterator pointing to the theoretical element preceding the first element in the vector}} 

$ Capacity
    `arr.size()                    {{Returns the number of elements in the array container}} 
    `arr.max_size()                {{Returns the maximum number of elements that the array container can hold}} 
    `arr.empty()                   {{Returns a bool value indicating whether the array container is empty}} 

$ Element Access
    `arri                          {{Returns a reference to the element at position n in the array container}} 
    `arr.at(i)                     {{Returns a reference to the element at position n in the array}} 
    `arr.front()                   {{Returns a reference to the first element in the array container}} 
    `arr.back()                    {{Returns a reference to the last element in the array container}} 
    `arr.data()                    {{Returns a pointer to the first element in the array object}} 

$ Modifiers
    `arr.fill(5)                   {{Sets val as the value for all the elements in the array object}} 
    `first.swap(second)            {{Exchanges the content of the array by the content of x, which is another array object of the same type}} 

$ Non-member Functions
    `std::get<i>(arr)              {{Returns a reference to the ith element of array arr}} 
    `Operators: ==, !=, <, <=, >, >=
>                                  {{Performs the appropriate comparison operation between the array containers lhs and rhs}} 

$ Helper Classes
    `struct tuple_element<I, std::array<T,N>>
>                                  {{Accesses the static type of the elements in an array object as if it was a tuple}} 
    `std::tuple_size<T>::value     {{Provides access to the number of elements in an std::array as a compile-time constant expression}} 

