# Rails Console

> Source: http://railsforzombies.org

> Aliases: ruby-on-rails-console

$ Start
    `rails console                 {{Start rails console}} 

$ Create
    `TableName.create(key1: value1)
>                                  {{Creates a new record with key1 equals to value1}} 

$ Read
    `TableName.find(3)             {{Returns the record with id 3}} 
    `TableName.find(3,4,5)         {{Returns an array of records with id's 3, 4 and 5}} 
    `TableName.first               {{Returns the first record in the table}} 
    `TableName.last                {{Returns the last record in the table}} 
    `TableName.all                 {{Returns all the records in the table}} 
    `TableName.count               {{Returns the total number of records in the table}} 
    `TableName.order(:key)         {{Returns all records, Ordered by key}} 
    `TableName.limit(10)           {{Returns the first 10 records}} 
    `TableName.where(key: value)   {{Returns all records where a key is equal to a certain value}} 

$ Method Chaining
    `TableName.where(key1: value1).order(:key2).limit(5)
>                                  {{Returns all records where key1 is equal to value1, Ordered by key2 and only the first 5 records}} 

$ Deletion
    `TableName.find(2).destroy     {{Deletes the record with id 2}} 
    `TableName.destroy_all         {{Deletes all records in the table}} 

