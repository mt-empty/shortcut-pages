# jQuery

> Source: http://api.jquery.com/

$ Selectors
    `*                             {{Selects all elements}} 
    `.class                        {{Selects all elements with class}} 
    `element                       {{Selects all elements with given tag name}} 
    `#id                           {{Selects a single element with given id}} 
    `:first                        {{Selects the first matched element}} 
    `:last                         {{Selects the last matched element}} 

$ Traversing
    `.each(function)               {{Execute a function on each element}} 
    `.parent(selector)             {{Get all ancestors filtered by selector}} 
    `.find(selector)               {{Get all descendants filtered by selector}} 
    `.children(selector)           {{Get immediate children filterd by selector}} 
    `.next()                       {{Get next sibling}} 
    `.nextAll(selector)            {{Get all siblings filtered by selector}} 
    `.prev()                       {{Get preceding sibling}} 

$ CSS
    `.addClass(className)          {{Adds the specified class(es) to element(s)}} 
    `.removeClass(className)       {{Remove class(es) from element(s)}} 
    `.toggleClass(className)       {{Toggle classes from element(s)}} 
    `.height(value)                {{Get computed height for first element or set all elements' height}} 
    `.innerHeight(value)           {{Get inner height (includes padding) for first element or set all elements' inner height}} 
    `.outerHeight(includeMargin)   {{Get and set outer height (includes padding, border and optionally margin)}} 
    `.width(value)                 {{Get computed width for the first element or set all elements' width}} 
    `.position()                   {{Get an object with properties .top and .left of the first element, relative to parent}} 
    `.offset()                     {{Get an object with properties .top and .left of the first element, relative to document}} 

$ Manipulation
    `.after(content)               {{Insert content after element(s)}} 
    `.before(content)              {{Insert content before element(s)}} 
    `.appendTo(target)             {{Insert every element in the set to the end of the target}} 
    `.detach(selector)             {{Remove matched elements from the DOM}} 
    `.empty()                      {{Remove all child nodes of the element(s) from the DOM}} 
    `.html(htmlString)             {{Set the HTML contents of the element(s)}} 
    `.wrap(wrappingElement)        {{Wrap an HTML structure around the element(s)}} 
    `.unwrap()                     {{Remove the parents from the DOM, leaving the element(s) in their spot}} 
    `.val(value)                   {{Set value of all element(s) or get the value of first element}} 
    `.replaceWith(newContent)      {{Replace element(s) in the set with new content and return removed ones}} 

$ Events
    `.load(handler)                {{Bind handler to 'load' event}} 
    `.ready(handler)               {{Run handler when DOM is fully loaded}} 
    `.unload(handler)              {{Bind handler to 'unload' event}} 
    `.click(handler)               {{Bind handler to 'click' event}} 
    `.dblclick(handler)            {{Bind handler to 'dblclick' event}} 
    `.mousedown(handler)           {{Bind handler to 'mousedown' event}} 
    `.mouseup(handler)             {{Bind handler to 'mouseup' event}} 
    `.mousemove(handler)           {{Bind handler to 'mousemove' event}} 
    `.hover( handlerIn, handlerOut )
>                                  {{Bind handlers to run when mouse pointer enters and leaves element(s)}} 
    `.keydown(handler)             {{Bind handler to 'keydown' event}} 
    `.keypress(handler)            {{Bind handler to 'keypress' event}} 
    `.keyup(handler)               {{Bind handler to 'keyup' event}} 
    `.change(handler)              {{Bind handler to 'change' event}} 
    `.focus(handler)               {{Bind handler to 'focus' event}} 
    `.select(handler)              {{Bind handler to 'select' event}} 
    `.submit(handler)              {{Bind handler to 'submit' event}} 

$ Event Object
    `event.pageX                   {{Mouse X position relative to document's left}} 
    `event.pageY                   {{Mouse Y position relative to document's top}} 
    `event.target                  {{DOM element that initiated the event}} 
    `event.timeStamp               {{Time of the event}} 
    `event.type                    {{Description of the event}} 
    `event.which                   {{Indicates the specific key or button that was pressed}} 

$ Effects
    `.animate(properties, duration, easing, complete)
>                                  {{Perform a custom animation of a set of CSS properties}} 
    `.fadeIn(duration, complete)   {{Display the element(s) by fading them to opaque}} 
    `.fadeOut(duration, complete)  {{Hide the element(s) by fading them to transparent}} 
    `.hide()                       {{Hide the element(s)}} 
    `.show()                       {{Display the element(s)}} 
    `.toggle()                     {{Toggle elements' visibility}} 
    `.slideDown(duration, complete)
>                                  {{Display the element(s) with a sliding motion}} 
    `.slideToggle(duration, complete)
>                                  {{Display or hide the element(s) with a sliding motion}} 
    `.slideUp(duration, complete)  {{Hide element(s) with a sliding motion}} 

$ Ajax
    `$.ajax(settings)              {{Perform an asynchronous HTTP (Ajax) request}} 
    `$.get(url, data, success, dataType)
>                                  {{Load data from the server using a HTTP GET request}} 
    `$.getJSON(url, data, success) {{Load JSON-encoded data from the server}} 
    `$.getScript(url, success)     {{Load and execute JavaScript file from the server}} 
    `$.param(obj)                  {{Create a serialized representation for use in a query or Ajax request}} 
    `$.post(url, data, success, dataType)
>                                  {{Load data from the server using a HTTP POST request}} 
    `.serialize()                  {{Encode a form's elements as a string for submission}} 
    `.serializeArray()             {{Encode a form's elements as an array of names and values}} 

$ Utilities
    `$.parseHTML(htmlString, context, keepScripts )
>                                  {{Parses a string into an array of DOM nodes}} 
    `$.parseJSON(jsonString)       {{Convert JSON string to JavaScript object}} 
    `$.parseXML(string)            {{Parses a string into an XML document}} 

