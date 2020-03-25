# WP-CLI

> Source: http://wp-cli.org/

$ Installing
    `curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar
>                                  {{Downloads wp-cli.phar.}} 
    `chmod +x wp-cli.phar          {{Changes file access permissions to executable.}} 
    `sudo mv wp-cli.phar /usr/local/bin/wp
>                                  {{Moves wp-cli.phar to PATH.}} 
    `wp --info                     {{Verify that wp-cli has been successfully installed.}} 

$ Core Commands
    `wp core download              {{Download core WordPress files.}} 
    `wp core install               {{Create the WordPress tables in the database.}} 
    `wp core check-update          {{Check for update via Version Check API.}} 
    `wp core update                {{Update WordPress.}} 

$ Plugin Commands
    `wp plugin list                {{List all currently installed plugins}} 
    `wp plugin update --all        {{Update all plugins.}} 
    `wp plugin install NAME        {{Installs plugin from wordpress.org. Replace NAME with intended plugin name.}} 
    `wp plugin activate NAME       {{Activates plugin. Replace NAME with intended plugin name.}} 

$ Theme Commands
    `wp theme list                 {{List all currently installed themes}} 
    `wp theme update --all         {{Update all themes.}} 
    `wp theme install NAME         {{Installs theme from wordpress.org. Replace NAME with intended theme name.}} 
    `wp theme activate NAME        {{Activates theme. Replace NAME with intended theme name.}} 
    `wp theme status               {{Shows the status of one or all themes}} 

