# Apache Cordova

> Source: https://cordova.apache.org/docs/en/latest/guide/cli/index.html

> Aliases: cordova, phonegap

$ Create a Project
    `cordova create hello com.example.hello HelloWorld
>                                  {{Create a Cordova project}} 

$ Add a Platform
    `cordova platform add <platform name>
>                                  {{Add a platform for which you want to build your app}} 
    `cordova platform ls           {{To check your current set of platforms}} 
    `cordova platform              {{For a complete list of platforms}} 

$ Run your App
    `cordova run <platform name>   {{Run the project from a specific platform}} 

$ Build the App
    `cordova build                 {{Build the project for all platforms}} 
    `cordova build <platform name> {{You can optionally limit the scope of each build to specific platforms}} 

$ Test the App
    `cordova emulate <platform name>
>                                  {{Run a command such as the following to rebuild the app and view it within a specific platform's emulator}} 
    `cordova run android           {{Before running this command, you need to set up the device for testing, following procedures that vary for each platform.}} 

$ Add Plugins
    `cordova plugin search <name>  {{You can also use the CLI to launch the search page}} 
    `cordova plugin add <plugin name>
>                                  {{To add the <plugin name>, we will specify the npm package name for the <plugin name>}} 
    `cordova plugin ls             {{To view currently installed plugins. Each displays by its identifier}} 

$ Updating Cordova and Your Project
    `sudo npm update -g cordova    {{update it to the latest version}} 
    `cordova -v                    {{To see which version is currently running}} 
    `cordova platform update <platform name> --save
>                                  {{To update platform that you're targeting}} 

