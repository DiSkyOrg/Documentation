# 🎨 Graphics (2D)

## Understanding the allocation system

When you create graphics, you need to allocate them. This means that you need to create a new graphics object, and then you need to draw on it. 

When you're done drawing, you need to dispose of it. This must be done by yourself in order to avoir memory leaks.

## Creating a graphics

You can easily create & store 2D graphics with the following expression:

```applescript
set {_graphics} to new graphics from image {_image}
```

!!! danger
    As explained above, you need to dispose of the graphics when you're done drawing on it. You can do so with the following effect:

    ```applescript
    dispose {_graphics}
    ```

    You won't be able to draw on the graphics after disposing it.

## Drawing on a graphics

### Shapes

You can draw several shapes on a graphics. You first need to create and configure the shape itself, then draw it at the specified location.

When you have a shape, you can draw it using the following effect:

=== "Normal (outline)"
    ```applescript
    draw shape {_shape} on {_graphics} at 0, 0
    ```
=== "Filled"
    ```applescript
    draw filled shape {_shape} on {_graphics} at 0, 0
    ```

!!! info
    The colors are Skript color. You can however use `color from rgb` to create a color from RGB values.

For these example, we'll have a blank (transparent) image of 100x100 pixels. Also, [anti-aliasing](#anti-aliasing) is enabled and the [stroke](#stroke) is set to a width of 5.

=== "Rectangle"
    ```applescript
    set {_shape} to new rectangle with width 80 and height 80 and color yellow
    ```

    ![rectangle.png](images/shape-1.png)

=== "Rounded rectangle"
    ```applescript
    new rounded rectangle with width 80 and height 80 and arc width 10 and arc height 10 and color yellow
    ```

    ![rounded-rectangle.png](images/shape-2.png)

=== "Arc"
    ```applescript
    set {_shape} to new arc with width 100 and height 100 and start angle 0 and arc angle 90 and color yellow
    ```

    ![arc.png](images/shape-3.png)

=== "Line"
    ```applescript
    set {_shape} to new line going to 90, 90 and color yellow
    ```

    ![line.png](images/shape-4.png)

=== "Polygon"
    ```applescript
    set {_shape} to new polygon with x points (50, 20, 80, 50, 20, 50) and y points (20, 80, 80, 100, 80, 80) and color yellow
    ```

    ![polygon.png](images/shape-5.png)

### Text

In order to draw a text, you'll have to create its object, configure its properties, and then draw it. 

The first thing to do is creating the font that will be used to draw the text. You can create a font with the following expression:

```applescript
set {_font} to new font named "Arial" with size 20
```

!!! warning
    The font name is case-sensitive. You can find the list of available fonts on your system by using the following expression:

    ```applescript
    all fonts
    ```

??? info "Wants to add a style?"
    You can add a style to the font by using the following expression:

    ```applescript
    set {_font} to new font named "Arial" and style "XXX" with size 20
    ```

    You can replace the `XXX` with the following styles:
    
    * `bold`
    * `italic`
    * `plain`
    * `bold italic`

??? info "How to use custom font?"
    You must **load** the font before using it. It's best to put the following effect inside a `on load` or `on skript load` event:

    ```applescript
    register text font from file "path/to/font.ttf" # single file
    register text font from file "path/to/fonts/" # folder (all files inside will be loaded)
    ```

    Supported formats are `.ttf`, `.otf` and `.ttc`.

Now that you have a font, you can create the text object:

```applescript
set {_text} to new text with font {_font} and text "Hello world!"
```

SkImage2 uses a powerful 'text format' system, therefore you can easily change the text's color by using Minecraft's colors, for example:

=== "Code"
    ```applescript
    set {_txt} to new text "$cHello $6world! $##00FF00This is green!%nl%$3works on multiple lines!" with font {_font} vert align horiz align
    ```

=== "Result"
    ![text.png](images/text-1.png)

As you can see here, you can use `$` to change the color of the text (using Minecraft's color codes, or HEX codes), and `%nl%` to create a new line. Also, you can specify either the vertical or horizontal alignment of the text.

??? tip "Supported Color Codes"
    === "Minecraft codes"
        * `$0` - Black
        * `$1` - Dark Blue
        * `$2` - Dark Green
        * `$3` - Dark Aqua
        * `$4` - Dark Red
        * `$5` - Dark Purple
        * `$6` - Gold
        * `$7` - Gray
        * `$8` - Dark Gray
        * `$9` - Blue
        * `$a` - Green
        * `$b` - Aqua
        * `$c` - Red
        * `$d` - Light Purple
        * `$e` - Yellow
        * `$f` - White

    === "HEX Code"
        The format is `$#000000` where `000000` is the HEX code.

You can now draw the text as when you draw a shape:

```applescript
draw {_text} on {_graphics} at 0, 0
```

!!! info
    If you center the text, the input position will be considered as 'offset' from the center of the text.

    Therefore, if you want your text perfectly centered, you'll have to set 0, 0 for the position when drawing the text!

### Images

You can also draw images on the graphics. Here again, simply draw the image as when you draw a shape:

```applescript
draw {_image} on {_graphics} at 0, 0
```

## Customizing a graphics

### Anti-aliasing

Anti-aliasing is a technique used to make the edges of shapes smoother:

![anti-aliases.png](images/anti-aliases.png)

__It is disabled by default.__ If you wish to enable it for both shapes & text, you can simply set the property to true, for instance:

```applescript
set anti-aliasing of {_graphics} to true
```

You can simply turn it off by setting it to false.

!!! info
    This will be taken in account for all shapes & text drawn **after** the property has been set!

### Stroke

The stroke is the outline of a shape, or how the *line* shape is drawn. By default, it has a width of 1 and is filled.

A stroke can have several properties:

* `width`: the width of the stroke (in pixel)
* `cap` (optional): the cap of the stroke. Can be `butt`, `round` or `square`. Defaults to `round`.
* `join` (optional): the join of the stroke. Can be `bevel`, `miter` or `round`. Defaults to `round`.
* `mitter limit` (optional): the mitter limit of the stroke. Defaults to 10.
* `dash array` (optional): the dash array of the stroke. Defaults to `none` (aka full line).
* `dash phase` (optional): the dash phase of the stroke. Defaults to 0.

Here's some example code when drawing a rectangle: (anti-aliasing is enabled)

=== "Width of 5"
    ```applescript
    set stroke of {_graphics} to new stroke with width 5
    ```
    
    ![stroke-1.png](images/stroke-1.png)

=== "Width of 5, Dashed"
    ```applescript
    set stroke of {_graphics} to new basic stroke with width 5 and miter limit 10 and dash array (2, 7) and dash phase 0
    ```

    ![stroke-2.png](images/stroke-2.png)

=== "Width of 5, Dashed, Rounded"
    ```applescript
    set stroke of {_graphics} to new basic stroke with width 5 and cap "round" and join "round" and dash array (2, 7) and dash phase 0
    ```

    ![stroke-3.png](images/stroke-3.png)