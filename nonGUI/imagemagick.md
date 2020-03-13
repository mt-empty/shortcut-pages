# ImageMagick

> Source: http://www.imagemagick.org/script/command-line-tools.php

> Aliases: image-magick, mogrify

$ Size
    `convert -resize 100x100 in.png out.png
>                                  {{Resize image to fit a 100x100px box maintaining aspect ratio}} 
    `convert -crop 40x30+10+10 in.png out.png
>                                  {{Crop image to 40x30 with 10px offset in X and Y}} 

$ Transform
    `convert -flip in.png out.ong  {{Invert vertical}} 
    `convert -flop in.png out.ong  {{Invert horizontal}} 
    `convert -transpose in.png out.ong
>                                  {{Invert vertical, then rotate 90deg}} 
    `convert -transverse in.png out.ong
>                                  {{Invert horizontal, then rotate 270deg}} 

$ Format
    `mogrify -format jpg -quality 85 *.png
>                                  {{Convert all png files to jpg in-place}} 
    `convert pic.jpg pic.pdf       {{Convert image to pdf doc}} 

