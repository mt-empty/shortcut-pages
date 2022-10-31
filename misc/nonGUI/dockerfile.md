# Dockerfile

> Source: https://docs.docker.com/engine/reference/builder/

$ Format
    `INSTRUCTION arguments         {{The instruction is not case-sensitive, however convention is for them to be UPPERCASE}} 
    `# Comment                     {{Comments start with a #}} 

$ Main Instructions
    `FROM <image> FROM <image>:<tag> FROM <image>@<digest>
>                                  {{Sets the Base Image for subsequent instructions}} 
    `MAINTAINER <name>             {{Allows you to set the Author field of the generated images}} 
    `ENTRYPOINT ["executable", "param1", "param2"]
>                                  {{Allows you to configure a container that will run as an executable}} 
    `RUN <command>                 {{Execute any commands in a new layer on top of the current image and commit the results}} 
    `EXPOSE <port> [<port>...]     {{Informs Docker that the container listens on the specified network ports at runtime}} 
    `COPY <src>... <dest>          {{Copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest>}} 
    `COPY ["<src>",... "<dest>"]   {{Copies new files or directories from <src> and adds them to the filesystem of the container at the path <dest> and is required for paths containing whitespace}} 
    `VOLUME ["/data"]              {{Creates a mount point with the specified name and marks it as holding externally mounted volumes from native host or other containers}} 
    `WORKDIR /path/to/workdir      {{Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions}} 
    `ENV <key>=<value> ...         {{Sets the environment variable <key> to the value <value>}} 

$ Other Instructions
    `CMD ["executable","param1","param2"]
>                                  {{Provide defaults for an executing container}} 
    `LABEL <key>=<value> <key>=<value> ...
>                                  {{Adds metadata to an image. Is a key-value pair}} 
    `ADD <src>... <dest>           {{Copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the container at the path <dest>}} 
    `USER daemon                   {{Sets the user name or UID to use when running the image}} 
    `ARG <name>[=<default value>]  {{Defines a variable that users can pass at build-time to the builder}} 
    `ONBUILD [INSTRUCTION]         {{Adds to the image a trigger instruction to be executed at a later time, when the image is used as the base for another build}} 
    `STOPSIGNAL signal             {{Sets the system call signal that will be sent to the container to exit}} 

