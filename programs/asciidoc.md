# Asciidoc

> Source: http://powerman.name/doc/asciidoc

> Aliases: adoc

$ Headers
    `= DOCTITLE                    {{Document Title}} 
    `= Heading                     {{H1. Can also be created by putting four or more dashes under Heading}} 
    `== Heading                    {{H2. Can also be created by putting four or more tildes under Heading}} 
    `=== Heading                   {{H3. Can also be created by putting four or more carets under Heading}} 
    `==== Heading                  {{H4. Can also be created by putting four or more pluses under Heading}} 

$ Emphasis
    `_text_                        {{Displays the text in italics}} 
    `*text*                        {{Displays the text in bold}} 
    `*_text_*                      {{Displays the text in bold and italics}} 
    `[line-through]#text#          {{Adds strikethrough effect to the text}} 
    `[line-through]*text*          {{Adds strikethrough effect to the text and makes it bold}} 

$ Lists
    `1. item1                      {{First ordered list item}} 
    `2. item2                      {{Second ordered list item}} 
    `. Item                        {{Ordered list item}} 
    `.. Item                       {{Ordered sublist item}} 
    `* Item                        {{Unordered list item}} 
    `** Item                       {{Unordered sublist item}} 

$ Links
    `https://duckduckgo.com[link text]
>                                  {{Inline-style link}} 
    `[[anchor-id]]                 {{Create an anchor for a block}} 
    `<<anchor-id, anchor text>>    {{Inline-style anchor link}} 

$ Images
    `image:https://github.com/n48.png[Logo Title]
>                                  {{Inline style}} 
    `image::https://github.com/n48.png[Logo Title]
>                                  {{Block style}} 
    `image:https://github.com/n48.png["Logo title",width=24,link="https://github.com/n48.png"]
>                                  {{Inline style with thumbnail width of 24px}} 

$ Code and Syntax Highlighting
    `[source,perl]----die 'connect: '.$dbh->errstr;----
>                                  {{Source block with perl syntax highlighting}} 

$ Blockquotes
    `[quote, cite author, cite source]____DuckDuckGo rocks____
>                                  {{Blockquotes, with optional citation}} 

$ Inline HTML
    `pass:[<b>Duck</b>DuckGo]      {{You can use raw HTML in your asciidoc}} 

$ Horizontal Rule
    `'''                           {{You can get a horizontal rule by typing three or more apostrophes (') on a line}} 

$ Special
    `:ATTRIBNAME: ATTRIBVAL        {{Set attribute ATTRIBNAME to ATTRIBVAL}} 
    `ATTRIBNAME                    {{Print the value of ATTRIBVNAME}} 
    `{ATTRIBNAME                   {{Print {ATTRIBNAME}}} 
    `include::file.adoc[]          {{Include the contents of file.adoc}} 

