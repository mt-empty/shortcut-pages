# Cryptography

> Source: https://en.wikipedia.org/wiki/Cryptography

$ Terminology
    `Asymmetric Algorithm          {{An algorithm in which the key used for encryption is different from that used for decryption. Also known as public key cryptography.}} 
    `Block Cipher                  {{An algorithm that encrypts data in blocks, commonly of 64 bits each.}} 
    `Cipher                        {{A cryptographic algorithm, i.e. a mathematical function used for encryption and decryption.}} 
    `Stream Cipher                 {{It is a method of encrypting data piece-by-piece, as opposed to encoding a contiguous chunk of data all at once like a block cipher.}} 
    `Decryption                    {{The science of turning enciphered text into plain text without prior knowledge of the algorithms or keys involved. This is what the interceptor or 'cracker' does.}} 
    `Digital Signature             {{An encrypted message digest which is appended to a plaintext or encrypted message to verify the identity of the sender. The signature is encrypted with the user's private key and can only be decrypted with the corresponding public key. The same key pairs may be used for signature and encryption purposes but separate key pairs for each purpose are usually recommended.}} 
    `Encryption                    {{Encryption is the process of turning a clear-text message (Plaintext) into a data stream which looks like a meaningless and random sequence of bits (ciphertext).}} 
    `Key                           {{A value that is used to encrypt or decrypt a message.}} 
    `PGP                           {{A complete public-key cryptosystem for electronic messaging that has been released to the public domain. It was originally designed by Phil Zimmerman. It uses IDEA, CAST or Triple DES for actual data encryption and RSA (with up to 2048-bit key) or DH/DSS (with 1024-bit signature key and 4096-bit encryption key) for key management and digital signatures. The RSA or DH public key is used to encrypt the IDEA secret key as part of the message.}} 

$ Terminology (cont.)
    `Private Key                   {{The secret part of a private key/public key pair used in public key cryptography. The Private Key is normally known only to the key owner. Messages are encrypted using the Public Key and decrypted using the Private Key. For digital signatures, however, a document is signed with a private key and authenticated with the corresponding Public Key.}} 
    `Public Key Cryptography       {{A concept first proposed by Diffie and Hellman in 1975 that has been largely responsible for opening up the science of cryptography for commercial use. The encryption key is made public but only the person who holds the corresponding private key can decrypt the message.}} 
    `Public Line                   {{A transmission channel which cannot be used to send information secretly. A public pay phone is an excellent example of this, so is the Internet.}} 
    `Secure Line                   {{A transmission channel which can be used to send information secretly (in other words, nobody can intercept and read that data).}} 
    `Steganography                 {{A method of hiding a secret message in another message, e.g. within a graphic image.}} 
    `Symmetric Algorithm           {{An encryption algorithm where the encryption key is the same as the decryption key, or where one key is easily calculated from the other. The sender and receiver have to agree on a key before they can communicate securely.}} 

$ Types of Cryptography
    `Asymmetric Key                {{Uses one key for encryption and another for decryption. Also called Public Key Cryptography.}} 
    `Hash Functions                {{Uses a mathematical transformation to irreversibly encrypt information.}} 
    `Symmetric Key                 {{Uses a single key for both encryption and decryption. Also called Secret Key Cryptography.}} 

$ Asymmetric Encryption Algorithms
    `RSA                           {{The best known public key algorithm, named after its inventors: Rivest, Shamir and Adleman. RSA uses public and private keys that are functions of a pair of large prime numbers. The algorithm is best known for its application in PGP. It is patented in the USA only.}} 
    `Diffie - Hellman              {{Diffie-Hellman is the first public key encryption algorithm, invented in 1976, using discrete logarithms in a finite field. Allows two users to exchange a secret key over an insecure medium without any prior secrets.}} 
    `Digital Signature Algorithm   {{Digital Signature Algorithm (DSA) is a United States Federal Government standard or FIPS for digital signatures. It was proposed by the National Institute of Standards and Technology (NIST) in August 1991 for use in their Digital Signature Algorithm.}} 
    `ElGamal                       {{The ElGamal is a public key cipher - an asymmetric key encryption algorithm for public-key cryptography which is based on the Diffie-Hellman key agreement. ElGamal is the predecessor of DSA.}} 
    `ECDSA                         {{Elliptic Curve DSA (ECDSA) is a variant of the Digital Signature Algorithm (DSA) which operates on elliptic curve groups. As with Elliptic Curve Cryptography in general, the bit size of the public key believed to be needed for ECDSA is about twice the size of the security level, in bits.}} 
    `XTR                           {{XTR is an encryption algorithm for public-key encryption. XTR is a novel method that makes use of traces to represent and calculate powers of elements of a subgroup of a finite field. It is based on the primitive underlying the very first public key cryptosystem, the Diffie-Hellman key agreement protocol.}} 
    `ECC                           {{Elliptic curve cryptography (ECC) is an approach to public-key cryptography based on the algebraic structure of elliptic curves over finite fields. ECC requires smaller keys compared to non-ECC cryptography (based on plain Galois fields) to provide equivalent security}} 

$ Hashing Algorithms
    `Message Digest Service Algorithm (MD5)
>                                  {{The message digest family of encryption algorithms provides encryption of 128-bits in strength and is designed to be fast and simple. Current standards are MD2, MD4 and MD5.}} 
    `Secure Hash Algorithm         {{SHA is used extensively by the US government and was developed by the National Security Agency (NSA). Four versions of SHA have so far been developed - SHA-0, SHA-1, SHA-2 and SHA-3. SHA-1 provides 160-bit hashing. SHA-1 is more secure than MD5 but involves a slower encryption process. SHA-2 also known as SHA-256 and SHA-512. SHA-256 uses 32-bit words where SHA-512 uses 64-bit words. SHA-3 supports the same hash lengths as SHA-2.}} 

$ Symmetric Encryption Algorithms
    `AES (Rijndael)                {{AES stands for Advanced Encryption Standard. AES is a symmetric key encryption technique which will replace the commonly used Data Encryption Standard (DES). It was the result of a worldwide call for submissions of encryption algorithms issued by the US Government's National Institute of Standards and Technology (NIST) in 1997 and completed in 2000.}} 
    `Blowfish                      {{Blowfish is a symmetric encryption algorithm designed in 1993 by Bruce Schneier as an alternative to existing encryption algorithms.}} 
    `CAST5                         {{CAST stands for Carlisle Adams and Stafford Tavares, the inventors of CAST. CAST is a popular 64-bit block cipher which belongs to the class of encryption algorithms known as Feistel ciphers.}} 
    `DES                           {{Digital Encryption Standard. A symmetric block cipher using a 56-bit key which was originally developed by the US National Institute of Standards and Technology (NIST) in 1977 as a standard encryption algorithm. In 1999, the Electronic Frontier Foundation (USA) developed a machine to demonstrate that DES could be broken in a few hours with a brute-force attack. Encryption using single DES is generally no longer considered to be secure.}} 
    `GOST 28147-89                 {{The GOST block cipher, defined in the standard GOST 28147-89, is a Soviet and Russian government standard symmetric key block cipher developed in the 1970s. Also based on this block cipher is the GOST hash function.The standard had been marked Top Secret and then downgraded to Secret in 1990. Shortly after the dissolution of the USSR, it was declassified and it was released to the public in 1994. GOST was a Soviet alternative to the United States standard algorithm, DES.}} 
    `IDEA                          {{International Data Encryption Algorithm. It was introduced in 1992 as a potential alternative to DES and is regarded as very secure. It is a block cipher using a symmetric algorithm based on a 128 bit key. IDEA is the data encryption algorithm used in PGP.}} 
    `RC2                           {{RC2 is a variable-key-length cipher. It was invented by Ron Rivest for RSA Data Security, Inc. Its details have not been published.}} 
    `RC4                           {{RC4 was developed by Ron Rivest in 1987. It is a variable-key-size stream cipher. It is a cipher with a key size of up to 2048 bits (256 bytes). RC4 is not regarded as a secure algorithm anymore.}} 
    `RC6                           {{RC6 is a symmetric key block cipher derived from RC5. It was designed by Ron Rivest, Matt Robshaw, Ray Sidney, and Yiqun Lisa Yin to meet the requirements of the Advanced Encryption Standard (AES) competition.}} 
    `Serpent                       {{Serpent is a very fast and reasonably secure block cipher developed by Ross Anderson, Eli Biham and Lars Knudsen.}} 
    `Triple DES                    {{A method of vastly increasing the security of DES by encrypting 3 times with different keys. Each triple encryption encrypts one block of 64 bits of data.}} 
    `Twofish                       {{Twofish is a symmetric block cipher. Twofish has a block size of 128 bits and accepts keys of any length up to 256 bits. Twofish has key dependent S-boxes like Blowfish. Twofish encryption algorithm was designed by Bruce Schneier, John Kelsey, Chris Hall, Niels Ferguson, David Wagner and Doug Whiting and was one of the five finalist of the Advanced Encryption Standard contest.}} 

