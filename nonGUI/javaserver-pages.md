# JavaServer Pages

> Source: http://overapi.com/jsp

> Aliases: jsp

$ Directives
    `<%@ page attribute="value" %> {{Defines page wide attributes 'value' is a string literal in single or double quotes}} 
    `<%@page language = "javascript" %>
>                                  {{The scripting language of a JSP page defaults to Java. The page directive can be used to configure the page to use any language that can call Java objects}} 
    `<%@ include file = "path" %>  {{Inserts content of specified file into a JSP page at the time of translation into a servlet}} 
    `<%@ taglib uri="tagLibraryURI" prefix="tagPrefix" %>
>                                  {{Defines a custom tag library used by a JSP page}} 
    `<tagPrefix:tagName>
...
</tagPrefix:tagName>
>                                  {{Use a tag implemented in the tag library as <prefix:tagname>, the prefix is the same as the prefix specified in the taglib directive}} 

$ Scripting Elements
    `<%! declaration %>            {{Creates page-wide definitions such as variables}} 
    `<% script code %>             {{Contains a block of scripting code A JSP page can contain multiple blocks of scripting code}} 
    `<%= expression %>             {{Defines expressions evaluated on the server before sending the page output to the client}} 
    `<%-- Comment string --%>      {{A JSP comment is not output to the client as part of the JSP page’s output}} 

$ Actions
    `<jsp:include page="path" flush="true"/>
>                                  {{jsp:include calls one JSP page from anotherUpon completion, the destination page returns control to the calling page}} 
    `<jsp:forward page="path" />   {{jsp:forward calls one JSP page from another Execution of the calling page is terminated by the call}} 
    `<jsp:plugin type="applet" codebase="dirname" code="MyAppletclass">
	...
</jsp:plugin>
>                                  {{jsp:plugin enables the invoking an applet on a client browser}} 
    `<jsp:useBean id="name" class="package.class" />
>                                  {{jsp:useBean defines an instance of a Java bean}} 
    `<jsp:setProperty name="beanName" property="someProperty" />
>                                  {{Sets the value of one or more properties in a bean, regardless of whether the bean is existing or new}} 
    `<jsp:useBean id="beanName">
...
	<jsp:setProperty name="beanName" 
	property="someProperty" />
</jsp:useBean>
>                                  {{The jsp:setProperty is executed only if a new object was instantiated, not if an existing one was found}} 
    `<jsp:getProperty name="beanName" property="propertyName" />
>                                  {{Writes the value of a bean property as a string to the out object}} 

$ Implicit Objects (Pre-defined values)
    `config(Type:javax.servlet.ServletConfig)
>                                  {{The ServletConfig object for the JSP page}} 
    `application(Type:javax.servlet.ServletContext)
>                                  {{The servlet context obtained from the servlet configuration object}} 
    `exception(Type:java.lang.Throwable)
>                                  {{The uncaught exception that resulted in the error page being invoked}} 
    `out(Type:javax.servlet.jsp.JspWriter)
>                                  {{An object that writes into a JSP page’s output stream}} 
    `pageContext(Type:javax.servlet.jspPageContext)
>                                  {{The page context for the JSP, it is intended as a means to access information about the page while avoiding most of the implementation details}} 
    `request(Type:javax.servlet.HttpServletRequest)
>                                  {{The client request}} 
    `response(Type:javax.servlet.HttpServletResponse)
>                                  {{The response to the client}} 
    `session(Type:javax.servlet.http.HttpSession)
>                                  {{The session object created for the requesting client}} 

