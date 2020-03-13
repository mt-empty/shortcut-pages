# Neko Std

> Source: http://nekovm.org/doc/libs#types

> Aliases: neko-types, neko-standard-lib, neko-standard-libraries, neko-standard-libs, neko-type, neko-std-types, neko-standard-library-types, neko-standard-types, neko-classes, neko-modules, neko-standard-library

$ Values
    `int                           {{31 bits integer in decimal form (12345) or hexadecimal (0x1A2B3C4D)}} 
    `float                         {{64-bit double-precision floating-point number}} 
    `bool                          {{Boolean. `true` and `false`}} 
    `string                        {{Sequence of 8-bit bytes. A string can contain `\0` characters.}} 
    `array                         {{Integer-indexed table of values, with the index starting at 0.}} 
    `object                        {{Object is a table, which associates an identifier or a string to a value.}} 
    `function                      {{Function is a value in Neko, and thus can be stored in any variable.}} 
    `null                          {{The special value `null` is used for uninitialized variables as well as programmer/language specific coding techniques.}} 
    `void                          {{Nothing or any meaningful value.}} 
    `abstract                      {{An abstract value is C data that cannot be accessed from a Neko program.}} 

$ Standard Types
    `Buffer                        {{A buffer can store any value as a string and will only allocate the total needed space when requested. It makes a copy of each value when stored so modifying them after is not a problem.}} 
    `Date                          {{Date are using standard C functions in order to manipulate a 32 bit integer. Dates are then represented as the number of seconds elapsed since 1st January 1970.}} 
    `File                          {{The file api can be used for different kind of file I/O.}} 
    `Int32                         {{Int32 is an abstract type that can be used to store the full 32 bits of an integer. The type 'int32 means that the value is a real int32. The type `#int32` means (int | 'int32) and accept then the both kind of integers.}} 
    `Math                          {{Mathematical functions.}} 
    `MD5                           {{MD5 digest functions.}} 
    `Memory                        {{An API for memory manipulation and statistics.}} 
    `Module                        {{An API for reflexion of Neko bytecode modules.}} 
    `Random                        {{A seeded pseudo-random generator.}} 
    `Serialize                     {{Serialization can be used in order to store permanantly some runtime value. Serialization of all values is possible, except Abstracts, with the special cases of 'int32 and 'hash which are handled as specific cases.}} 
    `Socket                        {{TCP and UDP sockets.}} 

$ Standard Types 
    `String                        {{Some useful functions dealing with string manipulation.}} 
    `System                        {{Interactions with the operating system.}} 
    `UTF8                          {{Operations on UTF8 strings.}} 
    `Xml                           {{The standard event-driven XML parser.}} 
    `Thread                        {{An Api to create and manage system threads.}} 
    `Ui                            {{Core native User Interface support. This API uses native WIN32 API on Windows, Carbon API on OSX, and GTK2 on Linux.}} 
    `Process                       {{An API for starting and communication with sub processes.}} 
    `Misc                          {{Miscellaneous functions for different usages.}} 
    `Regexp                        {{Regular expressions using PCRE engine.}} 
    `Mysql                         {{API to connect and use MySQL database.}} 
    `Mod_neko                      {{Apache access when running inside mod_neko.}} 
    `Sqlite                        {{Sqlite is a small embeddable SQL database that store all its data into a single file.}} 
    `ZLib                          {{Give access to the popular ZLib compression library, used in several file formats such as ZIP and PNG.}} 

$ Runtime Type Information
    `null $tnull                   {{0}} 
    `int $tint                     {{1}} 
    `float $tfloat                 {{2}} 
    `bool $tbool                   {{3}} 
    `string $tstring               {{4}} 
    `object $tobject               {{5}} 
    `array $tarray                 {{6}} 
    `function $tfunction           {{7}} 
    `abstract $tabstract           {{8}} 

$ Special Return Type Notations
    `any                           {{Any value is accepted.}} 
    `void                          {{Can be used if the function is not supposed to return any meaningful value.}} 
    `number                        {{Both `int` and `float` are accepted.}} 
    `function:n                    {{Function with `n` arguments is accepted (use -1 if multiple arguments).}} 
    `type array                    {{Array containing only elements of type `type`. e.g.: `int array`}} 
    `{ x => type, y => type }      {{Objects that must contain some fields of some types.}} 
    `type?                         {{Nullable, which means `null` value is accepted as well as some other type. e.g.: `int?` means `int` or `null`}} 
    `type|type                     {{Several types are accepted you can separate them with pipes. e.g.: `int | float`}} 

