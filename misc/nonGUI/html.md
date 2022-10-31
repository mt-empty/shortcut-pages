# HTML Elements

> Source: https://developer.mozilla.org/en-US/docs/Web/HTML/Element

> Aliases: html5, html-5

$ Document Metadata
    `<head>                        {{Provides metadata about the document, including its title, scripts and style sheets}} 
    `<link>                        {{Specifies a link to an external resource, typically style sheets}} 
    `<meta>                        {{Any metadata information that cannot be represented by one of the other HTML meta-related elements (<base>, <link>, <script>, <style> or <title>)}} 
    `<style>                       {{Contains style information for a document written in CSS}} 
    `<title>                       {{Defines the title of the document, shown in a browser's title bar or on the page's tab}} 

$ Content Sectioning
    `<body>                        {{Represents the content of a document. There can only be one <body> element in a document}} 
    `<footer>                      {{Represents a footer typically containing copyright data or links to related documents}} 
    `<header>                      {{Represents a group of elements like a logo, a search form, and navigation bar}} 
    `<h1>, <h2>, <h3>, <h4>, <h5>, <h6>
>                                  {{A heading element briefly describes the topic of the section it introduces. <h1> is the most important and <h6> is the least}} 
    `<nav>                         {{Represents a section of a page that links to other pages or to parts within the page}} 
    `<article>                     {{Specifies independent, self-contained content}} 

$ Text Content
    `<div>                         {{A generic container for flow content. It can be used to group elements for styling purposes (using the class or id attributes)}} 
    `<hr>                          {{Represents a thematic break between paragraphs, defined in semantic rather than presentational terms}} 
    `<li>                          {{Represents an item in a list and must be contained in a parent element: an ordered list (<ol>), an unordered list (<ul>), or a menu (<menu>)}} 
    `<ol>                          {{Represents an ordered list of items, typically displayed with a sequencial numbering}} 
    `<p>                           {{Represents a paragraph of text}} 
    `<pre>                         {{Represents preformatted text (i.e. text that is displayed without text formatting)}} 
    `<ul>                          {{Represents an unordered list of items, typically displayed with a bullet}} 
    `<address>                     {{Defines the contact information for the author/owner of a document or an article}} 

$ Inline Text Semantics
    `<a>                           {{Defines a hyperlink to a location on the same page or any other page on the Web}} 
    `<b>                           {{Represents a span of text whose typical presentation would be boldfaced}} 
    `<br>                          {{Produces a line break in text (carriage-return)}} 
    `<code>                        {{Represents a fragment of computer code and displayed in the browser's default monospace font}} 
    `<em>                          {{Marks text that has stress emphasis. The <em> element can be nested, with each level of nesting indicating a greater degree of emphasis}} 
    `<i>                           {{Represents a range of text that is typically displayed in italic type}} 
    `<s>                           {{Renders text with a strikethrough, or a line through it}} 
    `<span>                        {{A generic inline container for phrasing content It can be used to group elements for styling purposes (using the class or id attributes)}} 
    `<strong>                      {{Gives text strong importance, and is typically displayed in bold}} 
    `<u>                           {{Renders text with an underline, a line under the baseline of its content}} 

$ Images and Multimedia
    `<area>                        {{Defines a hot-spot region on an image, and optionally associates it with a hypertext link. This element is used only within a <map> element}} 
    `<audio>                       {{Used to embed sound content in documents}} 
    `<img>                         {{The HTML Image Element (<img>) represents an image of the document}} 
    `<map>                         {{Used with <area> elements to define an image map (a clickable link area)}} 
    `<track>                       {{Used as a child of <audio> and <video> elements. It lets you specify timed text tracks such as subtitles}} 
    `<video>                       {{The HTML <video> element is used to embed video content}} 

$ Table Content
    `<table>                       {{Represents tabular data}} 
    `<caption>                     {{Represents the title of a table}} 
    `<td>                          {{Defines a cell of a table that contains data}} 
    `<th>                          {{Defines a cell that is a header for a group of cells of a table}} 
    `<tr>                          {{Defines a row of cells in a table. Those can be a mix of <td> and <th> elements}} 

$ Forms
    `<button>                      {{Represents a clickable button}} 
    `<datalist>                    {{Contains a set of <option> elements that represent the values available for other controls}} 
    `<fieldset>                    {{Used to group several controls as well as labels (<label>) within a web form}} 
    `<form>                        {{Represents the parent element of a web form in a document section}} 
    `<input>                       {{Used to create interactive controls to accept data from the user}} 
    `<label>                       {{Represents a caption for an item in a user interface. A control element can be placed inside a <label> element, or by using the for attribute}} 
    `<legend>                      {{Represents a caption for the content of its parent <fieldset>}} 
    `<optgroup>                    {{Creates a grouping of options within a <select> element}} 
    `<option>                      {{Used to create a control representing an item within a <select>, an <optgroup> or a <datalist> element}} 
    `<output>                      {{Represents the result of a calculation or user action}} 
    `<select>                      {{Represents a control that presents a menu of options. The options within the menu are represented by <option> elements, which can be grouped by <optgroup> elements}} 
    `<textarea>                    {{Represents a multi-line plain text editing control}} 

$ Embedded Content
    `<embed>                       {{Represents an integration point for an external application or interactive content}} 
    `<iframe>                      {{Represents a nested browsing context, effectively embedding another HTML page into the current page}} 
    `<object>                      {{Represents an external resource, which can be treated as an image, a nested browsing context, or a resource to be handled by a plugin}} 
    `<param>                       {{Defines parameters for <object>}} 
    `<source>                      {{An empty element used to specify multiple media resources for <picture>, <audio> and <video> elements}} 

$ Scripting
    `<canvas>                      {{Used to draw graphics, photo compositions or animations via scripting, typically written in JavaScript}} 
    `<noscript>                    {{Defines a section of HTML to be inserted if a script type on the page is unsupported or if scripting is currently turned off in the browser}} 
    `<script>                      {{Used to embed or reference an executable script, typically written in JavaScript}} 

