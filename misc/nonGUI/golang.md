# Go Language

> Source: https://github.com/a8m/go-lang-cheat-sheet

> Aliases: go, go-lang, golang-operators, golang-functions, golang-script

$ Variables
    `var varname vartype           {{Declare a variable}} 
    `var varname vartype = value   {{Declare a variable and assign a value}} 
    `varname := value              {{Declare a variable shorthand, only in func bodies, omit var keyword, type is always implicit}} 
    `const constant = value        {{Declare a constant}} 

$ Functions
    `func functionName() {}        {{A simple function}} 
    `func functionName(param1 string, param2 int) {}
>                                  {{Function with parameters (types go after identifiers)}} 
    `func functionName(param1, param2 int) {}
>                                  {{Multiple parameters of the same type}} 
    `func functionName() int { 
 		return 42  
}
>                                  {{Return type declaration}} 
    `func returnMulti() (int, string) { 
		return 42, "foobar" 
} 
 var x, str = returnMulti()
>                                  {{Can return multiple values at once}} 
    `func returnMulti2() (n int, s string) { 
 		n = 42 
 		s = "foobar" 
  		// n and s will be returned 
 		return 
 } 
 var x, str = returnMulti2()
>                                  {{Return multiple named results simply by return}} 

$ Built In Types
    `bool                          {{Bool is the set of boolean values, true and false.}} 
    `string                        {{string is the set of all strings of 8-bit bytes, conventionally but not necessarily representing UTF-8-encoded text. A string may be empty, but not nil. Values of string type are immutable.}} 
    `int                           {{int is a signed integer type that is at least 32 bits in size. It is a distinct type, however, and not an alias for, say, int32.}} 
    `int8                          {{int8 is the set of all signed 8-bit integers. Range: -128 through 127.}} 
    `int16                         {{int16 is the set of all signed 16-bit integers. Range: -32768 through 32767.}} 
    `int32                         {{int32 is the set of all signed 32-bit integers. Range: -2147483648 through 2147483647.}} 
    `int64                         {{int64 is the set of all signed 64-bit integers. Range: -9223372036854775808 through 9223372036854775807.}} 
    `uint                          {{uint is an unsigned integer type that is at least 32 bits in size. It is a distinct type, however, and not an alias for, say, uint32.}} 
    `uint8                         {{uint8 is the set of all unsigned 8-bit integers. Range: 0 through 255.}} 
    `uint16                        {{uint16 is the set of all unsigned 16-bit integers. Range: 0 through 65535.}} 
    `uint32                        {{uint32 is the set of all unsigned 32-bit integers. Range: 0 through 4294967295.}} 
    `uint64                        {{uint64 is the set of all unsigned 64-bit integers. Range: 0 through 18446744073709551615.}} 
    `uintptr                       {{uintptr is an integer type that is large enough to hold the bit pattern of any pointer.}} 
    `byte                          {{byte is an alias for uint8 and is equivalent to uint8 in all ways. It is used, by convention, to distinguish byte values from 8-bit unsigned integer values.}} 
    `rune                          {{rune is an alias for int32 and is equivalent to int32 in all ways. It is used, by convention, to distinguish character values from integer values.}} 
    `float32                       {{float32 is the set of all IEEE-754 32-bit floating-point numbers.}} 
    `float64                       {{float64 is the set of all IEEE-754 64-bit floating-point numbers.}} 
    `complex64                     {{complex64 is the set of all complex numbers with float32 real and imaginary parts.}} 
    `complex128                    {{complex128 is the set of all complex numbers with float64 real and imaginary parts.}} 

$ Control Structures
    `func main() {...}             {{Main}} 
    `if x > 0 {
		 return x
} else {
		 return -x
}
>                                  {{If}} 
    `for i := 1; i < 10; i++ {...} {{For Loop}} 
    `for i < 10  {...}             {{For Loop (single condition)}} 
    `for {...}                     {{For Loop (no condition)}} 
    `switch operatingSystem {
case "darwin":
		fmt.Println("Mac OS Hipster")
case "linux":
		fmt.Println("Linux Geek")
default:
		fmt.Println("Other")
}
>                                  {{Switch}} 
    `switch os := runtime.GOOS; os {
case "darwin": ...
}
>                                  {{Switch (with preceeding assignement)}} 

