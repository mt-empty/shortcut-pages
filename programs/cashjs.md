# Cashjs

> Source: https://github.com/kenwheeler/cash

> Aliases: cash-js

$ Attributes
    `$.fn.addClass()               {{Adds the className argument to collection elements}} 
    `$.fn.attr()                   {{Without attrValue, returns the attribute value of the first element in the collection. With attrValue, sets the attribute value of each element of the collection}} 
    `$.fn.hasClass()               {{Returns the boolean result of checking if the first element in the collection has the className attribute}} 
    `$.fn.prop()                   {{Returns a property value when just property is supplied. Sets a property when property and value are supplied, and sets multiple properties when an object is supplied}} 
    `$.fn.removeAttr()             {{Removes attribute from collection elements}} 
    `$.fn.removeClass()            {{Removes className from collection elements. Accepts space-separated classNames for removing multiple classes. Providing no arguments will remove all classes}} 
    `$.fn.removeProp()             {{Removes property from collection elements}} 
    `$.fn.toggleClass              {{Adds or removes className from collection elements based on if the element already has the class. Accepts space-separated classNames for toggling multiple classes, and an optional force boolean to ensure classes are added (true) or removed (false)}} 

$ Collection
    `$.fn                          {{The main prototype for collections, allowing you to extend cash with plugins by adding methods to all collections}} 
    `$.fn.add()                    {{Returns a new collection with the element(s) added to the end}} 
    `$.fn.each()                   {{Iterates over a collection with callback(value, index, array)}} 
    `$.fn.eq()                     {{Returns a collection with the element at index}} 
    `$.fn.filter()                 {{Returns the collection that results from applying the filter method}} 
    `$.fn.first()                  {{Returns the first element in the collection}} 
    `$.fn.get()                    {{Returns the element at the index}} 
    `$.fn.index()                  {{Returns the index of the element in its parent if an element or selector isn't provided. Returns index within element or selector if it is}} 
    `$.fn.last()                   {{Returns last element in the collection}} 

$ CSS
    `$.fn.css()                    {{Returns a CSS property value when just property is supplied. Sets a CSS property when property and value are supplied, and set multiple properties when an object is supplied. Properties will be autoprefixed if needed for the user's browser}} 

$ Data
    `$.fn.data()                   {{Link some data (string, object, array, etc.) to an element when both key and value are supplied. If only a key is supplied, returns the linked data and falls back to data attribute value if no data is already linked. Multiple data can be set when an object is supplied}} 
    `$.fn.removeData()             {{Removes linked data and data-attributes from collection elements}} 

$ Dimensions
    `$.fn.height()                 {{Returns the height of the element}} 
    `$.fn.innerHeight()            {{Returns the height of the element + padding}} 
    `$.fn.innerWidth()             {{Returns the width of the element + padding}} 
    `$.fn.outerHeight()            {{Returns the outer height of the element. Includes margins if margin is set to true}} 
    `$.fn.outerWidth()             {{Returns the outer width of the element. Includes margins if margin is set to true}} 
    `$.fn.width()                  {{Returns the width of the element}} 

$ Events
    `$.fn.off()                    {{Removes event listener from collection elements}} 
    `$.fn.on()                     {{Adds event listener to collection elements. Event is delegated if delegate is supplied}} 
    `$.fn.one()                    {{Adds event listener to collection elements that only triggers once for each element. Event is delegated if delegate is supplied}} 
    `$.fn.ready()                  {{Calls callback method on DOMContentLoaded}} 
    `$.fn.trigger()                {{Triggers supplied event on elements in collection. Data can be passed along as the second parameter}} 

$ Forms
    `$.fn.serialize()              {{When called on a form, serializes and returns form data}} 
    `$.fn.val()                    {{Returns an inputs value. If value is supplied, sets all inputs in collection's value to the value argument}} 

$ Manipulation
    `$.fn.after()                  {{Inserts content or elements after the collection}} 
    `$.fn.append()                 {{Appends the target element to the each element in the collection}} 
    `$.fn.appendTo()               {{Adds the elements in a collection to the target element(s)}} 
    `$.fn.before()                 {{Inserts content or elements before the collection}} 
    `$.fn.clone()                  {{Returns a clone of the collection}} 
    `$.fn.empty()                  {{Empties an elements interior markup}} 
    `$.fn.html()                   {{Returns the HTML text of the first element in the collection, sets the HTML if provided}} 
    `$.fn.insertAfter()            {{Inserts collection after specified element}} 
    `$.fn.insertBefore()           {{Inserts collection before specified element}} 
    `$.fn.prepend()                {{Prepends element to the each element in collection}} 
    `$.fn.prependTo()              {{Prepends elements in a collection to the target element(s)}} 
    `$.fn.remove()                 {{Removes collection elements from the DOM}} 
    `$.fn.text                     {{Returns the inner text of the first element in the collection, sets the text if textContent is provided}} 

$ Offset
    `$.fn.offset()                 {{Get the coordinates of the first element in a collection relative to the document}} 
    `$.fn.offsetParent()           {{Get the first element's ancestor that's positioned}} 
    `$.fn.position()               {{Get the coordinates of the first element in a collection relative to its offsetParent}} 

$ Traversal
    `$.fn.children()               {{Without a selector specified, returns a collection of child elements. With a selector, returns child elements that match the selector}} 
    `$.fn.closest()                {{Returns the closest matching selector up the DOM tree}} 
    `$.fn.find()                   {{Returns selector match descendants from the first element in the collection}} 
    `$.fn.has()                    {{Returns boolean result of the selector argument against the collection}} 
    `$.fn.is()                     {{Returns whether the provided selector, element or collection matches any element in the collection}} 
    `$.fn.next()                   {{Returns next sibling}} 
    `$.fn.not()                    {{Filters collection by false match on selector}} 
    `$.fn.parent()                 {{Returns parent element}} 
    `$.fn.parents()                {{Returns collection of elements who are parents of element. Optionally filtering by selector}} 
    `$.fn.prev()                   {{Returns the previous adjacent element}} 
    `$.fn.siblings                 {{Returns a collection of sibling elements}} 

$ Type Checking
    `$.isArray()                   {{Check if the argument is an array}} 
    `$.isFunction()                {{Check if the argument is a function}} 
    `$.isNumeric()                 {{Check if the argument is numeric}} 
    `$.isString()                  {{Check if the argument is a string}} 

$ Utilities
    `$.each()                      {{Iterates through a collection and calls the callback method on each}} 
    `$.extend()                    {{Extends target object with properties from the source object. If no target is provided, cash itself will be extended}} 
    `$.matches()                   {{Checks a selector against an element, returning a boolean value for match}} 
    `$.parseHTML()                 {{Returns a collection from an HTML string}} 

