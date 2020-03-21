# CouchDB

> Source: http://docs.couchdb.org/

> Aliases: couch-api, couchdb-api, couch

$ General
    `couchdb start                 {{Starts a CouchDB instance}} 
    `http://localhost:5984/_utils  {{Starts a CouchDB instance}} 
    `brew install couchdb          {{Installs CouchDB on Mac OSx}} 
    `apt-get install couchdb -y    {{Installs CouchDB on Ubuntu}} 

$ HTTP API
    `curl -XGET localhost:5984     {{Retrieves information about this node (GET)}} 
    `curl -XGET localhost:5984/_active_tasks
>                                  {{Retrieves the list of active tasks (GET)}} 
    `curl -XGET localhost:5984/_all_dbs
>                                  {{Retrieves the list of database names (GET)}} 
    `curl -XGET localhost:5984/_config
>                                  {{Retrieves the instance configuration (GET)}} 
    `curl -XGET localhost:5984/_db_updates
>                                  {{Retrieves the latest database change (GET)}} 
    `curl -XGET localhost:5984/_log
>                                  {{Tails the main log file (GET)}} 
    `curl -XGET localhost:5984/_stats
>                                  {{Statistics about the current node (GET)}} 
    `curl -XGET localhost:5984/_uuids
>                                  {{UUIDs generated by CouchDB (GET)}} 

$ Document API
    `curl -XPUT localhost:5984/{db_name}
>                                  {{Creates a new database (POST)}} 
    `curl -XGET localhost:5984/{db_name}
>                                  {{Returns database information (GET)}} 
    `curl -XGET localhost:5984/{db_name}/_all_docs
>                                  {{Returns all the documents in the database (GET)}} 
    `curl -XGET localhost:5984/{db_name}/{doc_id}
>                                  {{Returns the document (GET)}} 
