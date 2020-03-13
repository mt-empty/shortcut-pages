# Intel 8086 Instruction Set

> Source: http://users.utcluj.ro/~elupu/Curs/fileloader.php?fileName=upload/Cursuri/Univ.Nord_BM1/Curs_5/8086_instruction_set.pdf

> Aliases: 8086-instructionset, 8086-instruction-set, 8086, 8086-programming, 8086-instructions

$ Data Transfer Instructions
    `MOV Destination, Source       {{Copies a word or byte of data from 'source' to 'destination'}} 
    `XCHG Destination, Source      {{Exchanges the content of 'source' and 'destination'}} 
    `LEA Register, Source          {{Stores the offset of the variable or memory location named as the 'source'  into the 16-bit register}} 
    `LDS - LDS Register, Memory address of the first word
>                                  {{This instruction loads new values into the specified register and into the DS register from four successive memory locations.}} 
    `LES - LES Register, Memory address of the first word
>                                  {{This instruction loads new values into the specified register and into the ES register from four successive memory locations}} 

$ Arithmetic Instructions
    `ADD Destination, Source       {{Adds the number in 'source' to the number in 'destination' and put the result in the 'destination'}} 
    `SUB Destination, Source       {{Subtracts the number in 'source' from the number in 'destination' and put the result in the 'destination'}} 
    `MUL Source                    {{Multiplies an unsigned byte in the 'source' with an unsigned byte in AL register or an unsigned word in the 'source' with an unsigned word in AX register}} 
    `DIV Source                    {{Divide an unsigned word by a byte in the 'source' or to divide an unsigned double word by a word in the 'source'}} 
    `INC Destination               {{Increments the content of 'destination' by one}} 
    `DEC Destination               {{Decrements the content of 'destination' by one}} 
    `DAA                           {{Decimal adjust after BCD addition}} 
    `AAA                           {{ASCII adjust for addition}} 

$ Logical Instructions
    `AND Destination, Source       {{ANDs each bit in the 'source' byte or word with the same numbered bit in a 'destination' byte or word}} 
    `OR Destination, Source        {{ORs each bit in a 'source' byte or word with the same numbered bit in a 'destination' byte or word}} 
    `XOR Destination, Source       {{Exclusive-ORs each bit in a 'source' byte or word with the same numbered bit in a 'destination' byte or word}} 
    `NOT Destinations              {{Inverts each bit (1’s complement) of a byte or word in the 'destination'}} 
    `CMP Destination, Source       {{Compares a byte / word in the 'source' with a byte / word in the 'destination'}} 
    `TEST Destination, Source      {{ANDs the byte / word in the 'source' with the byte / word in the 'destination'}} 

$ Rotate and Shift Instructions
    `RCL Destination, Count        {{Rotates all the bits in a word or byte  in the 'destination' to the left 'count' number of times through carry flag}} 
    `RCR Destination, Count        {{Rotates all the bits in a word or byte  in the 'destination' to the right 'count' number of times through carry flag}} 
    `ROL Destination, Count        {{Rotates all the bits in a word or byte  in the 'destination' to the left 'count' number of times. MSB is circled back into the LSB and CF contains a copy of the bit most recently moved out of the MSB}} 
    `ROR Destination, Count        {{Rotates all the bits in a word or byte  in the 'destination' to the right 'count' number of times. LSB is circled back into the LSB and CF contains a copy of the bit most recently moved out of the LSB}} 
    `SHL Destination, Count        {{Shifts each bit in the 'destination' to the left 'count' number of times and  a 0 is put in the LSB position for each shift}} 
    `SHR Destination, Count        {{Shifts each bit in the 'destination' to the right 'count' number of times and  a 0 is put in the MSB position for each shift}} 

$ Control Transfer Instructions
    `JMP Destination               {{Unconditional jump to the specified 'destination'}} 
    `JC Destination                {{Jump to the specified 'destination' if carry flag is set}} 
    `JZ Destination                {{Jump to the specified 'destination' if zero flag is set}} 
    `JS                            {{Jump to the specified 'destination' if sign flag is set}} 
    `LOOP                          {{Repeat a series of instructions some number of times. The number of times is loaded into CX}} 
    `CALL                          {{Transfer control to a subprogram or a procedure}} 

$ Flag Manipulation Instructions
    `STC                           {{Sets Carry Flag}} 
    `CLC                           {{Clear Carry Flag}} 
    `CMC                           {{Complement Carry Flag}} 
    `STD                           {{Sets Direction Flag}} 
    `CLD                           {{Clear Direction Flag}} 
    `STI                           {{Sets Interrupt Flag}} 
    `CLI                           {{Clear Interrupt Flag}} 

