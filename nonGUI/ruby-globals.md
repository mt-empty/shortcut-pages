# Ruby Globals

> Source: http://docs.ruby-lang.org/en/trunk/globals_rdoc.html

> Aliases: ruby-global-constant, ruby-global-constants, ruby-global, ruby-global-variable, ruby-global-variables

$ Short Variables
    `$!                            {{Last raised exception}} 
    `$@                            {{Backtrace array of the last raised exception}} 
    `$&                            {{Last successfully matched string}} 
    `$`                            {{String to the left  of the last successful match}} 
    `$'                            {{String to the right of the last successful match}} 
    `$+                            {{Highest group matched by the last successful match}} 
    `$1                            {{Nth group of the last successful match, may be > 1}} 
    `$~                            {{Match data from the last match in the current scope}} 
    `$=                            {{Case insensitive flag, nil by default, ineffective}} 
    `$/                            {{Input record separator, newline by default}} 
    `$\                            {{Output record separator for print and IO#write, nil by default}} 
    `$,                            {{Output field separator for print and Array#join, nil by default}} 
    `$;                            {{Default split pattern for String#split, nil by default}} 
    `$.                            {{Current input line number of the last file that was read}} 
    `$<                            {{Virtual concatenation file of files from command line or $stdin}} 
    `$>                            {{Default output for print and printf, $stdout by default}} 
    `$_                            {{Last input line of string by gets or readline}} 
    `$0                            {{Name of the script being executed, may be assignable}} 
    `$*                            {{Command line arguments given for the script sans args}} 
    `$$                            {{Process number of the Ruby running this script}} 
    `$?                            {{Status of the last executed child process, thread-local}} 
    `$:                            {{Load path for scripts and binary modules by load or require}} 
    `$"                            {{Array of module names loaded by require}} 

$ Long Variables
    `$DEBUG                        {{Debug flag, set by -d switch, enables printing of each exception raised to $stderr (but not its backtrace) when true}} 
    `$LOADED_FEATURES              {{Alias of $"}} 
    `$FILENAME                     {{Current input file from $<, same as $<.filename}} 
    `$LOAD_PATH                    {{Alias of $:}} 
    `$stderr                       {{Current standard error output}} 
    `$stdin                        {{Current standard input}} 
    `$stdout                       {{Current standard output}} 
    `$VERBOSE                      {{Verbose flag, set by -w or -v switch, enables warnings when true}} 

$ Command Line Switches
    `$-0                           {{Alias of input record separator $/}} 
    `$-a                           {{Autosplit mode flag, read-only}} 
    `$-d                           {{Alias of $DEBUG}} 
    `$-F                           {{Alias of split pattern $;}} 
    `$-i                           {{Extension for in-place-edit mode, otherwise nil}} 
    `$-I                           {{Alias of load path $:}} 
    `$-l                           {{Line ending processing mode flag, read-only}} 
    `$-p                           {{Print loop flag, read-only}} 
    `$-v                           {{Alias of $VERBOSE}} 
    `$-w                           {{Alias of $VERBOSE}} 

$ Global Constants
    `TRUE                          {{Value of true, the singleton instance of TrueClass}} 
    `FALSE                         {{Value of false, the singleton instance of FalseClass}} 
    `NIL                           {{Value of nil, the singleton instance of NilClass}} 
    `STDIN                         {{Standard input, default value for $stdin}} 
    `STDOUT                        {{Standard output, default value for $stdout}} 
    `STDERR                        {{Standard error output, default value for $stderr}} 
    `ENV                           {{Hash of current environment variables}} 
    `ARGF                          {{Alias of virtual input file $<}} 
    `ARGV                          {{Alias of command line arguments $*}} 
    `DATA                          {{Script file object, pointing just after __END__}} 
    `RUBY_VERSION                  {{Version string}} 
    `RUBY_RELEASE_DATE             {{Release date string}} 
    `RUBY_PLATFORM                 {{Platform identifier string}} 

