# Ember.js

> Source: https://guides.emberjs.com/v2.3.0/

> Aliases: ember.js

$ Basics
    `App.Router.map(fn)            {{Allows to add routes and resources to app}} 
    `App.advanceReadiness()        {{Call this function when app is ready to be initialized}} 
    `App.deferReadiness()          {{Delays initialization until advanceReadiness is called}} 
    `App.inject(type, property, injection)
>                                  {{Add a property onto every object of a specific type}} 

$ Ember.Application
    `Ember.Application.create: (   {{Creates an instance that will be app and app's namespace}} 
    `LOG_ACT/IVE_GENERATION: true  {{Activate logging of automatically generated routes and controllers}} 
    `LOG_STACKTRACE_ON_DEPRECATION: true
>                                  {{Activate logging of deprecated method or property usage}} 
    `LOG_TRANSITIONS: true         {{Activate basic logging of successful transitions}} 

$ Ember.View
    `attributeBindings: 'dataSize', 'href'
>                                  {{Array of View's property names used to calculate View's DOM element's attributes}} 
    `classNameBindings: 'isAvailable', 'color'
>                                  {{Array of View's property names used to calculate View's DOM element's class attribute}} 
    `classNames: 'color', 'size'   {{Array or string of View's class attribute}} 
    `Controller: Ember.Controller.create()
>                                  {{CONVERT(expression, datatype)}} 

$ Ember.Application.initializer
    `after: 'someInitializer'      {{Name of the initializer to run before running this initializer}} 
    `name: 'preload'               {{Name for this initializer}} 
    `initialize: function(container, application)
>                                  {{Function to execute when an app is initializing}} 

$ Ember.Route
    `beforeModel: function(transition)
>                                  {{Hook executed before resolving models}} 
    `activate: function            {{Hooked called when router enters route the first time}} 
    `afterModel: function          {{Hooked called after models are resolved}} 
    `deactivate: function          {{Hook executes when the router completely exits this route}} 
    `model: function               {{Provides data to be used by the controller and the view}} 
    `renderTemplate: function      {{Hook to override default template rendered for this route}} 
    `serialize: function(          {{Converts model into parameters for the url}} 
    `setupController: function     {{Function that can be used to configure the controller}} 
    `actions                       {{Object with properties}} 
    `actions: { willTransition: function(transition) }
>                                  {{Called whenever transition triggered on current route}} 

$ Ember.Object
    `init: function()              {{Method called when an instance of this class is created}} 

