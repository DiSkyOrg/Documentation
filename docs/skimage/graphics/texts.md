---
icon: material/format-text
---

# Text Drawing

In order to draw text, you'll have to create its object, configure its properties, and then draw it. 

## Creating and configuring fonts

The first thing to do is creating the font that will be used to draw the text. You can create a font with the following expression:

```applescript
set {_font} to new font named "Arial" with size 20
```

!!! warning
    The font name is case-sensitive. You can find the list of available fonts on your system by using the following expression:

    ```applescript
    all fonts
    ```

### Adding font styles

You can add a style to the font by using the following expression:

```applescript
set {_font} to new font named "Arial" and style "XXX" with size 20
```

You can replace the `XXX` with the following styles:

* `bold`
* `italic`
* `plain`
* `bold italic`

### Using custom fonts

You must **load** the font before using it. It's best to put the following effect inside a `on load` or `on skript load` event:

```applescript
register text font from file "path/to/font.ttf" # single file
register text font from file "path/to/fonts/" # folder (all files inside will be loaded)
```

Supported formats are `.ttf`, `.otf` and `.ttc`.

## Creating and drawing text

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
    ![text.png](../images/text-1.png)

As you can see here, you can use `$` to change the color of the text (using Minecraft's color codes, or HEX codes), and `%nl%` to create a new line. Also, you can specify either the vertical or horizontal alignment of the text.

You can now draw the text as when you draw a shape:

```applescript
draw {_text} on {_graphics} at 0, 0
```

!!! info
    If you center the text, the input position will be considered as 'offset' from the center of the text.

    Therefore, if you want your text perfectly centered, you'll have to set 0, 0 for the position when drawing the text!

## Supported Color Codes

### Minecraft codes
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

### HEX Code
The format is `$#000000` where `000000` is the HEX code.

!!! note
    For drawing text with semi-transparent colors, you need:
    
    * An image with RGBA format (see [image types](../images.md#loading-or-creating-an-image) for more information)
    * The proper composite effect set (see [composite effects](customizations.md#composite-effects) for details)