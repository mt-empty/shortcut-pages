# Latex

> Source: https://en.wikibooks.org/wiki/LaTeX

> Aliases: tex-doc, tex-document-writing, latex-doc, tex, latex-document-writing, tex-writing, latex-doc-writing, latex-writing, latex-document, tex-doc-writing

$ Relation operators
    `<                             {{Is less than}} 
    `\nless                        {{Is not less than}} 
    `\leq                          {{Is less than or equal to}} 
    `\nleq                         {{Is not less than or equal to}} 
    `\prec                         {{Precedes}} 
    `\preceq                       {{Precedes or equals}} 
    `>                             {{Is greater than}} 
    `\ngtr                         {{Is not greater than}} 
    `\geq                          {{Is greater than or equal to}} 
    `\ngeq                         {{Is not greater than or equal to}} 
    `\succ                         {{Succeeds}} 
    `\succeq                       {{Succeeds or equals}} 
    `\neq                          {{Is not equal to}} 
    `\equiv                        {{Is equivalent to}} 
    `\approx                       {{Is approximately}} 
    `\cong                         {{Is congruent to}} 
    `\sim                          {{Is similar to}} 

$ Unary operators
    `+                             {{Addition}} 
    `-                             {{Negation}} 
    `\neg                          {{Not}} 
    `!                             {{Factorial}} 
    `\#                            {{Primorial}} 

$ Binary operators
    `\pm                           {{Plus or minus}} 
    `\mp                           {{Minus or plus}} 
    `\times                        {{Multiplied by}} 
    `\div                          {{Divided by}} 
    `\ast                          {{Asterisk}} 

$ Negated binary operators
    `\neq                          {{Not equal to}} 
    `\nless                        {{Not less than}} 
    `\nprec                        {{Does not precede}} 
    `\npreceq                      {{Neither precedes nor equals}} 
    `\nsim                         {{Is not similar to}} 
    `\ngtr                         {{Is not greater than}} 
    `\nsucc                        {{Does not succeed}} 
    `\nsucceq                      {{Neither succedes nor equals}} 
    `\ncong                        {{Is not congruent to}} 
    `\nparallel                    {{Is not parallel with}} 

$ Set notation
    `\N                            {{Set of natural numbers}} 
    `\Z                            {{Set of integers}} 
    `\Q                            {{Set of rational numbers}} 
    `\R                            {{Set of real numbers}} 
    `\C                            {{Set of complex numbers}} 
    `\in                           {{Is a member of}} 
    `\notin                        {{Is not a member of}} 
    `\ni                           {{Owns(has member)}} 
    `\subseteq                     {{Is subset of}} 
    `\supseteq                     {{Is superset of}} 
    `\cup                          {{Set union}} 
    `\cap                          {{Set intersection}} 
    `\forall                       {{For all}} 
    `\neq                          {{Logical not}} 
    `\lor                          {{Logical or}} 
    `\land                         {{Logical and}} 
    `\exists                       {{There exists at least one}} 
    `\nexists                      {{There exist none}} 

$ Geometry
    `\angle                        {{Angle}} 
    `\triangle                     {{Triangle}} 
    `\|                            {{Is parallel with}} 
    `\perp                         {{Is perpendicular to}} 
    `\not\perp                     {{Is not perpendicular to}} 
    `\square                       {{Square}} 

$ Delimiters
    `|                             {{Divides}} 
    `\lceil                        {{Ceiling(left)}} 
    `\rceil                        {{Ceiling(right)}} 
    `\lfloor                       {{Floor(left)}} 
    `\rfloor                       {{Floor(right)}} 

$ Trignometric functions
    `\sin                          {{Sin}} 
    `\arcsin                       {{Sin inverse}} 
    `\cos                          {{Cos}} 
    `\arccos                       {{Cos inverse}} 
    `\tan                          {{Tan}} 
    `\arctan                       {{Tan inverse}} 
    `\csc                          {{Cosec}} 
    `\arccsc                       {{Cosec inverse}} 
    `\sec                          {{Sec}} 
    `\arcsec                       {{Sec inverse}} 
    `\cot                          {{Cot}} 
    `\arccot                       {{Cot inverse}} 

$ Other functions
    `\partial                      {{Partial derivative}} 
    `\hbar                         {{Reduced Planck's constant}} 
    `\Re                           {{Real part}} 
    `\Im                           {{Imaginary part}} 
    `\infty                        {{Infinity}} 
    `\aleph                        {{Aleph numbers}} 

$ Starting A New Document
    `\documentation{class}         {{Declares type of document you are writing; Must be at the top of document}} 
    `\begin{document}              {{Starts a document}} 
    `\end{document}                {{Ends a document}} 

$ Document Classes
    `article                       {{For short documents and journal articles. Is the most commonly used}} 
    `IEEEtran                      {{Articles with the IEEE Transactions format}} 
    `report                        {{Longer reports with several chapters, short books, thesis}} 
    `book                          {{Full length books}} 
    `letter                        {{Letter writing}} 
    `beamer                        {{Presentations and slides}} 

$ Title
    `\title{Document's title}      {{Title of document; Must go before \begin{document}}} 
    `\author{name}                 {{Author of document; Must go before \begin{document}}} 
    `\date{date}                   {{Date of document, Optional; Must go before \begin{document}}} 
    `\maketitle                    {{Produces title; Goes after \begin{document}}} 

$ Document Formatting
    `\\\                           {{Newline}} 
    `\pagebreak                    {{Begin new page}} 
    `\textbf{your text}            {{Bold text}} 
    `\underline{your text}         {{Underlined text}} 
    `\textit{your text}            {{Italicized text}} 
    `\verb|<your text>|            {{Verbatim text}} 
    `\par                          {{Starts a new paragraph}} 
    `%<your comment>               {{Add comment; Ignored by LaTex}} 
    `\begin{flushleft}<your text>\end{flushleft}
>                                  {{Left align text}} 
    `\begin{flushright}<your text>\end{flushright}
>                                  {{Right align text}} 
    `\begin{center}<your text>\end{center}
>                                  {{Center align text}} 

$ Lists
    `\begin{itemize}\item <your text> \end{itemize}
>                                  {{Create unordered list. Use enumerate instead of itemize for ordered list.}} 
    `\item                         {{All list entry must be preceded by \item}} 

$ Special Characters
    `\#                            {{Pound sign: #}} 
    `\$                            {{Dollar sign: $}} 
    `\%                            {{Percent sign: %}} 
    `\&                            {{Ampersand: &}} 

