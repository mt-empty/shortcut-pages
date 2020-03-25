# Flexbox

> Source: https://css-tricks.com/snippets/css/a-guide-to-flexbox/

> Aliases: css-flexbox, flexbox-properties, flexbox-guide, flex-box

$ Display
    `display: flex;                {{Defines a flex container and enables a flex context for all its direct children}} 

$ Flex-Direction
    `flex-direction:               {{This establishes the main-axis, thus defining the direction flex items are placed in the flex container}} 
    `row;                          {{Left to right in ltr; right to left in rtl (default)}} 
    `column;                       {{Same as row but top to bottom}} 
    `row-reverse;                  {{Right to left in ltr; left to right in rtl}} 
    `col-reverse;                  {{Same as row-reverse but bottom to top}} 

$ Justify-Content
    `justify-content:              {{This defines the alignment along the main axis}} 
    `flex-start;                   {{(default) Items are packed toward the start line}} 
    `flex-end;                     {{Items are packed toward to end line}} 
    `center;                       {{Items are centered along the line}} 
    `space-between;                {{Items are evenly distributed in the line; first item is on the start line, last item on the end line}} 
    `space-around;                 {{Items are evenly distributed in the line with equal space around them}} 

$ Align-Items
    `align-items:                  {{This defines the default behaviour for how flex items are laid out along the cross axis on the current line}} 
    `flex-start                    {{Cross-start margin edge of the items is placed on the cross-start line}} 
    `flex-end                      {{Cross-end margin edge of the items is placed on the cross-end line}} 
    `center                        {{Items are centered in the cross-axis}} 
    `baseline                      {{Items are aligned such as their baselines align}} 
    `stretch                       {{(default) Stretch to fill the container (still respect min-width/max-width)}} 

$ Flex-Wrap
    `flex-wrap:                    {{Flex items will all try to fit onto one line. You can change that and allow the items to wrap as needed with this property}} 
    `nowrap                        {{(default) Single-line - left to right in ltr; right to left in rtl}} 
    `wrap                          {{Multi-line - left to right in ltr; right to left in rtl}} 
    `wrap-reverse                  {{Multi-line - right to left in ltr; left to right in rtl}} 

