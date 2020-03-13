# Intel 8085 Instruction Set

> Source: http://scanftree.com/microprocessor/Instruction-Set-In-8085

> Aliases: 8085-programming, 8085, 8085-instruction-set, 8085-instructionset, 8085-instructions

$ Data Transfer Instructions
    `MOV Destination, Source       {{Copies a word or byte of data from 'source' to 'destination'}} 
    `MVI Destination, 8 bit data   {{Copies the given byte of data  to 'destination'}} 
    `LDA 16-bit address            {{Loads the 16-bit address in Accumulator}} 
    `LDAX B/D Reg. pair            {{Load accumulator indirect}} 
    `LXI Reg.Pair, 16-bit data     {{Loads 16-bit data in the register pair}} 
    `STA 16-bit address            {{Stores the content of Accumulator in memory location specified by the 16-bit address}} 
    `STAX Reg. pair                {{Stores the content of Accumulator in memory location specified by the contents of operand(Reg. pair)}} 
    `XCHG                          {{Contents of register H are exchanged with the contents of register D, and the contents of register L are exchanged with the contents of register E}} 
    `LHLD 16-bit address           {{Copies the contents of the memory location pointed out by the 16-bit address into register L and copies the contents of the next memory location into register H}} 
    `SPHL                          {{The instruction loads the contents of the H and L registers into the stack pointer register, the contents of the H register provide the high-order address and the contents of the L register provide the low-order address.}} 
    `XTHL                          {{The contents of the L register are exchanged with the stack location pointed out by the contents of the stack pointer register}} 
    `SHLD 16-bit address           {{Contents of register L are stored into the memory location specified by the 16-bit address in the operand and the contents of H register are stored into the next memory location}} 
    `OUT 8-bit port address        {{Contents of the accumulator are copied into the I/O port specified by the operand}} 
    `IN 8-bit port address         {{Contents of the input port designated in the operand are read and loaded into the accumulator}} 

$ Arithmetic Instructions
    `ADD R/M                       {{Adds the content of register or memory location  to the content of Accumulator and put the result in the Accumulator}} 
    `SUB R/M                       {{Subtracts the content of register or memory location  from the content of Accumulator and put the result in the Accumulator}} 
    `INX Reg.pair                  {{Contents of the designated register pair are incremented by 1}} 
    `DCX Reg.pair                  {{Contents of the designated register pair are decremented by 1}} 
    `INR R/M                       {{Contents of the designated register or memory location is incremented by one}} 
    `DCR R/M                       {{Contents of the designated register or memory location  is decremented by one}} 
    `DAA                           {{Decimal Adjust Accumulator}} 

$ Logical Instructions
    `ANA R/M                       {{Content of the Accumulator is logically ANDed with  the content of the operand}} 
    `ANI 8-bit data                {{Content of the Accumulator is logically ANDed with 8-bit data given as the operand}} 
    `ORA R/M                       {{Content of the Accumulator is logically ORed with  the content of the operand}} 
    `ORI 8-bit data                {{Content of the Accumulator is logically ANDed with 8-bit data given as the operand}} 
    `XRA R/M                       {{Content of the Accumulator is Exclusive-ORed with  the content of the operand}} 
    `XRI 8-bit data                {{Content of the Accumulator is Exclusive-ORed with  8-bit data given as the operand}} 
    `CMP R/M                       {{Compares the content in the register or memory location with content in Accumulator}} 
    `CPI 8-bit data                {{Compares the 8-bit data given as the operand with content in Accumulator}} 

$ Rotate Instructions
    `RCL                           {{Rotates each bits in the Accumulator to the left once. MSB is circled back into the LSB and CF contains a copy of the bit most recently moved out of the MSB}} 
    `RCR                           {{Rotates each bits in the Accumulator to the right once. LSB is circled back into the MSB and CF contains a copy of the bit most recently moved out of the LSB}} 
    `RAL                           {{Rotate accumulator left through carry}} 
    `RAR                           {{Rotate accumulator right through carry}} 
    `SHL Destination, Count        {{Shifts each bit in the 'destination' to the left 'count' number of times and  a 0 is put in the LSB position for each shift}} 
    `SHR Destination, Count        {{Shifts each bit in the 'destination' to the right 'count' number of times and  a 0 is put in the MSB position for each shift}} 

$ Control Transfer Instructions
    `JMP 16-bit address            {{Unconditional jump to the specified 16-bit address}} 
    `JC 16-bit address             {{Jump to the specified 16-bit address if carry flag is set}} 
    `JZ 16-bit address             {{Jump to the specified 16-bit address if zero flag is set}} 
    `JM 16-bit address             {{Jump to the specified 16-bit address if sign flag is set}} 
    `JP 16-bit address             {{Jump to the specified 16-bit address if sign flag is zero}} 
    `CALL 16-bit address           {{Program sequence is transferred to the memory location specified by the 16-bit address}} 
    `CC 16-bit address             {{Program sequence is transferred to the memory location specified by the 16-bit address if carry flag is set}} 
    `CZ 16-bit address             {{Program sequence is transferred to the memory location specified by the 16-bit address if zero flag is set}} 
    `CM 16-bit address             {{Program sequence is transferred to the memory location specified by the 16-bit address if sign flag is set}} 
    `CP 16-bit address             {{Program sequence is transferred to the memory location specified by the 16-bit address if sign flag is zero}} 

$ Control Instructions
    `NOP                           {{No operation is performed}} 
    `HLT                           {{Halt and enter wait state}} 
    `DI                            {{Disable Interrupts}} 
    `EI                            {{Enable Interrupts}} 
    `RIM                           {{Read Interrupt Mask}} 
    `SIM                           {{Set Interrupt Mask}} 
    `CLI                           {{Clear Interrupt Flag}} 

