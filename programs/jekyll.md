# Jekyll

> Source: https://jekyllrb.com/

$ Jekyll Commands
    `jekyll server                 {{Serve your site locally}} 
    `jekyll docs                   {{Launch local server with docs for Jekyll}} 
    `jekyll build                  {{Build your site}} 
    `jekyll doctor                 {{Search site and print specific deprecation warnings}} 
    `jekyll new                    {{Creates a new Jekyll site scaffold in PATH}} 
    `jekyll help                   {{Show the help message, optionally for a given subcommand}} 

$ Global Variables
    `site                          {{Sitewide information plus configuration settings from  _config.yml}} 
    `page                          {{Page specific information plus the front matter}} 
    `content                       {{In layout files, the rendered content of the Post or Page being wrapped}} 
    `docker events                 {{gets events from container}} 
    `docker port                   {{shows public facing port of container}} 
    `paginator                     {{When the paginate configuration option is set variable becomes available}} 

$ Site Variables
    `site.time                     {{The current time (when you run the jekyll command)}} 
    `site.pages                    {{A list of all Pages}} 
    `site.posts                    {{A reverse chronological list of all Posts}} 
    `site.html_pages               {{A list of all HTML Pages}} 
    `site.collections              {{A list of all the collections}} 
    `site.data                     {{A list containing the data loaded from the files located in the _data folder}} 
    `site.tags.TAG                 {{The list of all Posts with tag TAG}} 

$ Page Variables
    `page.content                  {{The content of the Page, rendered or un-rendered}} 
    `page.title                    {{The title of the Page}} 
    `page.excerpt                  {{The un-rendered excerpt of the Page}} 
    `page.url                      {{The URL of the Post without the domain, but with a leading slash}} 
    `page.id                       {{An identifier unique to the Post}} 
    `page.date                     {{The Date assigned to the Post}} 

$ Liquid Template Filters
    `{{ | capitalize }}            {{Capitalize words in the input sentence}} 
    `{{ 'foobarfoobar' | remove:'foo' }}
>                                  {{Remove each occurrence}} 
    `{{ | date }}                  {{Reformat a date}} 
    `{{ | first }}                 {{Get the first element of the passed in array}} 
    `{{ 4  | minus:2 }}            {{Subtraction}} 
    `{{ | escape }}                {{Escape a string}} 

$ Jekyll Filters
    `{{ site.time | date_to_rfc822 }}
>                                  {{Convert date to RFC-822 format}} 
    `{{ site.posts | sort: 'author' }}
>                                  {{Optional args for hashes}} 
    `{{ page.content | xml_escape }}
>                                  {{Escape some text for use in XML}} 
    `{{ page.tags | sort }}        {{Sort an array}} 
    `{{ page.excerpt | markdownify }}
>                                  {{Convert a Markdown-formatted string into HTML}} 
    `{{ page.content | number_of_words }}
>                                  {{Count the number of words in some text}} 

