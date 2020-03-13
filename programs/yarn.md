# Yarn

> Source: https://yarnpkg.com/en/docs/cli/

> Aliases: 

$ Working with a project
    `yarn init                     {{Initializes a new project and create the package.json file.}} 
    `yarn link                     {{Creates a globally-installed symbolic link from the current project's folder.}} 
    `yarn unlink                   {{Removes the symlink.}} 
    `yarn publish                  {{Publish a package to the npm registry.}} 
    `yarn owner ls <package>       {{Lists all owners of <package>.}} 
    `yarn owner add <user> <package>
>                                  {{Adds the <user> as an owner of <package>. You must be an owner of <package> in order to run this command.}} 
    `yarn owner rm <user> <package>
>                                  {{Removes the <user> from the list of owners of <package>. You must be an owner of <package> in order to run this command.}} 
    `yarn pack                     {{Creates a compressed gzip archive of the project's dependencies.}} 
    `yarn version                  {{Starts an interactive session to update the project version.}} 

$ Working with project dependencies
    `yarn ls                       {{Lists all installed packages.}} 
    `yarn add <package>            {{Install the <package> from the npm registry and save it to the project's package.json dependencies.}} 
    `yarn add <package> --dev      {{Install the <package> from the npm registry and save it to the project's package.json devDependencies.}} 
    `yarn remove <package>         {{Removes the <package> from the node_module folder as well as the project's package.json.}} 
    `yarn upgrade                  {{Upgrades all the dependecies in the project's package.json.}} 
    `yarn outdated                 {{Check the npm registry for any installed packages that are outdated.}} 
    `yarn install                  {{Creates a yarn.lock in the project's folder, describing all the project's dependencies.}} 
    `yarn licenses ls              {{Lists all the licenses for all your dependecies listed in package.json.}} 
    `yarn licenses generate-disclaimer
>                                  {{Automatically generate the license disclaimer based on all the licenses for all your dependencies listed in package.json.}} 
    `yarn why <package>            {{Identify why the <package> is installed.}} 
    `yarn check                    {{Verifies that the versions of the package dependencies in the project's package.json match those in yarn's lock file.}} 
    `yarn clean                    {{Free up space by removing unnecessary files and folders from node_modules. It generates a .yarnclean file.}} 
    `yarn info <package>           {{Retrieves information about <package> in a tree format.}} 

$ Working with project tasks
    `yarn start                    {{Runs the start script if provided in the project's package.json.}} 
    `yarn test                     {{Runs the test script if provided in the project's package.json.}} 
    `yarn run <task>               {{Runs the <task> script if provided in the project's package.json.}} 

$ Global tasks
    `yarn bin                      {{Print the folder where yarn will install executable files for your package.}} 
    `yarn config set <key> <value> {{Sets the config <key> to <value>.}} 
    `yarn config get <key>         {{Retrieves the value of <key> from config.}} 
    `yarn config delete <key>      {{Removes the <key> from config.}} 
    `yarn config list              {{Displays the current config.}} 
    `yarn global add <package>     {{Install the <package> from the npm registry globally instead of the project's package.json file.}} 
    `yarn cache ls                 {{Show the data in the yarn cache.}} 
    `yarn cache clean              {{Delete the data from the cache folder.}} 
    `yarn login                    {{Login to the npm registry.}} 
    `yarn logout                   {{Logout of the npm registry.}} 
    `yarn self-update              {{Updates yarn to the latest version.}} 

$ NPM equivalents
    `yarn init/link/publish/run/outdated/cache clean/login/start/test
>                                  {{These are all exact equivalents of init/link/publish/run/outdated/cache clean/login/start/test}} 
    `yarn add <package>            {{npm install <package> --save}} 
    `yarn remove <package>         {{npm unsinstall <package> --save}} 
    `yarn add <package> --dev      {{npm install <package> --save-dev}} 
    `yarn upgrade                  {{npm update --save}} 
    `yarn global add <package>     {{npm install <package> --global}} 

