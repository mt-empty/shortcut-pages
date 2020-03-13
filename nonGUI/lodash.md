# Lodash

> Source: https://lodash.com/docs

$ Array Methods
    `_.chunk(array, [size=0])      {{Creates an array of elements split into groups the length of size}} 
    `_.compact(array)              {{Creates an array with all falsey values removed}} 
    `_.concat(array, [values])     {{Creates a new array concatenating array with any additional arrays and/or values}} 
    `_.difference(array, [values]) {{Creates an array of unique array values not included in the other given arrays}} 
    `_.drop(array, [n=1])          {{Creates a slice of array with n elements dropped from the beginning}} 
    `_.dropRight(array, [n=1])     {{Creates a slice of array with n elements dropped from the end}} 
    `_.fill(array, value, [start=0], [end=array.length])
>                                  {{Fills elements of array with value from start up to, but not including, end}} 
    `_.flatten(array)              {{Flattens array a single level deep}} 
    `_.flattenDeep(array)          {{Recursively flattens array}} 
    `_.flattenDepth(array, depth=1)
>                                  {{Recursively flatten array up to depth times}} 
    `_.fromPairs(pairs)            {{This method returns an object composed from key-value pairs}} 
    `_.head(array)                 {{Gets the first element of array}} 
    `_.indexOf(array, value, [fromIndex=0])
>                                  {{Gets the index at which the first occurrence of value is found in array}} 
    `_.initial(array)              {{Gets all but the last element of array}} 
    `_.intersection([arrays])      {{Creates an array of unique values that are included in all given arrays}} 
    `_.join(array, [separator=','])
>                                  {{Converts all elements in array into a string separated by separator}} 
    `_.last(array)                 {{Gets the last element of array}} 
    `_.pull(array, [values])       {{Removes all given values from array}} 
    `_.remove(array, [predicate=_.identity])
>                                  {{Removes all elements from array that predicate returns truthy for and returns an array of the removed elements}} 
    `_.reverse()                   {{Reverses array so that the first element becomes the last, the second element becomes the second to last, and so on}} 
    `_.slice(array, [start=0], [end=array.length])
>                                  {{Creates a slice of array from start up to, but not including, end}} 
    `_.tail(array)                 {{Gets all but the first element of array}} 
    `_.take(array, [n=1])          {{Creates a slice of array with n elements taken from the beginning}} 
    `_.union([arrays])             {{Creates an array of unique values, in order, from all given arrays}} 

$ Collection Methods
    `_.countBy(collection, [iteratee=_.identity])
>                                  {{Creates an object composed of keys generated from the results of running each element of collection through iteratee}} 
    `_.every(collection, [predicate=_.identity])
>                                  {{Checks if predicate returns truthy for all elements of collection. Iteration is stopped once predicate returns falsey}} 
    `_.filter(collection, [predicate=_.identity])
>                                  {{Iterates over elements of collection, returning an array of all elements predicate returns truthy for}} 
    `_.find(collection, [predicate=_.identity])
>                                  {{Iterates over elements of collection, returning the first element predicate returns truthy for}} 
    `_.flatMap(collection, [iteratee=_.identity])
>                                  {{Creates an array of flattened values by running each element in collection through iteratee and concating its result to the other mapped values}} 
    `_.forEach(collection, [iteratee=_.identity])
>                                  {{Iterates over elements of collection invoking iteratee for each element}} 
    `_.includes(collection, value, [fromIndex=0])
>                                  {{Checks if value is in collection}} 
    `_.keyBy(collection, [iteratee=_.identity])
>                                  {{Creates an object composed of keys generated from the results of running each element of collection through iteratee}} 
    `_.map(collection, [iteratee=_.identity])
>                                  {{Creates an array of values by running each element in collection through iteratee}} 
    `_.partition(collection, [predicate=_.identity])
>                                  {{Creates an array of elements split into two groups}} 
    `_.reduce(collection, [iteratee=_.identity], [accumulator])
>                                  {{Reduces collection to a value which is the accumulated result of running each element in collection through iteratee, where each successive invocation is supplied the return value of the previous}} 
    `_.sample(collection)          {{Gets a random element from collection}} 
    `_.shuffle(collection)         {{Creates an array of shuffled values}} 
    `_.size(collection)            {{Gets the size of collection by returning its length for array-like values or the number of own enumerable properties for objects}} 
    `_.some(collection, [predicate=_.identity])
>                                  {{Checks if predicate returns truthy for any element of collection. Iteration is stopped once predicate returns truthy}} 

$ Date Methods
    `_.now()                       {{Gets the timestamp of the number of milliseconds that have elapsed since the Unix epoch}} 

$ Function Methods
    `_.after(n, func)              {{This method creates a function that invokes func once it’s called n or more times}} 
    `_.ary(func, [n=func.length])  {{Creates a function that accepts up to n arguments, ignoring any additional arguments}} 
    `_.before(n, func)             {{Creates a function that invokes func, with the this binding and arguments of the created function, while it’s called less than n times}} 
    `_.bind(func, thisArg, [partials])
