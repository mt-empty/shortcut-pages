# Redis Commands

> Source: http://redis.io/commands

$ Hashes
    `HDEL key field field ...      {{Delete one or more hash fields}} 
    `HEXISTS key field             {{Determine if a hash field exists}} 
    `HGET key field                {{Get the value of a hash field}} 
    `HGETALL key                   {{Get all the fields and values in a hash}} 
    `HINCRBY key field increment   {{Increment the integer value of a hash field by the given number}} 
    `HINCRBYFLOAT key field increment
>                                  {{Increment the float value of a hash field by the given amount}} 
    `HKEYS key                     {{Get all the fields in a hash}} 
    `HLEN key                      {{Get the number of fields in a hash}} 
    `HMGET key field field ...     {{Get the values of all the given hash fields}} 
    `HMSET key field value field value ...
>                                  {{Set multiple hash fields to multiple values}} 
    `HSET key field value          {{Set the string value of a hash field}} 
    `HSETNX key field value        {{Set the value of a hash field, only if the field does not exist}} 
    `HSTRLEN key field             {{Get the length of the value of a hash field}} 
    `HVALS key                     {{Get all the values in a hash}} 
    `HSCAN key cursor MATCH pattern COUNT count
>                                  {{Incrementally iterate hash fields and associated values}} 

$ Sets
    `SET key value EX seconds PX milliseconds NX|XX
>                                  {{Set the string value of a key}} 
    `SETBIT key offset value       {{Sets or clears the bit at offset in the string value stored at key}} 
    `SETEX key seconds value       {{Set the value and expiration of a key}} 
    `SETNX key value               {{Set the value of a key, only if the key does not exist}} 
    `SETRANGE key offset value     {{Overwrite part of a string at key starting at the specified offset}} 
    `SADD key member member ...    {{Add one or more members to a set}} 
    `SCARD key                     {{Get the number of members in a set}} 
    `SDIFF key key ...             {{Subtract multiple sets}} 
    `SDIFFSTORE destination key key ...
>                                  {{Subtract multiple sets and store the resulting set in a key}} 
    `SINTER key key ...            {{Intersect multiple sets}} 
    `SINTERSTORE destination key key ...
>                                  {{Intersect multiple sets and store the resulting set in a key}} 
    `SISMEMBER key member          {{Determine if a given value is a member of a set}} 
    `SMEMBERS key                  {{Get all the members in a set}} 
    `SMOVE source destination member
>                                  {{Move a member from one set to another}} 
    `SPOP key count                {{Remove and return one or multiple random members from a set}} 
    `SRANDMEMBER key count         {{Get one or multiple random members from a set}} 
    `SREM key member member ...    {{Remove one or more members from a set}} 
    `SUNION key key ...            {{Add multiple sets}} 
    `SUNIONSTORE destination key key ...
>                                  {{Add multiple sets and store the resulting set in a key}} 
    `SSCAN key cursor MATCH pattern COUNT count
>                                  {{Incrementally iterate Set elements}} 

$ Sorted Sets
    `ZADD key NX|XX CH INCR score member score member ...
>                                  {{Add one or more members to a sorted set, or update its score if it already exists}} 
    `ZCARD key                     {{Get the number of members in a sorted set}} 
    `ZCOUNT key min max            {{Count the members in a sorted set with scores within the given values}} 
    `ZINCRBY key increment member  {{Increment the score of a member in a sorted set}} 
    `ZINTERSTORE destination numkeys key key ... WEIGHTS weight weight ... AGGREGATE SUM|MIN|MAX
>                                  {{Intersect multiple sorted sets and store the resulting sorted set in a new key}} 
    `ZLEXCOUNT key min max         {{Count the number of members in a sorted set between a given lexicographical range}} 
    `ZRANGE key start stop WITHSCORES
>                                  {{Return a range of members in a sorted set, by index}} 
    `ZRANGEBYLEX key min max LIMIT offset count
>                                  {{Return a range of members in a sorted set, by lexicographical range}} 
    `ZREVRANGEBYLEX key max min LIMIT offset count
