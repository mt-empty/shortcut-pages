# Whitespace Cheatsheet

> Source: http://compsoc.dur.ac.uk/whitespace/tutorial.html

> Aliases: whitespace-language, white-space-language, white-space

$ Instruction Modification Parameter (IMP)
    `<Space>                       {{Stack Manipulation}} 
    `<Tab><Space>                  {{Arithmetic}} 
    `<Tab><Tab>                    {{Heap Access}} 
    `<Tab><Linefeed>               {{Input/Output}} 
    `<Linefeed>                    {{Flow control}} 

$ Stack Manipulation (IMP: <Space>)
    `<Space>                       {{Push the number onto the stack}} 
    `<Linefeed><Space>             {{Duplicate top item on the stack}} 
    `<Linefeed><Tab>               {{Swap the top two items on the stack}} 
    `<Linefeed><Linefeed>          {{Pop the topmost item from stack}} 

$ Arithmetic (IMP: <Tab><Space>)
    `<Space><Space>                {{Addition}} 
    `<Space><Tab>                  {{Subtraction}} 
    `<Space><Linefeed>             {{Multiplication}} 
    `<Tab><Space>                  {{Integer Division}} 
    `<Tab><Tab>                    {{Modulo}} 

$ Heap Access (IMP: <Tab><Tab>)
    `<Space>                       {{Store}} 
    `<Tab>                         {{Retrieve}} 

$ Flow Control (IMP: <Linefeed>)
    `<Space><Space>                {{Mark a location in the program}} 
    `<Space><Tab>                  {{Call a subroutine}} 
    `<Space><Linefeed>             {{Jump unconditionally to a label}} 
    `<Tab><Space>                  {{Jump to a label if the top of the stack is zero}} 
    `<Tab><Tab>                    {{Jump to a label if the top of the stack is negative}} 
    `<Tab><Linefeed>               {{End a subroutine and transfer control back to the caller}} 
    `<Linefeed><Linefeed>          {{End the program}} 

$ I/O (IMP: <Tab><Linefeed>)
    `<Space><Space>                {{Output the character at the top of the stack}} 
    `<Space><Tab>                  {{Output the number at the top of the stack}} 
    `<Tab><Space>                  {{Read a character and place it in the location given by the top of the stack}} 
    `<Tab><Tab>                    {{Read a character and place it in the location given by the top of the stack}} 

