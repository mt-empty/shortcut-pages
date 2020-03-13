# Skyscanner APIs

> Source: http://skyscanner.github.io/slate

> Aliases: skyscanner-b2b-apis, skyscanner-b2b-api, skyscanner-api

$ Flights: prices (live)
    `/pricing/v1.0 (POST)          {{Create your session. All query parameters (origin, destination, dates, etc) must be added to the body of the request. Returns the session key for polling results.}} 
    `/pricing/v1.0/{sessionKey}?apiKey={apiKey} (GET)
>                                  {{Poll results until status=UpdatesComplete (please allow up to a minute as we need to query all providers).}} 

$ Flights: bookings (live)
    `/pricing/v1.0/{session key}/booking?apiKey={apiKey} (PUT)
>                                  {{Request booking details and deeplink to provider after the live prices call. Initiates fresh live updates of the individual flights that make up the itinerary in order to retrieve an up to date price.}} 
    `/pricing/v1.0/{session key}/booking/{itinerary key}?apiKey={apiKey} (GET)
>                                  {{Poll booking details (until all item status='Current') to ensure that all prices are up-to-date.}} 

$ Flights: cheapest quotes (cached data)
    `/browsequotes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey} (GET)
>                                  {{Get the cheapest flight prices (if available) for multiple origins and/or destinations, and over many time frames.}} 

$ Flights: cheapest routes (cached data)
    `/browseroutes/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey} (GET)
>                                  {{Get the cheapest routes (if available) for multiple origins and/or destinations, and over many time frames.}} 

$ Flights: cheapest dates (cached data)
    `/browsedates/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey} (GET)
>                                  {{Get the cheapest dates (if available) for specific cities or airports over many time frames.}} 
    `/browsegrid/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={apiKey} (GET)
>                                  {{Similar to browsedates but returns a two-dimensional array with outbound days on one axis and the inbound days on the other axis to easily be displayed as a table.}} 

$ Flights: referral to Skyscanner site
    `/referral/v1.0/{market}/{currency}/{locale}/{originPlace}/{destinationPlace}/{outboundPartialDate}/{inboundPartialDate}?apiKey={shortApiKey}
>                                  {{Link to Skyscanner website for booking. If the query isn't specific enough to leed to the results page, it will link to a more general page, where the user will be asked to refine the search criteria.}} 

$ Car hire: prices (live)
    `/carhire/liveprices/v2/{market}/{currency}/{locale}/{pickupplace}/{dropoffplace}/{pickupdatetime}/{dropoffdatetime}/{driverage}?apiKey={apiKey}&userip={userip}
>                                  {{Returns all available cars from a range of car hire providers, for a specific pickup and dropoff airport, and specific dates and times.}} 

$ Car hire: referral to Skyscanner site
    `/referral/v1.0/{market}/{currency}/{locale}/{pickupplace}/{dropoffplace}/{pickupdatetime}/{dropoffdatetime}?apiKey={shortApiKey}&product=carhire&pickUpTime={pickupdatetime}&dropOffTime={dropoffdatetime}&driverAge={driverage}
>                                  {{Link to Skyscanner website for booking. If the query isn't specific enough to leed to the results page, it will link to a more general page, where the user will be asked to refine the search criteria.}} 

$ Additional Services
    `/reference/v1.0/currencies?apiKey={apiKey}
>                                  {{Get the list of valid currencies supported by Skyscanner, with additional information about how to display them.}} 
    `/reference/v1.0/locales?apiKey={apiKey}
>                                  {{Return the list of localizations supported by Skyscanner.}} 
    `/reference/v1.0/countries/{locale}?apiKey={apiKey}
>                                  {{Return the list of markets (countries) supported by Skyscanner.}} 
    `/autosuggest/v1.0/{market}/{currency}/{locale}/?query={query}&apiKey={apiKey}
>                                  {{Get a list of places (with corresponding IDs) that match the query string}} 
    `/autosuggest/v1.0/{market}/{currency}/{locale}/?id={id}&apiKey={apiKey}
>                                  {{Get information about a specific place given it's ID (for example city name and country name for an airport)}} 

