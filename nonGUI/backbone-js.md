# Backbone.js

> Source: http://backbonejs.org/

> Aliases: backbonejs, backbone, backbone.js

$ Events
    `object.on(event, callback, [context])[context])
>                                  {{Bind a callback function to an object}} 
    `object.off([event], [callback], [context])
>                                  {{Remove a previously-bound callback function from an object}} 
    `object.trigger(event, [*args])
>                                  {{Trigger callbacks for the given event, or space-delimited list of events}} 

$ Model
    `Backbone.Model.extend(properties, [classProperties])
>                                  {{Extend Backbone.Model to create a Model class}} 
    `new Model([attributes])       {{Create an instance of Model and pass attributes to Model}} 
    `model.get(attribute)          {{Get the current value of an attribute from the model}} 
    `model.set(attributes, [options])
>                                  {{Set a hash of attributes (one or many) on the model}} 
    `model.has(attribute)          {{Returns true if the attribute is set to a non-null or non-undefined value}} 
    `model.unset(attribute, [options])
>                                  {{Remove an attribute by deleting it from the internal attributes hash}} 
    `model.clear([options])        {{Removes all attributes from the model}} 
    `model.id                      {{A special property of models, the id is an arbitrary string (integer id or UUID)}} 
    `model.toJSON()                {{Return a copy of the model's attributes for JSON stringification}} 
    `model.fetch([options])        {{Resets the model's state from the server}} 
    `model.save([attributes], [options])
>                                  {{Save a model to your database (or alternative persistence layer), by delegating to Backbone.sync}} 
    `model.destroy([options])      {{Destroys the model on the server by delegating an HTTP DELETE request to Backbone.sync.}} 

$ Collection
    `Backbone.Collection.extend(properties, [classProperties])
>                                  {{Extend Backbone.Collection to create a Collection class}} 
    `collection.model              {{Override this property to specify the model class that the collection contains}} 
    `new Collection([models], [options])
>                                  {{Create a Collection instance passing array of models and comparator function as options}} 
    `collection.models             {{Raw access to the JavaScript array of models inside of the collection}} 
    `collection.toJSON()           {{Return an array containing the attributes hash of each model in the collection}} 
    `collection.add(models, [options])
>                                  {{Add a model (or an array of models) to the collection}} 
    `collection.remove(models, [options])
>                                  {{Remove a model (or an array of models) from the collection}} 
    `collection.length             {{Returns the numbers of models it contains}} 
    `collection.comparator         {{A function used to maintain the collection in sorted order}} 
    `collection.sort([options])    {{Force a collection to re-sort itself}} 
    `collection.url or collection.url()
>                                  {{Set the url property (or function) on a collection to reference its location on the server}} 
    `collection.fetch([options])   {{Fetch the default set of models for this collection from the server, resetting the collection when}} 

$ Router
    `Backbone.Router.extend(properties, [classProperties])
>                                  {{Define actions that are triggered when certain URL fragments are matched}} 
    `router.routes                 {{The routes hash maps URLs with parameters to functions on your router}} 
    `new Router([options])         {{Create a new router passing its route hash directly as an option}} 
    `router.route(route, name, [callback])
>                                  {{Manually create a route for the router}} 
    `router.navigate(fragment, [options])
>                                  {{Call navigate in order to update the URL}} 

$ History
    `Backbone.history.start([options])
>                                  {{Call Backbone.history.start() to begin monitoring hashchange events, and dispatching routes}} 

$ View
    `Backbone.View.extend(properties, [classProperties])
>                                  {{Extend Backbone.View to create a View class}} 
    `new View([options])           {{Create a new view while passing the options like 'el', 'model', 'collection','id'}} 
    `view.el                       {{el is the DOM element of the view}} 
    `view.$el                      {{A cached jQuery (or Zepto) object for the view's element}} 
    `view.attributes               {{A hash of attributes that will be set as HTML DOM element attributes on the view's el}} 
    `view.render()                 {{Override this function with your code that renders the view template from model data, and updates this.el with the new HTML}} 
    `view.remove()                 {{Convenience function for removing the view from the DOM}} 
    `delegateEvents([events])      {{Uses jQuery's delegate function to provide declarative callbacks for DOM events within a view}} 
    `undelegateEvents()            {{Removes all of the view's delegated events}} 

$ Utility
    `var backbone = Backbone.noConflict();
>                                  {{Returns the Backbone object back to its original value}} 
    `Backbone.setDomLibrary(jQueryNew);
>                                  {{Tell Backbone to use a particular object as it's DOM / Ajax library}} 

