# Greensock

> Source: https://greensock.com/

> Aliases: web-animation

$ TweenLite
    `var $box = $('#box');         {{Selects the element}} 
    `var tween = TweenLite.to($box , 2 , x:100 , ease:Power1.easeInOut , delay:2 , onComplete:myFunction , onCompleteParams:element,'param2');
>                                  {{Creates a Tween}} 

$ Default Easing Functions
    `ease:Power0.easeNone          {{Linear}} 
    `ease:Power1, Power2, Power3, Power4   .easeIn .easeOut .easeInOut
>                                  {{Power options}} 
