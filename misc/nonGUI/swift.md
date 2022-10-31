# Swift

> Source: http://kpbp.github.io/swiftcheatsheet/

> Aliases: apple-swift, swift-language

$ Basics
    `var myInt                     {{Declare a new variable}} 
    `let myInt = 1                 {{Declare a new constant}} 
    `var myString                  {{Declare a new string}} 
    `var colors = ["red", "blue"]  {{Declares a new string array}} 

$ Logical Operators
    `&&                            {{AND}} 
    `||                            {{OR}} 
    `!=                            {{Not equals}} 
    `==                            {{Equals}} 

$ Arithmetic Operators
    `+                             {{Addition}} 
    `-                             {{Subtraction}} 
    `*                             {{Multiplication}} 
    `/                             {{Division}} 
    `%                             {{Modulus}} 
    `+=1                           {{Increment by 1}} 
    `-=1                           {{Decrement by 1}} 

$ Comparison Operators
    `==                            {{Equal to}} 
    `!=                            {{Not equal to}} 
    `>                             {{Greater than}} 
    `<                             {{Less than}} 
    `>=                            {{Greater than or equal to}} 
    `<=                            {{Less than or equal to}} 

$ Printing
    `print("Hi")                   {{Prints Hi}} 

$ Dictionaries
    `var days = ["mon": "monday", "tue": "tuesday"]
>                                  {{Declare a new dictionary}} 
    `days["tue"] = "tuesday"       {{Change the value for key "tue"}} 
    `days.removeValueForKey("mon") {{Remove "mon" from the dictionary}} 
    `days["tue"] = nil             {{Remove "tue" from the dictionary}} 

$ Arrays
    `var someInts = [Int]()        {{Creating an Empty Array}} 
    `var threeDoubles = [Double](count: 3, repeatedValue: 0.0)
>                                  {{Creating an Array with a Default Value}} 
    `var shoppingList: [String] = ["Eggs", "Milk"]
>                                  {{Creating an Array with an Array Literal}} 
    `for item in shoppingList {
	print(item)
}
>                                  {{Iterating Over an Array}} 

$ Conditionals
    `if condition {
	// statements
}
>                                  {{If statement}} 
    `if condition {
	// statements
} else {
	// statements
}
>                                  {{If...Else statement}} 
    `switch control expression {
	case pattern 1:
		// statements
	case pattern 2:
		// statements
	default:
		// statements
}
>                                  {{Switch}} 

$ Loops
    `for item in list {
	//statements
}
>                                  {{For loop}} 
    `while count < n {
	//statements
}
>                                  {{While Loop}} 

$ Functions
    `func sayHello(personName: String) -> String {
	//statements
}
>                                  {{Function definition}} 

$ Classes
    `class SomeClass {
	// class definition
}
>                                  {{Define a new class}} 

$ Methods
    `func doIt() -> Int {
	return 0
}

func doIt(a:Int) -> Int {
	return a
}

func doIt(a:Int, b:Int) -> Int {
	return a+b
}
>                                  {{Define a method}} 

$ Instances
    `var a = MyClass()
a.myProperty
>                                  {{Creating/Using an Instance}} 

$ Enums
    `enum CollisionType: Int {
	case Player = 1
	case Enemy = 2
}
var type = CollisionType.Player
>                                  {{Define a new Enum}} 

