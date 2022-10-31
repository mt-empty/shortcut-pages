# Csharp

> Source: https://msdn.microsoft.com/en-IN/library/618ayhy6.aspx

$ Keywords
    `abstract                      {{The abstract modifier indicates that the thing being modified has a missing or incomplete implementation.}} 
    `as                            {{ Use the as operator to perform certain type of conversions between compatible reference types or nullable types.}} 
    `base                          {{The base keyword is used to access members of the base class from within a derived class.}} 
    `break                         {{The break statement terminates the closest enclosing loop or switch statement in which it appears.}} 
    `try-catch                     {{The try-catch statement consists of a try block followed by one or more catch clauses, which specify handlers for different exceptions.}} 
    `char                          {{The char keyword is used to represent a Unicode character}} 
    `const                         {{The const keyword to declare a constant field or a constant local. Constant fields and locals aren't variables and may not be modified.}} 
    `delegate                      {{A delegate is a reference type that can be used to encapsulate a named or an anonymous method.}} 
    `double                        {{The double keyword signifies a simple type that stores 64-bit floating-point values.}} 
    `enum                          {{The enum keyword is used to declare an enumeration.}} 
    `fixed                         {{The fixed statement prevents the garbage collector from relocating a movable variable.}} 
    `float                         {{The float keyword signifies a simple type that stores 32-bit floating-point values.}} 
    `goto                          {{The goto statement transfers the program control directly to a labeled statement.}} 
    `implicit                      {{The implicit keyword is used to declare an implicit user-defined type conversion operator.}} 
    `in                            {{For generic type parameters, the in keyword specifies that the type parameter is contravariant.}} 
    `interface                     {{An interface contains only the signatures of methods, properties, events or indexers.}} 
    `is                            {{Checks if an object is compatible with a given type.}} 
    `namespace                     {{The namespace keyword is used to declare a scope that contains a set of related objects.}} 
    `new                           {{The new keyword can be used as an operator, a modifier, or a constraint}} 
    `operator                      {{Use the operator keyword to overload a built-in operator or to provide a user-defined conversion in a class or struct declaration.}} 
    `out                           {{For generic type parameters, the out keyword specifies that the type parameter is covariant.}} 
    `sealed                        {{The ref keyword causes an argument to be passed by reference, not by value.}} 
    `this                          {{The this keyword refers to the current instance of the class and is also used as a modifier of the first parameter of an extension method.}} 
    `unsafe                        {{The unsafe keyword denotes an unsafe context, which is required for any operation involving pointers.}} 
    `volatile                      {{The volatile keyword indicates that a field might be modified by multiple threads that are executing at the same time.}} 

$ Primary Operators
    `.                             {{member access.}} 
    `?.                            {{ null conditional member access. Returns null if the left hand operand is null.}} 
    `f()                           {{ function invocation.}} 
    `?                             {{null conditional indexing.Returns null if the left hand operand is null.}} 
    `++                            {{increment operator.}} 
    `--                            {{decrement operator.}} 
    `Sizeof                        {{returns the size in bytes of the type operand.}} 
    `->                            {{pointer dereferencing combined with member access.}} 

$ Unary Operators
    `+x                            {{returns the value of x.}} 
    `-                             {{numeric negation.}} 
    `!                             {{logical negation.}} 
    `~                             {{bitwise complement.}} 
    `&                             {{address of.}} 

$ Multiplicative Operators
    `*                             {{ multiplication.}} 
    `/                             {{division.}} 
    `%                             {{modulus.}} 

$ Relational Operators
    `<                             {{less than}} 
    `>                             {{greater than}} 
    `<=                            {{less than or equal to.}} 
    `>=                            {{greater than or equal to.}} 

$ Assignment and Lambda Operators
    `=                             {{assignment.}} 
    `+=                            {{x+=y equivalent to x=x+y}} 
    `-=                            {{x-=y equivalent to x=x-y}} 
    `*=                            {{x*=y equivalent to x=x*y}} 
    `/=                            {{x/=y equivalent to x=x/y}} 
    `=>                            {{lambda declaration.}} 

$ Preprocessor Directives
    `#if                           {{When the C# compiler encounters an #if directive, followed eventually by an #endif directive, it will compile the code between the directives only if the specified symbol is defined.}} 
    `#elif                         {{#elif lets you create a compound conditional directive.}} 
    `#endif                        {{#endif specifies the end of a conditional directive, which began with the #if directive.}} 
    `#define                       {{ #define is used to define a symbol.}} 
    `#undef                        {{#undef is used to undefine a symbol}} 
    `#warning                      {{#warning lets you generate a level one warning from a specific location in your code.}} 
    `#error                        {{#error lets you generate an error from a specific location in your code.}} 
    `#line                         {{#line lets you modify the compiler's line number.}} 
    `#pragma                       {{#pragma gives the compiler special instructions for the compilation of the file in which it appears.}} 

$ Compiler Options
    `@                             {{Reads a response file for more options.}} 
    `/?                            {{Displays a usage message to stdout.}} 
    `/addmodule                    {{Links the specified modules into this assembly.}} 
    `/appconfig                    {{Specifies the location of app.config at assembly binding time.}} 
    `/checked                      {{Causes the compiler to generate overflow checks.}} 
    `/codepage                     {{Specifies the codepage to use when opening source files}} 
    `/debug                        {{Emits debugging information.}} 
    `/define                       {{returns the value of x.}} 
    `/errorreport                  {{Specifies how to handle internal compiler errors: prompt, send, or none. The default is none.}} 
    `/keycontainer                 {{Specifies a strong name key container.}} 
    `/lib                          {{Specifies additional directories in which to search for references.}} 
    `/link                         {{Makes COM type information in specified assemblies available to the project.}} 
    `/main                         {{Specifies the type that contains the entry point.}} 
    `/win32res                     {{Specifies the win32 resource file (.res).}} 

