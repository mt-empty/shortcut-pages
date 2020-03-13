# John the ripper

> Source: https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf

> Aliases: jtr

$ Installation
    `git clone https://github.com/magnumripper/JohnTheRipper -b bleeding-jumbo
>                                  {{Cloning}} 
    `cd JohnTheRipper/ && cd src/ && ./configure && make clean && make -s
>                                  {{Compile}} 
    `[path of JTR folder] ./john   {{Execute}} 

$ Cracking Modes
    `./john --wordlist=password.list hashfile
>                                  {{Wordlist Mode(Dictionary Attack)}} 
    `./john --wordlist=password.lst –rules:<rulename> hashfile
>                                  {{Mangling Rules Mode (hybrid)}} 
    `./john --incremental hashfile {{Incremental mode (Brute Force)}} 
    `./john --external: <rulename> hashfile
>                                  {{External mode (use a program to generate guesses)}} 
    `./john --loopback hashfile    {{Loopback mode (use POT as wordlist)}} 
    `./john --mask=?1?1?1?1?1?1?1?1 -1=A-Z hashfile -min-len=8
>                                  {{Mask mode (read MASK under /doc)}} 
    `./john -w=password.lst -mask='?l?l?w?l?l' hashfile
>                                  {{Hybrid Mask mode}} 
    `./john --prince=wordlist hashfile
>                                  {{Prince mode (Read PRINCE under /doc)}} 
    `./calc_stat wordlist markovstats && ./john -markov:200 -max-len:12 hashfile --mkv-stats=markovstats
>                                  {{Markov mode (Read MARKOV under /doc)}} 

$ Rule Sets
    `--rules:Single                {{For single mode}} 
    `--rules:Wordlist              {{To include a wordlist}} 
    `--rules:Extra                 {{}} 
    `--rules:Jumbo                 {{To include all above rule sets(Single, wordlist, extra)}} 
    `--rules:KoreLogic             {{}} 
    `--rules:All                   {{To include all possible rule sets}} 

$ Incremental Mode Options
    `--incremental:Lower           {{26 char}} 
    `--incremental:Alpha           {{52 char}} 
    `--incremental:Digits          {{10 char}} 
    `--incremental:Alnum           {{62 char}} 

$ Other Commands
    `./john --list=hidden-options  {{List all Hidden Options}} 
    `./john --incremental:Alpha -stdout -session=s1
>                                  {{Dsiplay guesses}} 
    `./john hashes -session=name   {{Create Session}} 
    `./john --restore:name         {{Restore Session}} 
    `./john hashes --pot=<> --show {{Show cracked Passwords}} 

