# C++ Algorithms

> Source: http://www.cplusplus.com/reference/algorithm/

> Aliases: cpp-algorithm, cpp-algo

$ Non-Modifying sequence operations
    `all_of (foo.begin(), foo.end(), pred)
>                                  {{Returns true if pred returns true for all the elements in the range or if the range is empty}} 
    `any_of (foo.begin(), foo.end(), pred)
>                                  {{Returns true if pred returns true for any of the elements in the range}} 
    `none_of (foo.begin(), foo.end(), pred)
>                                  {{Returns true if pred returns false for all the elements in the range}} 
    `for_each (foo.begin(), foo.end(), fn)
>                                  {{Apply function to range}} 
    `find (foo.begin(), foo.end(), const T& val)
>                                  {{Find value in range}} 
    `find_if (foo.begin(), foo.end(), pred)
>                                  {{Returns an iterator to the first element in the range for which pred returns true}} 
    `find_if_not (foo.begin(), foo.end(), pred)
>                                  {{Returns an iterator to the first element in the range for which pred returns false.}} 
    `find_end (foo.begin(), foo.end(), bar.begin(), bar.end())
>                                  {{Searches the foo range for the last occurrence of the sequence defined by bar range, and returns an iterator to its first element}} 
    `find_first_of (foo.begin(), foo.end(), bar.begin(), bar.end())
>                                  {{Returns an iterator to the first element in the foo range that matches any of the elements in bar range}} 
    `adjacent_find (foo.begin(), foo.end())
>                                  {{Find equal adjacent elements in range}} 
    `count (foo.begin(), foo.end(), const T& val)
>                                  {{Count appearances of value in range}} 
    `count_if (foo.begin(), foo.end(), pred)
>                                  {{Returns the number of elements in the range for which pred is true}} 
    `mismatch (foo.begin(), foo.end(), bar.begin())
>                                  {{Return first position where two ranges differ}} 
    `equal (foo.begin(), foo.end(), bar.begin())
>                                  {{Test whether the elements in two ranges are equal}} 
    `is_permutation (foo.begin(), foo.end(), bar.begin())
>                                  {{Test whether range1 is permutation of another}} 
    `search (foo.begin(), foo.end(), bar.begin(), bar.end())
>                                  {{Searches the range1 for the first occurrence of the sequence defined by range2, and returns an iterator to its first element}} 
    `search_n (foo.begin(), foo.end(), Size count, const T& val)
>                                  {{Searches the range1 for a sequence of count elements, each comparing equal to val}} 

$ Modifying sequence operations
    `copy (foo.begin(), foo.end(), result)
>                                  {{Copy range of elements}} 
    `copy_n (foo.begin(), Size n, result)
>                                  {{Copies the first n elements from the range beginning at foo.begin() into the range beginning at result}} 
    `copy_if (foo.begin(), foo.end(), result, pred)
>                                  {{Copies the elements in the range for which pred returns true to the range beginning at result}} 
    `copy_backward (foo.begin(), foo.end(), result)
>                                  {{Copies the elements in the range starting backward into the range terminating at result}} 
    `move (foo.begin(), foo.end(), result)
>                                  {{Moves the elements in the range1 into the range beginning at resul​t}} 
    `move_backward (foo.begin(), foo.end(), result)
>                                  {{Move range of elements backward}} 
    `swap (T& a, T& b)             {{Exchange values of two objects}} 
    `swap_ranges (foo.begin(), foo.end(), bar.begin())
>                                  {{Exchange values of two ranges}} 
    `iter_swap (a, b)              {{Exchange values of objects pointed to by two iterators}} 
    `transform (foo.begin(), foo.end(), result, op)
>                                  {{Applies op to each of the elements in the range and stores the value returned by each operation in the range that begins at result.}} 
    `replace (foo.begin(), foo.end(), const T& old_value, const T& new_value)
>                                  {{Replace value in range}} 
    `replace_if (foo.begin(), foo.end(), pred, const T& new_value )
>                                  {{Replace values in range for which pred returns true}} 
    `replace_copy (foo.begin(), foo.end(), result, const T& old_value, const T& new_value)
>                                  {{Copy range replacing value}} 
    `replace_copy_if (foo.begin(), foo.end(), result, pred, const T& new_value)
>                                  {{Copy range replacing value for which pred returns true}} 
    `fill (foo.begin(), foo.end(), const T& val)
>                                  {{Fill range with value}} 
    `fill_n (foo.begin(), Size n, const T& val)
>                                  {{Fill sequence with value}} 
    `generate (foo.begin(), foo.end(), gen)
>                                  {{Generate values for range with function}} 
    `generate_n (foo.begin(), Size n, gen)
>                                  {{Generate values for sequence with function}} 
    `remove (foo.begin(), foo.end(), const T& val)
>                                  {{Remove value from range}} 
    `remove_if (foo.begin(), foo.end(), pred)
>                                  {{Remove elements from range for which pred returns true}} 
    `remove_copy (foo.begin(), foo.end(), result, const T& val)
>                                  {{Copy range removing value}} 
    `remove_copy_if (foo.begin(), foo.end(), result, pred)
>                                  {{Copy range removing values for which pred returns true}} 
    `unique (foo.begin(), foo.end())