>                                  {{Creates a function that invokes func with the 'this' binding of 'thisArg' and prepends any additional '_.bind' arguments to those provided to the bound function}} 
    `_.bindKey(object, key, [partials])
>                                  {{Creates a function that invokes the method at 'object\[key\]' and prepends any additional '_.bindKey' arguments to those provided to the bound function}} 
    `_.curry(func, [arity=func.length])
>                                  {{Creates a function that accepts arguments of func and either invokes func returning its result}} 
    `_.defer(func, [args])         {{Defers invoking the func until the current call stack has cleared}} 
    `_.delay(func, wait, [args])   {{Invokes func after wait milliseconds}} 
    `_.flip(func)                  {{Creates a function that invokes func with arguments reversed}} 
    `_.memoize(func, [resolver])   {{Creates a function that memoizes the result of 'func'}} 
    `_.negate(predicate)           {{Creates a function that negates the result of the predicate 'func'}} 
    `_.once(func)                  {{Creates a function that is restricted to invoking 'func' once}} 
    `_.spread(func, [start=0])     {{Creates a function that invokes 'func' with the 'this' binding of the created function and an array of arguments}} 
    `_.throttle(func, [wait=0], [options])
>                                  {{Creates a throttled function that only invokes func at most once per every wait milliseconds}} 
    `_.unary(func)                 {{Creates a function that accepts up to one argument, ignoring any additional arguments}} 
    `_.wrap(value, [wrapper=identity])
>                                  {{Creates a function that provides value to the wrapper function as its first argument}} 

$ Lang Methods
    `_.castArray(value)            {{Casts value as an array if it’s not one}} 
    `_.clone(value)                {{Creates a shallow clone of value}} 
    `_.cloneDeep(value)            {{This method is like '_.clone' except that it recursively clones value}} 
    `_.eq(value, other)            {{Checks whether two values are equal or not}} 
    `_.gt(value, other)            {{Checks if 'value' is greater than 'other'}} 
    `_.isEqual(value, other)       {{Performs a deep comparison between two values to determine if they are equivalent}} 
    `_.isElement(value)            {{Checks if value is likely a DOM element}} 

$ Math Methods
    `_.add(augend, addend)         {{Adds two numbers}} 
    `_.ceil(number, [precision=0]) {{Computes number rounded up to precision}} 
    `_.floor(number, [precision=0])
>                                  {{Computes number rounded down to precision}} 
    `_.max(array)                  {{Computes the maximum value of array}} 
    `_.mean(array)                 {{Computes the mean of the values in array}} 
    `_.min(array)                  {{Computes the minimum value of 'array'}} 
    `_.round(number, [precision=0])
>                                  {{Computes 'number' rounded to 'precision'}} 

$ Number Methods
    `_.clamp(number, [lower], upper)
>                                  {{Clamps number within the inclusive lower and upper bounds}} 
    `_.inRange(number, [start=0], end)
>                                  {{Checks if 'n' is between 'start' and up to but not including, 'end'}} 
    `_.random([lower=0], [upper=1], [floating])
>                                  {{Produces a random number between the inclusive lower and upper bounds}} 

$ Object Methods
    `_.assign(object, [sources])   {{Assigns own enumerable properties of source objects to the destination object}} 
    `_.at(object, [paths])         {{Creates an array of values corresponding to paths of object}} 
    `_.create(prototype, [properties])
>                                  {{Creates an array of values corresponding to paths of object}} 
    `_.forIn(object, [iteratee=_.identity])
>                                  {{Iterates over own and inherited enumerable properties of an object invoking iteratee for each property}} 
    `_.get(object, path, [defaultValue])
>                                  {{Gets the value at 'path' of 'object'}} 
    `_.has(object, path)           {{Checks if path is a direct property of object}} 
    `_.merge(object, [sources])    {{Recursively merges own and inherited enumerable properties of source objects into the destination object}} 
    `_.pick(object, [props])       {{Creates an object composed of the picked object properties}} 

$ Seq Methods
    `_.chain(value)                {{Creates a lodash object that wraps value with explicit method chaining enabled}} 
    `_.tap(value, interceptor)     {{This method invokes interceptor and returns value}} 

$ String Methods
    `_.camelCase([string=''])      {{Converts string to camel case}} 
    `_.capitalize([string=''])     {{Converts the first character of string to upper case and the remaining to lower case}} 
    `_.pad([string=''], [length=0], [chars=' '])
>                                  {{Pads 'string' on the left and right sides if it’s shorter than 'length'}} 
    `_.split([string=''], separator, [limit])
>                                  {{Splits 'string' by 'separator'}} 
    `_.toLower([string=''])        {{Converts string, as a whole, to lower case}} 

$ Util Methods
    `_.attempt(func)               {{Attempts to invoke func, returning either the result or the caught error object}} 
    `_.bindAll(object, methodNames)
>                                  {{Binds methods of an object to the object itself, overwriting the existing method}} 
    `_.method(path, [args])        {{Creates a function that invokes the method at path of a given object}} 
    `_.noop()                      {{A no-operation function that returns undefined regardless of the arguments it receives}} 
    `_.property(path)              {{Creates a function that returns the value at path of a given object}} 
    `_.propertyOf(object)          {{Creates a function that returns the value at path of a given object}} 

