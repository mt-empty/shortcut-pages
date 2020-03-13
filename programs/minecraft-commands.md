# Minecraft Commands

> Source: http://minecraft.gamepedia.com/Commands

> Aliases: minecraft-cheats

$ Players/entities
    `/achievement <give|take> <name|*> [player]
>                                  {{Give or removes an achievement from a player}} 
    `/ban <name> [reason …]        {{Add player to banlist}} 
    `/ban-ip <address|name> [reason …]
>                                  {{Add IP address to banlist}} 
    `/banlist <ips|players>        {{Display banlist}} 
    `/clear [player] [item] [data] [maxCount] [dataTag]
>                                  {{Clear items from player inventory}} 
    `/deop <player>                {{Revoke operator status from a player}} 
    `/difficulty <difficulty>      {{Set the difficulty level}} 
    `/effect <player> <effect> [seconds] [amplifier] [hideParticles]
>                                  {{Add or remove status effects}} 
    `/enchant <player> <enchantment ID> [level]
>                                  {{Enchant a player item}} 
    `/entitydata <entity> <dataTag>
>                                  {{Modify the data tag of an entity}} 
    `/gamemode <mode> [player]     {{Set a player's game mode}} 
    `/give <player> <item> [amount] [data] [dataTag]
>                                  {{Give an item to a player}} 
    `/kick <player> [reason …]     {{Kick a player off a server}} 
    `/kill [player|entity]         {{Kill entities (players, mobs, items, etc.)}} 
    `/list [uuids]                 {{List players on the server}} 
    `/me <action ...>              {{Display a message about yourself}} 
    `/op <player>                  {{Grant operator status to a player}} 
    `/pardon[-ip] <<name>|<address>>
>                                  {{Remove entries from the banlist}} 
    `/particle <name> <x> <y> <z> <xd> <yd> <zd> <speed> [count] [mode] [player] [params ...]
>                                  {{Create particles}} 
    `/playsound <sound> <source> <player> [x] [y] [z] [volume] [pitch] [minimumVolume]
>                                  {{Play a sound}} 
    `/stopsound <player> [source] [sound]
>                                  {{Stop a sound}} 
    `/scoreboard <objectives|players|teams> …
>                                  {{Manage objectives, players, teams, and tags}} 
    `/setidletimeout <Minutes until kick>
>                                  {{Set the time before idle players are kicked}} 
    `/spawnpoint [[player] [<x> <y> <z>]]
>                                  {{Set the spawn point for a player}} 
    `/summon <EntityName> [x] [y] [z] [dataTag]
>                                  {{Summon an entity}} 
    `/tell <player> <message …>    {{Display a private message to other players}} 
    `/tellraw <player> <raw json message>
>                                  {{Display a JSON message to players}} 
    `/say <message …>              {{Display a message to multiple players}} 
    `/testfor <player> [dataTag]   {{Count entities matching specified conditions}} 
    `/title <player> <clear|reset|subtitle <title>|times <fadeIn> <stay> <fadeOut>|title <title>>
>                                  {{Manage screen titles}} 
    `/trigger <objective> <add|set> <value>
>                                  {{Set a trigger to be activated}} 
    `/whitelist <add <player>|list|off|on|reload|remove <player>>
>                                  {{Manage server whitelist}} 
    `/xp <amount>[L] [player]      {{Add or removes player experience}} 

$ Teleporting
    `/spreadplayers <x> <z> <spreadDistance> <maxRange> <respectTeams> <player …>
>                                  {{Teleport entities to random locations}} 
    `/teleport <target entity> <x> <y> <z> [<y-rot> <x-rot>]
>                                  {{Teleport entities}} 
    `/tp [target player] <<destination player>|<x> <y> <z> [<yaw> <pitch>]>
>                                  {{Teleport players}} 

$ World
    `/defaultgamemode <mode>       {{Set the default game mode}} 
    `/gamerule <rule name> [value] {{Set or queries a game rule value}} 
    `/publish                      {{Open single-player world to local network}} 
    `/save-all [flush]             {{Save the server to disk}} 
    `/saves-off                    {{Disable automatic server saves}} 
    `/saves-on                     {{Enable automatic server saves}} 
    `/seed                         {{Display the world seed}} 
    `/setworldspawn [<x> <y> <z>]  {{Set the world spawn}} 
    `/stop                         {{Stop a server}} 
    `/time <add|query|set> <value> {{Change or queries the world's game time}} 
    `/toggledownfall               {{Toggle the weather}} 
    `/weather <clear|rain|thunder> [duration]
>                                  {{Set the weather}} 
    `/worldborder <...>            {{Manage the world border}} 

$ Blocks
    `/blockdata <x> <y> <z> <dataTag>
>                                  {{Modify the data tag of a block}} 
    `/clone <x1> <y1> <z1> <x2> <y2> <z2> <x> <y> <z> [maskMode] [cloneMode] [TileName]
>                                  {{Copy blocks from one place to another}} 
    `/fill <x1> <y1> <z1> <x2> <y2> <z2> <TileName> [dataValue] [oldBlockHandling] [dataTag]
>                                  {{Fill a region with a specific block}} 
    `/setblock <x> <y> <z> <TileName> [dataValue] [oldBlockHandling] [dataTag]
>                                  {{Change a block to another block}} 
    `/testforblock <x> <y> <z> <TileName> [dataValue] [dataTag]
>                                  {{Test whether a block is in a location}} 
    `/testforblocks <x1> <y1> <z1> <x2> <y2> <z2> <x> <y> <z> [mode]
>                                  {{Test whether the blocks in two regions match}} 

$ Others
    `/debug <start|stop>           {{Start or stops a debugging session}} 
    `/execute <entity> <x> <y> <z> detect <x2> <y2> <z2> <block> <data> <command …>
>                                  {{Execute another command}} 
    `/help [page|command name]     {{Provide help for commands}} 
    `/replaceitem <entity <selector>|block> <slot> <item> [amount] [data] [dataTag]
>                                  {{Replace items in inventories}} 
    `/stats <...>                  {{Update objectives from command results}} 

