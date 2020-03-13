# AJAX

> Source: https://dzone.com/refcardz/getting-started-ajax

$ AJAX Request Methods
    `open(method, url, async)      {{Open a connection to a URL; method = HTTP verb (GET, POST, etc.); url = url to open, may include querystring; async = whether to make asynchronous request}} 
    `onreadystatechange            {{Assign a function object as callback}} 
    `setRequestHeader(namevalue)   {{Add a header to the HTTP request}} 
    `send(body)                    {{Send the request body = string to be used as request body}} 
    `abort()                       {{Stop the request from listening for the response}} 
    `readyState                    {{Stage in lifecycle of response (only populated after send() is called)}} 
    `httpStatus                    {{The HTTP return code (integer, only populated after response reaches the loaded state)}} 
    `responseText                  {{Body of response as a JavaScript string (only set after response reaches the interative readyState)}} 
    `responseXML                   {{Body of response as a XML document object (only set after response reaches the interactive readyState)}} 
    `getResponseHeader(name)       {{Read a response header by name}} 
    `getAllResponseHeaders()       {{Get an array of all response header names}} 

$ Common Mime Types
    `application/x-www-form-urlencoded
>                                  {{Implies that body is an encoded querystring of key-value pairs}} 
    `text/xml, application/xml     {{Implies that body is an XML document}} 
    `text/plain                    {{Implies that body is plain unformatted text}} 
    `text/html, text/xhtml         {{Implies that body is (X)HTML content}} 
    `text/javascript               {{Implies that body is a piece of JavaScript code}} 
    `image/png, image/jpeg, image/gif
>                                  {{Implies that body is a binary image}} 

$ Common HTTP Verbs
    `PUT - (create)                {{Add a new object instance to the domain model}} 
    `GET - (read)                  {{Get an existing domain object from the server}} 
    `POST - (update)               {{Modify an existing domain object}} 
    `DELETE - (delete)             {{Remove an existing object from the domain model}} 

$ AJAX Request ReadyState Values
    `0 - (Uninitialized)           {{The request hasn't yet been sent}} 
    `1 - (Loading)                 {{The request hasn't yet arrived}} 
    `2 - (Loaded)                  {{Request headers can be read}} 
    `3 - (Interactive)             {{Request body is incomplete, but can be read}} 
    `4 - (Complete)                {{Request body is complete}} 

