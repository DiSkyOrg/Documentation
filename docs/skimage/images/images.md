---
icon: material/image
---

# Images

The first step with SkImage will be to load and save images. That's what we'll see in this section.

## Loading or creating an image

In order to get an image, you can:

* load an image from a file (such as a `png` or `jpg` file)
* load an image from a URL
* create an image from scratch (with a specific size and type)

=== "Loading an image from file"
    ```applescript
    set {_image} to image from file "path/to/image.png"
    ```

=== "Loading an image from URL"
    ```applescript
    set {_image} to image from url "https://example.com/image.png"
    ```

=== "Creating an image"
    ```applescript
    set {_image} to new image with width 100 and height 100
    ```
    !!! info
        You can specify the type of the image as an int (by adding `with type X` at the end). The specified type will be used to create the encoding of the image:
    
        * `0` for `TYPE_INT_RGB` (such as a `jpg` image, no transparency)
        * `1` for `TYPE_INT_ARGB` (such as a `png` image, with transparency)
        * `2` for `TYPE_INT_ARGB_PRE` (such as a `png` image, with transparency and pre-multiplied alpha)
        
        And more are available at the [JavaDoc](https://docs.oracle.com/javase/7/docs/api/java/awt/image/BufferedImage.html#TYPE_CUSTOM).

## Saving an image

The only way to save an image is to use the `save` effect. It will save the image in the specified file path.

```applescript
save image {_image} to "path/to/image.png"
```

!!! info
    * If the desired file path doesn't exist, it will be created. 
    * If the file already exists, it will be overwritten.

## Manipulating images

SkImage2 provides several ways to manipulate images, including resizing, cropping, and applying effects like rounded corners.

### Resizing images

You can resize an image to a new width and height using the `resized` expression:

```applescript
set {_resized} to resized {_image} to 200, 150
```

By default, this uses the default scaling algorithm. You can specify a different algorithm for better quality:

```applescript
set {_resized} to resized {_image} to 200, 150 with algorithm "smooth"
```

Available algorithms include:

- `default` - Basic scaling
- `fast` - Optimized for speed but lower quality
- `smooth` - Higher quality but slower processing
- `replicate` - Pixel replication (nearest neighbor)

### Cropping images

You can crop an image to a specified width and height, starting from the top-left corner:

```applescript
set {_cropped} to cropped {_image} to 100, 100
```

This will create a new image with only the top-left 100x100 pixels of the original image.

### Rounded corners

You can create a rounded version of an image:

```applescript
# Create a rounded image with default corner radius
set {_rounded} to rounded {_image}

# Create a rounded image with specific corner radius (e.g., 20 pixels)
set {_rounded} to rounded {_image} with size 20
```

### Finding average color

You can determine the average (or main) color of an image:

```applescript
set {_avgColor} to average color of {_image}
```

This is useful for generating color schemes or determining the dominant color in an image.

## Image properties

You can retrieve various properties of an image:

```applescript
set {_width} to image width of {_image}
set {_height} to image height of {_image}
set {_type} to image type of {_image}
```