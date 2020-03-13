# Graph Operations

> Source: https://en.wikipedia.org/wiki/Graph_theory

> Aliases: graph-operation

$ Adjacency list
    `Storage                       {{O(|V|+|E|)}} 
    `Add Vertex                    {{O(1)}} 
    `Add Edge                      {{O(1)}} 
    `Remove Vertex                 {{O(|V| + |E|)}} 
    `Remove Edge                   {{O(|E|)}} 
    `Query                         {{O(|V|)}} 

$ Incidence list
    `Storage                       {{O(|V|+|E|)}} 
    `Add Vertex                    {{O(1)}} 
    `Add Edge                      {{O(1)}} 
    `Remove Vertex                 {{O(|E|)}} 
    `Remove Edge                   {{O(|E|)}} 
    `Query                         {{O(|E|)}} 

$ Adjacency matrix
    `Storage                       {{O(|V|²)}} 
    `Add Vertex                    {{O(|V|²)}} 
    `Add Edge                      {{O(1)}} 
    `Remove Vertex                 {{O(|V|²)}} 
    `Remove Edge                   {{O(1)}} 
    `Query                         {{O(1)}} 

$ Incidence matrix
    `Storage                       {{O(|V| ⋅ |E|)}} 
    `Add Vertex                    {{O(|V| ⋅ |E|)}} 
    `Add Edge                      {{O(|V| ⋅ |E|)}} 
    `Remove Vertex                 {{O(|V| ⋅ |E|)}} 
    `Remove Edge                   {{O(|V| ⋅ |E|)}} 
    `Query                         {{O(|E|)}} 

