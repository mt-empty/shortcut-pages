# Python Datetime

> Source: https://docs.python.org/3/library/datetime.html

> Aliases: datetime.datetime

$ Imports
    `from datetime import datetime {{Imports DateTime Object}} 
    `from datetime import date     {{Imports Date Object}} 

$ Date Formatting
    `%a                            {{Abbreviated weekday (Sun)}} 
    `%A                            {{Weekday (Sunday)}} 
    `%b                            {{Abbreviated month name (Jan)}} 
    `%B                            {{Month name (January)}} 
    `%c                            {{Date and time}} 
    `%d                            {{Day (leading zeros) (01 to 31)}} 
    `%H                            {{24 hour (leading zeros) (00 to 23)}} 
    `%I                            {{12 hour (leading zeros) (01 to 12)}} 
    `%j                            {{Day of year (001 to 366)}} 
    `%m                            {{Month (01 to 12)}} 
    `%M                            {{Minute (00 to 59)}} 
    `%p                            {{AM or PM}} 
    `%S                            {{Second (00 to 61⁴)}} 
    `%y                            {{Year without century (00 to 99)}} 
    `%Y                            {{Year (2008)}} 

$ DateTime Object Methods
    `now(timezone)                 {{Return the current local date and time}} 
    `utcnow()                      {{Return the current UTC date and time}} 
    `today()                       {{Return the current local date}} 
    `strptime(date, format)        {{Return a datetime corresponding to date_string, parsed according to format.}} 
    `strftime(format)              {{Returns a string representing the date, controlled by an explicit format string}} 
    `fromtimestamp(timestamp)      {{Return the local date and time corresponding to the POSIX timestamp}} 
    `utcfromtimestamp(timestamp)   {{Return the UTC datetime corresponding to the POSIX timestamp}} 
    `replace()                     {{Gives new values by whichever keyword arguments are specified}} 
    `combine(date, time)           {{Return a new datetime object whose date components are equal to the given date object’s}} 

$ Date Object Methods
    `fromordinal(ordinal)          {{Return the datetime corresponding to the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1}} 
    `toordinal()                   {{Returns the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1}} 
    `weekday()                     {{Returns the day of the week as an integer, where Monday is 0 and Sunday is 6}} 
    `isoweekday()                  {{Returns the day of the week as an integer, where Monday is 1 and Sunday is 7}} 
    `isocalendar()                 {{Returns a 3-tuple, (ISO year, ISO week number, ISO weekday)}} 
    `isoformat()                   {{Returns a string representing the date in ISO 8601 format, "YYYY-MM-DD"}} 
    `__str__()                     {{For a date d, str(d) is equivalent to d.isoformat()}} 
    `ctime()                       {{Returns a string representing the date}} 
    `__format__()                  {{Same as date.strftime(). This makes it possible to specify format string for a date object when using str.format()}} 

$ Time Object Methods
    `replace()                     {{Gives new values by whichever keyword arguments are specified}} 
    `utcoffset()                   {{Returns the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1}} 
    `dst()                         {{Returns the day of the week as an integer, where Monday is 1 and Sunday is 7}} 
    `tzname()                      {{Returns a 3-tuple, (ISO year, ISO week number, ISO weekday)}} 