$ Arrays, Slices, Ranges
    `var a [10]int                 {{Declare an int array with length 10. Array length is part of the type!}} 
    `a[3] = 42                     {{set elements}} 
    `i := a[3]                     {{Read elements}} 
    `var a = [2]int{1, 2}          {{Declare and initialize}} 
    `a := [2]int{1, 2}             {{Shorthand}} 
    `a := [...]int{1, 2}           {{Elipsis -&gt; Compiler figures out array length}} 
    `var a []int                   {{Declare a slice - similar to an array, but length is unspecified}} 
    `var a = []int {1, 2, 3, 4}    {{Declare and initialize a slice (backed by the array given implicitly)}} 
    `a := []int{1, 2, 3, 4}        {{Shorthand}} 
    `chars := []string{0:&quot;a&quot;, 2:&quot;c&quot;, 1: &quot;b&quot;}
>                                  {{ [ "a", "b", "c" ]}} 
    `var b = a[lo:hi]              {{Creates a slice (view of the array) from index lo to hi-1}} 
    `var b = a[1:4]                {{Slice from index 1 to 3}} 
    `var b = a[:3]                 {{Missing low index implies 0}} 
    `var b = a[3:]                 {{Missing high index implies len(a)}} 
    `a = make([]byte, 5, 5)        {{Create a slice with make, first arg length, second capacity}} 
    `a = make([]byte, 5)           {{Create a slice with make, capacity is optional}} 
    `x := [3]string{&quot;applies&quot;,&quot;oranges&quot;,&quot;kiwis&quot;}
>                                  {{Create a slice from an array}} 
    `s := x[:]                     {{A slice referencing the storage of x}} 

$ Maps
    `var m map[string]int
m = make(map[string]int)
m["key"] = 42
fmt.Println(m["key"])

delete(m, "key")
elem, ok := m["key"]
>                                  {{Map syntax}} 
    `var m = map[string]Vertex{
		"Bell Labs": {40.68433, -74.39967},
		"Google": {37.42202, -122.08408},
}
>                                  {{Map literal}} 

$ Structs
    `type Vertex struct {
		X, Y int
}
>                                  {{Struct declaration}} 
    `var v = Vertex{1, 2}          {{Creating}} 
    `var v = Vertex{X: 1, Y: 2}    {{Creates a struct by defining values with keys}} 
    `v.X = 4                       {{Accessing members}} 
    `func (v Vertex) Abs() float64 {
		return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
>                                  {{You can declare methods on structs. The struct you want to declare the method on (the receiving type) comes between the func keyword and the method name. The struct is copied on each method call.}} 
    `v.Abs()                       {{Call method}} 
    `func (v *Vertex) add(n float64) {
		v.X += n
		v.Y += n
}
>                                  {{For mutating methods, you need to use a pointer (see below) to the Struct as the type. With this, the struct value is not copied for the method call.}} 
    `point := struct {
		X, Y int
}{1, 2}
>                                  {{Anonymous structs}} 

$ Pointers
    `p := Vertex{1, 2}             {{p is a Vertex}} 
    `q := &p                       {{q is a pointer to a Vertex}} 
    `r := &Vertex{1, 2}            {{r is a pointer to a Vertex}} 
    `var s *Vertex = new(Vertex)   {{new creates a pointer to a new struct instance}} 

$ Interfaces
    `type Awesomizer interface {
		Awesomize() string
}
>                                  {{Interface declaration}} 
    `type Foo struct {}            {{Types do *not* declare to implement interfaces}} 
    `func (foo Foo) Awesomize() string {
		return "Awesome!"
}
>                                  {{Rather, types implicitly satisfy an interface if they implement all required methods}} 

$ Operators and aliases
    `+                             {{Addition}} 
    `-                             {{Subtraction}} 
    `*                             {{Multiplication}} 
    `/                             {{Quotient}} 
    `%                             {{Remainder}} 
    `&amp;                         {{Bitwise and}} 
    `|                             {{Bitwise or}} 
    `^                             {{Bitwise xor}} 
    `&amp;^                        {{Bit clear (and not)}} 
    `&lt;&lt;                      {{Left shift}} 
    `&gt;&gt;                      {{Right shift}} 
    `==                            {{Equal}} 
    `!=                            {{Not equal}} 
    `&lt;                          {{Less than}} 
    `&lt;=                         {{Less than or equal}} 
    `&gt;                          {{Greater than}} 
    `&gt;=                         {{Greater than or equal}} 
    `&amp;&amp;                    {{Logical and}} 
    `||                            {{Logical or}} 
    `!                             {{Logical not}} 
    `&amp;                         {{Address of / create pointer}} 
    `*                             {{Dereference pointer}} 
    `&lt;-                         {{Send / receive operator}} 

