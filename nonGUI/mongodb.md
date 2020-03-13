# MongoDB

> Source: https://blog.codecentric.de/files/2012/12/MongoDB-CheatSheet-v1_0.pdf

> Aliases: mongo-db, mongo-db-shell

$ Basic Concepts & Shell Commands
    `db.collection.<command>       {{Db – implicit handle to the used database, collection – name of the used collection}} 
    `use <database>                {{Switch to another database}} 
    `show collections              {{Lists the available collections}} 
    `help                          {{Prints available commands and help}} 

$ BSON Types
    `Double                        {{1}} 
    `String                        {{2}} 
    `Object                        {{3}} 
    `Array                         {{4}} 
    `Binary Data                   {{5}} 
    `Undefined                     {{6 (Deprecated)}} 
    `Object Id                     {{7}} 
    `Boolean                       {{8}} 
    `Date                          {{9}} 
    `Null                          {{10}} 

$ Inserting Documents
    `db.collection.insert(<document or array of documents>,{keys,options})
>                                  {{Insert a document or documents into collection}} 

$ Finding Documents
    `db.collection.findOne()       {{Find one arbitrary document}} 
    `db.collection.find().prettyPrint()
>                                  {{Find all documents and using nice formatting}} 
    `db.collection.find({}, {key:true, _id:false})
>                                  {{Shows only the respective key of the collection}} 
    `db.collection.findOne({'key':'value'})
>                                  {{Find one document by corresponding attribute}} 

$ Finding Documents using Operators
    `db.collection.find({class:{$gt:’P'}})
>                                  {{Greater than / greater than or equal}} 
    `db.collection.find({class:{$lte:’P'}})
>                                  {{Less than / less than or equal}} 
    `db.collection.find({type:{$exists:true}})
>                                  {{Does an attribute exist or not}} 
    `db.collection.find({name:{$regex:’^USS\sE’}})
>                                  {{Perl-style pattern matching}} 
    `db.collection.find({name:{$type:2}})
>                                  {{Search by type of an element}} 

$ Updating Documents
    `db.ships.update({key1:value1}, {key2:value2})
>                                  {{Replaces the whole document}} 
    `db.collection.update({key:value},{$set : {operator:opt, class:c}})
>                                  {{Sets / changes certain attributes of a given document}} 
    `db.collection.update({key:value},{$unset : {operator : 1}})
>                                  {{Sets / changes certain attributes of a given document}} 
    `db.collection.update({key:value},{$unset : {operator : 1}})
>                                  {{Removes an attribute from a given document}} 

$ Removing Documents
    `db.collection.remove({key:value})
>                                  {{Removes the document}} 
    `db.collection.remove({key:{$regex:’^USS\sE’}})
>                                  {{Removes using operator}} 

$ Working with Indexes
    `db.collection.ensureIndex(keys, options)
>                                  {{Creating an index}} 
    `db.collection.dropIndex(keys, options)
>                                  {{Dropping an index}} 
    `db.collection.ensureIndex(keys, options)
>                                  {{Creating a compound index}} 
    `db.collection.dropIndex({keys, options)
>                                  {{Dropping a compound index}} 
    `db.collection.ensureIndex(keys, options, {unique : true})
>                                  {{Creating a unique compound index}} 

$ Indexes - Hints & Stats
    `db.collection.find ({key:value}).explain()
>                                  {{Explains index usage}} 
    `db.collection.stats()         {{Index statistics}} 
    `db.collection.totalIndexSize()
>                                  {{Index size}} 

$ Top & Stats System Commands
    `./mongotop                    {{Shows time spent per operations per collection}} 
    `./mongostat                   {{Shows snapshot on the MongoDB system}} 

$ Pipeline Stages
    `$project                      {{Reshapes each document in the stream (add or remove) and for each input document, outputs one document}} 
    `$match                        {{Filters the document stream to allow only matching documents to pass and for each input document, outputs either one document (a match) or zero documents (no match)}} 
    `$group                        {{Groups input documents by a specified identifier expression and applies the accumulator expression(s) on all input documents and outputs single document}} 
    `$sort                         {{Reorders the document stream by a specified sort key and for each input document, outputs one document}} 
    `$skip                         {{Skips the first n documents where n is the specified skip number and passes the remaining documents unmodified to the pipeline}} 
    `$limit                        {{Passes the first n documents unmodified to the pipeline where n is the specified limit}} 
    `$unwind                       {{Deconstructs an array field from the input documents to output a document for each element and each input document, outputs n documents where n is the number of array elements and can be zero for an empty array}} 

$ Comparison with SQL
    `$match                        {{WHERE}} 
    `$group                        {{GROUP BY}} 
    `$match                        {{HAVING}} 
    `$project                      {{SELECT}} 
    `$sort                         {{ORDER BY}} 
    `$limit                        {{LIMIT}} 
    `$sum                          {{SUM}} 
    `$sum                          {{COUNT}} 
    `$unwind                       {{JOIN}} 

$ Replica Sets
    `Regular                       {{This is the most typical kind of node and act as a primary or secondary node}} 
    `Arbiter                       {{Arbiter nodes are only there for voting purposes and to ensure that number of nodes, even not that physical servers}} 
    `Delayed                       {{Often used as a disaster recovery node and the data stored here is usually a few hours behind the real working data}} 
    `Hidden                        {{Often used for analytics in the replica set}} 

$ Sharding
    `1                             {{Every document has to define a shard-key}} 
    `2                             {{The value of the shard-key is immutable}} 
    `3                             {{The shard-key must be part of an index and it must be the first field in that index}} 
    `4                             {{There can be no unique index unless the shard-key is part of it and is then the first field}} 
    `5                             {{Reads done without specifying the shard-key will lead to requests to all the different shards}} 
    `6                             {{The shard-key must offer sufficient cardinality to be able to utilize all shards}} 

$ Durability of Writes
    `{ w: <value>, j: <boolean>, wtimeout: <number> }
>                                  {{The w option to request acknowledgment that the write operation has propagated to a specified number of mongod instances. j, write operation written to the journal and wtimeout prevent write from blocking indefinitely}} 
    `w : 1                         {{Requests acknowledgement that the write operation has propagated to the standalone mongod and is the default write concern for MongoDB}} 
    `w : 0                         {{Requests no acknowledgment of the write operation and might return information about socket exceptions and networking errors to the application}} 
    `w : 0 && j : true             {{It prevails to request acknowledgement from the standalone mongod or the primary of a replica set}} 
    `w : "majority"                {{It  implies j: true along, the primary also writes to the on-disk journal before acknowledging the write}} 

