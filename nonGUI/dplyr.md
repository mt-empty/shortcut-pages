# Dplyr

> Source: https://www.rstudio.com/wp-content/uploads/2015/02/data-wrangling-cheatsheet.pdf

> Aliases: dplyr-syntax, data-wrangling-in-r, data-cleaning-in-r, data-munging-in-r

$ Basics
    `dplyr::tbl_df(iris)           {{Converts data to tbl class. tbl's are easier to examine than data frames}} 
    `dplyr::glimpse(iris)          {{Information dense summary of tbl data}} 
    `dplyr::%>%                    {{Passes object on left as 1st argument of function on right. x %>% f(y) is the same as f(x, y)}} 

$ Reshaping Data
    `dplyr::data_frame(a = 1:3, b = 4:6)
>                                  {{Combine vectors into data frame (optimized)}} 
    `dplyr::arrange(dataframe, variableName)
>                                  {{Order rows in dataframe by values of variableName (low to high)}} 
    `dplyr::arrange(dataframe, desc(variableName))
>                                  {{Order rows in dataframe by values of variableName (high to low)}} 
    `dplyr::rename(dataframe, newname1 = oldname1, newname2 = oldname2)
>                                  {{Rename the columns of a dataframe}} 

$ Subset Observations (Row)
    `dplyr::filter(iris, Sepal.Length > 7)
>                                  {{Extract rows that meet logical criteria}} 
    `dplyr::distinct(iris)         {{Remove duplicate rows}} 
    `dplyr::sample_frac(iris, 0.5, replace = TRUE)
>                                  {{Randomly select fraction of rows}} 
    `dplyr::sample_n(iris, 10, replace = TRUE)
>                                  {{Randomly select n rows}} 
    `dplyr::slice(iris, 10:15)     {{Select rows by position}} 
    `dplyr::top_n(iris, 2, Sepal.Length)
>                                  {{Select and order top n entries (by group if grouped data)}} 

$ Subset Variables (Columns)
    `dplyr::select(iris, Sepal.Width, Petal.Length, Species)
>                                  {{Select columns by name}} 
    `dplyr::select(iris, contains('.'))
>                                  {{Select columns whose name contains a character string}} 
    `dplyr::select(iris, starts_with('Sepal'))
>                                  {{Select columns whose name starts with a character string}} 
    `dplyr::select(iris, ends_with('Length'))
>                                  {{Select columns whose name ends with a character string}} 
    `dplyr::select(iris, num_range('x', 1:5))
>                                  {{Select columns named x1, x2, x3, x4, x5}} 
    `dplyr::select(iris, one_of(c('Species', 'Genus')))
>                                  {{Select columns whose names are in a group of names}} 
    `dplyr::select(iris, -Species) {{Select all columns except Species}} 

$ Summarize Data
    `dplyr::summarise(iris, avg = mean(Sepal.Length))
>                                  {{Summarise data into single row of values}} 
    `dplyr::summarise_each(select(iris,-Species), funs('mean','min','max'))
>                                  {{Apply summary function (funs) to each column}} 
    `dplyr::count(iris, Species, wt = Sepal.Length)
>                                  {{Count number of rows with each unique value of variable (with or without weights)}} 

$ Make New Variables
    `dplyr::mutate(iris, sepal = Sepal.Length + Sepal.Width)
>                                  {{Compute and append one or more new columns}} 
    `dplyr::mutate_each(select(iris,-Species), funs(. * 0.5))
>                                  {{Apply window function (funs) to each column}} 
    `dplyr::transmute(iris, sepal = Sepal.Length + Sepal.Width)
>                                  {{Compute one or more new columns. Drop original columns}} 

$ Combine Data Sets
    `dplyr::left_join(a, b, by = 'x1')
>                                  {{Join matching rows from b to a}} 
    `dplyr::right_join(a, b, by = 'x1')
>                                  {{Join matching rows from a to b}} 
    `dplyr::inner_join(a, b, by = 'x1')
>                                  {{Join data. Retain only rows in both sets}} 
    `dplyr::full_join(a, b, by = 'x1')
>                                  {{Join data. Retain all values, all rows}} 
    `dplyr::semi_join(a, b, by = 'x1')
>                                  {{All rows in a that have a match in b}} 
    `dplyr::anti_join(a, b, by = 'x1')
>                                  {{All rows in a that do not have a match in b}} 
    `dplyr::intersect(y, z)        {{Rows that appear in both y and z}} 
    `dplyr::union(y, z)            {{Rows that appear in either or both y and z}} 
    `dplyr::setdiff(y, z)          {{Rows that appear in y but not z}} 
    `dplyr::bind_rows(y, z)        {{Append z to y as new rows}} 
    `dplyr::bind_cols(y, z)        {{Append z to y as new columns. Caution: matches rows by position}} 

$ Group Data
    `dplyr::group_by(iris, Species)
>                                  {{Group data into rows with the same value of Species}} 
    `dplyr::ungroup(iris)          {{Remove grouping information from data frame}} 

