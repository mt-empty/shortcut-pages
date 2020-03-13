# Kotlin

> Source: https://kotlinlang.org/docs/reference/

$ Basic syntax
    `fun main(args: Array<String>) { }
>                                  {{Program entry point}} 
    `fun meaningOfLife() = 42      {{Define a function}} 
    `println("Hello World")        {{Call a function}} 
    `myList.joinToString(separator = ", ")
>                                  {{Call a function with named parameters}} 
    `{ x: Int, y: Int -> x + y }   {{Define a lambda function}} 
    `"Hello ${name}"               {{Interpolate strings}} 
    `department?.building?.address {{Null-safe property access}} 
    `val (name, int) = myPerson    {{Destructuring classes or collections}} 

$ Variables
    `val weather = "sunny"         {{Define a final, non-null variable}} 
    `var weather = "sunny"         {{Define a non-null variable}} 
    `var weather : String = "sunny"
>                                  {{Define a variable with an explicit non-null type}} 
    `var weather : String? = null  {{Define a nullable variable}} 

$ Defining collections
    `arrayOf(1, 2, …)              {{Create an array}} 
    `listOf(1, 2, …)               {{Create an immutable list}} 
    `mapOf("id" to "k", "name" to "Kotlin", …)
>                                  {{Create an immutable map}} 
    `setOf(1, 2, …)                {{Create an immutable set}} 

$ Working with collections
    `myList5                       {{Get an element from a collection}} 
    `myList.forEach { println(it) }
>                                  {{Call a method on all entries of a collection}} 
    `val doubled = myList.map { it * 2 }
>                                  {{Map all entries of a collection}} 
    `val sorted = names.sortedBy { it.length }
>                                  {{Sort a collection}} 
    `a + b                         {{Create a union of two collections a and b}} 
    `a - b                         {{Create a collection of all items of a that do not occur in b}} 

$ Control structures
    `if (a < b) a else b           {{Conditional}} 
    `possiblyNull ?: "default"     {{Elvis operator for working with nullable variables}} 
    `while (a < b) { }             {{While loop}} 
    `for (i in 1..10) { println(i) }
>                                  {{Iterate from 1 to 10 (inclusive)}} 
    `for(i in 10 downTo 1) { println(i) }
>                                  {{Iterate from 10 to 1 (inclusive)}} 

$ Defining classes
    `class Person { … }            {{Define a class}} 
    `class Person(name: String) { … }
>                                  {{Define a class with a constructor}} 
    `class Person(val name: String) { … }
>                                  {{Set a property in the constructor}} 
    `class MyList : ArrayList() { … }
>                                  {{Inherit from another class or interface}} 
    `enum class Direction { UP, DOWN }
>                                  {{Define an enum}} 
    `data class Person(val name: String, val age: Int)
>                                  {{Define a data class, with automatic equals(), hashCode(), and toString()}} 

