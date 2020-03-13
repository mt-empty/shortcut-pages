# JavaScript and the DOM

> Source: http://overapi.com/javascript/

> Aliases: java-script-dom, js-dom, java-script-events, javascript-events, js-events

$ Document Methods
    `adoptNode(node)               {{Adopts a node from another document to this document, and returns the adopted node}} 
    `createAttribute()             {{Creates an attribute node}} 
    `createComment()               {{Creates a Comment node with the specified text}} 
    `createDocumentFragment()      {{Creates an empty DocumentFragment node}} 
    `createElement()               {{Creates an Element node}} 
    `createTextNode()              {{Creates a Text node}} 
    `getElementsByClassName()      {{Returns an array-like object of all child elements which have all of the given class names}} 
    `getElementById()              {{Returns the element that has the ID attribute with the specified value}} 
    `getElementsByTagName()        {{Returns a NodeList containing all elements with the specified tagname}} 
    `querySelector()               {{Returns the first element matching the specified CSS selector}} 
    `querySelectorAll()            {{Returns a NodeList containing all elements that match the specified CSS selector}} 
    `importNode()                  {{Imports a node from another document}} 

$ DOM Events-Form
    `blur                          {{The event occurs when a form element loses focus}} 
    `change                        {{The event occurs when the content of a form element, the selection, or the checked state have changed}} 
    `focus                         {{The event occurs when an element has received focus}} 
    `reset                         {{The event occurs when a form is reset}} 
    `select                        {{The event occurs when a user selects text}} 
    `submit                        {{The event occurs when a form is submitted (fired only on the form element, not the button or submit input)}} 

$ DOM Events-Keyboard
    `keydown                       {{The event occurs when the user is pressing a key or holding down a key}} 
    `keypress                      {{The event occurs when the user is pressing a key or holding down a key}} 
    `keyup                         {{The event occurs when a keyboard key is released}} 

$ DOM Events-Mouse
    `click                         {{The event occurs when the user clicks on an element}} 
    `dblclick                      {{The event occurs when the user double-clicks on an element}} 
    `mousedown                     {{The event occurs when a user presses a mouse button over an element}} 
    `mousemove                     {{The event occurs when a user moves the mouse pointer while over an element}} 
    `mouseover                     {{The event occurs when a user moves the mouse pointer onto an element}} 
    `mouseout                      {{The event occurs when a user moves the mouse pointer out of an element}} 
    `mouseup                       {{The event occurs when a user releases a mouse button over an element}} 

$ DOM Events-UI/Frame
    ` error                        {{The event occurs when an image does not load properly}} 
    `load                          {{The event occurs when a document, frameset, or <object> has been loaded}} 
    `resize                        {{The event occurs when a document view is resized}} 
    `scroll                        {{The event occurs when a document view is scrolled}} 
    `unload                        {{The event occurs when a document is removed from a window or frame (for <body> and <frameset>)}} 

$ Element Methods
    `getAttribute()                {{Returns the specified attribute value}} 
    `getAttributeNode()            {{Returns the specified attribute node}} 
    `getElementsByClassName()      {{Returns a collection of all child elements with the specified class name}} 
    `getElementsByTagName()        {{Returns a collection of all child elements with the specified tagname}} 
    `hasAttribute()                {{Returns true if the element has the specified attribute, otherwise it returns false}} 
    `querySelector()               {{Returns the first element that is a descendant of the element on which it is invoked that matches the specified CSS selector}} 
    `querySelectorAll()            {{Returns a NodeList containing all elements descended from the element on which it is invoked that matches the specified CSS selector}} 
    `removeAttribute()             {{Removes the specified attribute}} 
    `removeAttributeNode()         {{Removes the specified attribute node, and returns the removed node}} 
    `setAttribute()                {{Sets or changes the specified attribute, to the specified value}} 
    `setAttributeNode()            {{Sets or changes the specified attribute node}} 

$ Event Object Methods
    `preventDefault()              {{To cancel the event if it is cancelable, meaning that any default action normally taken by the implementation as a result of the event will not occur}} 
    `stopPropagation()             {{To prevent further propagation of an event during event flow}} 

$ EventTarget
    `addEventListener()            {{Allows the registration of event listeners on the event target (IE8 = attachEvent())}} 
    `dispatchEvent()               {{Allows to send the event to the subscribed event listeners (IE8 = fireEvent())}} 
    `removeEventListener()         {{Allows the removal of event listeners on the event target (IE8 = detachEvent())}} 

$ Node Properties
    `childNodes                    {{Returns a live collection of child nodes}} 
    `baseURI                       {{Specify absolute base URI of the node}} 
    `firstChild                    {{Returns the first child of a node}} 
    `lastChild                     {{Returns the last child of a node}} 
    `localName                     {{Specify name of the local part of a node}} 
    `namespaceURI                  {{Specify the namespace URI of a node}} 
    `nextSibling                   {{Returns the node immediately following the specified one}} 
    `nodeName                      {{Returns the name of a node, depending on its type}} 
    `nodeType                      {{Code representing the type of the underlying object}} 
    `nodeValue                     {{Specify the value of a node depending on their types}} 
    `parentNode                    {{Returns the parent node of a node}} 
    `previousSibling               {{Returns the node immediately preceding the specified one}} 
    `textContent                   {{Sets or returns the textual content of a node and its descendants}} 

$ Node Methods
    `appendChild()                 {{Adds a new child node, to the specified node, as the last child node}} 
    `cloneNode()                   {{Returns a duplicate of the node on which this method was called}} 
    `compareDocumentPosition()     {{Compares the document position of two nodes}} 
    `contains()                    {{Returns a Boolean value indicating whether a node is a descendant of a given node or not}} 
    `hasChildNodes()               {{Returns true if a node has any child nodes, otherwise it returns false}} 
    `insertBefore()                {{Inserts a new child node before a specified, existing, child node}} 
    `isEqualNode()                 {{Checks if two nodes are equal}} 
    `normalize()                   {{Joins adjacent text nodes and removes empty text nodes}} 
    `removeChild()                 {{Removes a child node}} 
    `replaceChild()                {{Replaces a child node}} 

