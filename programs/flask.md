# Flask

> Source: http://flask.pocoo.org/

> Aliases: python-flask

$ Get Flask
    `pip install flask             {{Installs flask}} 

$ Minimum Viable Example
    `from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
		return 'hello world'

if __name__ == "__main__":
		app.run()
>                                  {{A bare bones flask example}} 

$ Start Flask
    `from flask import Flask       {{Imports Flask into current namespace}} 
    `app = flask(__name__)         {{Class Instanciation. __name__ parameter is the application module or package}} 
    `if __name__ == "__main__":
		app.run()
>                                  {{If involked directly, execute}} 

$ Creating Pages
    `@app.route('/')
def index():
		return 'hello, world'
>                                  {{Renders the text 'hello, world' in the browser}} 
    `from flask import Flask, render_template

..

@app.route('/')
def index():
		return render_template('index.html')

..
>                                  {{Renders the template templates/index.html in the browser}} 

