---
icon: material/file-gif-box
---

# Gifs

Gifs (Graphics Interchange Format) are animated images that can be created via SkImage. Basically, you'll add frames to a gif, and then save it.

### Creating a gif

You first need to create a gif object. To be honest, that's the most complex part as you'll configure everything right now:

```applescript
set {_gif} to new infinite gif manager with new image with size 100, 100 with delay 1 and store it in file "test.gif"
``` 

That may look complicated, but it's actually not. Let's break it down:

* `new infinite gif manager` creates a new gif manager. Using the *infinite* keyword will make the gif loop infinitely.
* `with new image with size 100, 100` creates and defines the image that will be used for the gif. In this case, it's a 100x100 transparent image.
* `with delay 1` defines the delay between each frame. In this case, it's 1 millisecond.
* `and store it in file "test.gif"` defines the file where the gif will be saved. In this case, it's `test.gif` in the server's root folder.

!!! warning ""
    * The file extension must be `.gif`!
    * The delay is in **milliseconds**, not seconds!
    * Once the gif created using the expression, __**you'll have to close/save it at the end**__!

### Adding frames

Now that the gif is created, you can add frames to it. To do so, simply use the `gif images` properties:

```applescript
# We create the image
set {_img} to new image with size 100, 100

# We make a random color
set {_r} to random integer between 0 and 255
set {_g} to random integer between 0 and 255
set {_b} to random integer between 0 and 255
set {_color} to color from rgb {_r}, {_g}, {_b}

# We draw a rectangle on the image
draw filled (new rectangle with width 100 and height 100 and color {_color}) on {_img} at 0, 0

# We add the image to the gif
add {_img} to images of {_gif}
```

!!! info ""
    You can also get the current images of the gif using the `gif images` property!

### Closing the gif

Once you're done adding frames, you'll have to close the gif. It will save the gif to the file specified when you created the gif manager, and close any ongoing stream.

To do so, simply use the `close` expression:

```applescript
close gif {_gif}
```

??? tip "Forgot to close the gif?"
    If you forgot to close a gif in your code, you can use the `/skimage close` command to force close all gifs!

### Example

Let's create a gif that will display a random color every second. It'll contain 10 frames, and will be saved in the server's root folder as `test.gif`.

=== "Code"

    ```applescript
    # We create the gif manager
    set {_gif} to new infinite gif manager with new image with size 100, 100 with delay 1000 and store it in file "plugins/test.gif"
    
    # We create 10 different images
    loop 10 times:
        set {_img} to new image with size 100, 100
        set {_r} to random integer between 0 and 255
        set {_g} to random integer between 0 and 255
        set {_b} to random integer between 0 and 255
        set {_color} to color from rgb {_r}, {_g}, {_b}
        
        draw filled (new rectangle with width 100 and height 100 and color {_color}) on {_img} at 0, 0
        add {_img} to images of {_gif}
     
    # We close the gif
    close gif {_gif}
    ```

=== "Result"
    ![Gif](images_files/gif.gif) 
