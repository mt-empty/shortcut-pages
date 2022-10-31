# Mainframe

> Source: http://www.mainframes.com/Commands.html

> Aliases: main-frame, mainframe-cli

$ Job Entry Subsystem 2 (JES2)
    `$DSPL,JOBS=5                  {{Display all jobs using 5% or more of the spool}} 
    `$A A                          {{Release all jobs}} 
    `$ACTIVATE                     {{Activate new functions at the current release level of JES2}} 
    `$ADD APPL                     {{Dynamically define a VTAM application to JES2 at the specified JES2 node.}} 
    `$ADD DESTID                   {{Dynamically define a symbolic name for a JES2 route code.}} 
    `$ADD FSS                      {{Dynamically define a functional subsystem (FSS) to JES2}} 
    `$ADD LINE (nnnn)              {{Dynamically add a line}} 
    `$ADD LOGON (nn)               {{Creates a new LOGON pseudo-device, which defines JES2 as an application program to VTAM}} 
    `$ADD PRT                      {{Dynamically add a local printer}} 
    `$ADD REDIRECT                 {{Specify redirection for commands entered at the entry console}} 
    `$ADD RMT (nnnn)               {{Add one or more RJE workstations}} 
    `$C A                          {{Cancel the processing of all or specified automatic command entries and delete those entries}} 
    `$C A 3                        {{Cancel auto job id=3}} 
    `$C job                        {{Immediately cancel jobs or TSU sessions currently executing on any member of the MAS and, if desired, provide a storage dump.}} 
    `$D A,L                        {{Display information about currently active jobs}} 
    `$D BUFDEF                     {{Display the current values of all parameters defined on the BUFDEF initialization statement or command}} 
    `$D SPOOL                      {{Display the Status of Spool Volumes}} 
    `$D SPOOLDEF                   {{Display the JES2 spooling environment characteristics}} 
    `$TA,I=900,T=11.15,'$VS,[]D A,L[]'
>                                  {{Display active list every 15 minutes}} 
    `$TA,I=86400,T=04.15,'$VS,''S TMSDAILY[]'
>                                  {{Start job TMSDAILY every 24 hours starting at 0415 hours}} 
    `$TA,I=86400,T=01.15,'$VS,[]S BACKUP[]'
>                                  {{Start job BACKUP every 24 hours starting at 0115 hours}} 
    `$vs, 'v (234,235,236),offline','d a'
>                                  {{Varys offline devices 234,235,236 and displays all at JES2 startup}} 

$ Multiple Virtual Storage (MVS)
    `DS QT,483,1                   {{Display Status information on device}} 
    `D IOS,MIH,DEV=484             {{Display IOS control unit group information}} 
    `D ASM                         {{Display Page Data Set Information}} 
    `D IPLINFO                     {{Display IPL information}} 
    `D LOGREC                      {{Display the Logrec Recording Medium}} 
    `D M                           {{Display all the resources}} 
    `D PARMLIB                     {{Display PARMLIB data sets and volumes Information}} 
    `D PROD,REGISTERED             {{Display Registered Products}} 
    `D PROG,LNKLST                 {{Display LNKLST Information}} 
    `D PROG,APF                    {{Display Entries in the List of APF-Authorized Libraries}} 
    `D SMF                         {{Display System Management Facilities}} 
    `D SMF,O                       {{Display SMF Data}} 
    `D SMS,STORGRP (storgrp)       {{Display storage group status using the DISPLAY SMS command}} 
    `D SYMBOLS                     {{Display assigned name of the systems}} 
    `D U,IPLVOL                    {{Display Device Status and Allocation}} 
    `F TSO,USERMAX=1               {{Set TSO user to max of one user}} 
    `D XCF,COUPLE                  {{Display info on the couple data sets, which used at IPL, names, DASD, etc}} 
    `VARY CN(*),ACTIVATE           {{Activate the console you are on}} 
    `D C,HCONLY                    {{Display hard copy consoles}} 

$ Data Facility System Managed Storage (DFSMS)
    `F CATALOG,REPORT,CACHE        {{Reports caching statistics for both caching approaches of catalog management to cache catalog information}} 
    `F CATALOG,REPORT,PERFORMANCE  {{This new modify catalog command reports counts for various events and the average elapsed time for these events}} 
    `F CATALOG,LIST (id|yyyyyy) | LISTJ (jobname)
>                                  {{Detail information and used in real-time diagnosis when problems arise}} 

$ Time Sharing Option/Extensions (TSO/E)
    `SYNC                          {{Command to initialize SYS1.BRODCAST data set and to synchronize it with the RACF data set, SYS1.UADS, or both}} 
    `SHOWMVS                       {{List all kinds of info on your system (by using ISPF).}} 

$ Virtual Telecommunications Access Method (VTAM)
    `D NET,MAJNODES                {{Display the all active nodes in the domain}} 
    `Z NET                         {{Take down VTAM normally but not allowing LU sessions to end normally}} 
    `Z NET,CANCEL                  {{Take down VTAM when the above 2 options fail. Cancel will kill everything whether they are in Pending states}} 
    `D NET,BFRUSE,BUFFER=SHORT     {{Display information about VTAM buffer used}} 

$ Virtual Lookaside Facility (VLF)
    `F CATALOG,REPORT,CACHE        {{Determining Catalogs in VLF}} 
    `F CATALOG,NOVLF (your.catname)
>                                  {{Removing Catalogs from VLF}} 

$ System Display and Search Facility (SDSF)
    `XDC                           {{Typing this command on the line of the job you want to save as a data set. It displays a self explaining menu. Your job is NOT remove for the output queue}} 

