# Pandas

> Source: http://www.analyticsvidhya.com/blog/2015/07/11-steps-perform-data-analysis-pandas-python/

> Aliases: python-pandas

$ Reading and Writing Methods
    `df=pd.read_csv('Anyname.csv') {{Reading a CSV file}} 
    `df.to_csv(Newfile.csv)        {{Writing content of dataframe to CSV file}} 
    `df=pd.read_excel('File_Name.xlsx','sheet1')
>                                  {{Reading an Excel file}} 
    `df.to_excel('Abc.xlsx',sheet_name='sheet2')
>                                  {{Writing content of dataframe to Excel file}} 

$ Getting Preview of Dataframe
    `df.head(n)                    {{Looking at top n records}} 
    `df.tail(n)                    {{Looking at bottom n records}} 
    `df.columns                    {{View columns name}} 

$ Rename Columns of Dataframe
    `df2=df.rename(columns='old_columnname':'new_columnname')
>                                  {{Create a new dataframe}} 
    `df.rename(columns='old_columnname':'new_columnname',inplace=True
>                                  {{To rename the column of existing dataframe}} 

$ Selecting Columns and Rows
    `df'column1','column2'         {{Accessing sub dataframes}} 
    `dfdf'column1'>10              {{Filtering Records}} 
    `df[(df['column1']>10) & df['column2']==50]
>                                  {{Filtering Records using &(and)}} 
    `df[(df['column1']>10) | df['column2']==50]
>                                  {{Filtering Records using |(or)}} 

$ Handling Missing Values
    `df1.dropna()                  {{Drop rows and columns having missing data}} 
    `df2.filna(value=5)            {{Replace all missing values with 5}} 
    `mean=df2'column1'.mean()      {{Find mean value of column}} 
    `df2'column1'.filna(mean)      {{Replace all the missing values of column1 with mean of available values}} 

$ Creating New Columns
    `df'NewColumn1'=df'column2'    {{Create a copy of existing column2}} 
    `df'NewColumn2'=df'column2'+10 {{Add 10 to existing column2 then create new column}} 
    `df'NewColumn3'=df'column1'+df'column2'
>                                  {{Add elements of column1 and column2 then create new column}} 

$ Aggregate
    `df.groupby('column1').sum() df.groupby(['column1','column2']).count()
>                                  {{Spliting the data into groups and apply fucntions to each groups indivdually}} 
    `pd.pivot_table(df,values='column1',index='column2','column3',columns='column4')
>                                  {{Pivot table helps to genrate data structure. it has three components index, columns and values}} 
    `pd.pivot_table(df,values='column1',index='column2','column3',columns='column4',aggfunc=len
>                                  {{To find count in column in Pivot table}} 
    `pd.crosstab(df.column1,df.column2)
>                                  {{Crosstab computes the simple cross tabulation of two factors}} 

$ Merging/Concatinating Dataframes
    `pd.concat(df1,df2)            {{Concatinate two or more dataframes based on columns}} 
    `pd.merge(df1,df2,on='column1',how='inner') pd.merge(df1,df2,on='column1',how='left') pd.merge(df1,df2,on='column1',how='right')
>                                  {{We can perform right, left and inner joins also}} 

$ Applying Functions to Dataframes
    `df['column1'].map(lambda x:10+x)
>                                  {{Map: This will add 10 to each element of column1}} 
    `df['column1'].map(lambda x:'hello'+x)
>                                  {{Concatinate 'hello' at the beginning of each elements}} 
    `df'column1','column2'.apply(sum)
>                                  {{Apply: Applies a fucntion along any axis of the dataframe}} 

$ Identify Unique Values
    `df'column1'.unique()          {{Returns unique values of a column}} 

$ Basic Statical Methods
    `df.describe()                 {{Returns a quick stats(count, mean, std, min, first quartile) on suitable columns}} 
    `df.cov()                      {{Returns co-variance between suitable columns}} 
    `df.corr()                     {{Returns co-relation between suitable columns}} 