>                                  {{Return a range of members in a sorted set, by lexicographical range, ordered from higher to lower strings.}} 
    `ZRANGEBYSCORE key min max WITHSCORES LIMIT offset count
>                                  {{Return a range of members in a sorted set, by score}} 
    `ZRANK key member              {{Determine the index of a member in a sorted set}} 
    `ZREM key member member ...    {{Remove one or more members from a sorted set}} 
    `ZREMRANGEBYLEX key min max    {{Remove all members in a sorted set between the given lexicographical range}} 
    `ZREMRANGEBYRANK key start stop
>                                  {{Remove all members in a sorted set within the given indexes}} 
    `ZREMRANGEBYSCORE key min max  {{Remove all members in a sorted set within the given scores}} 
    `ZREVRANGE key start stop WITHSCORES
>                                  {{Return a range of members in a sorted set, by index, with scores ordered from high to low}} 
    `ZREVRANGEBYSCORE key max min WITHSCORES LIMIT offset count
>                                  {{Return a range of members in a sorted set, by score, with scores ordered from high to low}} 
    `ZREVRANK key member           {{Determine the index of a member in a sorted set, with scores ordered from high to low}} 
    `ZSCORE key member             {{Get the score associated with the given member in a sorted set}} 
    `ZUNIONSTORE destination numkeys key key ... WEIGHTS weight weight ... AGGREGATE SUM|MIN|MAX
>                                  {{Add multiple sorted sets and store the resulting sorted set in a new key}} 
    `ZSCAN key cursor MATCH pattern COUNT count
>                                  {{Incrementally iterate sorted sets elements and associated scores}} 

$ Strings
    `APPEND key value              {{Append a value to a key}} 
    `BITCOUNT key start end        {{Count set bits in a string}} 
    `BITOP operation destkey key key ...
>                                  {{Perform bitwise operations between strings}} 
    `BITPOS key bit start end      {{Find first bit set or clear in a string}} 
    `DECR key                      {{Decrement the integer value of a key by one}} 
    `DECRBY key decrement          {{Decrement the integer value of a key by the given number}} 
    `GET key                       {{Get the value of a key}} 
    `GETBIT key offset             {{Returns the bit value at offset in the string value stored at key}} 
    `GETRANGE key start end        {{Get a substring of the string stored at a key}} 
    `GETSET key value              {{Set the string value of a key and return its old value}} 
    `INCR key                      {{Increment the integer value of a key by one}} 
    `INCRBY key increment          {{Increment the integer value of a key by the given amount}} 
    `INCRBYFLOAT key increment     {{Increment the float value of a key by the given amount}} 
    `MGET key key ...              {{Get the values of all the given keys}} 
    `MSET key value key value ...  {{Set multiple keys to multiple values}} 
    `MSETNX key value key value ...
>                                  {{Set multiple keys to multiple values, only if none of the keys exist}} 
    `PSETEX key milliseconds value {{Set the value and expiration in milliseconds of a key}} 
    `STRLEN key                    {{Get the length of the value stored in a key}} 

