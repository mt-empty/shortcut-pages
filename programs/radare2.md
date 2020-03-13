# Radare2

> Source: https://github.com/radare/radare2book/blob/master/refcard/radare2_rc.pdf

> Aliases: r2

$ Survival Guide
    `aa                            {{Auto analyze}} 
    `pdf@fcn[Tab]                  {{Disassemble function}} 
    `f fcn[Tab]                    {{List functions}} 
    `f str[Tab]                    {{List strings}} 
    `fr <flagname> <newname>       {{Rename flag}} 
    `psz <offset>                  {{Print string}} 
    `arf <flag>                    {{Find cross ref for a flag}} 

$ Flagspaces
    `fs                            {{Display flagspaces}} 
    `fs *                          {{Select all flagspaces}} 
    `fs <sections>                 {{Select one flagspace}} 

$ Flags
    `f                             {{List flags}} 
    `fj                            {{Display flags in json}} 
    `fl                            {{Show flag length}} 
    `fx                            {{Show hexdump of flag}} 
    `fC <name> <cmt>               {{Set flag comment}} 

$ Info
    `ii                            {{Info on imports}} 
    `iI                            {{Info on binary}} 
    `ie                            {{Display entrypoint}} 
    `iS                            {{Display sections}} 
    `ir                            {{Display relocations}} 

$ Print String
    `psz <offset>                  {{Print string}} 
    `psb <offset>                  {{Print strings in current block}} 
    `psx <offset>                  {{Show string with scaped chars}} 
    `psp <offset>                  {{Print pascal string}} 
    `psw <offset>                  {{Print wide string}} 

$ Visual Mode
    `V                             {{Enter visual mode}} 
    `(p / P)                       {{Rotate modes (hex, disasm, debug, words, buf)}} 
    `c                             {{Toggle (c)ursor}} 
    `q                             {{Back to radare shell}} 
    `hjkl                          {{Move around (left-down-up-right)}} 
    `Enter                         {{Follow address of jump/call}} 
    `sS                            {{Step / step over}} 
    `Enter                         {{Follow address of jump/call}} 
    `o                             {{Go/seek to given offset}} 
    `.                             {{Seek to program counter}} 
    `/                             {{In cursor mode search in current block}} 
    `:cmd                          {{Run radare command}} 
    `;[-]cmt                       {{Add/remove comment}} 
    `/*+-[]                        {{Change block size, [] = resize hex.cols}} 
    `>||<                          {{Seek aligned to block size}} 
    `i                             {{Insert code}} 
    `a                             {{Assemble code}} 
    `A                             {{Visual Assembler}} 
    `b                             {{Toggle breakpoint}} 
    `B                             {{Automatic block size}} 
    `d[f?]                         {{Define function, data, code, ...}} 
    `D                             {{Enter visual diff mode (set diff.from/to)}} 
    `e                             {{Edit eval configuration variables}} 
    `f/F                           {{Set/unset flag}} 
    `gG                            {{Go seek to begin and end of file (0-$s)}} 
    `mK/’K                         {{Mark/go to Key (any key)}} 
    `M                             {{Walk the mounted filesystems}} 
    `n/N                           {{Seek next/prev function/flag/hit (scr.nkey)}} 
    `C                             {{Toggle (C)olors}} 
    `R                             {{Randomize color palette (ecr)}} 
    `t                             {{Track flags (browse symbols, functions..)}} 
    `T                             {{Browse anal info and comments}} 
    `v                             {{Visual code analysis menu}} 
    `V                             {{View graph (agv?)}} 
    `W                             {{Open WebUI}} 
    `uU                            {{Undo/redo seek}} 
    `x                             {{Show xrefs to seek between them}} 
    `yY                            {{Copy and paste selection}} 
    `z                             {{Toggle zoom mode}} 

$ Searching
    `/ foo\\00                     {{Search for string foo\0}} 
    `/b                            {{Search backwards}} 
    `//                            {{Repeat last search}} 
    `/w foo                        {{Search for wide string f\0o\0o\0}} 
    `/wi foo                       {{Search for wide string ignoring case}} 
    `/! ff                         {{Search for first occurrence not matching}} 
    `/i foo                        {{Search for string foo ignoring case}} 
    `/e /E.F/i                     {{Match regular expression}} 
    `/x ff0.23                     {{Search for hex string}} 
    `/x ff..33                     {{Search for hex string ignoring some nibbles}} 
    `/x ff43 ffd0                  {{Search for hexpair with mask}} 
    `/d 101112                     {{Search for a deltified sequence of bytes}} 
    `/!x 00                        {{Inverse hexa search (find first byte != 0x00)}} 
    `/c jmp <esp>                  {{Search for asm code (see search.asmstr)}} 
    `/a jmp eax                    {{Assemble opcode and search its bytes}} 
    `/A                            {{Search for AES expanded keys}} 
    `/r sym.printf                 {{Analyze opcode reference an offset}} 
    `/R                            {{Search for ROP gadgets}} 
    `/P                            {{Show offset of previous instruction}} 
    `/m magicfile                  {{Search for matching magic file}} 
    `/p patternsize                {{Search for pattern of given size}} 
    `/z min max                    {{Search for strings of given size}} 
    `/v[?248] num                  {{Look for a asm.bigendian 32bit value}} 

$ Saving
    `Po <file>                     {{Open project}} 
    `Ps <file>                     {{Save project}} 
    `Pi <file>                     {{Show project information}} 

$ Usable Variables in Expression
    `$$                            {{Here (current virtual seek)}} 
    `$o                            {{Here (current disk io offset)}} 
    `$s                            {{File size}} 
    `$b                            {{Block size}} 
    `$w                            {{Get word size, 4 if asm.bits=32, 8 if 64}} 
    `$c                            {{Get width of terminal}} 
    `$r                            {{Get height of terminal}} 
    `$S                            {{Section offset}} 
    `$SS                           {{Section size}} 
    `$j                            {{Jump address (jmp 0x10, jz 0x10 => 0x10)}} 
    `$f                            {{Jump fail address (jz 0x10 => next instruction)}} 
    `$I                            {{Number of instructions of current function}} 
    `$F                            {{Current function size}} 
    `$Jn                           {{Get nth jump of function}} 
    `$Cn                           {{Get nth call of function}} 
    `$Dn                           {{Get nth data reference in function}} 
    `$Xn                           {{Get nth xref of function}} 
    `$m                            {{Opcode memory reference (mov eax,[0x10] => 0x10)}} 
    `$l                            {{Opcode length}} 
    `$e                            {{1 if end of block, else 0}} 
    `$ev                           {{Get value of eval config variable}} 
    `$?                            {{Last comparision value}} 

