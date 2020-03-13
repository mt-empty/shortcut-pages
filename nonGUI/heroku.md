# Heroku

> Source: https://devcenter.heroku.com/categories/command-line

> Aliases: heroku-cli, heroku-toolbelt, heroku-command-line

$ Basics
    `heroku --version              {{Check Command-line Tool Version}} 
    `heroku update                 {{Update Command-line Tool}} 
    `which heroku                  {{Find where executable is located}} 
    `heroku help                   {{Help}} 

$ Get Started
    `heroku login                  {{Login to Heroku}} 
    `heroku create appname         {{Create App}} 
    `heroku apps:rename newappname {{Rename App}} 
    `git push heroku master        {{Deploy App}} 
    `heroku open                   {{Open App in Web Browser}} 

$ Useful Info About Your App
    `heroku info                   {{Basic App Info}} 
    `heroku config                 {{View App Config}} 
    `heroku ps                     {{Show State of App}} 
    `heroku logs                   {{Show App Logs}} 

$ Manage SSH Keys
    `heroku keys:add               {{Add Keys}} 
    `heroku keys:remove keyname    {{Remove Keys}} 
    `heroku keys                   {{List all Keys}} 

