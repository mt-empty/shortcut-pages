# Unix Time Format Sequences

> Source: http://manpages.debian.org/cgi-bin/man.cgi?query=date

> Aliases: time-formats, unix-date, strftime-format, strftime, strptime-format-specifier, strptime, strftime-formats, date-format, strptime-formats, strftime-format-specifiers, time-formatting, date-formatting, strftime-format-specifier, linux-time, unix-time, date-formats, linux-date, format-date, strptime-format, format-time, time-format, strptime-format-specifiers

$ Day
    `%a                            {{locale's abbreviated weekday name (e.g., Sun)}} 
    `%A                            {{locale's full weekday name (e.g., Sunday)}} 
    `%d                            {{day of month (e.g., 01)}} 
    `%e                            {{day of month, space padded; same as %_d}} 
    `%j                            {{day of year (001..366)}} 
    `%u                            {{day of week (1..7); 1 is Monday}} 
    `%w                            {{day of week (0..6); 0 is Sunday}} 

$ Week
    `%U                            {{week number of year, with Sunday as first day of week (00..53)}} 
    `%V                            {{ISO week number, with Monday as first day of week (01..53)}} 
    `%W                            {{week number of year, with Monday as first day of week (00..53)}} 

$ Month
    `%b                            {{locale's abbreviated month name (e.g., Jan)}} 
    `%B                            {{locale's full month name (e.g., January)}} 
    `%h                            {{same as %b}} 
    `%m                            {{month (01..12)}} 

$ Year
    `%C                            {{century; like %Y, except omit last two digits (e.g., 20)}} 
    `%g                            {{last two digits of year of ISO week number (see %G)}} 
    `%G                            {{year of ISO week number (see %V); normally useful only with %V}} 
    `%y                            {{last two digits of year (00..99)}} 
    `%Y                            {{year}} 

$ Date
    `%c                            {{locale's date and time (e.g., Thu Mar 3 23:05:25 2005)}} 
    `%D                            {{date; same as %m/%d/%y}} 
    `%F                            {{full date; same as %Y-%m-%d}} 
    `%x                            {{locale's date representation (e.g., 12/31/99)}} 

$ Time
    `%H                            {{hour (00..23)}} 
    `%I                            {{hour (01..12)}} 
    `%k                            {{hour, space padded ( 0..23); same as %_H}} 
    `%l                            {{hour, space padded ( 1..12); same as %_I}} 
    `%M                            {{minute (00..59)}} 
    `%N                            {{nanoseconds (000000000..999999999)}} 
    `%p                            {{locale's equivalent of either AM or PM; blank if not known}} 
    `%P                            {{like %p, but lower case}} 
    `%r                            {{locale's 12-hour clock time (e.g., 11:11:04 PM)}} 
    `%R                            {{24-hour hour and minute; same as %H:%M}} 
    `%s                            {{seconds since 1970-01-01 00:00:00 UTC}} 
    `%S                            {{second (00..60)}} 
    `%T                            {{time; same as %H:%M:%S}} 
    `%X                            {{locale's time representation (e.g., 23:13:48)}} 

$ Time Zone
    `%z                            {{+hhmm numeric time zone (e.g., -0400)}} 
    `%:z                           {{+hh:mm numeric time zone (e.g., -04:00)}} 
    `%::z                          {{+hh:mm:ss numeric time zone (e.g., -04:00:00)}} 
    `%:::z                         {{numeric time zone with : to necessary precision (e.g., -04, +05:30)}} 
    `%Z                            {{alphabetic time zone abbreviation (e.g., EDT)}} 

$ Misc
    `%%                            {{a literal %}} 
    `%n                            {{a newline}} 
    `%t                            {{a tab}} 

$ Examples
    `%Y-%m-%dT%H:%M:%S%:z (short: %FT%T%:z)
>                                  {{ISO-8601 (1970-01-01T00:00:00+00:00)}} 
    `%a, %d %b %y %H:%M:%S %z      {{RFC 822 (Thu, 01 Jan 70 00:00:00 +0000)}} 
    `%A, %d-%b-%y %H:%M:%S %Z      {{RFC 850 (Thursday, 01-Jan-70 00:00:00 UTC)}} 
    `%a, %d %b %Y %H:%M:%S %z      {{RFC 2822 (Thu, 01 Jan 1970 00:00:00 +0000)}} 
    `%Y-%m-%d %H:%M:%S%:z          {{RFC 3339 (1970-01-01 00:00:00+00:00)}} 

