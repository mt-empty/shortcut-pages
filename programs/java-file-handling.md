# Java File Handling

> Source: https://docs.oracle.com/javase/tutorial/essential/io/

> Aliases: java-file-handling-methods, java-file-i/o

$ Byte Streams
    `FileInputStream in = 
	new FileInputStream("xanadu.txt");
>                                  {{Uses byte stream to perform input of 8 bits at a time}} 
    `FileOutputStream out = 
	new FileOutputStream("outagain.txt");
>                                  {{Uses byte stream to perform output of 8 bits}} 
    `FileOutputStream out = 
	new FileOutputStream("outagain.txt",true);
>                                  {{This form of the constructor appends data you write instead of overwriting old data}} 

$ Byte Stream Methods
    `read()                        {{The read method returns integer or long, EOF is detected by -1}} 
    `write(int b) or write(byte[] b)
>                                  {{Write method writes a byte or b.length bytes to the file}} 

$ Character Streams
    `FileReader inputStream = new FileReader
("xanadu.txt");
>                                  {{Reads from file in terms of 16 bits, Integer c holds character value in its last 16 bits}} 
    `FileWriter outputStream = new FileWriter
("characteroutput.txt");
>                                  {{Writes to file in terms of 16 bits}} 
    `FileWriter outputStream = new FileWriter
("characteroutput.txt",true);
>                                  {{Use this constructor of FileWriter to append data to file, The second parameter(append) can be true or false}} 

$ Buffered Streams
    `BufferedReader inputStream = 
	new BufferedReader(
	 new FileReader("xanadu.txt"));
>                                  {{Buffered input streams read data from a memory area known as a buffer; the native input API is called only when the buffer is empty.}} 
    `BufferedWriter outputStream = 
	new BufferedWriter(
	 new FileWriter("characteroutput.txt"));
>                                  {{Buffered output streams write data to a buffer, and the native output API is called only when the buffer is full.}} 
    `BufferedInputStream in = 
	new BufferedInputStream(
	 new FileInputStream("xanadu.txt"));
>                                  {{Reads data in terms of 8 bits from file but every read is not handled directly by the OS, it reads data from a memory area known as a buffer}} 
    `BufferedOutputStream out = 
	new BufferedOutputStream(
	 new FileOutputStream("outagain.txt"));
>                                  {{Writes byte data to file but writes data to a buffer, and the native output API is called only when the buffer is full.}} 

$ Data Streams
    `DataInputStream in = new DataInputStream(
	new BufferedInputStream(
	 new FileInputStream("input.txt")));
>                                  {{Data streams support binary I/O of primitive data type values. DataInputStream can only be used as a wrapper for an existing byte stream.}} 
    `DataOutputStream out = new DataOutputStream(
	new BufferedOutputStream(
	 new FileOutputStream(dataFile)));
>                                  {{A DataOutputStream can only be created as a wrapper for an existing byte stream object.}} 

$ Data Stream Methods
    `readInt()                     {{Reads four input bytes and returns an int value}} 
    `readDouble()                  {{Reads eight input bytes and returns a double value}} 
    `readUTF()                     {{Reads in a string that has been encoded using a modified UTF-8 format}} 
    `writeInt(int b)               {{Writes an int value, which is comprised of four bytes, to the output stream}} 
    `writeDouble(double d)         {{Writes a double value, which is comprised of eight bytes, to the output stream}} 
    `writeUTF(String s)            {{Writes two bytes of length information to the output stream, followed by the modified UTF-8 representation of every character in the string s}} 

$ Line Oriented I/O
    `BufferedReader inputStream = 
	new BufferedReader(
	 new FileReader("xanadu.txt"));
>                                  {{Character I/O usually occurs in bigger units than single characters, BufferedReader is used for line oriented reading and writing of a file}} 
    `PrintWriter outputStream = 
	new PrintWriter(
	 new FileWriter("characteroutput.txt"));
>                                  {{Character I/O usually occurs in bigger units than single characters, PrintWriter is used for line oriented reading and writing of a file}} 
    `Method readLine()             {{Used to read and write a line at a time, EOF is detected when value read is null}} 
    `Method println(String line)   {{Used to read and write a line at a time, EOF is detected when value read is null}} 

