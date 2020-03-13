# Drush

> Source: http://drushcommands.com

$ Other commands
    `make                          {{Turns a makefile into a working Drupal codebase.}} 
    `make-generate                 {{Generate a makefile from the current Drupal site.}} 

$ Runserver commands
    `runserver                     {{Runs a lightweight built in http server for development.}} 

$ Field commands
    `field-clone                   {{Clone a field and all its instances.}} 
    `field-create                  {{Create fields and instances. Returns urls for field editing.}} 
    `field-delete                  {{Delete a field and its instances.}} 
    `field-info                    {{View information about fields, field_types, and widgets.}} 
    `field-update                  {{Return URL for field editing web page.}} 

$ Core drush commands
    `archive-dump                  {{Backup your code, files, and database into a single file.}} 
    `archive-restore               {{Expand a site archive into a Drupal web site.}} 
    `cache-clear                   {{Clear a specific cache, or all drupal caches.}} 
    `cache-get                     {{Fetch a cached object and display it.}} 
    `cache-set                     {{Cache an object expressed in JSON or var_export() format.}} 
    `cache-rebuild                 {{Rebuild a Drupal 8 site and clear all its caches.}} 
    `core-config                   {{Edit drushrc, site alias, and Drupal settings.php files.}} 
    `core-cron                     {{Run all cron hooks in all active modules for specified site.}} 
    `core-execute                  {{Execute a shell command. Usually used with a site alias.}} 
    `core-quick-drupal             {{Download, install, serve and login to Drupal with minimal configuration and dependencies.}} 
    `core-requirements             {{Provides information about things that may be wrong in your Drupal installation, if any.}} 
    `core-rsync                    {{Rsync the Drupal tree to/from another server using ssh.}} 
    `core-status                   {{Provides a birds-eye view of the current Drupal installation, if any.}} 
    `core-topic                    {{Read detailed documentation on a given topic.}} 
    `drupal-directory              {{Return path to a given module/theme directory.}} 
    `help                          {{Print this help message. See `drush help help` for more options.}} 
    `image-flush                   {{Flush all derived images for a given style.}} 

$ SQL commands
    `sql-cli                       {{Open a SQL command-line interface using Drupal's credentials.}} 
    `sql-connect                   {{A string for connecting to the DB.}} 
    `sql-create                    {{Create a database.}} 
    `sql-drop                      {{Drop all tables in a given database.}} 
    `sql-dump                      {{Exports the Drupal DB as SQL using mysqldump or equivalent.}} 
    `sql-query                     {{Execute a query against the site database.}} 
    `sql-sync                      {{Copy and import source database to target database. Transfers via rsync.}} 

$ User commands
    `user-add-role                 {{Add a role to the specified user accounts.}} 
    `user-block                    {{Block the specified user(s).}} 
    `user-cancel                   {{Cancel a user account with the specified name.}} 
    `user-create                   {{Create a user account with the specified name.}} 
    `user-information              {{Print information about the specified user(s).}} 
    `user-login                    {{Display a one time login link for the given user account (defaults to uid 1).}} 
    `user-password                 {{(Re)Set the password for the user account with the specified name.}} 
    `user-remove-role              {{Remove a role from the specified user accounts.}} 
    `user-unblock                  {{Unblock the specified user(s).}} 

$ Project manager commands
    `pm-disable                    {{Disable one or more extensions (modules or themes).}} 
    `pm-download                   {{Download projects from drupal.org or other sources.}} 
    `pm-enable                     {{Enable one or more extensions (modules or themes).}} 
    `pm-info                       {{Show detailed info for one or more extensions (modules or themes).}} 
    `pm-list                       {{Show a list of available extensions (modules and themes).}} 
    `pm-refresh                    {{Refresh update status information.}} 
    `pm-releasenotes               {{Print release notes for given projects.}} 
    `pm-releases                   {{Print release information for given projects.}} 
    `pm-uninstall                  {{Uninstall one or more modules.}} 
    `pm-update                     {{Update Drupal core and contrib projects and apply any pending database updates (Same as pm-updatecode + updatedb).}} 
    `pm-updatecode                 {{Update Drupal core and contrib projects to latest recommended releases.}} 

$ Config commands
    `config-edit                   {{Open a config file in a text editor}} 
    `config-export                 {{Export configuration to a directory}} 
    `config-get                    {{Display a config value, or a whole configuration object}} 
    `config-list                   {{List config names by prefix}} 
    `config-pull                   {{Export and transfer config from one environment to another}} 
    `config-set                    {{Set config value directly}} 
    `config-import                 {{Import config from a config directory}} 

