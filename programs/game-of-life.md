# Conway's Game of Life

> Source: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

> Aliases: conway's-game, conways-game, gol

$ Terms
    `Grid                          {{An infinite two-dimensional grid composed of square cells.}} 
    `Cell                          {{A single square in a grid. Can be in one of two states: dead or alive.}} 
    `Neighbour                     {{Every cell has 8 neighbours. They are the cells horizontally, vertically and diagonally immediately adjacent to it.}} 
    `Seed                          {{The initial pattern of cells on the grid.}} 
    `Transition                    {{Also known as a tick, every transition is a step in time. During each transition, every cell checks the number of neighbours it has to see whether or not it should change state. Every cell changes state at once.}} 
    `Generation                    {{The number of transitions since the seed was set.}} 

$ Transition Rules
    `Any live cell with fewer than two live neighbours dies
>                                  {{As if caused by under-population}} 
    `Any live cell with two or three live neighbours lives on to the next generation.
>                                  {{}} 
    `Any live cell with more than three live neighbours dies
>                                  {{As if caused by over-population}} 
    `Any dead cell with exactly three live neighbours becomes a live cell
>                                  {{As if caused by reproduction}} 

$ Live Cell Cheat Sheet
    `No Neighbours                 {{Dead}} 
    `One Neighbour                 {{Dead}} 
    `Two Neighbours                {{Alive}} 
    `Three Neighbours              {{Alive}} 
    `Four Neighbours               {{Dead}} 
    `Five Neighbours               {{Dead}} 
    `Six Neighbours                {{Dead}} 
    `Seven Neighbours              {{Dead}} 
    `Eight Neighbours              {{Dead}} 

$ Dead Cell Cheat Sheet
    `No Neighbours                 {{Dead}} 
    `One Neighbour                 {{Dead}} 
    `Two Neighbours                {{Dead}} 
    `Three Neighbours              {{Alive}} 
    `Four Neighbours               {{Dead}} 
    `Five Neighbours               {{Dead}} 
    `Six Neighbours                {{Dead}} 
    `Seven Neighbours              {{Dead}} 
    `Eight Neighbours              {{Dead}} 

