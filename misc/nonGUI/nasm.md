# NASM

> Source: http://ccm.net/faq/1559-compiling-an-assembly-program-with-nasm

> Aliases: nasm-install, nasm-on-ubuntu, compiling-nasm-program

$ Install on Ubuntu
    `sudo apt-get install nasm     {{Installs NASM software on your machine.}} 

$ NASM Manual
    `man nasm                      {{Gives the mannual pages for NASM}} 

$ Assemble Source File
    `nasm -f elf [filename].asm    {{Assembles the source file (filename.asm) and creates an object file (filename.o) in the current directory. NOTE: This file is not executable.}} 

$ Make Executable File
    `ld [filename].o -o [filename] {{Use if program begins with a procedure called "_start". Creates executable file(filename.exe)}} 
    `gcc [filename].o -o [filename]
>                                  {{Use if program begins with a procedure called "main". Creates executable file(filename.exe)}} 

$ Execute
    `. / [filename]                {{Runs the program.}} 

