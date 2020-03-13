# Java

> Source: http://www.cheatography.com/sschaub/cheat-sheets/java-fundamentals/

$ Program Compilation and Execution
    `javac Hello.java              {{Compile Java File}} 
    `java Hello                    {{Execute Java Program}} 

$ Data Types
    `byte/short/int/long           {{Integer Datatype}} 
    `float/double                  {{Floating Point Datatype}} 
    `char                          {{A Single Character}} 
    `boolean                       {{Represents True,False}} 
    `String                        {{Java object To Represent A Sequence Of Characters}} 

$ Statements
    `if(expression)&nbsp;{
	statements
}&nbsp;else&nbsp;{
	statements
}
>                                  {{If Statement}} 
    `while(expression)&nbsp;{
	statements
}
>                                  {{While Loop}} 
    `do&nbsp;{
	statements
}&nbsp;while(expression)
>                                  {{Do While Loop}} 
    `for(Initialization;&nbsp;Condition;&nbsp;Update)&nbsp;{
	statements
}
>                                  {{For Loop}} 
    `for(var&nbsp;:&nbsp;collection)&nbsp;{
	statements
}
>                                  {{For Each Loop ( Also known as Advanced or Enhanced For Loop )}} 
    `try&nbsp;{
	statements
}&nbsp;catch(ExceptionType&nbsp;e1){
	statements
}&nbsp;catch(Exception&nbsp;e2)&nbsp;{
	catch-all&nbsp;statements
}&nbsp;finally&nbsp;{
	statements&nbsp;}
>                                  {{Exception Handling}} 

$ Data Conversions
    `int&nbsp;i&nbsp;=&nbsp;Integer.parseInt(str);

double&nbsp;d&nbsp;=&nbsp;Double.parseDouble(str);
>                                  {{String to Number}} 
    `String&nbsps&nbsp=&nbspString.valueOf(value);
>                                  {{Any Type to String}} 
    `int&nbspi&nbsp=&nbsp(int)&nbspnumeric&nbspexpression;
>                                  {{Numeric Conversions}} 

$ Text Formatting
    `System.out.printf("Count&nbsp;is&nbsp;%d",&nbsp;count);

s&nbsp;=&nbsp;String.format("Count&nbsp;is&nbsp;%d",&nbsp;count);
>                                  {{printf style formatting}} 
    `MessageFormat.format("0&nbsp;rows.",&nbsp;5);
>                                  {{MessageFormat style formatting}} 
    `NumberFormat.getCurrencyInstance().format(x);

SimpleDateFormat(""h:mm&nbsp;a"").format(new&nbsp;Date());

DecimalFormat("#,##0.00").format(125.32);
>                                  {{Individual Numbers and Dates}} 

$ String Methods
    `s.length()                    {{Length Of S}} 
    `s.charAt(i)                   {{Extract ith Character}} 
    `s.substring(start, end)       {{Substring From Start To End}} 
    `s.toUpperCase()/lowerCase()   {{Returns Copy Of s In Caps/Lower Case}} 
    `s.indexOf(x)                  {{Index Of First Occurence Of x}} 
    `s.replace(old, new)           {{Search And Replace}} 
    `s.split(regex)                {{Splits Into Tokens}} 
    `s.trim()                      {{Trims Surrounding White Space}} 
    `s.equals(s2)                  {{True If s Equals s2}} 
    `s.compareTo(s2)               {{0 if Equal or +ve If s > s2 or -ve If s < s2}} 

$ ArrayList Methods
    `l.add(item)                   {{Add Item To List}} 
    `l.get(i)                      {{Return ith Item}} 
    `l.size()                      {{Returns The Number Of Items}} 
    `l.remove(i)                   {{Remove ith Item}} 
    `l.set(i, value)               {{Put value At Position i}} 

$ HashMap Methods
    `m.put(key,value)              {{Inserts Value With Key}} 
    `m.get(key)                    {{Retrieves Value With Key}} 
    `m.containsKey(key)            {{True If m Contains Key}} 

