# Meteor

> Source: http://docs.meteor.com/#/full/

> Aliases: meteor-framework, meteor.js, meteorjs

$ Getting Started
    `meteor create <app-name>      {{Create a new Meteor app}} 
    `meteor npm install            {{Install basic npm packages in project}} 
    `meteor                        {{Run app on localhost}} 

$ Core
    `Meteor.isClient               {{True if running in client environment.}} 
    `Meteor.isServer               {{True if running in server environment.}} 
    `Meteor.startup(func)          {{Run code when a client or a server starts.}} 
    `Meteor.absoluteUrl(path, options)
>                                  {{Generate an absolute URL pointing to the application}} 
    `Meteor.settings               {{Object containing deployment-specific configuration options}} 
    `Meteor.release                {{A string containing the name of the release with which the project was built.It is undefined if the project was built using a git checkout of Meteor.}} 

$ Publish and Subscribe
    `Meteor.publish(name, func)    {{Publish a record set. Available on the server only}} 
    `Meteor.subscribe(name , arg1, arg2, …, callbacks)
>                                  {{Subscribe to a record set publish on the server. Returns a handle that provides stop() and ready() methods.Available on client.}} 

$ Methods
    `Meteor.methods(methods)       {{Defines functions that can be invoked over the network by clients.'methods' is an object of functions}} 
    `Meteor.call(name, arg1, arg2..., asyncCallback)
>                                  {{Invokes a method by passing it's name and any number of arguments as well as an option callback function.}} 
    `new Meteor.Error(error, reason, details)
>                                  {{This class represents a symbolic error thrown by a method.}} 
    `Meteor.apply(name, args, options, (Boolean), asyncCallback)
>                                  {{Invoke a method passing an array of arguments.It is just like Meteor.call, except that the method arguments are passed as an array rather than directly as arguments, and you can specify options about how the client executes the method.}} 

$ Check
    `check(value, pattern)         {{Check that a value matches a pattern. If the value does not match the pattern, throw a Match.Error.Particularly useful to assert that arguments to a function have the right types and structure.}} 
    `Match.test(value, pattern)    {{Returns true if the value matches the pattern.}} 

$ Server connections
    `Meteor.status()               {{This method returns an object containing the status of the connection between the client and the server.}} 
    `Meteor.reconnect()            {{Force an immediate reconnection attempt if the client is not connected to the server.}} 
    `Meteor.disconnect()           {{Disconnect the client from the server.While the client is disconnected it will not receive updates to collections, method calls will be queued until the connection is reestablished, and hot code push will be disabled.}} 
    `Meteor.onConnection(callback) {{Register a callback to be called when a new DDP connection is made to the server.}} 
    `DDP.connect(url)              {{Connect to the server of a different Meteor application to subscribe to its document sets and invoke its remote methods.}} 

$ Collections
    `new Mongo.Collection(name, options)
>                                  {{Constructor for a Collection}} 
    `collection.findOne(selector, options)
>                                  {{Finds the first document that matches the selector, as ordered by sort and skip options.}} 
    `collection.insert(doc, callback)
>                                  {{Insert a document in the collection. Returns its unique _id.}} 
    `collection.update(selector, modifier, options, callback)
>                                  {{Modify one or more documents in the collection. Returns the number of affected documents.}} 
    `collection.upsert(selector, modifier, options, callback)
>                                  {{Modify one or more documents in the collection, or insert one if no matching documents were found. Returns an object with keys numberAffected (the number of documents modified) and insertedId (the unique _id of the document that was inserted, if any).}} 
    `collection.remove(selector, callback)
>                                  {{Remove documents from the collection}} 
    `collection.allow(options)     {{Allow users to write directly to this collection from client code, subject to limitations you define.}} 
    `collection.deny(options)      {{Override allow rules.}} 
    `collection.rawCollection()    {{Returns the Collection object corresponding to this collection from the npm mongodb driver module which is wrapped by Mongo.Collection.}} 
    `collection.rawDatabase()      {{Returns the Db object corresponding to this collection's database connection from the npm mongodb driver module which is wrapped by Mongo.Collection.}} 

$ Templates
    `Template.myTemplate.events(eventMap)
>                                  {{Specify event handlers for this template.'myTemplate' is the value of the name attribute of a given HTML template element}} 
    `Template.myTemplate.helpers(helpers)
>                                  {{Specify template helpers available to this template.}} 
    `Template.myTemplate.onRendered
>                                  {{Register a function to be called when an instance of this template is inserted into the DOM.}} 
    `Template.myTemplate.onCreated {{Register a function to be called when an instance of this template is created.}} 
    `Template.myTemplate.onDestroyed
>                                  {{Register a function to be called when an instance of this template is removed from the DOM and destroyed.}} 
    `Template.body                 {{The template object representing your <body> tag.}} 

$ Command line
    `meteor help                   {{Get help on meteor command line usage. Running meteor help by itself will list the common meteor commands. Running meteor help command will print detailed help about the command.}} 
    `meteor run                    {{Run a meteor development server in the current project.}} 
    `meteor debug                  {{Run the project, but suspend the server process for debugging.}} 
    `meteor deploy <site>          {{Deploy the project in your current directory to Galaxy. Galaxy is a hosting service for meteor}} 
    `meteor update                 {{Attempts to bring you to the latest version of Meteor, and then to upgrade your packages to their latest versions}} 
    `meteor add <package>          {{Add packages to your Meteor project.}} 
    `meteor build                  {{Package this project up for deployment.}} 
    `meteor mongo                  {{Open a MongoDB shell on your local development database, so that you can view or manipulate it directly.}} 
    `meteor reset                  {{Reset the current project to a fresh state. Removes the local mongo database.}} 
    `meteor search                 {{Searches for Meteor packages and releases, whose names contain the specified regular expression.}} 
    `meteor shell                  {{Open a shell that is connected to a running meteor server. Serves as a REPL for your application}} 

