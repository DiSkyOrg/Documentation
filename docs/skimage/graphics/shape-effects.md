---
icon: material/auto-fix
---

# Shape Effects

Shape effects (also called object effects) allow you to apply visual enhancements to individual shapes and text before drawing them. Unlike image effects that apply to entire images, shape effects target specific objects and adjust their appearance based on their actual shape and transparency.

!!! note
    Shape effects work by analyzing the alpha channel of objects to create effects that follow the exact contours of your shapes and text.

## Available Effects

### Glow Effect

The glow effect adds a colored aura around your shapes, making them stand out with a luminous appearance.

```applescript
set {_effect} to glow effect with color yellow, radius 10 and intensity 0.7
set {_shape} to new rectangle with width 100 and height 100 and color red
set {_glowing_shape} to {_shape} with object effect {_effect}
draw filled {_glowing_shape} on {_graphics} at 50, 50
```

**Parameters:**

- `color`: The color of the glow aura
- `radius`: The size of the glow (higher values create larger glows)
- `intensity`: The strength of the glow effect (0.0 - 1.0)

### Drop Shadow Effect

Drop shadow creates a shadow behind your object, giving it depth and making it appear to float above the background.

```applescript
set {_effect} to drop shadow effect with color black, offset 5, 5, blur 3 and opacity 0.5
set {_shape} to new circle with radius 50 and color blue
set {_shadowed_shape} to {_shape} with object effect {_effect}
draw filled {_shadowed_shape} on {_graphics} at 100, 100
```

**Parameters:**

- `color`: The color of the shadow
- `offset X, Y`: The horizontal and vertical displacement of the shadow
- `blur radius`: How blurred the shadow appears (0 = sharp, higher = softer)
- `opacity`: The transparency of the shadow (0.0 - 1.0)

### Bevel Effect

Bevel effect gives your shapes a 3D appearance by adding highlights and shadows to different edges, simulating depth and dimension.

```applescript
set {_effect} to bevel effect with highlight color white, shadow color black, size 3 and intensity 0.7
set {_shape} to new rounded rectangle with width 120 and height 80 and arc width 10 and arc height 10 and color gray
set {_beveled_shape} to {_shape} with object effect {_effect}
draw filled {_beveled_shape} on {_graphics} at 200, 150
```

**Parameters:**

- `highlight color`: The color used for raised/lit edges
- `shadow color`: The color used for recessed/shadowed edges  
- `size`: The thickness of the bevel effect in pixels
- `intensity`: The strength of the bevel effect (0.0 - 1.0)

## Applying Effects to Shapes

To apply an effect to a shape, use the `with object effect` syntax:

```applescript
set {_shape_with_effect} to {_original_shape} with object effect {_effect}
```

You can then draw the enhanced shape normally:

```applescript
draw filled {_shape_with_effect} on {_graphics} at x, y
```

## Applying Effects to Text

Effects work equally well with text objects:

```applescript
set {_font} to new font named "Arial" with style "bold" and size 48
set {_text} to new text with content "$cGlowing Text" with font {_font}
set {_glow} to glow effect with color blue, radius 15 and intensity 1.5
set {_glowing_text} to {_text} with object effect {_glow}
draw {_glowing_text} on {_graphics} at 100, 200
```

## Combining Multiple Effects

You can apply multiple effects to the same object by chaining them:

```applescript
set {_glow} to glow effect with color yellow, radius 8 and intensity 0.6
set {_shadow} to drop shadow effect with color black, offset 3, 3, blur 2 and opacity 0.4
set {_shape} to new polygon with x points (50, 100, 150, 100) and y points (50, 25, 50, 75) and color red

# Apply both effects
set {_enhanced_shape} to {_shape} with object effects {_glow} and {_shadow}
draw filled {_enhanced_shape} on {_graphics} at 250, 100
```

## Complete Example

Here's a comprehensive example showing different effects applied to various shapes:

=== "Code"

    ```applescript
    command shape-effects-demo:
        trigger:
            # Create image and graphics
            set {_image} to new image with width 800 and height 600
            set {_graphics} to new graphics from {_image}
            set anti aliasing of {_graphics} to true
            
            # Fill background
            draw filled (new rectangle with width 800 and height 600 and color black) on {_graphics} at 0, 0
            
            # Glow effect on rectangle
            set {_glow} to glow effect with color cyan, radius 20 and intensity 0.8
            set {_rect} to new rectangle with width 120 and height 100 and color red
            set {_glowing_rect} to {_rect} with object effect {_glow}
            draw filled {_glowing_rect} on {_graphics} at 100, 100
            
            # Drop shadow on circle
            set {_shadow} to drop shadow effect with color blue, offset 4, 4, blur 2 and opacity 0.6
            set {_circle} to new circle with radius 50 and color green
            set {_shadowed_circle} to {_circle} with object effect {_shadow}
            draw filled {_shadowed_circle} on {_graphics} at 400, 150
            
            # Bevel effect on polygon
            set {_bevel} to bevel effect with highlight color white, shadow color black, size 4 and intensity 0.8
            set {_poly} to new polygon with x points (50, 100, 100, 75, 25) and y points (25, 25, 75, 100, 75) and color purple
            set {_beveled_poly} to {_poly} with object effect {_bevel}
            draw filled {_beveled_poly} on {_graphics} at 600, 300
            
            # Glowing text
            set {_font} to new font named "Arial" with style "bold" and size 36
            set {_text_glow} to glow effect with color orange, radius 12 and intensity 1.0
            set {_text} to new text with content "$eGLOWING TEXT" with font {_font}
            set {_glowing_text} to {_text} with object effect {_text_glow}
            draw {_glowing_text} on {_graphics} at 250, 450
            
            # Clean up and save
            dispose {_graphics}
            save image {_image} to "plugins/SkImage2/shape-effects-demo.png"
            send "✓ Shape effects demo saved!"
    ```

=== "Result"
    ![Shape Effects Demo](../images_files/shape-effects-demo.png)

## Tips and Best Practices

### Performance Considerations

- Effects add processing time, especially with large radius values
- Use moderate intensity values (0.3-0.8) for subtle, professional-looking results
- Glow and shadow effects with large radii can significantly impact performance

### Visual Design Tips

- **Glow effects**: Work best on dark backgrounds and with contrasting colors
- **Drop shadows**: Use subtle offsets (2-5 pixels) for realistic depth
- **Bevel effects**: Most effective on medium-toned shapes where highlights and shadows are visible

### Color Combinations

- For glow: Use complementary colors (red shape with cyan glow, blue shape with orange glow)
- For shadows: Use darker versions of the background color or neutral grays/blacks
- For bevel: White or light gray highlights with black or dark gray shadows work universally

!!! warning "Transparency Requirements"
    For optimal effect rendering, especially with semi-transparent elements:
    
    * Use images created with RGBA format (type 1 when creating images)  
    * Set appropriate composite effects if needed
    * See [image types](../images/images.md#loading-or-creating-an-image) and [composite effects](customizations.md#composite-effects) for details