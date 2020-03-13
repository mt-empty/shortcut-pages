# TypeScript

> Source: http://www.typescriptlang.org/Handbook

> Aliases: type-script-lang, typescript-lang, type-script

$ Primitive Types
    `any                           {{Any type (explicitly untyped)}} 
    `void                          {{void type (null or undefined, use for function returns only)}} 
    `string                        {{String}} 
    `number                        {{Number}} 
    `boolean                       {{Boolean}} 

$ Named types
    `interface IChild extends IParent, SomeClass { }
>                                  {{Create interface IChild extending interface IParent and class SomeClass}} 
    `class Child extends Parent implements IChild, IOtherChild { }
>                                  {{Create class Child inheriting Parent class and implementing IChild and IOtherChild interfaces}} 
    `enum Options {FIRST, EXPLICIT=1}
>                                  {{Create an Enum}} 
    `#define name(var) text        {{Define a parameterized macro}} 

$ Object Type Literals
    `{ foo; bar; }                 {{Object with implicit Any properties}} 
    `{ required:Type; optional?:Type; }
>                                  {{Object with optional property}} 
    `{ [key:string]:Type; }        {{Hash map}} 

$ Arrays
    `string[] or Array<string>     {{Array of strings}} 
    `{ ():string; }[] or Array<()=>string>
>                                  {{Array of functions that return strings}} 

$ Functions
    `{ (arg1:Type, argN:Type):Type; } or (arg1:Type, argN:Type) => Type;
>                                  {{Declare a function}} 
    `{ new ():ConstructedType; } or new () => ConstructedType;
>                                  {{Create a new instance of ConstructedType}} 
    `(arg1:Type, optional?:Type) =>; ReturnType
>                                  {{Function type with optional param}} 
    `(arg1:Type, ...allOtherArgs:Type[]) =>; ReturnType
>                                  {{Function type with rest param}} 
    `{ ():Type; staticProp:Type; } {{Function type with static property}} 
    `function fn(arg1:Type = 'default'):ReturnType {}
>                                  {{Default argument}} 
    `(arg1:Type):ReturnType =>; {} or (arg1:Type):ReturnType =>; Expression
>                                  {{Arrow function}} 

$ Generics
    `<T>(items:T[], callback:(item:T) => T):T[]
>                                  {{Function using type parameters}} 
    `interface Pair<T1, T2> { first:T1; second:T2; }
>                                  {{Interface with multiple types}} 
    `<T extends ConstrainedType>():T
>                                  {{Constrained type parameter}} 

$ Other
    `typeof varName                {{Returns type of a variable}} 

