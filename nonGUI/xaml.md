# XAML

> Source: http://www.cheat-sheets.org/saved-copy/wpfcheatsheet.pdf

> Aliases: xaml-layout, xaml-resources, xaml-snippets, xaml-data-binding, xaml-styles-and-triggers, xaml-for-wpf, xaml-transforms, xaml-brushes

$ Data Binding
    `Binding                       {{Binds the current DataContext}} 
    `Binding propertyName          {{Binds the property of the current DataContext}} 
    `Binding Source=StaticResourceresName
>                                  {{Binds to a staticresource such as a string}} 
    `Binding ElementName= elementName, Path= propertyName
>                                  {{Binds to the property of the given element}} 
    `TemplateBindingpropertyName   {{Binds to the template parents given property inside a ControlTemplate}} 
    `<XmlDataProvider x:Key="name" Source="filePath" />
>                                  {{Added to resources to allow xml data binding}} 
    `IsSynchronizedWithCurrentItem="True"
>                                  {{Synchronizes elements bound to same data source}} 

$ Styles and Triggers
    `<Style x:Key=”styleName”>     {{Style applied to elements that set this style}} 
    `<SetterProperty=”propertyName”Value=”value”/>
>                                  {{Setter sets a property of the current target type}} 
    `<Style.Triggers>              {{Holds Triggers to set a style dependant on event}} 
    `<Trigger Property=”propertyName” Value=”value”>
>                                  {{Triggered when dependency property is set}} 
    `<DataTriggerBinding="BindingPath=propertyName"Value="theValue">
>                                  {{Triggered when bound value is set}} 
    `<EventTriggerRoutedEvent=”eventName”>
>                                  {{Triggered when the given routed event is fired}} 

$ Resources
    `<element Name.Resources>      {{Holds resources accessible to anything under the element}} 
    `<system:String x:Key="resName">stringValue </system:String>
>                                  {{Creates a string resource}} 
    `<SolidColorBrush x:Key="resName"Color="colourValue" />
>                                  {{Placed inside Resources tag, creates a resource with the value}} 
    `StaticResource                {{Applied once, when needed}} 
    `DynamicResource               {{Applied as the resources changes}} 
    `Fill="StaticResourceresName"  {{Sets fill to the resource}} 

$ Transforms
    `LayoutTransform               {{Holds transform or group, executed before layout, moves surrounding elements}} 
    `RenderTransform               {{Holds transform or group executed before layout, create overlapping elements}} 
    `TransformGroup                {{Used to hold multiple transforms}} 
    `RotateTransform               {{Rotates the given element by setting Angle, CenterX and CenterY}} 
    `TranslateTransform            {{Moves elements based on X and Y}} 
    `SkewTransform                 {{Skews the given element using AngleX AngleY, CenterX and CenterY}} 
    `MatrixTransform               {{Complex transform based on matrix}} 

$ Brushes
    `SolidColorBrush               {{A solid colour brush}} 
    `LinearGradientBrush           {{Gradient brush using GradientStops}} 
    `RadialGradientBrush           {{Gradient radiating out from a point}} 
    `ImageBrush                    {{Brush from an ImageSource}} 
    `DrawingBrush                  {{Brush based on a given GeometryDrawing}} 
    `VisualBrush                   {{Brush using a visual elements image}} 

$ Layout
    `Window                        {{Primary container for windows applications}} 
    `Page                          {{Container with navigation support}} 
    `StackPanel                    {{Horizontal or Vertical stacking of elements}} 
    `Grid                          {{Grid layout via Grid.Row and Grid.Column}} 
    `Canvas                        {{Arrange elements using X and Y co-ordinates}} 
    `WrapPanel                     {{Horizontal or Vertical wrapping of visual elements as space is available}} 
    `DockPanel                     {{Dock elements via DockPannel.Dock}} 

