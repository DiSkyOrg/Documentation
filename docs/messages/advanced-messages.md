---
icon: material/message-bulleted
---

# Advanced Messages

[[[% import 'macros.html' as macros %]]]

Advanced (or **rich** messages) are messages that contain multiple properties, such as text content, embeds, components, and files, all within the same message.

## Overview

In order to create a new rich message, you'll need the `create message` section:

```applescript
create a new message and store it in {_msg}:
    ...

reply with {_msg}
```

??? tip "Want to create a message based on an existing one? (since DiSky v4.22.1)"
    Specify your message in the section code:

    ```applescript
    create a new message based on {_msg} and store it in {_newMsg}:
        # do something with the new message
    ```

Once our message will be created, it will be stored in the `{_msg}` variable, then replied in the event channel. We'll reference our **message builder** within the section as `last message builder` (but `message` can also work!).

## Add a content

Now we have our setup, we can try to send back a "simple" message, with just text content:

```applescript
create a new message and store it in {_msg}:
    set the content of the message to "Hello World!"

reply with {_msg}
```

This is gonna results in the same output as before:

<figure markdown>
  ![Image title](../images/image (7).png)
  <figcaption>The results.</figcaption>
</figure>

## Add an embed

Now we have some text, let's link an embed to our message. [For embed creation, take a look at the reference page of the wiki](simple-messages.md#simple-embed-message)!

```applescript
create a new message and store it in {_msg}:
    set the content of the message to "Hello World!"
    
    make embed:
        set title of embed to "Amazing embeds :D"
        set embed color of embed to orange
        set footer of embed to "Created with DiSky v4!"
    add last embed to the embeds of the message

reply with {_msg}
```

!!! warning
    A bot-message can only contain one embed. However, if using webhooks, you can provide a maximum of 5 embeds!

<figure markdown>
  ![Image title](../images/image (1) (2).png)
  <figcaption>The output of the code above.</figcaption>
</figure>

??? tip "Want to serialize embeds via JSON?"
    Since **DiSky v4.12.1**, it's possible to convert an embed into its **JSON string representation**, and the way back too. Let's say we have an embed in a `{_embed}` variable:

    === "Embed to JSON"
        
        ```
        set {_json} to embed {_embed} as json
        ```

    === "JSON to embed"
        
        ```
        set {_embed} to embed from json {_json}
        ```

## Add attachments

Attachments are files that you can link to your message. If **SkImage** is installed, you can pass an image to the attachments. By default, you provide the file's local path to your file:

```applescript
create a new message and store it in {_msg}:
    set the content of the message to "Hello World!"
    
    make embed:
        set title of embed to "Amazing embeds :D"
        set embed color of embed to orange
        set footer of embed to "Created with DiSky v4!"
    add last embed to the embeds of the message
    
    add "plugins/Skript/scripts/msg.sk" to the attachments of the message

reply with {_msg}
```

<figure markdown>
  ![Image title](../images/image (4) (1).png)
  <figcaption>The results.</figcaption>
</figure>

!!! warning
    Thanks to discord, you cannot change the order of the elements. For instance, here, you cannot make the attachment displays under the embed.

## Add Poll

[[[ macros.required_version('4.14.0') ]]]

More details about polls (creation, ...) can be found [here](polls.md "Polls"). You can however add a poll to your rich message using message:

```applescript
set poll of the message to {_poll}
```

## Add components

!!! info
    A wiki page providing how to make components will be written soon!


A message can only contain up to 5 component rows. Text inputs are not **allowed** here through.

```applescript
create a new message and store it in {_msg}:
    set the content of the message to "Hello World!"
    
    make embed:
        set title of embed to "Amazing embeds :D"
        set embed color of embed to orange
        set footer of embed to "Created with DiSky v4!"
    add last embed to the embeds of the message
    
    add "plugins/Skript/scripts/msg.sk" to the attachments of the message
    
    # simple button that'll take one row for itself
    add new danger button with id "btn-1" named "RDR II" to rows of the message 
    # mutliple buttons within the same row
    make new component row and store it in {_row}:
        add new success button with id "btn-2" named "Green lands!" with reaction "smile" to components of the row builder
        add new link button with id "https://forum.itsthesky.info/discord/" named "DiSky's Discord" to components of the row builder
    add {_row} to rows of the message
    
    # dropdown/select menu
    set {_dp} to new dropdown with id "selector"
    set min range of {_dp} to 1
    set max range of {_dp} to 2
    set placeholder of {_dp} to "Dropdown"
    add new option with value "one" named "One!" with description "Click to select" with reaction "sparkles" to options of {_dp}
    add new option with value "two" named "Two!?" with description "Click to select" with reaction "sparkles" to options of {_dp}
    add new option with value "three" named "THREE!!!" with description "Click to select" with reaction "sparkles" to options of {_dp}
    add {_dp} to the rows of message

reply with {_msg}
```

<figure markdown>
  ![Image title](../images/image (5) (1).png)
  <figcaption>The results.</figcaption>
</figure>