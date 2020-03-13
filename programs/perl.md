# Perl

> Source: http://www.cheatography.com/mishin/cheat-sheets/perl-reference-card/

$ Input/Output
    `open(INFILE,"in.txt") or die; {{Open file for input}} 
    `open(INFILE,"<:utf8","file"); {{Open file with encoding}} 
    `open(TMP,"+>", undef);        {{Open anonymous temp file}} 
    `open(MEMORY,'>', \$var);      {{open in-memory file}} 
    `open(OUT,">out.txt") or die;  {{Open output file}} 
    `open(LOG,">>my.log") or die;  {{Open file for append}} 
    `$line = <INFILE>;             {{Get next line}} 
    `@lines = <INFILE>;            {{Slurp infile}} 
    `print STDERR "Warning 1.\n";  {{Print to STDERR}} 
    `close INFILE;                 {{Close filehandle}} 

$ Scalars and Strings
    `chomp($str);                  {{Discard trailing \n}} 
    `$v = chop($str);              {{$v becomes trailing char}} 
    `eq, ne, lt, gt, le, ge, cmp   {{String comparison}} 
    `$v = index($str, $x);         {{Find index of $x in $str,}} 
    `$v = rindex($str, $x);        {{Starting from left or right}} 
    `$v = substr($str, $strt, $len);
>                                  {{Extract substring}} 
    `$cnt = $sky =~ tr/0-9//;      {{Count the digits in $sky}} 
    `$str =~ tr/a-zA-Z//cs;        {{Change non-alphas to space}} 
    `$v = sprintf(“%10s %08d”,$s,$n);
>                                  {{Format string}} 

$ Arrays and Lists
    `@a = (1..5);                  {{Array initialization}} 
    `$i = @a;                      {{Number of elements in @a}} 
    `($a, $b) = ($b, $a);          {{Swap $a and $b}} 
    `$x = $a[1];                   {{Access to index 1}} 
    `$i = $#a;                     {{Last index in @a}} 
    `push(@a, $s);                 {{Appends $s to @a}} 
    `$a = pop(@a);                 {{Removes last element}} 
    `chop(@a);                     {{Remove last char (per el.)}} 
    `$a = shift(@a);               {{Removes first element}} 
    `reverse(@a);                  {{Reverse @a}} 
    `@a = sort{$ela <=> $elb}(@a); {{Sort numerically}} 
    `@a = split(/-/,$s);           {{Split string into @a}} 

$ Hashes
    `%h=(k1 => “val1”,k2 => 3);    {{Hash initialization}} 
    `$val = $map{k1};              {{Recall value}} 
    `@a = %h;                      {{Array of keys and values}} 
    `%h = @a;                      {{Create hash from array}} 
    `foreach $k (keys(%h)){..}     {{Iterate over list of keys}} 
    `foreach $v (vals(%h)){..}     {{Iterate over list of values}} 
    `while (($k,$v)=each %h){..}   {{Iterate over key-value-pairs}} 
    `delete $h{k1};                {{Delete key}} 

$ Basic Syntax
    `($a, $b) = @ARGV;             {{Read command line params}} 
    `sub p{my $var = shift; ...}   {{Define subroutine}} 
    `p(“bla”);                     {{Execute subroutine}} 
    `if(expr){} elsif {} else {}   {{Conditional}} 
    `unless (expr){}               {{Negative conditional}} 
    `while (expr){}                {{While-loop}} 
    `until (expr){}                {{Until-loop}} 
    `do {} until (expr)            {{Postcheck until-loop}} 
    `for($i=1; $i<=10; $i++){}     {{For-loop}} 
    `foreach $i (@list){}          {{Foreach-loop}} 
    `last, next, redo              {{End loop, skip to next, jump to top}} 

$ References and Data Structures
    `$aref = \@a;                  {{Reference to array}} 
    `$aref = [1,"foo",undef,13];   {{Anonymous array}} 
    `$el = $aref->[0]; / $el = @{$aref}[0];
>                                  {{Access element of array}} 
    `$aref2 = [@{$aref1}];         {{Copy array}} 
    `$href = \%h;                  {{Reference to hash}} 
    `$href ={APR => 4,AUG => 8};   {{Anonymous hash}} 
    `$el = $href->{APR}; / $el = %{$href}{APR};
>                                  {{Access element of hash}} 
    `$href2 = {%{$href1}};         {{Copy hash}} 
    `if (ref($r) eq "HASH") {}     {{Checks if $r points to hash}} 
    `@a = ([1, 2],[3, 4]);         {{2-dim array}} 
    `$i = $a[0][1];                {{Access 2-dim array}} 

$ System Interaction
    `system(“cat $f|sort -u>$f.s”);
>                                  {{System call}} 
    `@a = readpipe(“lsmod”);       {{Catch output}} 
    `$today = “Today: “.date;      {{Catch output}} 
    `chroot(“/home/user/”);        {{Change root}} 
    `while (<*.c>) {}'             {{Operate on all c-files}} 
    `unlink(“/tmp/file”);          {{Delete file}} 
    `if (-f “file.txt”){...}       {{File test}} 

