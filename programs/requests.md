# Requests Cheat Sheet

> Source: http://docs.python-requests.org/

> Aliases: python-requests

$ GET
    `response = requests.get(
	'https://httpbin.org/get'
)
>                                  {{Make a GET request to the specified URL}} 
    `response = requests.get(
	'https://httpbin.org/get',
	params={'foo': 'bar'}
)
>                                  {{Make a GET request to the specified URL with the params key:value pairs as URL-encoded GET parameters}} 

$ POST
    `response = requests.post(
	'https://httpbin.org/post',
	data={'foo': 'bar'}
)
>                                  {{Make a POST request to the specified URL with data key:value pairs as form-encoded data. Passing a string instead of a dictionary passes the data as-is}} 

$ Headers and Cookies
    `response = requests.get(
	'https://httpbin.org/get',
	headers={'user-agent': 'binbot'}
	cookies={'chocolate': 'chip'}
)
>                                  {{Add headers and cookies as dictionaries to requests via keyword arguments}} 
    `response.headers              {{Get a Python dictionary of response header name:value pairs}} 
    `response.cookies              {{Get a Python dictionary of response cookie name:value pairs}} 

$ Responses
    `response.status_code          {{Get the HTTP status code of the response}} 
    `response.text                 {{Get the response as decoded text}} 
    `response.json                 {{Get a Python dictionary representation of the response's JSON}} 

$ Other Methods
    `requests.put
requests.delete
requests.head
requests.options
>                                  {{Requests similarly supports other HTTP methods}} 

$ Sessions
    `session = requests.Session()
session.cookies['stay-logged-in'] = 'true'
session.get('https://httpbin.org/get')
...
>                                  {{Maintain a session with session objects that have a similar API to the requests module}} 

$ Authentication
    `repsonse = requests.get(
	'https://httpbin.org/basic-auth/foo/bar',
	auth=('foo', 'bar')
)
>                                  {{Basic HTTP authentication. Requests supports a few other methods and has an API for building custom authentication types}} 

