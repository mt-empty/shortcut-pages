# prove

> Source: http://perldoc.perl.org/prove.html

$ Usage
    `prove [option] [filepath]     {{Start prove}} 

$ Options
    `-I<filepath>                  {{Include this filepath}} 
    `-l                            {{Include ./lib}} 
    `-r                            {{Recursively exec test files}} 
    `-j <n>                        {{Number of jobs in parallel}} 
    `-v                            {{Verbose output}} 
    `-h                            {{Display help text}} 
    `-PPretty                      {{Prettify the test result}} 
    `--exec <program>              {{Run tests with another program (not Perl)}} 

$ Examples
    `prove -lr                     {{Run all *.t tests in t/}} 
    `prove -l t/01-Basics.t        {{Run the t/01-Basics.t test file}} 
    `prove -lrv                    {{Run all *.t tests in t/ with verbose output}} 
    `prove -lr -j 4                {{Run all *.t tests in t/ with 4 processes}} 
    `prove -r /test-dir            {{Run all *.t tests in /test-dir}} 
    `prove --exec perl6 test-dir/  {{Run all *.t tests in test-dir/ with perl6}} 
    `prove -h                      {{Display help page}} 

