# Perforce

> Source: https://www.perforce.com

> Aliases: perforce-command-line-client, p4, p4-command-line

$ Develop
    `p4 add                        {{Open a new file to add it to the depot}} 
    `p4 change                     {{Create or edit a changelist description}} 
    `p4 changes                    {{Display list of pending and submitted changelists}} 
    `p4 client                     {{Create or edit a client specification and its view}} 
    `p4 clients                    {{Display a list of known clients}} 
    `p4 clean                      {{Delete or refresh local files to match depot state}} 
    `p4 diff                       {{Display diff of client file with depot file}} 
    `p4 edit                       {{Open an existing file for edit}} 
    `p4 flush                      {{Update a client workspace's have list without copying any files}} 
    `p4 have                       {{List revisions last synced}} 
    `p4 lock                       {{Lock an opened file against changelist submission}} 
    `p4 move                       {{Move file from one location to another}} 
    `p4 opened                     {{Display list of files opened for pending changelist}} 
    `p4 print                      {{Print contents of a depot file to standard output}} 
    `p4 reconcile                  {{Opens files for edit, add or delete}} 
    `p4 rename                     {{Rename a file}} 
    `p4 reopen                     {{Change the type or changelist number of an opened file}} 
    `p4 resolve                    {{Merge open files with other revisions or files}} 
    `p4 resolved                   {{Show files that have been merged but not submitted}} 
    `p4 revert                     {{Discard changes from an opened file}} 
    `p4 shelve                     {{Store files from a pending changelist into the depot}} 
    `p4 status                     {{Reports which files need to be added, opened or deleted}} 
    `p4 submit                     {{Submit open files to the depot}} 
    `p4 sync                       {{Synchronize the client with its view of the depot}} 
    `p4 unlock                     {{Release a locked file but leave it open}} 
    `p4 unshelve                   {{Restore shelved files from a pending changelist into a workspace}} 
    `p4 update                     {{Update workspace without clobbering files changed since last sync}} 

$ Local Security
    `p4 tickets                    {{Display list of sessions tickets for this user}} 
    `p4 trust                      {{Establish trust of an SSL connection to a Perforce service}} 

$ Server Security
    `p4 login                      {{Login to Perforce by obtaining session ticket}} 
    `p4 logout                     {{Logout of Perforce by removing or invalidating ticket}} 
    `p4 passwd                     {{Set user password on server}} 
    `p4 set                        {{Set variables in the registry (Windows only)}} 

$ Investigate
    `p4 annotate                   {{Print file lines along with their revisions}} 
    `p4 cstat                      {{List the changes not synchronized in the current client}} 
    `p4 depots                     {{Display list of depots}} 
    `p4 describe                   {{Display a changelist description}} 
    `p4 diff2                      {{Display diff of two depot files}} 
    `p4 dirs                       {{List subdirectories of a give depot directory}} 
    `p4 filelog                    {{List revision history of files}} 
    `p4 files                      {{List files in the depot}} 
    `p4 fstat                      {{Dump file info}} 
    `p4 grep                       {{Print lines in files(or revisions of files) that match a pattern}} 
    `p4 help                       {{Print help message}} 
    `p4 info                       {{Print out client and server information}} 
    `p4 integrated                 {{Show integrations that have been submitted}} 
    `p4 interchanges               {{Lists changes not yet integrated from source to target}} 
    `p4 istat                      {{Show the stream's integration status}} 
    `p4 sizes                      {{Display size information for files in the depot}} 
    `p4 where                      {{Show how file names map through the client view}} 

$ Branching and Merging
    `p4 branch                     {{Create or edit a branch specification}} 
    `p4 branches                   {{Display list of branches}} 
    `p4 copy                       {{Make target identical to source by branching, replacing or deleting}} 
    `p4 integrate                  {{Schedule integration from one file to another}} 
    `p4 merge                      {{Merge changes from one set of files into another}} 
    `p4 populate                   {{Branch files to target without requiring a workspace}} 
    `p4 prune                      {{Remove unmodified branched files from a stream}} 
    `p4 stream                     {{Create or edit a stream specification}} 
    `p4 streams                    {{Display a list of known streams}} 
    `p4 switch                     {{Switch to and/or create a new stream/branch (DVCS)}} 

$ Jobs
    `p4 fix                        {{Mark jobs as being fixed by named changelists}} 
    `p4 fixes                      {{List what changelists fix what job}} 
    `p4 job                        {{Create or edit a job (defect) specification}} 
    `p4 jobs                       {{Display a list of jobs}} 

$ Labels
    `p4 label                      {{Create or edit a label specification and its view}} 
    `p4 labels                     {{Display a list of labels}} 
    `p4 labelsync                  {{Synchronize label with current client contents}} 
    `p4 tag                        {{Tag files with a label}} 

