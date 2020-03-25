# Underscore JS

> Source: http://www.underscorejs.org

> Aliases: underscore, underscorejs

$ Arrays
    `_.first(array,n)              {{Returns the first element of array. Passing n will return the first n elements of the array}} 
    `_.last(array,n)               {{Returns the last element of array. Passing n will return the last n elements of the array}} 
    `_.union(*arrays)              {{Computes the union of passed in arrays}} 
    `_.intersection(*arrays)       {{Computes the intersection of passed in arrays}} 
    `_.without(array, *values)     {{Returns a copy of the array with all instances of the values removed}} 

$ Objects
    `_.keys(object)                {{Returns a list of the object's own enumerable properties}} 
    `_.values(object)              {{Returns a list of the object's own values}} 
    `_.pairs(object)               {{Converts an object into a list of [key,value] pairs}} 
    `_.has(object,key)             {{Checks if an object has a given key}} 
    `_.isEqual(object1, object2)   {{Performs an optimized deep comparison between the two objects, to determine if they should be considered equal}} 
    `_.isEmpty(object)             {{Returns true if an enumerable object contains no values}} 
    `_.isUndefined(val)            {{Returns true if value is undefined}} 

$ Collections
    `_.map(list, iteratee, context)
>                                  {{Produces a new array of values by mapping each value in list through a transformation function (iteratee)}} 
    `_.where(list, properties)     {{Looks through each value in the list, returning an array of all the values that contain all of the key-value pairs listed in properties}} 
    `_.pluck(list, propertyName)   {{Returns a list of property values}} 
    `_.max(list, iteratee, context)
>                                  {{Returns the maximum value in list. If an iteratee function is provided, it will be used on each value to generate the criterion by which the value is ranked}} 
    `_.min(list, iteratee, context)
>                                  {{Returns the minimum value in list. If an iteratee function is provided, it will be used on each value to generate the criterion by which the value is ranked}} 
    `_.shuffle(list)               {{Returns a shuffled copy of the list}} 
    `_.sample(list,n)              {{Produce a random sample from the list. Produces a list of n random elements from the list, if n is passed}} 
    `_.size(list)                  {{Returns the number of values in the list}} 
    `_.partition(array, predicate) {{Split array into two arrays: one whose elements all satisfy predicate and one whose elements all do not satisfy predicate}} 

$ Utility
    `_.random(min,max)             {{Returns a random integer between min and max, inclusive}} 
    `_.now()                       {{Returns an integer timestamp for the current time}} 

