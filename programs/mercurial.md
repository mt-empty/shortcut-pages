# Mercurial(hg)

> Source: http://www.cheatography.com/codeshane/cheat-sheets/mercurial-hg/

> Aliases: hg

$ Create Local Repositories
    `hg init [project-name]        {{Creates a ./.hg/ subfolder and repository}} 
    `hg add                        {{Begin tracking all files}} 
    `hg commit -m "[descriptive message]"
>                                  {{Save files and Commit message to Repo}} 

$ File Operations
    `hg add [file]                 {{Begin tracking changes}} 
    `hg addremove                  {{Track new but forget missing files}} 
    `hg forget [file]              {{Stop tracking a file}} 
    `hg remove [file]              {{Stop tracking and delete a file}} 
    `hg copy [file] [target]       {{Copy a file}} 
    `hg move [file] [target]       {{Move a file}} 

$ Work Status
    `hg diff                       {{List tracked file changes}} 
    `hg diff [file]                {{List changes to a file}} 
    `hg status                     {{List status of files}} 

$ Work Directory Updates
    `hg update [tip]               {{Update Work to match Tip}} 
    `hg update -r [REV]            {{Update Work to specified Revision}} 
    `hg revert                     {{Undo all uncommitted changes}} 

$ Repository History
    `hg log [file/dir]             {{History of changesets}} 
    `hg annotate [file]            {{Who changed what, when}} 
    `hg paths                      {{List known remote repos}} 
    `hg heads                      {{List heads}} 
    `hg diff -rREV -rREV           {{Shows differences between REVs}} 

$ Remote Repositories
    `hg clone [url] [local dir name]
>                                  {{Cloning a Remote Repository for local work}} 
    `hg incoming [Remote]          {{List changesets available from Remote}} 
    `hg pull                       {{Pull all new changesets into Local}} 
    `hg pull -r [Remote]           {{Pull specified changesets into Local}} 
    `-u                            {{Also update working directory}} 
    `hg push [Remote]              {{Push changesets to Remote}} 
    `hg share                      {{Sync history with parent and siblings}} 

$ Merge Operations
    `hg pull --force               {{Forcefully pull changes overwriting local changes}} 
    `hg merge                      {{Merge changes}} 
    `hg commit                     {{Commit changes}} 

$ Command Options
    `-r [REV]                      {{Specify a Rev number (default parent)}} 
    `-y                            {{Don't prompt; pick first option}} 
    `-q                            {{Quiet (suppress output)}} 
    `-v                            {{Verbose (additional detail)}} 
    `-f                            {{Force (override reasonable warnings)}} 

$ Help
    `hg                            {{See a basic command list}} 
    `hg help                       {{Full command list}} 
    `hg help [command]             {{Detailed help reference}} 

$ Terminology
    `Repository                    {{Repo. Collection of Revisions}} 
    `Revision                      {{Rev. Committed changeset, by REV number.}} 
    `Changeset                     {{Set of Work changes saved as Diffs}} 
    `Diff                          {{Changes between files}} 
    `Tag                           {{Name for a specific Rev}} 
    `Parent                        {{Immediate ancestor of Rev or Work}} 
    `Branch                        {{Child of Rev}} 
    `Merge                         {{Rev with two parents}} 
    `Head                          {{Latest Rev in Branch}} 
    `Tip                           {{Latest Rev in ANY Branch}} 
    `Patch                         {{All Diffs between two Revs}} 
    `Bundle                        {{Patch with permissions and rename support}} 

