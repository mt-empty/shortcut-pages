# CSS

> Source: http://www.w3schools.com/css/default.asp

> Aliases: cascading-style-sheets, style-sheet

$ Inserting Stylesheet
    `<link rel="stylesheet" type="text/css" href="style.css" />
>                                  {{External stylesheet}} 
    `<style type="text/css">selector {property: value;}</style>
>                                  {{Internal style}} 
    `<tag style="property: value"> {{Inline style}} 
    `@import url("style.css");     {{Import CSS}} 
    `@import url("style.css") list-of-media-queries;
>                                  {{Import CSS and apply only to the corresponding media type}} 

$ General Syntax
    `selector {property: value;}   {{Basic syntax of css declaration block}} 
    `selector:pseudo-class {property: value;}
>                                  {{Class selector selects and styles all elements having state defined by 'pseudo-class'}} 
    `.class                        {{Class selector selects and styles all elements with class="class"}} 
    `#id                           {{ID selector styles the element with id="id"}} 

$ General Properties
    `color:                        {{Changes foreground color}} 
    `cursor:                       {{Specifies appearance of the cursor}} 
    `display:                      {{Specifies the type of box used for an HTML element}} 
    `overflow:                     {{Specifies how content overflowing its box is handled}} 
    `visibility:                   {{Specifies whether or not an element is visible}} 

$ Font Properties
    `font-style:                   {{Specifies the font style for a text}} 
    `font-variant:                 {{Specifies whether or not a text should be displayed in a small-caps font}} 
    `font-weight:                  {{Sets how thick or thin characters in text should be displayed}} 
    `font-size:                    {{Sets the size of a font}} 
    `font-family:                  {{Specific font(s) to be used}} 

$ Text Properties
    `letter-spacing:               {{Increases or decreases the space between characters in a text}} 
    `line-height:                  {{Specifies the line height}} 
    `text-align:                   {{Specifies the horizontal alignment of text in an element}} 
    `text-decoration:              {{Specifies the decoration added to text}} 
    `text-indent:                  {{Specifies the indentation of the first line in a text-block}} 
    `text-transform:               {{Controls the capitalization of text}} 
    `vertical-align:               {{Sets the vertical alignment of an element}} 
    `word-spacing:                 {{Increases or decreases the white space between words}} 
    `direction:                    {{Changes the text direction of an element}} 

$ Box-Model Properties
    `height:                       {{Sets the height of an element}} 
    `width:                        {{Sets the width of an element}} 
    `margin:                       {{Defines the space around elements}} 
    `padding:                      {{Defines the space between the element border and the element content}} 

$ Position Properties
    `clear:                        {{Specifies on which sides of an element where floating elements are not allowed to float}} 
    `float:                        {{Specifies whether or not an element should float}} 
    `left:                         {{The left position of an element}} 
    `top:                          {{The top position of an element}} 
    `position:                     {{Specifies the type of positioning method used for an element}} 
    `z-index:                      {{Specifies the stack order of an element}} 

$ Background Properties
    `background-color:             {{Specifies the background color of an element}} 
    `background-image:             {{Specifies an image to use as the background of an element}} 
    `background-repeat:            {{Specify how image should be repeated (x or y axis)}} 
    `background-attachment:        {{Sets whether a background image is fixed or scrolls with the rest of the page}} 
    `background-position:          {{Sets the starting position of a background image.}} 

$ List Properties
    `list-style-type:              {{Specifies the type of list-item marker in a list}} 
    `list-style-position:          {{Specifies if the list-item markers should appear inside or outside the content flow}} 
    `list-style-image:             {{Replaces the list-item marker with an image}} 

