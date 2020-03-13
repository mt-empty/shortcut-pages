# Splunk Eval Functions

> Source: http://docs.splunk.com/Documentation/Splunk/latest/SearchReference/CommonEvalFunctions

> Aliases: splunk-functions, splunk-evaluation, splunk-eval, splunk-where

$ Comparison and Conditional Functions
    `case(X,"Y",...)               {{... | eval description=case(error == 404, "Not found", error == 500, "Internal Server Error", error == 200, "OK")}} 
    `cidrmatch("X",Y)              {{... | eval isLocal=if(cidrmatch("123.132.32.0/25",ip), "local", "not local")}} 
    `coalesce(X,...)               {{... | eval ip=coalesce(clientip,ipaddress)}} 
    `if(X,Y,Z)                     {{... | eval err=if(error == 200, "OK", "Error")}} 
    `like(TEXT, PATTERN)           {{... | eval is_a_foo=if(like(field, "foo%"), "yes a foo", "not a foo")}} 
    `match(SUBJECT, "REGEX")       {{... | eval n=if(match(field, "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"), 1, 0)}} 
    `null()                        {{null()}} 
    `nullif(X,Y)                   {{... | eval n=nullif(fieldA,fieldB)}} 
    `searchmatch(X)                {{... | eval n=searchmatch("foo AND bar")}} 
    `validate(X,Y,...)             {{... | eval n=validate(isint(port), "ERROR: Port is not an integer", port >= 1 AND port <= 65535, "ERROR: Port is out of range")}} 

$ Conversion Functions
    `tonumber(NUMSTR,BASE)         {{... | eval n=tonumber("0A4",16)}} 
    `tostring(X,Y)                 {{... | eval n=tostring(1==1) + " " + tostring(15, "hex") + " " + tostring(12345.6789, "commas")}} 

$ Cryptographic Functions
    `md5(X)                        {{... | eval n=md5(field)}} 
    `sha1(X)                       {{... | eval n=sha1(field)}} 
    `sha256(X)                     {{... | eval n=sha256(field)}} 
    `sha512(X)                     {{... | eval n=sha512(field)}} 

$ Date and Time Functions
    `now()                         {{... | eval now=now()}} 
    `relative_time(X,Y)            {{... | eval n=relative_time(now(), "-1d@d")}} 
    `strftime(X,Y)                 {{... | eval n=strftime(_time, "%H:%M")}} 
    `strptime(X,Y)                 {{... | eval n=strptime(timeStr, "%H:%M")}} 
    `time()                        {{... | eval time=time()}} 

$ Informational Functions
    `isbool(X)                     {{... | eval n=if(isbool(field),"yes","no")}} 
    `isint(X)                      {{... | eval n=if(isint(field), "int", "not int")}} 
    `isnotnull(X)                  {{... | eval n=if(isnotnull(field),"yes","no")}} 
    `isnull(X)                     {{... | eval n=if(isnull(field),"yes","no")}} 
    `isnum(X)                      {{... | eval n=if(isnum(field),"yes","no")}} 
    `isstr(X)                      {{... | eval n=if(isstr(field),"yes","no")}} 
    `typeof(X)                     {{... | eval n=typeof(12) + typeof("string") + typeof(1==2) + typeof(badfield)}} 

$ Mathematical Functions
    `abs(X)                        {{... | eval absnum=abs(number)}} 
    `ceil(X), ceiling(X)           {{... | eval n=ceil(1.9)}} 
    `exact(X)                      {{... | eval n=exact(3.14 * num)}} 
    `exp(X)                        {{... | eval y=exp(3)}} 
    `floor(X)                      {{... | eval n=floor(1.9)}} 
    `ln(X)                         {{... | eval lnBytes=ln(bytes)}} 
    `log(X,Y)                      {{... | eval num=log(number,2)}} 
    `pi()                          {{... | eval area_circle=pi()*pow(radius,2)}} 
    `pow(X,Y)                      {{... | eval area_circle=pi()*pow(radius,2)}} 
    `round(X,Y)                    {{... | eval n=round(2.555, 2)}} 
    `sigfig(X)                     {{... | eval n=sigfig(1.00*1111)}} 
    `sqrt(X)                       {{... | eval n=sqrt(9)}} 

