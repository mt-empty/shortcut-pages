# Git flow

> Source: https://danielkummer.github.io/git-flow-cheatsheet

> Aliases: gf, git-flow

$ Initialize
    `git flow init                 {{Initialize an existing git repository to use git flow.}} 

$ Working with features
    `git flow feature start <feature>
>                                  {{Start developing a new feature. It creates a new branch based on develop.}} 
    `git flow feature finish <feature>
>                                  {{Finish development of a feature, which will merge it into develop, remove the feature branch and switch to develop.}} 
    `git flow feature publish <feature>
>                                  {{Publish a feature to the remote server so others can work on it too.}} 
    `git flow feature pull <remote> <feature>
>                                  {{Get a published feature on your local machine.}} 
    `git flow feature track <feature>
>                                  {{Track a feature on origin.}} 

$ Doing a release
    `git flow release start <version>
>                                  {{Start a release branch. It creates a new branch based on develop.}} 
    `git flow release publish <version>
>                                  {{Publish a release to the remote server so others can see it.}} 
    `git flow release finish <version>
>                                  {{Finish development of a release, which will merge it back into master, tag master with its <version>, merge it into develop and remove the release branch.}} 

$ Making a hotfix
    `git flow hotfix start <version>
>                                  {{Start a new hotfix branch. It creates a new branch from master.}} 
    `git flow hotfix finish <version>
>                                  {{Finish a hotfix, which merges it back into develop and into master. Master is also tagged with the hotfix <version> number.}} 

$ Working with support branches [EXPERIMENTAL]
    `git flow support start <support> <tag>
>                                  {{Start a support branch. It creates a branch called <support> based on <tag>. The <tag> must be a commit on the master branch.}} 

