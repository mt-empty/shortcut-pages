# NodeJS

> Source: https://www.gosquared.com/resources/node-cheat-sheet/

> Aliases: node-js, node.js

$ Getting Started
    `node script.js                {{Run script}} 
    `npm install <package>         {{Install package with npm}} 

$ Globals
    `var variable                  {{Initialize local variable to module}} 
    `process                       {{Properties and methods for current process}} 
    `console                       {{Print out to stdout and stderr}} 
    `require()                     {{To require modules}} 
    `require.resolve               {{Lookup location of module}} 
    `require.paths                 {{Paths to search for modules}} 
    `module                        {{reference to current module}} 
    `_filename                     {{Filename of script being executed}} 

$ Stdio
    `stdio                         {{Object for printing out to stdout and stderr}} 
    `console.log(string)           {{Print to stdout with new line}} 
    `console.error(string)         {{Print to stderr with new line}} 
    `console.error(string)         {{Print to stderr with new line}} 
    `console.time(label)           {{Set time marker}} 
    `console.timeEnd(label)        {{Finish timer and record output}} 
    `console.trace()               {{Print stack trace}} 

$ Process
    `process                       {{Global object. Instance of EventEmitter}} 
    `process.on(SIGNAL, callback)  {{Signal emitted when process receives a signal}} 
    `process.on('exit', function(code) );
>                                  {{Emitted when the process is about to exit}} 
    `uncaughtException             {{Exception bubbled back to event loop}} 
    `process.argv                  {{An array containing the command line arguments}} 
    `process.config                {{An Object containing the JavaScript representation of the configure options that were used to compile the current node executable}} 
    `process.abort();              {{This causes node to emit an abort. This will cause node to exit and generate a core file}} 

$ Util
    `util.debug(message)           {{Synchronous console.error(message)}} 
    `util.log(message)             {{Print timestamped message to stdout}} 
    `util.format(format, ...);     {{Returns a formatted string using the first argument as a printf-like format. (%s, %d, %j)}} 
    `util.puts(...);               {{A synchronous output function. Will block the process and output all arguments to stdout with newlines after each argument}} 
    `util.isArray(object);         {{Returns true if the given object is an Array, false otherwise}} 
    `util.inherits(constructor, superConstructor);
>                                  {{Inherit the prototype methods from one constructor into another}} 
    `util.isDate(object);          {{Returns true if the given object is a Date, false otherwise.}} 

$ Event Emitter
    `events                        {{Callback functions executed when events occur are listeners}} 
    `emitter.on(event, listener)   {{Add a listener for event}} 
    `emitter.once(event, listener) {{Fire listener once}} 
    `emitter.removeListener(event,listener)
>                                  {{Remove a listener}} 
    `emitter.removeAllListeners(event)
>                                  {{Remove all listeners}} 
    `emitter.emit(event, arg1, arg2, ...)
>                                  {{Execute listeners for this event with supplied args}} 

$ Net
    `net                           {{Asynchronous network wrapper for creating streams}} 
    `server.listenFD(fd)           {{Listen on file descriptor fd}} 
    `server.close()                {{Stop accepting new connections}} 
    `socket.bufferSize             {{Number of characters in internal write buffer}} 
    `socket.end()                  {{Send FIN packet}} 
    `socket.pause()                {{Pause reading of data}} 

$ Events
    `connect                       {{Socket connection established}} 
    `end                           {{Other end of socket sent FIN packet}} 
    `data                          {{Data is received}} 
    `timeout                       {{Timed out from inactivity}} 
    `drain                         {{Write buffer has become empty}} 
    `error                         {{Error has occurred. close event emitted after}} 
    `close                         {{Socket fully closed}} 

