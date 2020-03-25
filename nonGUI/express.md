# Express

> Source: http://expressjs.com/en/4x/api.html

> Aliases: expressjs, express-js

$ Express
    `var express = require('express'); var app = express();
>                                  {{Creates an Express application}} 
    `var router = express.Router([options]);
>                                  {{Creates a new router object}} 

$ Application
    `app.use([path,] function [, function...])
>                                  {{Mounts the specified middleware function or functions at the specified path}} 
    `app.set(name, value)          {{Assigns setting name to value, where name is one of the application level properties like 'env'}} 
    `app.route(path)               {{Returns an instance of a single route, which you can then use to handle HTTP verbs with optional middleware}} 
    `app.render(view, [locals], callback)
>                                  {{Returns the rendered HTML of a view via the callback function}} 
    `app.put(path, callback [, callback ...])
>                                  {{Routes HTTP PUT requests to the specified path with the specified callback functions}} 
    `app.post(path, callback [, callback ...])
>                                  {{Routes HTTP POST requests to the specified path with the specified callback functions}} 
    `app.path()                    {{Returns the canonical path of the app, a string}} 
    `app.param([name], callback)   {{Add callback triggers to route parameters, where name is the name of the parameter}} 
    `app.METHOD(path, callback [, callback ...])
>                                  {{Routes an HTTP request, where METHOD is the HTTP method of the request, such as GET, PUT, POST, and so on, in lowercase}} 
    `app.listen(port, [hostname], [backlog], [callback])
>                                  {{Binds and listens for connections on the specified host and port}} 
    `app.get(path, callback [, callback ...])
>                                  {{Routes HTTP GET requests to the specified path with the specified callback functions}} 
    `app.get(name)                 {{Returns the value of name app setting, where name is one of strings in the application settings}} 
    `app.engine(ext, callback)     {{Registers the given template engine callback as ext}} 
    `app.enabled(name)             {{Returns true if the setting name is enabled (true), where name is one of the properties from the application settings}} 
    `app.enable(name)              {{Sets the Boolean setting name to true, where name is one of the properties from the application settings}} 
    `app.disabled(name)            {{Returns true if the Boolean setting name is disabled (false), where name is one of the properties from application settings}} 
    `app.disable(name)             {{Sets the Boolean setting name to false, where name is one of the properties from the application settings}} 
    `app.delete(path, callback [, callback ...])
>                                  {{Routes HTTP DELETE requests to the specified path with the specified callback functions}} 
    `app.all(path, callback [, callback ...])
>                                  {{This method matches all HTTP verbs}} 
    `app.locals({ title: "MyApp" });
>                                  {{The app.locals object has properties that are local variables within the application}} 

$ Request
    `req.is(type)                  {{Returns true if the incoming request’s “Content-Type” HTTP header field matches the MIME type specified by the type parameter}} 
    `req.get(field)                {{Returns the specified HTTP request header field (case-insensitive match). The Referrer and Referer fields are interchangeable}} 
    `req.xhr                       {{A Boolean property that is true if the request’s X-Requested-With header field is "XMLHttpRequest", indicating that the request was issued by a client library such as jQuery}} 
    `req.secure                    {{A Boolean property that is true if a TLS connection is established. Equivalent to}} 
    `req.query                     {{This property is an object containing a property for each query string parameter in the route}} 
    `req.path                      {{Contains the path part of the request URL}} 
    `req.params                    {{This property is an object containing properties mapped to the named route "parameters"}} 
    `req.ip                        {{Contains the remote IP address of the request}} 
    `req.cookies                   {{When using cookie-parser middleware, this property is an object that contains cookies sent by the request}} 
    `req.body                      {{Contains key-value pairs of data submitted in the request body}} 
    `req.baseUrl                   {{The URL path on which a router instance was mounted}} 
    `req.app                       {{This property holds a reference to the instance of the Express application that is using the middleware}} 

$ Response
    `res.type(type)                {{Sets the Content-Type HTTP header to the MIME type as determined by mime.lookup() for the specified type}} 
    `res.status(code)              {{Sets the HTTP status for the response. It is a chainable alias of Node’s response.statusCode}} 
    `res.set(field [, value])      {{Sets the response’s HTTP header field to value}} 
    `res.sendFile(path [, options] [, fn])
>                                  {{Transfers the file at the given path}} 
    `res.send([body])              {{Sends the HTTP response}} 
    `res.render(view [, locals] [, callback])
>                                  {{Renders a view and sends the rendered HTML string to the client}} 
    `res.redirect([status,] path)  {{Redirects to the URL derived from the specified path, with specified status, a positive integer corresponds to an HTTP status code}} 
    `res.location(path)            {{Sets the response Location HTTP header to the specified path parameter}} 
    `res.links(links)              {{Joins the links provided as properties of the parameter to populate the response’s Link HTTP header field}} 
    `res.jsonp([body])             {{Sends a JSON response with JSONP support}} 
    `res.json([body])              {{Sends a JSON response}} 
    `res.get(field)                {{Returns the HTTP response header specified by field}} 
    `res.end([data] [, encoding])  {{Ends the response process}} 
    `res.clearCookie(name [, options])
>                                  {{Clears the cookie specified by name}} 
    `res.attachment([filename])    {{Sets the HTTP response Content-Disposition header field to \“attachment\”}} 
    `res.append(field [, value])   {{Appends the specified value to the HTTP response header field.}} 
    `res.locals                    {{An object that contains response local variables scoped to the request}} 
    `res.headersSent               {{Boolean property that indicates if the app sent HTTP headers for the response}} 

$ Router
    `router.use([path], [function, ...] function)
>                                  {{Uses the specified middleware function or functions, with optional mount path path, that defaults to "/"}} 
    `router.route(path)            {{Returns an instance of a single route which you can then use to handle HTTP verbs with optional middleware}} 
    `router.METHOD(path, [callback, ...] callback)
>                                  {{The router.METHOD() methods provide the routing functionality in Express, where METHOD is one of the HTTP methods}} 
    `router.all(path, [callback, ...] callback)
>                                  {{This method is just like the router.METHOD() methods, except that it matches all HTTP methods}} 

