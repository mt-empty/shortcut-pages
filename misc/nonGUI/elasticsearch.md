# Elasticsearch

> Source: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

> Aliases: elastic-search

$ Basics
    `bin/elasticsearch             {{Start Elastic instance}} 
    `curl -X GET  'http://localhost:9200/?pretty=true'
>                                  {{View instance metadata}} 
    `curl -X POST 'http://localhost:9200/_shutdown'
>                                  {{Shutdown Elastic instance}} 
    `curl -X GET 'http://localhost:9200/_cat?pretty=true'
>                                  {{List all admin methods}} 
    `curl -X GET 'http://localhost:9200/_cat/indices?pretty=true'
>                                  {{List all indices}} 
    `curl -X GET 'http://localhost:9200/_cluster/health?pretty=true'
>                                  {{View Cluster Health}} 

$ Indexing
    `curl -X GET  'http://localhost:9200/<index name>'
>                                  {{View specific index}} 
    `curl -X POST 'http://localhost:9200/<index name>'
>                                  {{Create an index}} 
    `curl -X DELETE 'http://localhost:9200/<index name>'
>                                  {{Delete an index}} 
    `curl -X GET  'http://localhost:9200/<index name>/_search'
>                                  {{Search an index}} 
    `curl -X GET  'http://localhost:9200/<index name>/<type>/_search'
>                                  {{Search an index type}} 

$ Retrieving and modifying documents
    `curl -X GET  'http://locahost:9200/<index name>/<type>/<id>'
>                                  {{Retrieve a specific document}} 
    `curl -X POST 'http://locahost:9200/<index name>/<type>/'
>                                  {{Create a document}} 
    `curl -X PUT  'http://locahost:9200/<index name>/<type>/<id>'
>                                  {{Create/Update a specific document}} 
    `curl -X DELETE 'http://localhost:9200/<index name>/<type>/<id>'
>                                  {{Delete a specific document}} 

$ Mappings and settings
    `curl -X GET  'http://localhost:9200/<index name>/_mappings'
>                                  {{View mappings for index}} 
    `curl -X GET  'http://localhost:9200/<index name>/_settings'
>                                  {{View setting information for an index}} 
    `curl -X GET  'http://localhost:9200/<index name>/<type>/_mappings'
>                                  {{View mappings for an index type}} 
    `curl -X GET  'http://localhost:9200/<index name>/<type>/_settings'
>                                  {{View setting information for an index type}} 

