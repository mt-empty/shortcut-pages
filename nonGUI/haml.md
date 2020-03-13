# HAML Cheatsheet

> Source: http://haml.info/docs/yardoc/file.REFERENCE.html

> Aliases: html-abstraction-markup-language

$ Basics
    `Plain text                    {{Lines not interpreted as HAML are passed through unmodified}} 
    `<div id="blah">Blah!</div>    {{HTML tags are passed through unmodified as well}} 
    `\= @title                     {{A backslash escapes the first character of a line, allowing use of otherwise interpreted characters as plain text.}} 

$ HTML Elements
    `%one                          {{<one>}} 
    `%one 
 %two 
 %three Divs are easily nested
>                                  {{<one> 
 < two > 
 < three > Divs are easily nested < /three> 
 < /two> 
 < /one>}} 
    `%br/                          {{<br />}} 
    `%div#things                   {{<div id='things'>}} 
    `%span#rice Chicken Fried      {{<span id='rice'>Chicken Fried</span>}} 
    `%p.beans{ :food => 'true' } The magical fruit
>                                  {{<p class='beans' food='true'>The magical fruit</p>}} 
    `%h1.class.otherclass#id La La La
>                                  {{<h1 class='class otherclass' id='id'>La La La</h1>}} 
    `%a{ :href => 'https://duckduckgo.com/' }
>                                  {{<a href='https://duckduckgo.com/'>}} 

$ Comments
    `/ This is the peanutbutterjelly element
>                                  {{<!-- This is the peanutbutterjelly element -->}} 
    `/[if IE]                      {{<!--[if IE]>}} 
    `-# This is a comment          {{The hyphen followed immediately by the pound sign signifies a silent comment. Any text following this isn’t rendered in the resulting document at all.}} 

$ Doctypes
    `!!!                           {{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">}} 
    `!!! 5                         {{<!DOCTYPE html>}} 
    `!!! Strict                    {{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">}} 
    `!!! Frameset                  {{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">}} 

$ Ruby Evaluation
    `= ['hi', 'there', 'reader!'].join " "
>                                  {{hi there reader!}} 
    `%p= "hello"                   {{<p>hello</p>}} 
    `- (42...47).each do |i| 
 % p = i
>                                  {{<p>42</p> 
 < p > 43 < /p> 
 < p > 44 < /p> 
 < p > 45 < /p> 
 < p > 46 < /p>}} 

$ Filters
    `:cdata                        {{Surrounds the filtered text with CDATA tags.}} 
    `:coffee                       {{Compiles the filtered text to Javascript using Cofeescript. You can also reference this filter as :coffeescript. This filter is implemented using Tilt.}} 
    `:css                          {{Surrounds the filtered text with <style> and (optionally) CDATA tags. Useful for including inline CSS. Use the :cdata option to control when CDATA tags are added.}} 
    `:erb                          {{Parses the filtered text with ERb, like an RHTML template. Not available if the :suppress_eval option is set to true. Embedded Ruby code is evaluated in the same context as the Haml template. This filter is implemented using Tilt.}} 
    `:escaped                      {{Works the same as plain, but HTML-escapes the text before placing it in the document.}} 
    `:javascript                   {{Surrounds the filtered text with <script> and (optionally) CDATA tags. Useful for including inline Javascript. Use the :cdata option to control when CDATA tags are added.}} 
    `:less                         {{Parses the filtered text with Less to produce CSS output. This filter is implemented using Tilt.}} 
    `:markdown                     {{Parses the filtered text with Markdown. This filter is implemented using Tilt.}} 
    `:maruku                       {{Parses the filtered text with Maruku, which has some non-standard extensions to Markdown.}} 
    `:plain                        {{Does not parse the filtered text. This is useful for large blocks of text without HTML tags, when you don’t want lines starting with . or - to be parsed.}} 
    `:preserve                     {{Inserts the filtered text into the template with whitespace preserved. preserved blocks of text aren’t indented, and newlines are replaced with the HTML escape code for newlines, to preserve nice-looking output.}} 
    `:ruby                         {{Parses the filtered text with the normal Ruby interpreter. Creates an IO object named haml_io, anything written to it is output into the Haml document.}} 
    `:sass                         {{Parses the filtered text with Sass to produce CSS output. This filter is implemented using Tilt.}} 
    `:scss                         {{Parses the filtered text with Sass like the :sass filter, but uses the newer SCSS syntax to produce CSS output. This filter is implemented using Tilt.}} 
    `:textile                      {{Parses the filtered text with Textile. Only works if RedCloth is installed.}} 

