# Scratch

> Source: http://wiki.scratch.mit.edu/wiki/Scratch_Wiki:Table_of_Contents/Block_Types

$ Motion
    `move _ steps                  {{The block moves its sprite forward the specified amount of steps in the direction it is facing}} 
    `turn right                    {{The blocks turn their sprite the specified amount of degrees clockwise or counter-clockwise (depending on which block is used); this changes the direction the sprite is facing}} 
    `turn left                     {{The blocks turn their sprite the specified amount of degrees clockwise or counter-clockwise (depending on which block is used); this changes the direction the sprite is facing}} 
    `point in direction            {{The block points its sprite in the specified direction; this rotates the sprite}} 
    `point towards                 {{The block points its sprite towards the mouse-pointer or another sprite depending on its costume center; this changes the sprite's direction and rotates the sprite}} 
    `go to x y                     {{The block sets its sprite's X and Y position to the specified amounts. This block is related to the Set X to () and the Set Y to () blocks}} 
    `go to                         {{The block sets its sprite's X and Y position to that of the mouse-pointer or another sprite}} 
    `glide _ secs to x y           {{The block moves its sprite steadily to the specified X and Y position in the specified amount of seconds}} 
    `change x by                   {{The block moves its sprite costume center's X position by the specified amount}} 
    `set x to                      {{The block changes the selected sprite's X position to a specified value}} 
    `change y by                   {{The block moves its sprite's Y position by the specified amount}} 
    `set y to                      {{The block sets its sprite's Y (up and down) position to the specified amount}} 
    `if on edge, bounce            {{The block checks to see if its sprite is touching the edge of the screen with the move steps block; and if it is, the sprite will point in a direction that mirrors the direction from which it is coming}} 
    `set rotation style            {{The block changes the Rotation Style of the sprite in-project}} 
    `x position                    {{ The block holds its sprite's X position}} 
    `y position                    {{The block holds its sprite's Y position}} 
    `direction                     {{The block holds its sprite's direction, measured in degrees}} 

$ Looks
    `say _ for _ secs              {{The block displays a speech bubble with the specified text for the sprite that runs it}} 
    `say _                         {{The block gives its sprite a speech bubble with the specified text — the speech bubble stays until an another speech or thought block is activated, or the stop sign is pressed}} 
    `think _ for _ secs            {{The block give its sprite a thought bubble with the specified text, which stays for the specified amount of seconds}} 
    `think _                       {{The block gives its sprite a thought bubble with the specified text. The thought bubble stays until a speech or thought block with its text block empty is activated, or the stop sign is pressed}} 
    `show                          {{If the block's sprite is hidden, it will show the sprite — if the sprite is already showing, nothing will change}} 
    `hide                          {{If the block's sprite is shown, it will hide the sprite — if the sprite is already hidden, nothing happens}} 
    `switch costume to _           {{The block changes its sprite's costume to a specified one}} 
    `next costume                  {{The block changes its sprite's costume to the next in the costumes pane, but if the current costume is the last in the list, the block will loop to the first}} 
    `next backdrop                 {{The block changes the backdrop to the next in the list of backdrops, but if the current backdrop is the last in the list, the block will loop to the first}} 
    `switch backdrop to _          {{The block changes the Stage's backdrop to the specified one}} 
    `switch backdrop to _ and wait {{This block waits for scripts under any When Backdrop Switches to () blocks to finish}} 
    `change _ effect by _          {{The block changes the specified effect on its sprite by the specified amount. There are seven different effects to choose from: color, fisheye, whirl, pixelate, mosaic, brightness and ghost}} 
    `set _ effect to _             {{The block sets the specified effect on its sprite to the specified amount. There are seven different effects to choose from: color, fisheye, whirl, pixelate, mosaic, brightness and ghost}} 
    `clear graphic effects         {{This block resets all 7 graphic effects (color, fisheye, whirl, pixelate, mosaic, brightness and ghost) on its sprite}} 
    `change size by _              {{The block changes its sprite's size by the specified amount}} 
    `set size to _ %               {{The block sets its sprite's size to the specified amount}} 
    `go to front                   {{The block will place a sprite in front of all other sprites}} 
    `go back _ layers              {{The block changes its sprite's layer value by the specified amount}} 
    `costume #                     {{The block holds its sprite's current costume number}} 
    `backdrop name                 {{The block holds the current backdrop name}} 
    `backdrop #                    {{The block hold the current backdrop number}} 
    `size                          {{The block holds its sprite's size}} 

$ Sound
    `play sound _                  {{The block will play the specified sound}} 
    `play sound _ until done       {{The block will play the specified sound, pausing its script until the sound has finished playing}} 
    `stop all sounds               {{The block will stop any sounds currently being played on all sprites and the Stage}} 
    `play drum _ for _ beats       {{The block will play the specified instrument for the specified amount of seconds using a MIDI drumset}} 
    `rest for _ beats              {{The block pauses its script for the specified amount of beats, which can be a decimal number}} 
    `play note _ for _ beats       {{The block will play the specified note with a set MIDI instrument for the specified amount of beats}} 
    `set instrument to _           {{The block changes the set MIDI instrument that the Play Note () for () Beats block will play}} 
    `change volume by _            {{The block changes the volume of a sprite by the specified amount}} 
    `set volume to _ %             {{The block sets its sprite's volume to the specified amount}} 
    `change tempo by _             {{The block changes the project's tempo by the specified amount}} 
    `set tempo to _ bpm            {{The block sets the Scratch project's tempo, or speed, to the specified amount, using the unit bpm, or beats per minute}} 
    `tempo                         {{The block holds the Scratch project's tempo}} 
    `volume                        {{The block holds a sprite's or the Stage's volume}} 

$ Pen
    `clear                         {{The block removes all marks made by the pen or stamps}} 
    `stamp                         {{When used in a script, the Sprite will produce a bitmap image of itself, which is stamped onto the Stage}} 
    `pen down                      {{The block will make its sprite continuously pen a trail wherever it moves (until the Pen Up block is used)}} 
    `pen up                        {{If a sprite is currently using the pen feature because of the Pen Down block, the block will stop it from continuing}} 
    `set pen color to [color]      {{The block sets the pen's color to the color chosen with the block's color-picker (eyedropper tool)}} 
    `set pen color to [number]     {{The block sets the pen's color to the color chosen}} 
    `change pen shade by _         {{The block changes the pen's shade by the specified amount}} 
    `set pen shade to _            {{The block sets the pen's shade to the specified amount}} 
    `change pen size by _          {{The block changes the pen's size by the specified amount}} 
    `set pen size to _             {{The block sets the pen's size to the specified amount}} 

$ Data
    `variable                      {{The block simply holds its variable}} 
    `set _ to _                    {{The block will set the specified variable to the given value: a string or number}} 
    `change _ by _                 {{The block will change the specified variable by a given amount}} 
    `show variable _               {{The block shows the specified variable's Stage monitor}} 
    `hide variable _               {{he block hides the specified variable's Stage monitor}} 
    `list                          {{The block simply reports the items of its list as a string}} 
    `add _ to _                    {{The block adds an item onto the end of the specified list, the item containing the given text}} 
    `delete _ of _                 {{The block can delete the item inputted, the last item, or all items of the specified list depending on the option selected}} 
    `insert _ at _ of _            {{The block inserts an item containing the given text into the list, at the given position}} 
    `replace item _ of _ with _    {{The block replaces the specified item; in other words, it changes the item's content to the given text}} 
    `item _ of _                   {{The block reports the value of the specified entry in a specified list}} 
    `length of _                   {{The block reports how many items a list contains}} 
    `_ contains _                  {{The block checks if any items in the specified list are equal to the given text}} 
    `show list _                   {{The block shows the specified list's Stage monitor}} 
    `hide list _                   {{The block hides the specified list's Stage monitor}} 

$ Events
    `when green flag clicked       {{Scripts that wear this block will activate once the Green Flag has been clicked; these scripts can activate other scripts and enable the entire program}} 
    `when _ key pressed            {{Scripts placed underneath this block will activate when the specified key is pressed}} 
    `when this sprite clicked      {{Scripts that wear the block will activate once its sprite or clone of the sprite is clicked. Contrary to its definite name, the block will also execute the clone's script when the clone is clicked on}} 
    `when backdrop switches to _   {{Scripts that wear this block will be invoked once the specified backdrop has been switched to on the Stage}} 
    `when _ > _                    {{It starts the script below it when a value (chosen by the dropdown menu) is greater than another value (entered by the number input). The available options are loudness, timer, and video motion}} 
    `when I receive _              {{Scripts that begin with this block will be invoked once the specified broadcast has been sent by a calling script}} 
    `broadcast _                   {{Any scripts in any sprites that are hatted with the When I Receive () block that is set to a specified broadcast will activate}} 
    `broadcast _ and wait          {{The block sends a broadcast throughout the whole Scratch project — any scripts that are halted with the When I Receive () block and are set to the broadcast will activate}} 

$ Control
    `wait _ secs                   {{The block pauses its script for the specified amount of seconds — the wait can also be a decimal number}} 
    `repeat _                      {{Blocks held inside this block will loop a given amount of times, before allowing the script to continue}} 
    `forever                       {{Blocks held inside this block will be in a loop}} 
    `if _ then                     {{The block will check its boolean condition. If the condition is true, the blocks held inside it will run, and then the script involved will continue}} 
    `if _ then else                {{The block will check its boolean condition: if the condition is true, the code held inside the first C (space) will activate, and then the script will continue; if the condition is false, the code inside the second C will activate}} 
    `wait until _                  {{The block pauses its script until the specified boolean condition is true}} 
    `when I start as a clone       {{It activates in a clone when it gets created}} 
    `repeat until _                {{Blocks held inside this block will loop until the specified boolean statement is true, in which case the code beneath the block (if any) will execute}} 
    `stop _                        {{The block would deactivate all scripts in the project, stopping it completely}} 
    `create clone of _             {{It creates a clone of the sprite in the argument. It can also clone the sprite it is running in, creating clones of clones, recursively}} 
    `delete this clone             {{It deletes the clone it runs in}} 

$ Sensing
    `touching _                    {{The block checks if its sprite is touching the mouse-pointer, edge, or another sprite (a Reporter block holding the sprite's name can be used). If the sprite is touching the selected object, the block returns true; if it is not, it returns false}} 
    `touching color _ ?            {{The block checks if its sprite is touching the specified color}} 
    `color _ is touching _ ?       {{The block checks if a color on its sprite is touching another color; if the color on its sprite is touching the color, the block returns true; if it is not, it returns false}} 
    `distance to _                 {{The block reports the distance (a measurement of pixels) between it and a specified sprite's costume center, or the mouse-pointer}} 
    `answer                        {{The block holds the most recent text imputed with the Ask () and Wait block}} 
    `key _ pressed?                {{The block checks if the specified key is pressed. If the key is being pressed, the block returns true; if it is not, it returns false}} 
    `mouse down?                   {{The block checks if the computer mouse's primary button is activated (being clicked)}} 
    `mouse x                       {{he block holds (reports) the mouse-pointer's current Mouse X}} 
    `mouse y                       {{The block holds the mouse-pointer's current Mouse Y}} 
    `loudness                      {{The block reports how loud the noise is that a microphone receives, on a scale of 0 to 100}} 
    `video _ on _                  {{It gets values of the video, either motion (on a scale of 1 to 100) or direction (which way the detected motion is going, measured on the same plane as sprite direction), on either the Stage, or the current sprite}} 
    `turn video _                  {{It can turn the webcam on, off, or on flipped horizontally, depending on the argument}} 
    `set video transparency to _ % {{It sets the transparency of the video stream to a certain value}} 
    `timer                         {{The block starts at 0 when Scratch is launched and increases gradually; every second it will have increased by 1}} 
    `reset timer                   {{The block sets the timer's value back to 0.0}} 
    `_ of _                        {{The block will report a specified value of the specified sprite or the Stage}} 
    `current _                     {{It reports either the current local year, month, date, day of the week, hour, minutes, or seconds, depending on the argument}} 
    `days since 2000               {{It reports the amount of days (and fractions of a day) since 00:00:00 1 January 2000 (UTC)}} 
    `username                      {{It reports the username of the user viewing the project, which can be used for saving progress in a project, either with a variable encoder or cloud lists (once they are released with string-storage capabilities), as well as other purposes}} 

$ Operators
    `_ add _                       {{The block adds two values and reports the result}} 
    `_ subtract _                  {{The block subtracts the second value from the first and reports the result}} 
    `_ multiply _                  {{The block multiplies the two values and reports the result}} 
    `_ devide _                    {{The block divides the second value from the first and returns the result}} 
    `pick random _ to _            {{The block picks a pseudorandom number ranging from the first given number to the second, including both endpoints}} 
    `_ less than _                 {{The block checks if the first value is less than the second value}} 
    `_ equals _                    {{The block checks if the first value is equal to the other value}} 
    `_ greater than _              {{The block checks if the first value is greater than the other value}} 
    `_ and _                       {{The block joins two boolean blocks so they both have to be true to return true. If they are both true, the block returns true; if they are not all true or none true, it returns false}} 
    `_ or _                        {{The block joins two boolean blocks so any one of them can be true to return true}} 
    `not _                         {{This block outputs the opposite boolean value of the condition (true and false)}} 
    `join _ _                      {{The block concatenates, or links the two values together and reports the result}} 
    `letter _ of _                 {{The block reports the specified character of the given text}} 
    `length of _                   {{The block reports how many characters the given string contains}} 
    `_ mod _                       {{The block reports the remainder of the division when the first value is divided by the second}} 
    `round _                       {{The block rounds the given number to the nearest integer}} 
    `_ of _                        {{The block performs a specified function on a given number and reports the result}} 

$ More Blocks
    `define custom block , custom block
>                                  {{This block is unique among the blocks for several reasons, including its lack of appearance in the Block Palette, its shape and color, and its edit menu when right-clicked}} 

