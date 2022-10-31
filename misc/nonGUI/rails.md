# Rails

> Source: http://api.rubyonrails.org/

> Aliases: rails-4, ruby-on-rails, rake, bundle

$ Rails Commands
    `rails new name                {{Creates a new Ruby on Rails application with the given name here.}} 
    `rails generate scaffold name attribute:type
>                                  {{The scaffold command magically generates all the common things needed for a new resource for you! This includes controllers, models and views.}} 
    `rails generate controller name
>                                  {{Creates a new controller and its respective views with the given name here.}} 
    `rails generate model name attribute:type
>                                  {{Creates a new model with the given name here and its respective migration with attributes mentioned.}} 
    `rails server                  {{Launches a small web server named WEBrick which comes bundled with Ruby on port 3000}} 
    `rails console                 {{The console command lets you interact with your Rails application from the command line.}} 

$ Rake Commands
    `rake db:create                {{Creates the database for the current environment}} 
    `rake db:create:all            {{Creates the databases for all environments}} 
    `rake db:drop                  {{Drops the database for the current environment}} 
    `rake db:drop:all              {{Drops the databases for all environments}} 
    `rake db:migrate               {{Runs migrations for the current environment that have not run yet}} 
    `rake db:rollback              {{Rolls back the last migration}} 
    `rake db:seed                  {{(only) runs the db/seed.rb file}} 
    `rake db:migrate:redo          {{Runs (db:migrate:down db:migrate:up) or (db:rollback db:migrate) depending on the specified migration}} 
    `rake db:migrate:reset         {{Runs db:drop db:create db:migrate}} 
    `rake tmp:clear                {{Clears session, cache, and socket files}} 
    `rake assets:precompile        {{Compile all the assets named in config.assets.precompile}} 

$ Bundle Commands
    `bundle install                {{Install the current environment's gems to the system}} 
    `bundle exec                   {{Run the command in context of the bundle}} 
    `bundle clean                  {{Cleans up unused gems in your bundler directory}} 
    `bundle config                 {{Retrieve or set a configuration value}} 
    `bundle console                {{Opens an IRB session with the bundle pre-loaded}} 
    `bundle init                   {{Generates a Gemfile into the current working directory}} 
    `bundle update                 {{Update the current environment}} 
    `bundle show                   {{Shows all gems that are part of the bundle, or the path to a given gem}} 

