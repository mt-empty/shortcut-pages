# Youtube-dl

> Source: https://github.com/rg3/youtube-dl/blob/master/README.md#readme

> Aliases: youtube-dl

$ Network Options
    `--proxy URL                   {{Use the specified HTTP/HTTPS proxy. Pass in an empty string (--proxy ) for direct connection}} 
    `-4, --force-ipv4              {{ Make all connections via IPv4}} 
    `-6, --force-ipv6              {{ Make all connections via IPv6}} 
    `--source-address IP           {{Client-side IP address to bind to}} 

$ Video Selection
    `--playlist-start NUMBER       {{Playlist video to start at (default is 1)}} 
    `--playlist-end NUMBER         {{Playlist video to end at (default is last)}} 
    `--max-downloads NUMBER        {{Abort after downloading NUMBER files}} 
    `--include-ads                 {{Download advertisements as well}} 
    `--yes-playlist                {{Download the playlist, if the URL refers to a video and a playlist}} 

$ Download Options
    `-r, --rate-limit LIMIT        {{Maximum download rate in bytes per second}} 
    `-R, --retries RETRIES         {{Number of retries (default is 10), or infinite}} 
    `--buffer-size SIZE            {{Size of download buffer (e.g. 1024 or 16K)}} 
    `--external-downloader COMMAND {{Use the specified external downloader Currently supports}} 
    `--external-downloader-args ARGS
>                                  {{Give these arguments to the external downloader}} 

$ Filesystem Options
    `-a, --batch-file FILE         {{File containing URLs to download}} 
    `--id                          {{Use only video ID in file name}} 
    `--autonumber-size NUMBER      {{Specify the number of digits in %(autonumber)s when it is present in output filename template or --auto-number option is given}} 
    `-c, --continue                {{Force resume of partially downloaded files. By default, youtube-dl will resume downloads if possible.}} 
    `--no-continue                 {{Do not resume partially downloaded files}} 
    `--cookies FILE                {{File to read cookies from and dump cookie jar in}} 

$ Video Format Options
    `-f, --format FORMAT           {{Video format code, see the FORMAT SELECTION for all the info}} 
    `--all-formats                 {{Download all available video formats}} 
    `--prefer-free-formats         {{Prefer free video formats unless a specific one is requested}} 
    `-F, --list-formats            {{List all available formats of requested videos}} 
    `--youtube-skip-dash-manifest  {{Do not download the DASH manifests and related data on YouTube videos}} 
    `--merge-output-format FORMAT  {{If a merge is required (e.g. bestvideo+bestaudio), output to given container format. One of mkv, mp4, ogg, webm, flv. Ignored if no merge is required}} 

