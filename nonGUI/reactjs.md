# React

> Source: https://facebook.github.io/react/docs/getting-started.html

> Aliases: react-js, react, react.js

$ ReactDOM
    `ReactDOM.render(<MyComponent />, document.getElementById('container'));
>                                  {{Renders MyComponent into element with id 'container' and returns a reference to the component}} 
    `ReactDOM.findDOMNode(componentRef);
>                                  {{Returns the corresponding DOM element if the component has been mounted}} 
    `ReactDOM.unmountComponentAtNode(document.getElementById('MyComponent'))
>                                  {{Remove a mounted React component from the DOM and clean up its event handlers and state}} 
    `ReactDOMServer.renderToString(<MyComponent />);
>                                  {{Render a ReactElement to its initial HTML. This should only be used on the server.}} 

$ Component
    `this.setState({someKey: 'a new value'});
>                                  {{Performs a shallow merge of nextState into current state and triggers UI updates}} 
    `this.forceUpdate();           {{Causes render() to be called on the component, skipping shouldComponentUpdate()}} 

$ Component Specifications
    `render: function ()           {{This is a required method that returns a DOM Element to be rendered}} 
    `statics: { }                  {{This allows to define static methods that can be called on the component class}} 
    `displayName: "MyComponent"    {{The displayName string is used in debugging messages}} 

$ Lifecycle Methods
    `componentWillMount: function ()
>                                  {{Invoked once, both on the client and server, immediately before the initial rendering occurs}} 
    `componentDidMount: function ()
>                                  {{Invoked once, only on the client (not on the server), immediately after the initial rendering}} 
    `componentWillReceiveProps: function (nextProps)
>                                  {{Invoked when component is receiving props, not for initial 'render'}} 
    `shouldComponentUpdate: function (nextProps, nextState)
>                                  {{Invoked before rendering with new props, not for initial 'render'}} 
    `componentDidUpdate: function (prevProps, prevState)
>                                  {{Invoked immediately after DOM updates, not for initial 'render'}} 
    `componentWillUnmount: function ()
>                                  {{Invoked immediately before a component is unmounted from the DOM}} 

$ Prop Validation
    `optionalArray: React.PropTypes.array,
>                                  {{An optional array property for the component}} 
    `requiredBoolean: React.PropTypes.bool.isRequired
>                                  {{A required boolean property for the component}} 
    `requiredFunction: React.PropTypes.func.isRequired
>                                  {{A required function property for the component}} 

$ Test Utilities
    `TestUtils.Simulate.click(DOMElement element, [object eventData]);
>                                  {{Simulate an event dispatch on a DOM node with optional eventData event data}} 
    `var componentTree = TestUtils.renderIntoDocument(ReactElement instance)
>                                  {{Render a component into a detached DOM node in the document}} 
    `TestUtils.isElement(ReactElement element)
>                                  {{Returns true if element is any ReactElement}} 
    `TestUtils.isElementOfType(ReactElement element, function componentClass)
>                                  {{Returns true if element is a ReactElement whose type is of a React componentClass}} 
    `TestUtils.isDOMComponent(ReactComponent instance)
>                                  {{Returns true if instance is a DOM component}} 

