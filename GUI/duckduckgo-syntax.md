# DuckDuckGo Syntax

> Source: https://duck.co/help/results/syntax

> Aliases: duckduckgo-search, duckduckgo-search-syntax, ddg-search, duck-duck-go-search, duck-duck-go-search-syntax

$ Triggers
    `LeBron James news             {{Add "news" to your searches to generate instant-answer news results}} 
    `Philadelphia map              {{Add "map" to your search to generate instant-answer map results}} 

$ Go directly to other sites
    `\futurama                     {{Use \ to go to directly to the first search result. We call this I'm Feeling Ducky}} 
    `!a blink182                   {{Use ! to search other sites' search engines directly. We call these !Bangs. (!a blink182 searches Amazon.com for blink182)}} 

$ Group search terms
    `Apple AND Mango               {{Every search term should be used by default. That is, we try hard not to autocorrect your query. In other words, we treat your terms as if you typed AND in between them}} 
    `Apple OR Mango                {{If you want to include one term or another, use the uppercase keyword OR in between terms. OR will only operate on adjacent words. Foo bar OR baz is equivalent to Foo ((bar)OR(baz)).}} 
    `"Eat food" OR "Drink water"   {{Use double quotes to include an entire phrase inside a syntax block. "foo bar" OR baz is equivalent to ((foo bar)OR(baz)).}} 
    `Apple OR Mango OR Food        {{In a chain of ORs, the middle groups are automatically quoted. steve jobs OR ballmer microsoft OR dedalus searches steve ((jobs)OR(ballmer microsoft)OR(dedalus)). If you don't want this to happen, you can use ANDs to group ORs together, as detailed below.}} 
    `Apple OR Mango AND Food OR Water
>                                  {{term1 OR term2 AND term3 OR term4 searches for ((term1)OR(term2)AND(term3)OR(term4)).}} 
    `Foodo Apple OR Orrange AND "Drink Water" OR "Eat"
>                                  {{ORs are applied before ANDs. foo bar OR baz AND "term1 term2" OR term3 is equfoo bar OR baz AND "term1 term2" OR term3 eqivalent to foo (((bar)OR(baz)AND(term1 term2)OR(term3))). This will return pages with the word foo, one of either bar or baz, and one of either "term1 term2" and term3.}} 
    `"The Incredible Hulk" site:rottentomatoes.com OR site:imdb.com
>                                  {{You can use OR in conjunction with the site-search syntax. "The Incredible Hulk" site:rottentomatoes.com OR site:imdb.com will return results containing that phrase from both IMDb and Rotten Tomatoes.}} 
    `                              {{If you're going to use parentheses, make sure you don't have any spaces between a parenthesis and a syntax keyword (OR/AND). Double up parens on the ends and don't include quotes. For instance, use ((foo)OR(bar)) rather than (foo) OR (bar). Likewise, use ((steve jobs)AND((iphone)OR(tablet))) rather than ("steve jobs") AND (iphone OR tablet). If you think you should use parentheses yourself, chances are there is a way to reformulate your query in a manner that makes them unnecessary.}} 

$ Drop terms
    `Apple -mango                  {{Use minus (-) before a word or quoted phrase to have it not appear in results. Excluded words must be the last words in the search}} 

$ Safe search
    `                              {{Add !safeoff to the end of your search to turn off safe search for that search}} 

$ Regional search
    `apple de                      {{Add region:cc (e.g. de) to boost a region.}} 
    `mango region:none             {{Similarly you can do region:none to turn off a region if you have one set by default.}} 
    `streets r:de                  {{Use r: as a shorter abbreviation for region.}} 
    `website site:.cc              {{Use site:.cc to restrict to a country level domain, e.g. site:.uk would only show results from domains ending in .uk.}} 

$ Site search
    `contribute site:duck.co       {{You can add site:domain to your search to restrict the results to a particular domain.}} 
    `duckduckgo site:washingtonpost.com,wsj.com
>                                  {{To use site-search for multiple domains, just separate them with commas.}} 
    `Other tricks                  {{Click on the site icon at the bottom left of a result to do a site search for the domain related to that result. You can also do the same by clicking the More results link to the right of the URL line for a given result.}} 

$ Result filters
    `google.com inbody:about       {{Use inbody: (b: for short) to make sure something appears in the body of the page.}} 
    `google.com intitle:about      {{Use intitle: (t: for short) to make sure something appears in the title of the page.}} 
    `foo bar filetype:pdf          {{Use filetype: (f: for short) to make sure the results are mostly files of that type, e.g. f:pdf.}} 

