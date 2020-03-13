# IRC

> Source: http://www.cheat-sheets.org/saved-copy/wikiHow_IRC_Cheat_Sheet.pdf

> Aliases: internet-relay-chat

$ Main
    `/server serverurl             {{Joining a Server}} 
    `/join #Channel                {{Joining a Channel}} 
    `/away <reason>                {{Setting yourself away}} 
    `/back                         {{Removing your away status}} 
    `/part <Message>               {{Leaving a channel}} 
    `/quit <Message>               {{Quitting IRC}} 
    `/msg NickServ register PASSWORD email
>                                  {{Registering your Name}} 
    `/nick NAME                    {{Changing Your Name}} 
    `/msg NickServ identify PASSWORD
>                                  {{Identifing to nickserv}} 
    `/msg NickServ set password PASSWORD
>                                  {{Changing your password (You have to repeat this for all of your linked nicks, which can be found with msg NickServ info YOUR NICK)}} 
    `/topic NEW TOPIC              {{Changing the topic of the channel (some channels restrict this command to operators)}} 
    `/whois USERNAME               {{Get more information on another user}} 
    `/whois USERNAME USERNAME      {{Get Idle time and signon time in addition to normal WHOIS (USERNAME repeated twice)}} 

$ Commands for channel operators
    `/msg ChanServ op #channel     {{Opping yourself}} 
    `/msg chanserv op #channel NICKNAME
>                                  {{Opping another person}} 
    `/mode #channel +o NICKNAME    {{Opping another person (when opped)}} 
    `/kick NICKNAME (reason)       {{Kicking people}} 
    `/quote remove #CHANNEL NICKNAME :REASON
>                                  {{Removing people (When opped)}} 
    `/mode #channel +q NAME        {{Quieting another person (when opped)}} 
    `/msg ChanServ clear #channel ops
>                                  {{Clearing ops}} 
    `/msg ChanServ clear #channel voices
>                                  {{Clearing voices}} 
    `/msg chanserv op #channel -NAME
>                                  {{Removing just one op}} 
    `/mode -o NAME                 {{Removing just one op (when opped)}} 
    `/msg ChanServ voice #channel -NAME
>                                  {{Removing just one voice}} 
    `/mode #channel +b nick!realname@hostmask.com
>                                  {{Banning a user}} 
    `/msg nickserv ghost YourUsername yourpassword
>                                  {{Ghosting Yourself}} 

$ Information
    `/msg ChanServ access #channel list
>                                  {{To see who has what access}} 
    `/whois <nickname>             {{When adding a user to the access list, note whether they own their current nick}} 
    `None = default for anyone off the street
>                                  {{Various flags}} 
    `+votiA = ops                  {{Various flags (alternative)}} 
    `+votsriRfA - able to set access levels
>                                  {{Various flags (alternative)}} 
    `+vVoOtsriRfAF = Channel founder
>                                  {{Various flags (alternative)}} 

