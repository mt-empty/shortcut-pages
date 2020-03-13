# GNU Privacy Guard

> Source: https://www.gnupg.org/documentation/manpage.en.html

> Aliases: gnu-privacy-guard, gpg

$ Encrypting / Decrypting
    `gpg -e -r [recipient key] [file]
>                                  {{Encrypt a file to a recipient}} 
    `gpg -se -r [recipient key] [file]
>                                  {{Encrypt and sign a file to a recipient}} 
    `gpg -c [file]                 {{Encrypt a file with a password}} 
    `gpg -d [file]                 {{Decrypt a file}} 

$ Signing
    `gpg --detach-sign -a [file]   {{Sign a file (detached ASCII signature)}} 
    `gpg --clearsign [file]        {{Clear-sign a file}} 
    `gpg -s -a [file]              {{Sign a file}} 
    `gpg -v [file]                 {{Verify a signature}} 
    `gpg --sign-key [key]          {{Sign a key}} 

$ Key Management
    `gpg -o [file.asc] --export -a [key]
>                                  {{Export a public key to an ascii-armoured file}} 
    `gpg -o [file.asc] --export-secret-key -a [key]
>                                  {{Export a secret key to an ascii-armoured file}} 
    `gpg --import [file]           {{Import key(s) into the local keychain}} 
    `gpg --delete-keys [key(s)]    {{Delete key(s) from the local keychain}} 
    `gpg --list [optional search]  {{List keys in local keychain}} 
    `gpg --fingerprint [key(s)]    {{List key fingerprint(s)}} 
    `gpg --gen-key                 {{Generate a new key pair}} 
    `gpg --gen-revoke [key]        {{Generate a revocation certificate for a key}} 
    `gpg --edit [key]              {{Sign or edit a key}} 

$ Key Server
    `gpg --send-keys [key(s)]      {{Send a key to a key server}} 
    `gpg --recv-keys [key(s)]      {{Retrieve a key from a key server}} 
    `gpg --search-keys [search]    {{Search for keys on a key server}} 
    `gpg --refresh-keys            {{Refresh all keys in local keyring}} 

