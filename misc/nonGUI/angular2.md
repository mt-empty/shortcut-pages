# Angular2

> Source: https://angular.io/docs/ts/latest/guide/cheatsheet.html

> Aliases: angularjs-2, angular-2

$ Bootstraping
    `bootstrap​(MyAppComponent, [MyService, provide(...)]);
>                                  {{Bootstraps an application with MyAppComponent as the root component and configures the DI providers}} 

$ Template Syntax
    `<input [value]="firstName">   {{Binds property value to the result of expression firstName}} 
    `<div [class.extra-sparkle]='isDelightful'>
>                                  {{Binds the presence of the CSS class extra-sparkle on the element to the truthiness of the expression isDelightful}} 
    `<div [style.width.px]="mySize">
>                                  {{Binds style property width to the result of expression mySize in pixels. Units are optional}} 
    `<button (click)="readRainbow($event)">
>                                  {{Calls method readRainbow when a click event is triggered on this button element (or its children) and passes in the event object}} 
    `<p>Hello {{greeting}}</p>     {{Binds text content to an interpolated string, e.g. "Hello World!"}} 
    `<my-cmp [(title)]="name">     {{Sets up two-way data binding. Equivalent to: <my-cmp \[title\]="name" (titleChange)="name=$event">}} 
    `<p *myUnless="myExpression">...</p>
>                                  {{The * symbol means that the current element will be turned into an embedded template}} 
    `<p>Employer: {{employer?.companyName}}</p>
>                                  {{The Elvis operator (?) means that the employer field is optional and if undefined, the rest of the expression should be ignored}} 

$ Built-in Directives
    `<section *ngIf="showSection"> {{Removes or recreates a portion of the DOM tree based on the showSection expression}} 
    `<li *ngFor="#item of list">   {{Turns the li element and its contents into a template, and uses that to instantiate a view for each item in list}} 
    `<div [ngClass]="{active: isActive, disabled: isDisabled}">
>                                  {{Binds the presence of CSS classes on the element to the truthiness of the associated map values. The right-hand side expression should return \{class-name: true/false\} map}} 

$ Forms
    `<input [(ngModel)]="userName">
>                                  {{Provides two-way data-binding, parsing and validation for form controls}} 

$ Class Decorators
    `@Component({...}) 
 class MyComponent() {}
>                                  {{Declares that a class is a component and provides metadata about the component}} 
    `@Pipe({...}) 
 class MyPipe() {}
>                                  {{Declares that a class is a pipe and provides metadata about the pipe}} 
    `@Injectable() 
 class MyService() {}
>                                  {{Declares that a class has dependencies that should be injected into the constructor when the dependency injector is creating an instance of this class}} 

$ Directive Configuration
    `selector: '.cool-button:not(a)'
>                                  {{Specifies a CSS selector that identifies this directive within a template. Supported selectors include element, \[attribute\], .class, and :not(). 
 Does not support parent-child relationship selectors}} 
    `providers: [MyService, provide(...)]
>                                  {{Array of dependency injection providers for this directive and its children}} 

$ Component Configuration
    `viewProviders: [MyService, provide(...)]
>                                  {{Array of dependency injection providers scoped to this component's view}} 
    `template: 'Hello {{name}}' 
 templateUrl: 'my-component.html'
>                                  {{Inline template / external template URL of the component's view}} 
    `styles: ['.primary {color: red}'] 
 styleUrls: ['my-component.css']
>                                  {{List of inline CSS styles / external stylesheet URLs for styling component’s view}} 
    `directives: [MyDirective, MyComponent]
>                                  {{List of directives used in the the component’s template}} 

$ Dependency Injection
    `provide(MyService, {useClass: MyMockService})
>                                  {{Sets or overrides the provider for MyService to the MyMockService class}} 
    `provide(MyService, {useFactory: myFactory})
>                                  {{Sets or overrides the provider for MyService to the myFactory factory function}} 
    `provide(MyValue, {useValue: 41})
>                                  {{Sets or overrides the provider for MyValue to the value 41}} 