>                                  {{Remove consecutive duplicates in range}} 
    `unique_copy (foo.begin(), foo.end(), result)
>                                  {{Copy range removing duplicates}} 
    `reverse (foo.begin(), foo.end())
>                                  {{reverse range}} 
    `reverse_copy (foo.begin(), foo.end(), result)
>                                  {{Copy range replacing value}} 
    `rotate (foo.begin(), middle, foo.end())
>                                  {{Rotate left the elements in range}} 
    `rotate_copy (foo.begin(), middle, foo.end(), result)
>                                  {{Copy range rotated left}} 
    `random_shuffle (foo.begin(), foo.end())
>                                  {{Randomly rearrange elements in range}} 
    `shuffle (foo.begin(), foo.end(), URNG&& g)
>                                  {{Randomly rearrange elements in range using generator}} 

$ Partitions
    `is_partitioned (foo.begin(), foo.end(), pred)
>                                  {{Test whether range is partitioned}} 
    `partition (foo.begin(), foo.end(), pred)
>                                  {{Partition range in two}} 
    `stable_partition (foo.begin(), foo.end(), pred)
>                                  {{Partition range in two - stable ordering}} 
    `partition_copy (foo.begin(), foo.end(), result_true, result_false, pred)
>                                  {{Copies the elements in the range for which pred returns true into the range pointed by result_true, and else to the range pointed by result_false}} 
    `partition_point (foo.begin(), foo.end(), pred)
>                                  {{Get partition point}} 

$ Sorting
    `sort (foo.begin(), foo.end()) {{Sort elements in range}} 
    `stable_sort (foo.begin(), foo.end())
>                                  {{Sort elements preserving order of equivalents}} 
    `partial_sort (foo.begin(), middle, foo.end())
>                                  {{Partially sort elements in range in such a way that the elements before middle(random access iterator) are the smallest elements in the entire range}} 
    `partial_sort_copy (foo.begin(), foo.end(), result_first, result_last)
>                                  {{Copy and partially sort range}} 
    `is_sorted_until (foo.begin(), foo.end())
>                                  {{Check whether range is sorted}} 
    `nth_element (foo.begin(), nth, foo.end())
>                                  {{Rearranges the elements in the range, in such a way that the element at the nth position(random access iterator) is the element that would be in that position in a sorted sequence}} 

$ Binary search
    `lower_bound (foo.begin(), foo.end(), const T& val)
>                                  {{Return iterator to lower bound}} 
    `upper_bound (foo.begin(), foo.end(), const T& val)
>                                  {{Return iterator to upper bound}} 
    `equal_range (foo.begin(), foo.end(), const T& val)
>                                  {{Get subrange of equal elements}} 
    `binary_search (foo.begin(), foo.end(), const T& val)
>                                  {{Test if value exists in sorted sequence}} 

$ Merge
    `merge (foo.begin(), foo.end(), bar.begin(), bar.end(), result)
>                                  {{Merge sorted ranges}} 
    `inplace_merge (foo.begin(), middle, foo.end())
>                                  {{Merge consecutive sorted ranges, here middle is a bidirectional iterator}} 
    `includes (foo.begin(), foo.end(), bar.begin(), bar.end() )
>                                  {{Test whether sorted range includes another sorted range}} 
    `set_union (foo.begin(), foo.end(), bar.begin(), bar.end(), result)
>                                  {{Union of two sorted ranges}} 
    `set_intersection (foo.begin(), foo.end(), bar.begin(), bar.end(), result)
>                                  {{Intersection of two sorted ranges}} 
    `set_difference (foo.begin(), foo.end(), bar.begin(), bar.end(), result)
>                                  {{Difference of two sorted ranges}} 
    `set_symmetric_difference (foo.begin(), foo.end(), bar.begin(), bar.end(), result)
>                                  {{Symmetric difference of two sorted ranges}} 

$ Heap
    `push_heap (foo.begin(), foo.end())
>                                  {{Push element into heap range}} 
    `pop_heap (foo.begin(), foo.end())
>                                  {{Pop element from heap range}} 
    `make_heap (foo.begin(), foo.end())
>                                  {{Make heap from range}} 
    `sort_heap (foo.begin(), foo.end())
>                                  {{Sort elements of heap}} 
    `is_heap (foo.begin(), foo.end())
>                                  {{Test if range is heap}} 
    `is_heap_until (foo.begin(), foo.end())
>                                  {{Find foo.begin() element not in heap order}} 

$ Min/Max
    `min (const T& a, const T& b)  {{Return the smallest}} 
    `max (const T& a, const T& b)  {{Return the largest}} 
    `minmax (const T& a, const T& b)
>                                  {{Return smallest and largest elements}} 
    `min_element (foo.begin(), foo.end())
>                                  {{Return smallest element in range}} 
    `max_element (foo.begin(), foo.end())
>                                  {{Return largest element in range}} 
    `minmax_element (foo.begin(), foo.end())
>                                  {{Return smallest and largest elements in range}} 

$ Other
    `lexicographical_compare (foo.begin(), foo.end(), bar.begin(), bar.end())
>                                  {{Lexicographical less-than comparison}} 
    `next_permutation (foo.begin(), foo.end())
>                                  {{Transform range to next permutation}} 
    `prev_permutation (foo.begin(), foo.end(), comp)
>                                  {{Transform range to previous permutation}} 

