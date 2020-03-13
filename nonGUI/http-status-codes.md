# HTTP Status Codes

> Source: http://www.cheatography.com/kstep/cheat-sheets/http-status-codes/

> Aliases: http-response-code, http-response-status-code, http-error-codes, http-error-code, http-response-status-codes, http-status-code, http-response-codes

$ HTTP Informational Codes (1xx)
    `100                           {{Continue}} 
    `101                           {{Switching Protocols}} 
    `102                           {{Processing}} 
    `103                           {{Checkpoint}} 
    `122                           {{Request-URL too long(IE7)}} 

$ HTTP Successful Codes (2xx)
    `200                           {{OK}} 
    `201                           {{Created}} 
    `202                           {{Accepted}} 
    `203                           {{Non-authorative information}} 
    `204                           {{No content}} 
    `205                           {{Reset Content}} 
    `206                           {{Partial Content}} 
    `207                           {{Multi Status}} 
    `208                           {{Already Reported}} 
    `226                           {{IM used}} 

$ HTTP Redirection Codes (3xx)
    `300                           {{Multiple Choices}} 
    `301                           {{Moved Permanently}} 
    `302                           {{Found}} 
    `303                           {{See Other}} 
    `304                           {{Not Modified}} 
    `305                           {{Use Proxy}} 
    `306                           {{Switch Proxy(unused)}} 
    `307                           {{Temporary Redirect}} 
    `308                           {{Resume Incomplete(PUT POST)}} 

$ HTTP Client Error Codes (4xx)
    `400                           {{Bad Request}} 
    `401                           {{Unauthorized}} 
    `402                           {{Payment Required}} 
    `403                           {{Forbidden}} 
    `404                           {{Not Found}} 
    `405                           {{Method Not Allowed}} 
    `406                           {{Not Acceptable}} 
    `407                           {{Proxy Authentication Required}} 
    `408                           {{Request Timeout}} 
    `409                           {{Conflict}} 
    `410                           {{Gone}} 
    `411                           {{Length Required}} 
    `412                           {{Precondition Failed}} 
    `413                           {{Request Entity Too Large}} 
    `414                           {{Request URL Too Long}} 
    `415                           {{Unsupported Media Type}} 
    `416                           {{Request Range Not Satisfiable}} 
    `417                           {{Expectation Failed}} 
    `418                           {{I'm a Teapot}} 
    `422                           {{Unprocessable Entity}} 
    `423                           {{Locked}} 
    `424                           {{Failed Dependency}} 
    `425                           {{Unordered Collection}} 
    `426                           {{Upgrade Required}} 
    `428                           {{Precondition Required}} 
    `429                           {{Too Many Requests}} 
    `431                           {{Request Header Fields Too Large}} 
    `444                           {{No Response}} 
    `449                           {{Retry With(MS)}} 
    `450                           {{Blocked by Parental Controls(MS)}} 
    `451                           {{Unavailable for Legal Reasons}} 
    `499                           {{Client Closed Request}} 

$ HTTP Server Error Codes (5xx)
    `500                           {{Internal Server Error}} 
    `501                           {{Not Implemented}} 
    `502                           {{Bad Gateway}} 
    `503                           {{Service Unavailable}} 
    `504                           {{Gateway Timeout}} 
    `505                           {{HTTP Version Not Supported}} 
    `506                           {{Variant Also Negotiates}} 
    `507                           {{Insufficient Storage}} 
    `508                           {{Loop Detected}} 
    `509                           {{Bandwidth Exceeded}} 
    `510                           {{Not Extended}} 
    `511                           {{Network Authentication Required}} 
    `598                           {{Network Read Timeout}} 
    `599                           {{Network Connect Timeout}} 

