# R Language

> Source: https://cran.r-project.org/doc/contrib/Short-refcard.pdf

> Aliases: r-language

$ Getting Help
    `help(topic)                   {{documentation on topic}} 
    `help.start()                  {{start the HTML version of help}} 
    `str(a)                        {{display the internal structure of an R object}} 

$ Basic Syntax
    `#                             {{comment}} 
    `<- or =                       {{assignment}} 
    `<<-                           {{deep assignment}} 
    `*                             {{scalar multiplication}} 
    `%*%                           {{matrix multiplication}} 
    `/                             {{division}} 
    `%/%                           {{integer division}} 
    `%%                            {{modulus}} 

$ Input and Output
    `load()                        {{load datasets written with save}} 
    `data(x)                       {{loads specified data sets}} 
    `library(x)                    {{load add-on package x, see https://cran.r-project.org}} 
    `read.table("filename", sep=",")
>                                  {{reads information in from file with a variable delimiter}} 
    `read.csv("filename",header=TRUE)
>                                  {{read csv file into dataframe}} 
    `write.csv("filename")         {{writes a dataframe or matrix (or tries to convert input to one) and saves to csv}} 

$ Data Creation
    `c(...)                        {{concatenate, e.g. v <- c(1, 2, 3, 4)}} 
    `rbind(...)                    {{row concatenate}} 
    `cbind(...)                    {{column concatenate}} 
    `list(...)                     {{R’s implementation of a hash, takes multiple variables or variable tag pairs; e.g. list(a=c(1, 2), b="hi", c=3i)}} 
    `data.frame(...)               {{Takes multiple variables with the same number of rows and creates a dataframe}} 
    `matrix(...)                   {{create matrix; e.g. mat <- matrix(v, nrow=2, ncol=2)}} 

$ Data Selection and Manipulation
    `v[1]                          {{select first}} 
    `tail(v, 1)                    {{select last}} 
    `mat[1,]                       {{select row 1}} 
    `mat[,2])                      {{select column 2}} 
    `v[c(1, 3)]                    {{select the first and third values}} 
    `v[-c(1, 3)]                   {{select all but the first and third values}} 
    `mat[, c(1, 2)]                {{select columns 1 and 2}} 
    `mat[, 1:5]                    {{select columns 1 to 5}} 
    `mat[, "col"]                  {{select column named "col"}} 
    `sort(x)                       {{sorts the elements of x in increasing order}} 
    `unique(x)                     {{returns object vector or data frame with duplicate elements suppressed}} 
    `length(x)                     {{length of vector}} 
    `dim(x)                        {{dimensions of vector/matrix/data frame}} 
    `names(x)                      {{names of columns}} 

$ Math
    `sum(x)                        {{sum of the elements of x}} 
    `max(x)                        {{maximum of the elements of x}} 
    `min(x)                        {{minimum of the elements of x}} 
    `prod(x)                       {{product}} 
    `mean(x)                       {{mean}} 
    `median(x)                     {{median}} 
    `sd(x)                         {{standard deviation}} 
    `round(x, n)                   {{rounds the elements of x to n decimals}} 

$ Strings
    `tolower(x)                    {{convert to lowercase}} 
    `toupper(x)                    {{convert to uppercase}} 
    `strsplit(x, split)            {{split x by the substring "split"}} 
    `grep(pattern, x)              {{searches for matches to pattern within x}} 
    `gsub(pattern, replacement, x) {{replaces all match occurences determined by regular expression}} 

$ Date and Time
    `date()                        {{returns the current date and time}} 
    `format(today, format="%B %d %Y")
>                                  {{returns formatted date}} 
    `%d                            {{day as a number (0-31)}} 
    `%A                            {{unabbreviated weekday}} 
    `%m                            {{month (00-12)}} 
    `%B                            {{unabbreviated month}} 
    `%Y                            {{4-digit year}} 
    `%d                            {{day as a number (0-31)}} 

$ Plotting
    `plot(x)                       {{plot of the values of x (on the y-axis) ordered on the x-axis}} 
    `title(main, sub, xlab, ylab)  {{label the currently open plot}} 
    `hist(x)                       {{histogram of the frequencies of x}} 
    `barplot(x)                    {{histogram of the values of x; use horiz=FALSE for horizontal bars}} 
    `boxplot(x)                    {{"box-and-whiskers" plot}} 

