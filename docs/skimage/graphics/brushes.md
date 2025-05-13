---
icon: material/brush
---

# Brushes

Instead of simple colors, you can use brushes to create more complex fills for your shapes. Brushes allow you to create gradients, patterns, textures, and other visual effects.

!!! note
    For drawing with semi-transparent colors using brushes, you need:
    
    * An image with RGBA format (see [image types](../images.md#loading-or-creating-an-image) for more information)
    * The proper composite effect set (see [composite effects](customizations.md#composite-effects) for details)

## Solid Color Brush

The most basic brush is a solid color:

```applescript
set {_brush} to new solid brush with color red
set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
```

## Gradient Brushes

Gradient brushes create a smooth transition between multiple colors:

=== "Horizontal Gradient"
    ```applescript
    set {_brush} to new horizontal gradient brush with colors red, yellow, blue
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Vertical Gradient"
    ```applescript
    set {_brush} to new vertical gradient brush with colors red, yellow, blue
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Radial Gradient"
    ```applescript
    set {_brush} to new radial gradient brush with colors red, yellow, blue
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

## Pattern Brushes

Pattern brushes create repeating patterns:

=== "Checkerboard Pattern"
    ```applescript
    set {_brush} to new checkerboard pattern brush with primary color black and secondary color white and size 10
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Dots Pattern"
    ```applescript
    set {_brush} to new dots pattern brush with primary color black and secondary color white and size 8
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Stripes Pattern"
    ```applescript
    set {_brush} to new stripes pattern brush with primary color black and secondary color white and size 8
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

## Hatch Brushes

Hatch brushes create line-based patterns:

=== "Horizontal Hatch"
    ```applescript
    set {_brush} to new horizontal hatch brush with primary color black and secondary color white and spacing 5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Vertical Hatch"
    ```applescript
    set {_brush} to new vertical hatch brush with primary color black and secondary color white and spacing 5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Diagonal Hatch"
    ```applescript
    set {_brush} to new diagonal hatch brush with primary color black and secondary color white and spacing 5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Cross Hatch"
    ```applescript
    set {_brush} to new cross hatch brush with primary color black and secondary color white and spacing 5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Dotted Hatch"
    ```applescript
    set {_brush} to new dotted hatch brush with primary color black and secondary color white and spacing 5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

## Special Effect Brushes

These brushes create more complex visual effects:

=== "Marble Brush"
    ```applescript
    set {_brush} to new marble brush with primary color blue and secondary color white and turbulence 0.5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Metallic Brush"
    ```applescript
    # Create a gold-like metallic effect
    set {_brush} to new metallic brush with color rgb(212, 175, 55) and shininess 0.7
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Noise Brush"
    ```applescript
    set {_brush} to new noise brush with color green and intensity 0.5
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

=== "Reflective Brush"
    ```applescript
    set {_brush} to new reflective brush with color silver and light at x 20, y 20 and intensity 0.8
    set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
    ```

## Texture Brush

You can use an existing image as a texture brush:

```applescript
set {_texture} to image from file "plugins/SkImage2/textures/grass.png"
set {_brush} to new texture brush from {_texture}
set {_shape} to new rectangle with width 80 and height 80 and brush {_brush}
```