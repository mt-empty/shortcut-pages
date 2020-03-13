# Jinja

> Source: jinja.pocoo.org

> Aliases: jinja-template

$ Template Design
    `{% ... %}                     {{For control statements}} 
    `{{ ... }}                     {{For expressions to print to the template output}} 
    `# ... ##                      {{For line statements}} 
    `{# ... #}                     {{For comments not included in the template output}} 

$ Control Statements
    `{% for var in foo %} ... {% endfor %}
>                                  {{For loop}} 
    `{% foo %} ... {% endif %}     {{If statement}} 
    `{% macro foo(param1,param2,.. %} ... {% endmacro %}
>                                  {{Macros are comparable with functions in regular programming languages}} 

$ Builtin Filters
    `abs(number)                   {{Return the absolute value of the argument}} 
    `attr(obj, name)               {{Get an attribute of an object}} 
    `capitalize(s)                 {{Capitalize a value. The first character will be uppercase, all others lowercase}} 
    `center(value, width=number)   {{Centers the value in a field of a given width}} 
    `escape(s)                     {{Convert the characters &, <, >, ‘, and ” in string s to HTML-safe sequences}} 
    `first(seq)                    {{Return the first item of a sequence}} 
    `groupby(value, attribute)     {{Group a sequence of objects by a common attribute}} 
    `sort(value, reverse=False, case_sensitive=False, attribute=None)
>                                  {{Sort an iterable. Default is ascending}} 
    `trim(value)                   {{Strip leading and trailing whitespace}} 
    `wordcount(s)                  {{Count the words in that string}} 

$ Global Functions
    `range([start, ]stop[, step])  {{Return a list containing an arithmetic progression of integers}} 
    `lipsum(n=num, html=True, min=min, max=max)
>                                  {{Generates some lorem ipsum for the template}} 
    `dict(**items)                 {{A convenient alternative to dict literals}} 
    `Reset()                       {{Resets the cycle to the first item}} 
    `Next()                        {{Goes one item ahead and returns the then-current item}} 
    `Current                       {{Returns the current item}} 

$ Math Operators
    `+                             {{Adds two objects together}} 
    `-                             {{Subtract the second number from the first one}} 
    `/                             {{Divide two numbers and returns a floating point number}} 
    `//                            {{Divide two numbers and return the truncated integer result}} 
    `%                             {{Calculate the remainder of an integer division}} 
    `*                             {{Multiply the left operand with the right one}} 
    `**                            {{Raise the left operand to the power of the right operand}} 

$ Autoescape
    `{% autoescape true %}...{% endautoescape %}
>                                  {{Autoescaping is active within this block}} 
    `{% autoescape false %}...{% endautoescape %}
>                                  {{Autoescaping is inactive within this block}} 

