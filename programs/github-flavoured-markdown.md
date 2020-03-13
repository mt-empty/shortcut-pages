# Github Flavoured Markdown

> Source: https://help.github.com/articles/github-flavored-markdown/

> Aliases: gfm, ghfmd

$ Multiple Underscores In Words
    `eat_apple_daily               {{Markdown transforms underscores (_) into italics, GFM ignores underscores in words}} 

$ URL Autolinking
    `http://example.com            {{GFM will autolink standard URLs, so if you want to link to a URL, instead of setting link text}} 

$ Strikethrough
    `~~text~~                      {{GFM adds syntax to create strikethrough text, which is missing from standard Markdown}} 

$ Fenced Code Blocks
    ```` Code block... ```         {{Standard Markdown converts text with four spaces at the beginning of each line into a code block; GFM also supports fenced blocks.}} 

$ Syntax Highlighting
    ````ruby ... code block ```    {{Code blocks can be taken a step further by adding syntax highlighting. In your fenced block, add an optional language identifier}} 

$ Tables
    `First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
>                                  {{You can create tables by assembling a list of words and dividing them with hyphens -
(for the first row), and then separating each column with a pipe |}} 

$ Inline HTML
    `<p>text</p>                   {{You can use a subset of HTML within your READMEs, issues, and pull requests}} 

