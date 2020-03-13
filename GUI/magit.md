# Magit

> Source: http://daemianmack.com/magit-cheatsheet.html

$ Buffers
    `M-x, magit-status             {{Magit's status buffer}} 
    `$                             {{Magit-process buffer}} 
    `g                             {{Reload status buffer}} 

$ Section Visibility
    `TAB                           {{Toggle visibility of current section}} 
    `S-TAB                         {{Toggle visibility of current section and its children}} 
    `1,2,3,4                       {{Expand current section to the corresponding level of detail - 1, 2, 3 or 4}} 
    `M-1,2,3,4                     {{Expand all sections to the corresponding level of detail - 1, 2, 3 or 4}} 

$ Untracked Files
    `s                             {{Add untracked file to staging area}} 
    `i                             {{Add file to .gitignore}} 
    `C-u, i                        {{Prompt for file/directory to add to .gitignore}} 
    `I                             {{Add file to .git/info/exclude instead of .gitignore}} 

$ Staging and Committing
    `s                             {{Stage current hunk}} 
    `u                             {{Unstage current hunk}} 
    `S                             {{Stage all hunks}} 
    `U                             {{Unstage all hunks}} 
    `k                             {{Discard uncommitted changes}} 
    `c                             {{Prepare for commit}} 
    `C-c, C-c                      {{Execute commit}} 
    `C-c, C-a                      {{Make the next commit an amend}} 

$ History
    `l                             {{History}} 
    `L                             {{Verbose history}} 
    `C-u, l                        {{History segment}} 
    `RET                           {{Inspect commit}} 
    `a                             {{Stage current commit on your current branch}} 
    `A                             {{Commit current commit on your current branch}} 
    `C-w                           {{Copy sha1 of current commit into kill ring}} 
    `=                             {{Show differences between current and marked commits}} 
    `., .                          {{Mark current commit}} 
    `.                             {{Unmark current commit if marked}} 
    `C-u, ., .                     {{Unmark marked commit from anywhere}} 

$ Reflogs
    `h                             {{Browse reflog from HEAD}} 
    `H                             {{Browse reflog from chosen point}} 

$ Diffing
    `d                             {{Show changes between working tree and HEAD}} 
    `D                             {{Show changes between two arbitrary revisions}} 
    `a                             {{Apply current changes to working tree}} 
    `v                             {{Apply current changes to working tree in reverse}} 

$ Tagging
    `t                             {{Make lightweight tag}} 
    `T                             {{Prepare annotated tag}} 
    `C-c, C-c                      {{Commit annotated tag}} 

$ Resetting
    `x                             {{Reset your current head to chosen revision}} 
    `X                             {{Reset working tree and staging area to most recent committed state}} 

$ Stashing
    `z                             {{Create new stash}} 
    `Z                             {{Create new stash and maintain state}} 
    `RET                           {{View stash}} 
    `a                             {{Apply stash}} 
    `A                             {{Pop stash}} 
    `k                             {{Drop stash}} 

$ Branching
    `b                             {{Switch to different branch}} 
    `B                             {{Create and switch to new branch}} 

$ Wazzup
    `w                             {{Show summary of how other branches relate to current branch}} 
    `i                             {{Toggle ignore branch}} 
    `C-u, w                        {{Show all branches including ignored ones}} 

$ Merging
    `m                             {{Initiate manual merge}} 
    `M                             {{Initiate automatic merge}} 

$ Rebasing
    `R                             {{Initiate or continue a rebase}} 
    `E                             {{Initiate an interactive rebase}} 

$ Rewriting
    `r, s                          {{Start a rewrite}} 
    `v                             {{Revert a given commit}} 
    `r, t                          {{Remove bookkeeping information from buffer}} 
    `r, a                          {{Abort rewriting}} 
    `r, f                          {{Finish rewriting}} 
    `r, *                          {{Toggle the * mark on a pending commit}} 
    `r, ., .                       {{Toggle the . mark on a pending commit}} 

$ Pushing and Pulling
    `P                             {{git push}} 
    `C-u, P                        {{git push to specified remote repository}} 
    `C-u, C-u, P                   {{git push to specified remote as specified branch}} 
    `f                             {{git remote update}} 
    `F                             {{git pull}} 

$ Interfacing with Subversion
    `N, r                          {{git svn rebase}} 
    `N, c                          {{git svn dcommit}} 

