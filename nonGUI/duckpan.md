# DuckPan

> Source: http://docs.duckduckhack.com/resources/duckpan-overview.html

> Aliases: duck-pan, duckpan-tool, duck-pan-tool

$ Help Commands
    `duckpan                       {{Prints out the DuckPAN man page}} 
    `duckpan help                  {{Prints out the DuckPAN man page}} 
    `man duckpan                   {{Prints out the DuckPAN man page}} 

$ Update Commands
    `duckpan update                {{The update command will update to the latest version of the duckpan tool}} 
    `duckpan upgrade               {{The upgrade command will update both the duckpan tool and the DDG package}} 

$ Generating Instant Answer Boilerplate in the Goodie repository
    `duckpan new                   {{This command has several preset file templates you can choose from}} 
    `duckpan new --template default
>                                  {{Creates the basic file types you might need in your Goodie: a Perl file and a test file, both in their correct directories}} 
    `duckpan new --template cheatsheet
>                                  {{Creates the single necessary JSON file for a cheatsheet in the correct directory}} 
    `duckpan new --template javascript
>                                  {{Creates a JavaScript-heavy Goodie, including a minimal Perl file, a frontend JavaScript file, and a test file}} 
    `duckpan new --template all    {{creates all possible file types you might need in your Goodie}} 
    `duckpan new --template cheatsheet
>                                  {{Creates the single necessary JSON file for a cheatsheet in the correct directory}} 

$ Generating Instant Answer Boilerplate in the Spice repository
    `duckpan new                   {{This command has several preset file templates you can choose from}} 
    `duckpan new --template default
>                                  {{Creates the basic file types you might need in your Spice}} 
    `duckpan new --template all    {{Creates all possible file types you might need in your Spice}} 

$ Instant Answer Testing
    `duckpan query                 {{Test Goodie and Spice triggers interactively on the command line}} 
    `duckpan server --verbose      {{To provide more details}} 
    `duckpan server --no-cache     {{To prevent DuckPAN's cache from being used (this forces the requested files to be pushed into the cache)}} 
    `duckpan server --port         {{To specify which port DuckPAN's server should run on}} 

$ Configuration Commands
    `duckpan env                   {{View env commands and also shows the env variables currently stored in ~/.duckpan/env.ini}} 
    `duckpan env <name> <value>    {{Add an environment variable that duckpan will remember. Useful for spice API keys. Variables are stored in ~/.duckpan/env.ini}} 
    `duckpan env <name>            {{Retrieve the matching key for a given env variable}} 
    `duckpan env rm <name>         {{Remove an environment variable from duckpan}} 
    `duckpan release               {{Release the project of the current directory to DuckPAN}} 

$ Advanced Install Commands
    `duckpan installdeps           {{Install all requirements of the specific DuckDuckHack project (if possible)}} 
    `duckpan roadrunner            {{Same as installdeps, but avoids testing anything}} 
    `duckpan check                 {{Check if you fulfill all requirements for the development environment}} 
    `duckpan reinstall             {{Force installation of the latest released versions of DuckPAN and DDG}} 

