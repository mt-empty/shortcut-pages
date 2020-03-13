# VB.NET

> Aliases: visual-basic, visual-basic-net, visual-basic-.net, vb.net, vbnet, visual-basic-dot-net, vb

$ General Structure
    `Option Explicit               {{Enforces strong typing}} 
    `Option Strict                 {{Restricts implicit data type conversions to only widening conversions}} 
    `Imports System.IO             {{Import another namespace}} 
    `Public Class Name
	'methods
End Class
>                                  {{Classes contain methods and events}} 
    `Public Sub ShowMessage(ByVal message As String)
	MsgBox(message)
End Sub
>                                  {{A subroutine is a block of code that does not return a value back}} 
    `Public Function Add(ByVal num1 As Integer, ByVal num2 As Integer) As Integer
	Return num1 + num2
End Function
>                                  {{A function is a block of code that does returns a value back}} 
    `Dim message As String         {{Declare a variable named "message" of type "String"}} 
    `Dim NumArray() As Integer = New Integer(3) {1, 2, 3}
>                                  {{Declare an Integer array named "NumArray" that's holding 3 values: 1, 2, and 3}} 
    `message = "Hello " & vbCrLf & "world!"
>                                  {{String concatenation, where "vbCrLf" inserts a new line}} 
    `'this is a comment            {{Single-line comment. Multi-line comments require a single quote on each line}} 

$ Common Functions and Keywords
    `Console.WriteLine("Hi DuckDuckGo!")
>                                  {{Write to the output window}} 
    `MsgBox("Hi DuckDuckGo!")      {{Open an alert box}} 
    `My.                           {{The My namespace offers easier access to some functions such as file I/O and form control}} 
    `Me                            {{Refers to the current instance of a class or structure}} 

$ Control Structures
    `If expression1 Then
	'do thing A
End If
>                                  {{Do thing A if expression1 is True}} 
    `ElseIf expression2 Then
	'do thing B
>                                  {{Do thing B if expression2 is True}} 
    `Else
	'do thing C             {{Do thing C if all other conditions are false}} 
    `For index = 1 To 10 Step 2
	'expressions
Next
>                                  {{Create Integer index, set index to 1, and loop through until index is 10, incrementing by 2 each time}} 
    `For Each x In y
	'expressions
Next
>                                  {{Loop through collection y, setting x to the current item of each iteration}} 
    `While expression
	'expressions
End While
>                                  {{Loop the code block while the expression is true}} 
    `Try
	'expressions
Catch ex As Exception
	Console.WriteLine(ex.Message)
End Try
>                                  {{Catch possible errors}} 
    `Continue [ Do | For | While ] {{Skip the rest of the current iteration and go to the next iteration of the specified loop}} 
    `Exit [ Do | For | Function | Property | Select | Sub | Try | While ]
>                                  {{Skip the rest of the specified code block}} 

$ Comparison Operators
    `=                             {{Either the assignment operator or the conditional operator depending on context}} 
    `<                             {{Less than}} 
    `>                             {{Greater than}} 
    `<=                            {{Less than or equal to}} 
    `>=                            {{Greater than or equal to}} 
    `<>                            {{Not equal to}} 

$ Boolean Operators
    `And                           {{Boolean AND}} 
    `AndAlso                       {{Boolean AND, but the second condition is not evaluated if the first is false}} 
    `Or                            {{Boolean OR}} 
    `OrElse                        {{Boolean OR, but the second condition is not evaluated if the first is true}} 
    `Xor                           {{Boolean exclusive OR}} 
    `Not                           {{Boolean NOT}} 
    `If(condition, is_True, is_False)
>                                  {{Conditional operator or inline if}} 
    `If(nullable_type, is_Nothing) {{Null-coalescing operator}} 

$ Arithmetic Operators
    `a + b                         {{Adds a and b}} 
    `a - b                         {{Subtracts b from a}} 
    `a * b                         {{Multiplies a and b}} 
    `a / b                         {{Divides a by b and returns the full decimal quotient}} 
    `a \ b                         {{Divides a by b and returns the integer quotient}} 
    `a Mod b                       {{Divides a by b and returns remainder}} 
    `a ^ b                         {{Returns a raised to the power of b}} 

$ Basic Data Types
    `Boolean                       {{2 bytes - True or False}} 
    `Byte                          {{1 byte - 0 to 255 (unsigned)}} 
    `Char                          {{2 bytes - 0 to 65,535 (unsigned)}} 
    `Date                          {{8 bytes - Jan 1, 0001 to Dec 31, 9999}} 
    `Decimal                       {{16 bytes - approx +/-7.9228 x 10^28}} 
    `Double                        {{8 bytes - double-precision floating-point}} 
    `Integer                       {{4 bytes - +/-2,147,483,647}} 
    `Long                          {{8 bytes - +/- 9.2 x 10^18}} 
    `Object                        {{4 bytes - any type of variable}} 
    `SByte                         {{1 byte - -128 to 127}} 
    `Short                         {{2 bytes - +/-32,767}} 
    `Single                        {{4 bytes - single-precision floating-point}} 
    `String                        {{2 byte sequence - 0 to approx 2 billion Unicode characters}} 
    `Structure (user-defined type) {{sum of the sizes of its members - holds data in a cumtom defined format}} 
    `UInteger                      {{4 bytes - 0 to 4,294,967,295}} 
    `ULong                         {{8 byte - 0 to 1.84 x 10^19}} 
    `UShort                        {{2 bytes - 0 to 65,535}} 

