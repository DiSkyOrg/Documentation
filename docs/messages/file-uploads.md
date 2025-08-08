---
icon: material/file-upload
status: new
---

# File Uploads

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.24.0') ]]]

File uploads are a new way to handle attachments in DiSky, replacing the previous attachment system. They allow you to upload files from various sources, such as local files, URLs, Discord attachments, or SkImage's Images.

## Creating a File Upload

When create a file upload, you can specify a name that will be sent over by discord (that may be different from the original file name) and whether the file should be marked as a spoiler.

!!! tip
    Whatever the source, you can always specify a different name (and spoiler) for the file upload. If none is specified, DiSky will try to find one based on the source (e.g. file name, URL, etc.)

Here's how to create a file upload from different sources:

=== "From a local file"
    !!! quote ""
        ```applescript
        [new] file (data|upload) from [local] file %string% [(with name|named) %-string%] [with spoiler %-boolean%]
        ```

        You have to specify the absolute or relative file path.
    
        !!! tip "Example"
            ```applescript
            set {_data} to new file data from file "plugins/DiSky/assets/image.png" with name "test.png"
            ```

=== "From a URL"
    !!! quote ""
        ```applescript
        [new] file (data|upload) from ur(l|i) %string% [(with name|named) %-string%] [with spoiler %-boolean%]
        ```
    
        You have to specify the URL of the file. Besides HTTP(S) URLs, you can also use FTP URLs.
    
        !!! tip "Example"
            ```applescript
            set {_data} to new file data from url "https://example.com/image.mp3" with name "test.mp3"
            ```

=== "From a Discord Attachment"
    !!! quote "" 
        ```applescript
        [new] file (data|upload) from attachment %attachment% [(with name|named) %-string%] [with spoiler %-boolean%]
        ```

        This represents any attachment sent **by** Discord (any message's attachment, the value of an attachment argument in a slash command, ...).
        
        !!! tip "Example"
            ```applescript
            set {_data} to new file data from attachment {_attachment} with name "test.png"
            ```

=== "From an SkImage's Image"
    !!! quote ""
        !!! warning "SkImage2 must be installed for it to work!"
        
        ```applescript
        [new] file (data|upload) from image %image% [(with name|named) %-string%] [with spoiler %-boolean%]
        ```

        You have to specify the SkImage's Image you want to use.
    
        !!! tip "Example"
            ```applescript
            set {_data} to new file data from image {_image} with name "test.png"
            ```

## Using a File Upload

Now you can *upload* that "file upload" via different contexts, such as:

### In a Message

```applescript
create a new message and store it in {_msg}:
    set the content of the message to "This message has an attachment!"

    set {_upload} to new file upload from file "plugins/DiSky/assets/image.png" with name "test.png"
    add {_upload} to the attachments of the message

reply with {_msg}
# or post the message
```

### As an embed's image

```applescript hl_lines="6"
create a new message and store it in {_msg}:

    make embed and store it in {_embed}:
        set title of embed to "Amazing embeds :D"
        set embed color of embed to orange
        set image of embed to "attachment://test.png"

    add {_embed} to the embeds of the message
    
    set {_a} to new file upload from attachment arg-1 named "test.png" #(1)!
    add {_a} to the attachments of the message
    
reply with {_msg}
```

1. The name of the file upload must match the one specified in the embed's image URL (e.g. `attachment://test.png`).