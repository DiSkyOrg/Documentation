---
icon: material/image
---

# Images

The first step with SkImage will be to load and save images. That's what we'll see in this section.

## Loading or creating an image

In order to get an image, you can:

* load an image from a file (such as a `png` or `jpg` file)
* create an image from scratch (with a specific size and type)

=== "Loading an image"
    ```applescript
    set {_image} to image from file "path/to/image.png"
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