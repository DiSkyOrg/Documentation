---
icon: material/drawing
---

# Graphics 2D Management

## Understanding the allocation system

When you create graphics, you need to allocate them. This means that you need to create a new graphics object, and then you need to draw on it. 

When you're done drawing, you need to dispose of it. This must be done by yourself in order to avoid memory leaks.

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

For these example, we'll have a blank (transparent) image of 100x100 pixels. Also, [anti-aliasing](customizations.md#anti-aliasing) is enabled and the [stroke](customizations.md#stroke) is set to a width of 5.

=== "Rectangle"
    ```applescript
    set {_shape} to new rectangle with width 80 and height 80 and color yellow
    ```

    ![rectangle.png](../images/shape-1.png)

=== "Rounded rectangle"
    ```applescript
    new rounded rectangle with width 80 and height 80 and arc width 10 and arc height 10 and color yellow
    ```

    ![rounded-rectangle.png](../images/shape-2.png)

=== "Arc"
    ```applescript
    set {_shape} to new arc with width 100 and height 100 and start angle 0 and arc angle 90 and color yellow
    ```

    ![arc.png](../images/shape-3.png)

=== "Line"
    ```applescript
    set {_shape} to new line going to 90, 90 and color yellow
    ```

    ![line.png](../images/shape-4.png)

=== "Polygon"
    ```applescript
    set {_shape} to new polygon with x points (50, 20, 80, 50, 20, 50) and y points (20, 80, 80, 100, 80, 80) and color yellow
    ```

    ![polygon.png](../images/shape-5.png)

### Images

You can also draw images on the graphics:

```applescript
draw {_image} on {_graphics} at 0, 0
```

!!! note
    For drawing with semi-transparent colors, you need:
    
    * An image with RGBA format (see [image types](../images.md#loading-or-creating-an-image) for more information)
    * The proper composite effect set (see [composite effects](customizations.md#composite-effects) for details)