# pygame

> Source: http://www.pygame.org/docs/

> Aliases: basic-pygame, pygame-2d-framework, pygame-tutorial, pygame-package, pygame-python-module

$ Load and Launch Pygame
    `import pygame                 {{Imports the package with all the available Pygame modules.}} 
    `pygame.init()                 {{This calls to 'pygame.init()' initializes each of these modules.}} 

$ Display
    `pygame.display.update()       {{Redraws the main display surface if argument list is empty.}} 
    `pygame.display.get_surface()  {{Returns a reference to the Surface instantiated with the set_mode() function.}} 
    `screen = pygame.display.set_mode((width, height))
>                                  {{Initializes and creates the window where your game will run.}} 

$ Surfaces, Images, and Transformations
    `Surface.fill(color)           {{Fills surface with a solid color. The argument is a tuple of RGB values.
e.g. (255,0,255).}} 
    `Surface.convert()             {{Changes pixel format of the Surface’s image to the format used by the main display.}} 
    `Surface.convert_alpha()       {{Same as above, but when the Surface’s image has alpha transparency values to deal with.}} 
    `Surface.get_rect()            {{Returns a Rect that will tell you the dimensions and location of the surface.}} 
    `pygame.image.load(filename)   {{Loads image from disk and returns a Surface.}} 
    `pygame.transform.rotate(Surface, angle)
>                                  {{Rotates Surface counterclockwise by degrees.}} 
    `pygame.transform.scale(Surface, (width, height))
>                                  {{Resizes Surface to new resolution.}} 
    `Surface.blit(sourceSurface, destinationRect, optionalSourceRect)
>                                  {{Copies pixels from one Surface to another. Used to draw images to the screen.}} 

$ Rects
    `Rect.move(x, y)               {{Returns a Rect moved x pixels horizontally and y pixels vertically.}} 
    `Rect.move_ip(x, y)            {{Moves the Rect x pixels horizontally and y pixels vertically.}} 

$ Time
    `pygame.time.Clock()           {{Creates a Clock object.}} 
    `pygame.time.delay(milliseconds)
>                                  {{Pauses game for time specified.}} 
    `pygame.time.get_ticks()       {{Returns the number of milliseconds passed since pygame.init() was called.}} 

$ Events
    `pygame.event.get()            {{Call once per frame to get a list of events that occurred since the last time pygame.event.get() was called.}} 

$ Fonts
    `f = pygame.font.Font(None, 32)
>                                  {{Creates a font object of size 32 using the default system font.}} 
    `sf = f.render(“Hello”, 1, color, color)
>                                  {{Creates a surface of rendered text using the font of the font object.}} 

