# Metasploit

> Source: http://www.cheatography.com/huntereight/cheat-sheets/metasploit-4-5-0-dev-15713/

$ Database Commands
    `db_connect                    {{connect database}} 
    `db_disconnect                 {{disconnect database}} 
    `db_export                     {{export database}} 
    `db_import                     {{import scan result}} 
    `db_status                     {{status of database}} 
    `hosts                         {{display hosts}} 
    `loot                          {{display loot}} 
    `notes                         {{display notes}} 
    `services                      {{display services}} 
    `vulns                         {{display vulnerabilities}} 
    `workspace                     {{switch between workspace}} 
    `db_nmap                       {{nmap scan into database}} 

$ Core Commands
    `?                             {{display help}} 
    `help                          {{display help (alternative)}} 
    `back                          {{go back}} 
    `cd                            {{change directory}} 
    `color                         {{toggle color}} 
    `connect                       {{communicate with a host}} 
    `exit                          {{exit metasploit}} 
    `info                          {{display info of module}} 
    `irb                           {{go into irb}} 
    `jobs                          {{display and manage jobs}} 
    `kill                          {{stop a job}} 
    `load                          {{load a plugin}} 
    `loadpath                      {{load a plugin from path}} 
    `makerc                        {{print commands entered to a path}} 
    `previous                      {{set previous module as current module}} 
    `popm                          {{pops the latest module off of the module stack and makes it active}} 
    `pushm                         {{pushes the active or list of modules onto the module stack}} 
    `quit                          {{quit the console}} 
    `resource                      {{run commands stored in a file}} 
    `route                         {{route traffic through a connection}} 
    `save                          {{save datastores}} 
    `search                        {{search for modules}} 
    `sessions                      {{dump session listings and display information about sessions}} 
    `set                           {{set variable of a module}} 
    `setg                          {{set a global variable}} 
    `show                          {{display modules of a type, or all modules}} 
    `sleep                         {{do nothing for x seconds}} 
    `spool                         {{write all output to a files}} 
    `threads                       {{manipulate threads}} 
    `unload                        {{unload a plugin}} 
    `unset                         {{unset a variable}} 
    `unsetg                        {{unset a global variable}} 
    `use                           {{use a module (by name)}} 
    `version                       {{show metasploit info}} 

$ Meterpreter Core and File System
    `background                    {{background the current session}} 
    `bgkill                        {{kill a background meterpreter script}} 
    `channel                       {{displays info about active channels}} 
    `close                         {{close a channel}} 
    `disable_unicode_encoding      {{displays info about active channels}} 
    `enable_unicode_encoding       {{enable encoding of unicode strings}} 
    `exit                          {{exit meterpreter shell}} 
    `help                          {{display help}} 
    `info                          {{display info about active post module}} 
    `interact                      {{interact with a channel}} 
    `irb                           {{drop into irb scripting mode}} 
    `load                          {{load one or more meterpreter extensions}} 
    `migrate                       {{migrate the server to another process}} 
    `quit                          {{terminate the meterpreter sessions}} 
    `read                          {{reads data from a channel}} 
    `resource                      {{run the commands stored in a file}} 
    `run                           {{executes a meterpreter script or post module}} 
    `write                         {{write data to a channel}} 
    `cat                           {{read the contents of a file to the screen}} 
    `cd                            {{change directory}} 
    `download                      {{download file to your computer}} 
    `edit                          {{edit a file}} 
    `getlwd                        {{print local working directory}} 
    `getwd                         {{print working directory}} 
    `lcd                           {{change local working directory}} 
    `lpwd                          {{print local working directory}} 
    `ls                            {{list files}} 
    `mkdir                         {{make directory}} 
    `pwd                           {{print working directory}} 
    `rm                            {{delete the specified file}} 
    `rmdir                         {{remove directory}} 
    `search                        {{search for files}} 
    `upload                        {{upload file to target}} 

$ Meterpreter User Interface Commands
    `enumdesktops                  {{list all accessible desktops and window stations}} 
    `getdesktop                    {{get the current meterpreter desktop}} 
    `idletime                      {{display the amount of time the user has been idle}} 
    `keyscan_start                 {{start capturing keystrokes}} 
    `keyscan_stop                  {{stop capturing keystrokes}} 
    `keyscan_dump                  {{dump the keystroke buffer}} 
    `screenshot                    {{screenshot of the gui}} 
    `setdesktop                    {{change the meterpreters current desktop}} 
    `uictl                         {{control some of the user interface components}} 

$ Meterpreter System Commands
    `clearev                       {{clear the event log}} 
    `drop_token                    {{relinquishes any active impersonation token}} 
    `execute                       {{execute a command}} 
    `getpid                        {{get the current process identifier}} 
    `getprivs                      {{attempt to enable all privileges available to the current process}} 
    `getuid                        {{get the user that the server is running as}} 
    `kill                          {{terminate a process}} 
    `ps                            {{list running processes}} 
    `reboot                        {{reboots the remote computer}} 
    `reg                           {{interact with the remote registry}} 
    `rev2self                      {{calls reverttoself() on the remote machine}} 
    `shell                         {{drop into a system command shell}} 
    `shutdown                      {{shuts down the remote computer}} 
    `steal_token                   {{attempt to steal an impersonation token from the process}} 
    `sysinfo                       {{gets information about the remote system}} 

$ Meterpreter Priv Commands
    `webcam_list                   {{list webcams}} 
    `webcam_snap                   {{take a snapshot from the specified webcam}} 
    `getsystem                     {{attempt to elevate your privilege to that of local system}} 
    `hashdump                      {{dumps the contents of the sam database}} 
    `timestomp                     {{manipulate mace attributes}} 

