# HDFS Shell Commands

> Source: http://hadoop.apache.org/docs/r2.7.1/hadoop-project-dist/hadoop-common/FileSystemShell.html

$ Commands
    `hdfs dfs -ls /user/abc        {{List contents of a directory.}} 
    `hdfs dfs -put file.txt /user/abc
>                                  {{Upload file from local file system.}} 
    `hdfs dfs -cat /user/abc/file.txt
>                                  {{Read contents of a file on HDFS.}} 
    `hdfs dfs -chmod 700 /user/abc/file.txt
>                                  {{Change file permission.}} 
    `hdfs dfs -setrep -w <N> /user/adam/songs.txt
>                                  {{Set replication factor to N.}} 
    `hdfs dfs -du -h /user/abc/file.txt
>                                  {{Check size of a file}} 
    `hdfs dfs -mv file.txt dir/    {{Move file to subdirectory dir}} 
    `hdfs dfs -rm file.txt         {{Delete file from HDFS.}} 

