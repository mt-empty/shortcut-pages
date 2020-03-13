# Scala

> Source: http://docs.scala-lang.org/cheatsheets/

$ Program Compilation and Execution
    `scalac Hello.scala            {{Compile Scala File}} 
    `scala Hello                   {{Execute Scala Program}} 
    `scala                         {{Start Scala interactive shell}} 

$ Variables
    `var x = 5                     {{Variable (type inferred)}} 
    `val x = 5                     {{Constant (type inferred)}} 
    `var x: Double = 5             {{Variable (explicit type)}} 

$ Statements
    `if (check) happy else sad     {{If Statement}} 
    `while (x < 5) { println(x); x += 1 }
>                                  {{While Loop}} 
    `do { println(x); x += 1 } while (x < 5)
>                                  {{Do While Loop}} 
    `for (i <- 1 to 5) { println(i) }
>                                  {{For comprehension - basic iteration}} 
    `for (x <- xs; y <- ys) yield x*y
>                                  {{For comprehension - cross product}} 
    `try { fun(); } catch { case e: Exception => println("exception caught"); }
>                                  {{Exception Handling}} 

$ Functions
    `def square(x: Int) = { x * x }
>                                  {{Define Function}} 
    `def f(x: => R)                {{Function with call by name parameters}} 
    `(x:R) => x*x                  {{Anonymous function}} 
    `def zscore(mean:R, sd:R) = (x:R) => (x-mean)/sd
>                                  {{Function currying}} 

$ Data structures
    `(1, 2, 3)                     {{Tuple}} 
    `var (x,y,z) = (1,2,3)         {{Tuple unpacking}} 
    `var xs = List(1,2,3)          {{List (immutable)}} 
    `var xs = Set(1,2,3)           {{Set (immutable)}} 
    `Map(1 -> "one", 2 -> "two")   {{Map (immutable)}} 

$ Packages
    `import scala.collection.Vector
>                                  {{Selective Import}} 
    `import scala.collection._     {{Wildcard Import}} 
    `import scala.collection.{ Vector => Vec28 }
>                                  {{Renaming Import}} 
    `package pkg                   {{Declare Package}} 

