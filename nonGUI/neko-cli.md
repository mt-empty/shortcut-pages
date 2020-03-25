# Neko VM

> Source: http://nekovm.org/doc/tools

> Aliases: neko, nekoc, nekovm, nekotools, neko-vm, neko-tool, neko-tools, neko-toolkit, neko-compiler, nekoml-compiler, neko-virtual-machine

$ Setup
    `export NEKOPATH=/custom/libs/path[:/another/path]
>                                  {{Setup the $NEKOPATH environment variable so the runtime can find the Neko libraries. 
Paths is separated by `:` like a $PATH.}} 
    `neko test                     {{Run the tests to check that everything is setup correctly.}} 

$ Virtual Machine
    `neko bytecode_file.n          {{Run the bytecode in the bytecode_file.n module.}} 
    `neko -version                 {{Print version.}} 

$ Neko Compiler
    `nekoc source_file.neko        {{Compile your hello.neko file into a hello.n file containing the compiled bytecode of your sources.}} 
    `nekoc --help                  {{Show the list of options.}} 
    `nekoc -link <output.n> [input.n] [input.n] ...
>                                  {{Join together several bytecode files into a single file.}} 
    `nekoc -doc <source_file>      {{Documentation is exported to HTML, which being produced from comments in Neko source code.}} 
    `nekoc -console                {{Run a read-execute-print loop. Type '!' to execute the code.}} 
    `nekoc -d <bytecode_file>      {{Dump the bytecode from a compiled file. It will output a file with '.dump' as the extension.}} 
    `nekoc -z <bytecode_file>      {{Strip the debug information and global names from compiled bytecode. This is done in-place and doesn't create a new file.}} 
    `nekoc -p <source_file>        {{Prettify, create a properly formatted version of a source file.}} 
    `nekoc -version                {{Set the bytecode version.}} 
    `-o [directory]                {{Set the output directory.}} 
    `-v                            {{Verbosity mode on.}} 

$ NekoML Compiler
    `nekoml [options] <source_file> [source_file] ...
>                                  {{Compile NekoML source files.}} 
    `nekoml --help                 {{Show the list of optional keys.}} 
    `-p <path>                     {{Additional file search path.}} 
    `-v                            {{Verbose mode on.}} 
    `-n                            {{Generate intermediate .neko files.}} 
    `-pack <file>                  {{Build module packages.}} 
    `-use <file>                   {{Use specified module package.}} 
    `-nostd                        {{Disable std lib}} 

$ Web Server
    `nekotools server [options]    {{Start a Neko web server.}} 
    `open http://localhost:2000/server:config
>                                  {{Server configuration page.}} 
    `nekotools server --help       {{Show the list of options for web server.}} 
    `-p <port>                     {{Change server port.}} 
    `-h <host>                     {{Change server host.}} 
    `-d <dir>                      {{Change the server base directory. Default: $PWD.}} 
    `-log <file>                   {{Set log file.}} 
    `-rewrite                      {{Activate pseudo mod-rewrite for smart urls.}} 

$ Utilities
    `nekotools --help              {{Show the list of commands.}} 
    `nekotools boot <file.n>       {{Build an standalone executable from Neko bytecode.}} 

