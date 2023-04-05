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

=== "Rectangle"
    ```applescript
    set {_shape} to new rectangle with width 100 and height 100 and color red
    ```
=== "Rounded rectangle"
    ```applescript
    set {_shape} to new rounded rectangle with width 100 and height 100 and arc width 10 and arc height 10 and color red
    ```
=== "Arc"
    ```applescript
    set {_shape} to new arc with width 100 and height 100 and start angle 0 and arc angle 90 and color red
    ```