$ Keys
    `DEL key key ...               {{Delete a key}} 
    `DUMP key                      {{Return a serialized version of the value stored at the specified key.}} 
    `EXISTS key key ...            {{Determine if a key exists}} 
    `EXPIRE key seconds            {{Set a key's time to live in seconds}} 
    `EXPIREAT key timestamp        {{Set the expiration for a key as a UNIX timestamp}} 
    `KEYS pattern                  {{Find all keys matching the given pattern}} 
    `MIGRATE host port key destination-db timeout COPY REPLACE
>                                  {{Atomically transfer a key from a Redis instance to another one.}} 
    `MOVE key db                   {{Move a key to another database}} 
    `OBJECT subcommand arguments arguments ...
>                                  {{Inspect the internals of Redis objects}} 
    `PERSIST key                   {{Remove the expiration from a key}} 
    `PEXPIRE key milliseconds      {{Set a key's time to live in milliseconds}} 
    `PEXPIREAT key milliseconds-timestamp
>                                  {{Set the expiration for a key as a UNIX timestamp specified in milliseconds}} 
    `PTTL key                      {{Get the time to live for a key in milliseconds}} 
    `RANDOMKEY                     {{Return a random key from the keyspace}} 
    `RENAME key newkey             {{Rename a key}} 
    `RENAMENX key newkey           {{Rename a key, only if the new key does not exist}} 
    `RESTORE key ttl serialized-value REPLACE
>                                  {{Create a key using the provided serialized value, previously obtained using DUMP.}} 
    `SORT key BY pattern LIMIT offset count GET pattern GET pattern ... ASC|DESC ALPHA STORE destination
>                                  {{Sort the elements in a list, set or sorted set}} 
    `TTL key                       {{Get the time to live for a key}} 
    `TYPE key                      {{Determine the type stored at key}} 
    `WAIT numslaves timeout        {{Wait for the synchronous replication of all the write commands sent in the context of the current connection}} 
    `SCAN cursor MATCH pattern COUNT count
>                                  {{Incrementally iterate the keys space}} 

$ Lists
    `BLPOP key key ... timeout     {{Remove and get the first element in a list, or block until one is available}} 
    `BRPOP key key ... timeout     {{Remove and get the last element in a list, or block until one is available}} 
    `BRPOPLPUSH source destination timeout
>                                  {{Pop a value from a list, push it to another list and return it; or block until one is available}} 
    `LINDEX key index              {{Get an element from a list by its index}} 
    `LINSERT key BEFORE|AFTER pivot value
>                                  {{Insert an element before or after another element in a list}} 
    `LLEN key                      {{Get the length of a list}} 
    `LPOP key                      {{Remove and get the first element in a list}} 
    `LPUSH key value value ...     {{Prepend one or multiple values to a list}} 
    `LPUSHX key value              {{Prepend a value to a list, only if the list exists}} 
    `LRANGE key start stop         {{Get a range of elements from a list}} 
    `LREM key count value          {{Remove elements from a list}} 
    `LSET key index value          {{Set the value of an element in a list by its index}} 
    `LTRIM key start stop          {{Trim a list to the specified range}} 
    `RPOP key                      {{Remove and get the last element in a list}} 
    `RPOPLPUSH source destination  {{Remove the last element in a list, prepend it to another list and return it}} 
    `RPUSH key value value ...     {{Append one or multiple values to a list}} 
    `RPUSHX key value              {{Append a value to a list, only if the list exists}} 

$ HyperLogLog
    `PFADD key element element ... {{Adds the specified elements to the specified HyperLogLog}} 
    ` PFMERGE destkey sourcekey sourcekey ...
>                                  {{Merge N different HyperLogLogs into a single one}} 
    `PFCOUNT key key ...           {{Return the approximated cardinality of the set(s) observed by the HyperLogLog at key(s)}} 

$ Geo
    `GEOADD key longitude latitude member longitude latitude member ...
>                                  {{Add one or more geospatial items in the geospatial index represented using a sorted set}} 
    `GEOHASH key member member ... {{Returns members of a geospatial index as standard geohash strings}} 
    `GEOPOS key member member ...  {{Returns longitude and latitude of members of a geospatial index}} 
    `GEODIST key member1 member2 unit
>                                  {{Returns the distance between two members of a geospatial index}} 
    `GEORADIUS key longitude latitude radius m|km|ft|mi WITHCOORD WITHDIST WITHHASH COUNT count
>                                  {{Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a point}} 
    `GEORADIUSBYMEMBER key member radius m|km|ft|mi WITHCOORD WITHDIST WITHHASH COUNT count
>                                  {{Query a sorted set representing a geospatial index to fetch members matching a given maximum distance from a member}} 

