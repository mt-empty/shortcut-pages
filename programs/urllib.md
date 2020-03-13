# Python urllib cheatsheet

> Source: https://docs.python.org/2/library/urllib.html

> Aliases: python-urllib

$ High-level interface
    `urllib.urlopen(url)           {{Open a network object denoted by a URL for reading}} 
    `urllib.urlretrieve(url, filename)
>                                  {{Copy a network object denoted by a URL to a local file}} 
    `urllib.urlcleanup()           {{Clear the cache that may have been built up by previous calls to urlretrieve()}} 

$ Utility functions
    `urllib.quote(string)          {{Replace special characters in string using the %xx escape}} 
    `urllib.quote_plus(string)     {{Like quote(), but also replaces spaces by plus signs}} 
    `urllib.unquote(string)        {{Replace %xx escapes by their single-character equivalent}} 
    `urllib.unquote_plus(string)   {{Like unquote(), but also replaces plus signs by spaces}} 
    `urllib.urlencode(query)       {{Convert a sequence of two-element tuples to a “percent-encoded” string}} 
    `urllib.pathname2url(path)     {{Convert the path from local syntax to percent-encoded URL}} 
    `urllib.url2pathname(path)     {{Convert path from a percent-encoded URL to local syntax for path}} 
    `urllib.getproxies()           {{Returns a dictionary of scheme to proxy server URL mappings.}} 

$ URL Opener objects
    `class urllib.URLopener(...)   {{Base class for opening and reading URLs}} 
    `class urllib.FancyURLopener(...)
>                                  {{Provides default handling for the following HTTP response codes: 301, 302, 303, 307 and 401}} 

