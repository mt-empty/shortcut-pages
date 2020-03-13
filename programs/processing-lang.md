# Processing

> Source: https://www.processing.org/reference/

> Aliases: processing

$ Basic Structure
    `void setup()                  {{Runs once}} 
    `void draw()                   {{Runs repeatedly during execution}} 

$ Basic Functions
    `size(width,height)            {{Sets main window size}} 
    `background(color)             {{Sets window background color}} 
    `smooth()                      {{Set antialiasing on}} 
    `frameRate(fps)                {{Sets the fps}} 
    `println(string)               {{Writes a string to console}} 

$ Random and Noise
    `random(low,high)              {{Returns a random value within the limits}} 
    `randomSeed(seed)              {{Changes random seed}} 
    `noise(value)                  {{Returns a value in Perlin Noise sequence}} 
    `noiseDetail(octaves)          {{Sets threshold for noise function result}} 
    `noiseSeed(seed)               {{Changes noise seed}} 

$ Matrix Operations
    `pushMatrix()                  {{Saves currrent matrix}} 
    `popMatrix()                   {{Go back to last saved matrix}} 
    `translate(posx,posy)          {{Move anchor point to position}} 
    `scale(x.y)                    {{Scale the plane}} 
    `shearX(radians)               {{Apply a shear on x-axis}} 
    `rotate(X)                     {{Apply rotation to x-axis}} 
    `pushStyle()                   {{Saves current style}} 

$ Basic Geometry
    `ellipse(posx,posy,width,height)
>                                  {{Draws ellipse with given values}} 
    `rect(posx,posy,width,height)  {{Draws rectangle with given values}} 
    `line(posx,posy,width,height)  {{Draws line with given values}} 

$ Image Functions
    `image(img,posx,posy,width,height)
>                                  {{Draws an image in main screen}} 
    `loadImage(filename)           {{Initializes PI image}} 
    `tint(color)                   {{Sets tint value}} 
    `noTint()                      {{Disables image tint}} 
    `saveFrame(filename)           {{Saves screenshot to current frame}} 

$ Events Capture
    `void mousePressed()           {{Runs when mouse button is pressed}} 
    `void mouseClick()             {{Runs when mouse button is pressed and released}} 
    `void mouseMoved()             {{Runs everytime mouse is moved}} 
    `void keyPressed()             {{Runs on key press event}} 
    `void keyReleased()            {{Runs on key release event}} 

$ Array Functions
    `append(array,value)           {{Add a value to an array}} 
    `concat(a,b)                   {{Concatenates two strings}} 
    `expand(array,newSize)         {{Expands array's size value}} 
    `reverse(array)                {{Reverses an array}} 
    `shorten(array)                {{Reduces array size}} 
    `sort(array)                   {{Sort array in increasing order}} 

$ Color Functions
    `colorMode(mode)               {{Set color mode}} 
    `red(color)                    {{Returns red value of color}} 
    `hue(color)                    {{Returns hue value of color}} 
    `saturation(color)             {{Returns saturation value of color}} 
    `alpha(color)                  {{Returns transparency value of color}} 
    `lerpColor(color1,color2,moment)
>                                  {{Returns a color value between two colors}} 

$ Camera
    `beginCamera()                 {{Runs when mouse button is pressed}} 
    `camera()                      {{Runs when mouse button is pressed and released}} 
    `perspective()                 {{Runs everytime mouse is moved}} 
    `printCamera()                 {{Runs on key press event}} 
    `printProjection()             {{Runs on key release event}} 

