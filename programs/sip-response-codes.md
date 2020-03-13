# SIP Response Codes

> Source: https://en.wikipedia.org/wiki/List_of_SIP_response_codes

> Aliases: sip-status-codes

$ 1xx - Provisional Responses
    `100 Trying                    {{Extended search being performed may take a significant time so a forking proxy must send a 100 Trying response}} 
    `180 Ringing                   {{Destination user agent received INVITE, and is alerting user of call}} 
    `181 Call is Being Forwarded   {{Servers can optionally send this response to indicate a call is being forwarded}} 
    `182 Queued                    {{Indicates that the destination was temporarily unavailable, so the server has queued the call until the destination is available. A server may send multiple 182 responses to update progress of the queue}} 
    `183 Session in Progress       {{This response may be used to send extra information for a call which is still being set up}} 
    `199 Early Dialog Terminated   {{Can be used by User Agent Server to indicate to upstream SIP entities (including the User Agent Client (UAC)) that an early dialog has been terminated}} 

$ 2xx - Successful Responses
    `200 OK                        {{Indicates the request was successful}} 
    `202 Accepted                  {{Indicates that the request has been accepted for processing, but the processing has not been completed. Deprecated}} 
    `204 No Notification           {{Indicates the request was successful, but the corresponding response will not be received}} 

$ 3xx - Redirection Responses
    `300 Multiple Choices          {{The address resolved to one of several options for the user or client to choose between, which are listed in the message body or the message's Contact fields}} 
    `301 Moved Permanently         {{The original Request-URI is no longer valid, the new address is given in the Contact header field, and the client should update any records of the original Request-URI with the new value}} 
    `302 Moved Temporarily         {{The client should try at the address in the Contact field. If an Expires field is present, the client may cache the result for that period of time}} 
    `305 Use Proxy                 {{The Contact field details a proxy that must be used to access the requested destination}} 
    `380 Alternative Service       {{The call failed, but alternatives are detailed in the message body}} 

$ 4xx - Client Failure Responses
    `400 Bad Request               {{The request could not be understood due to malformed syntax}} 
    `401 Unauthorized              {{The request requires user authentication. This response is issued by UASs and registrars}} 
    `402 Payment Required          {{Reserved for future use}} 
    `403 Forbidden                 {{The server understood the request, but is refusing to fulfil it}} 
    `404 Not Found                 {{The server has definitive information that the user does not exist at the domain specified in the Request-URI. This status is also returned if the domain in the Request-URI does not match any of the domains handled by the recipient of the request}} 
    `405 Method Not Allowed        {{The method specified in the Request-Line is understood, but not allowed for the address identified by the Request-URI}} 
    `406 Not Acceptable            {{The resource identified by the request is only capable of generating response entities that have content characteristics but not acceptable according to the Accept header field sent in the request}} 
    `407 Proxy Authentication Required
>                                  {{The request requires user authentication. This response is issued by proxys}} 
    `408 Request Timeout           {{Couldn't find the user in time. The server could not produce a response within a suitable amount of time, for example, if it could not determine the location of the user in time. The client MAY repeat the request without modifications at any later time}} 
    `409 Conflict                  {{User already registered. Deprecated by omission from later RFCs and by non-registration with the IANA}} 
    `410 Gone                      {{The user existed once, but is not available here any more}} 
    `411 Length Required           {{The server will not accept the request without a valid Content-Length. Deprecated by omission from later RFCs and by non-registration with the IANA}} 
    `412 Conditional Request Failed
>                                  {{The given precondition has not been met}} 
    `413 Request Entity Too Large  {{Request body too large}} 
    `414 Request-URI Too Long      {{The server is refusing to service the request because the Request-URI is longer than the server is willing to interpret}} 
    `415 Unsupported Media Type    {{Request body in a format not supported}} 
    `416 Unsupported URI Scheme    {{Request-URI is unknown to the server}} 
    `417 Unknown Resource-Priority {{There was a resource-priority option tag, but no Resource-Priority header}} 
    `420 Bad Extension             {{Bad SIP Protocol Extension used, not understood by the server}} 
    `421 Extension Required        {{The server needs a specific extension not listed in the Supported header}} 
    `422 Session Interval Too Small
>                                  {{The received request contains a Session-Expires header field with a duration below the minimum timer}} 
    `423 Interval Too Brief        {{Expiration time of the resource is too short}} 
    `424 Bad Location Information  {{The request's location content was malformed or otherwise unsatisfactory}} 
    `428 Use Identity Header       {{The server policy requires an Identity header, and one has not been provided}} 
    `429 Provide Referrer Identity {{The server did not receive a valid Referred-By token on the request}} 
    `430 Flow Failed               {{A specific flow to a user agent has failed, although other flows may succeed. This response is intended for use between proxy devices, and should not be seen by an endpoint (and if it is seen by one, should be treated as a 400 Bad Request response)}} 
    `433 Anonymity Disallowed      {{The request has been rejected because it was anonymous}} 
    `436 Bad Identity-Info         {{The request has an Identity-Info header, and the URI scheme in that header cannot be dereferenced}} 
    `437 Unsupported Certificate   {{The server was unable to validate a certificate for the domain that signed the request}} 
    `438 Invalid Identity Header   {{The server obtained a valid certificate that the request claimed was used to sign the request, but was unable to verify that signature}} 
    `439 First Hop Lacks Outbound Support
>                                  {{The first outbound proxy the user is attempting to register through does not support the "outbound" feature of RFC 5626, although the registrar does}} 

$ 4xx - Client Failure Responses (continued)
    `470 Consent Needed            {{The source of the request did not have the permission of the recipient to make such a request}} 
    `480 Temporarily Unavailable   {{Callee currently unavailable}} 
    `481 Call/Transaction Does Not Exist
>                                  {{Server received a request that does not match any dialog or transaction}} 
    `482 Loop Detected             {{Server has detected a loop}} 
    `483 Too Many Hops             {{Max-Forwards header has reached the value '0'}} 
    `484 Address Incomplete        {{Request-URI incomplete}} 
    `485 Ambiguous                 {{Request-URI is ambiguous}} 
    `486 Busy Here                 {{Callee is busy}} 
    `487 Request Terminated        {{Request has terminated by bye or cancel}} 
    `488 Not Acceptable Here       {{Some aspect of the session description or the Request-URI is not acceptable}} 
    `489 Bad Event                 {{The server did not understand an event package specified in an Event header field}} 
    `491 Request Pending           {{Server has some pending request from the same dialog}} 
    `493 Undecipherable            {{Request contains an encrypted MIME body, which recipient can not decrypt}} 
    `494 Security Agreement Required
>                                  {{The server has received a request that requires a negotiated security mechanism, and the response contains a list of suitable security mechanisms for the requester to choose between, or a digest authentication challenge}} 

$ 5xx - Server Failure Responses
    `500 Server Internal Error     {{The server could not fulfill the request due to some unexpected condition}} 
    `501 Not Implemented           {{The server does not have the ability to fulfill the request, such as because it does not recognize the request method. (Compare with 405 Method Not Allowed, where the server recognizes the method but does not allow or support it.)}} 
    `502 Bad Gateway               {{The server is acting as a gateway or proxy, and received an invalid response from a downstream server while attempting to fulfill the request}} 
    `503 Service Unavailable       {{The server is undergoing maintenance or is temporarily overloaded and so cannot process the request. A "Retry-After" header field may specify when the client may reattempt its request}} 
    `504 Server Time-out           {{The server attempted to access another server in attempting to process the request, and did not receive a prompt response}} 
    `505 Version Not Supported     {{The SIP protocol version in the request is not supported by the server}} 
    `513 Message Too Large         {{The request message length is longer than the server can process}} 
    `580 Precondition Failure      {{The server is unable or unwilling to meet some constraints specified in the offer}} 

$ 6xx - Global Failure Responses
    `600 Busy Everywhere           {{All possible destinations are busy. Unlike the 486 response, this response indicates the destination knows there are no alternative destinations (such as a voicemail server) able to accept the call}} 
    `603 Decline                   {{The destination does not wish to participate in the call, or cannot do so, and additionally the destination knows there are no alternative destinations (such as a voicemail server) willing to accept the call}} 
    `604 Does Not Exist Anywhere   {{The server has authoritative information that the requested user does not exist anywhere}} 
    `606 Not Acceptable            {{The user's agent was contacted successfully but some aspects of the session description such as the requested media, bandwidth, or addressing style were not acceptable}} 

