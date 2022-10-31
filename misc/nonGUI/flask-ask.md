# Flask-Ask

> Source: https://alexatutorial.com/flask-ask/

> Aliases: flask-alexa-skill-kit, python-flask-ask

$ Installation
    `pip install flask-ask         {{Installs flask-ask}} 

$ Minimal Voice User Interface
    `Filename: app.pyfrom flask import Flask, render_template
from flask_ask import Ask, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.intent('HelloIntent')
def hello(firstname):
	text = render_template('hello', firstname=firstname)
	return statement(text).simple_card('Hello', text)

if __name__ == '__main__':
	app.run(debug=True)
>                                  {{Sample minimal viable code}} 
    `Filename: templates.yamlhello: Hello, {{ firstname }}
>                                  {{Jinja template loader}} 

$ Handling Requests
    `@ask.launch
def launched():
	return question('Welcome to Foo')
>                                  {{The launch decorator handles launch requests}} 
    `@ask.intent('HelloWorldIntent')
def hello():
	return statement('Hello, world')
>                                  {{The intent decorator handles intent requests}} 
    `@ask.session_ended
def session_ended():
	return "", 200
>                                  {{The session_ended decorator is for the session ended request}} 
    `@ask.on_session_started
def new_session():
	log.info('new session started')
>                                  {{Launch and intent requests can both start sessions. Avoid duplicate code with the on_session_started callback}} 
    `@ask.intent('WeatherIntent', mapping={'city': 'City'})
def weather(city):
	return statement('I predict great weather for {}'.format(city))
>                                  {{Tell Flask-Ask when slot and view function parameter names differ with mapping}} 
    `@ask.intent('HelloIntent', default={'name': 'World'})
def hello(name):
	return statement('Hello, {}'.format(name))
>                                  {{Use the default parameter for default values instead of None}} 

$ Converting Slots Values to Python Data Types
    `@ask.intent('AddIntent', convert={'x': int, 'y': int})
def add(x, y):
	z = x + y
	   return statement('{} plus {} equals {}'.format(x, y, z))
>                                  {{Above, x and y will both be passed to int() and thus converted to int instances.}} 
    `convert={'the_date': 'date'}  {{Converts '2015-11-24', '2015-W48-WE', or '201X' into a datetime.date}} 
    `convert={'appointment_time': 'time'}
>                                  {{Converts '06:00', '14:15', or '23:59' into a datetime.time.}} 
    `convert={'ago': 'timedelta'}  {{Converts 'PT10M', 'PT45S', or 'P2YT3H10M' into a datetime.timedelta.}} 
    `"slots": {
	"age": {
		"name": "age",
		"value": "?"
	}
}from flask_ask import statement, question, convert_errors

@ask.intent('AgeIntent', convert={'age': int})
def say_age(age):
	if 'age' in convert_errors:
		# since age failed to convert, it keeps its string
		# value (e.g. "?") for later interrogation.
		return question("Can you please repeat your age?")
	# conversion guaranteed to have succeeded
	# age is an int
	return statement("Your age is {}".format(age))
>                                  {{Handling Conversion Errors}} 

$ Context Locals
    `from flask import App, request, session
from flask_ask import (
	Ask,
	request as ask_request,
	session as ask_session,
	version
)
>                                  {{Use both Flask and Flask-Ask context locals in the same module}} 

$ Building Response
    `@ask.intent('SampleStatement')
def all_your_base():
	return statement('This is a smaple statement.')
>                                  {{Statement closes the session}} 
    `@ask.intent('SampleQuestion')
def make_appointment():
	return question("What is foo?") \
.reprompt("Reprompting. What is foo?")
>                                  {{Asking with question prompts the user for a response while keeping the session open with a reprompt}} 
    `session.attributes['date'] = date
>                                  {{Session management: stores session date variable}} 
    `@ask.intent('SampleSimpleCardIntent')
def all_your_base():
	return statement('Sample simple card') \
.simple_card(title='CATS says...', content='Make your time')
>                                  {{Simple cards display a title and message}} 
    `@ask.intent('SampleStandardCardIntent')
def all_your_base():
	return statement('Sample Standard card') \
.standard_card(title='CATS says...',
text='Make your time',
          small_image_url='https://example.com/small.png',
                      large_image_url='https://example.com/large.png')
>                                  {{Standard cards are like simple cards but they also support small and large image URLs}} 