$ Multivalue Functions
    `commands(X)                   {{... | eval x=commands("search foo | stats count | sort count")}} 
    `mvappend(X,...)               {{... | eval fullName=mvappend(initial_values, "middle value", last_values)}} 
    `mvcount(MVFIELD)              {{... | eval n=mvcount(multifield)}} 
    `mvdedup(X)                    {{... | eval s=mvdedup(mvfield)}} 
    `mvfilter(X)                   {{... | eval n=mvfilter(match(email, "\.net$") OR match(email, "\.org$"))}} 
    `mvfind(MVFIELD,"REGEX")       {{... | eval n=mvfind(mymvfield, "err\d+")}} 
    `mvindex(MVFIELD,STARTINDEX)   {{... | eval n=mvindex(multifield, 2)}} 
    `mvjoin(MVFIELD,STR)           {{... | eval n=mvjoin(foo, ";")}} 
    `mvrange(X,Y,Z)                {{... | eval mv=mvrange(1,11,2)}} 
    `mvsort(X)                     {{... | eval s=mvsort(mvfield)}} 
    `mvzip(X,Y,"Z")                {{... | eval nserver=mvzip(hosts,ports)}} 

$ Statistical Functions
    `max(X,...)                    {{... | eval n=max(1, 3, 6, 7, "foo", field)}} 
    `min(X,...)                    {{... | eval n=min(1, 3, 6, 7, "foo", field)}} 
    `random()                      {{... | eval n=random()}} 

$ Text Functions
    `len(X)                        {{... | eval n=len(field)}} 
    `lower(X)                      {{... | eval username=lower(username)}} 
    `ltrim(X,Y)                    {{... | eval x=ltrim(" ZZZZabcZZ ", " Z")}} 
    `replace(X,Y,Z)                {{... | eval n=replace(date, "^(\d{1,2})/(\d{1,2})/", "\2/\1/")}} 
    `rtrim(X,Y)                    {{... | eval n=rtrim(" ZZZZabcZZ ", " Z")}} 
    `spath(X,Y)                    {{... | eval locDesc=spath(_raw, "vendorProductSet.product.desc.locDesc")}} 
    `split(X,"Y")                  {{... | eval n=split(foo, ";")}} 
    `substr(X,Y,Z)                 {{... | eval n=substr("string", 1, 3) + substr("string", -3)}} 
    `trim(X,Y)                     {{... | eval n=trim(" ZZZZabcZZ ", " Z")}} 
    `upper(X)                      {{... | eval n=upper(username)}} 
    `urldecode(X)                  {{... | eval n=urldecode("http%3A%2F%2Fwww.splunk.com %2Fdownload%3Fr%3Dheader")}} 

$ Trigonometry and Hyperbolic Functions
    `acos(X)                       {{... | eval degrees=acos(0)*180/pi()}} 
    `acosh(X)                      {{... | eval n=acosh(2)}} 
    `asin(X)                       {{... | eval degrees=asin(1)*180/pi()}} 
    `asinh(X)                      {{... | eval n=asinh(1)}} 
    `atan(X)                       {{... | eval n=atan(0.50)}} 
    `atan2(Y, X)                   {{.. | eval n = atan2(0.50, 0.75)}} 
    `atanh(X)                      {{... | eval n=atanh(0.500)}} 
    `cos(X)                        {{... | eval n=cos(pi())}} 
    `cosh(X)                       {{... | eval n=cosh(1)}} 
    `hypot(X,Y)                    {{... | eval n=hypot(3,4)}} 
    `sin(X)                        {{... | eval n=sin(90 * pi()/180)}} 
    `sinh(X)                       {{... | eval n=sinh(1)}} 
    `tan(X)                        {{... | eval n=tan(1)}} 
    `tanh(X)                       {{... | eval n=tanh(1)}} 

