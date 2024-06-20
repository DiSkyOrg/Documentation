---
icon: material/check-all
---

# Webhooks

!!! danger "This is NOT for DiSky!"
    This page is for the **Webhooks Module**, that is now **deprecated**. You can see the new [Webhooks](../messages/webhooks.md) page for the new way to use webhooks with DiSky.

[[[% import 'macros.html' as macros %]]]

!!! success
    This documentation page includes all the elements from the module **[Webhooks](../modules/webhooks.md)**.

## Make Client Send Builder

[[[ macros.required_version('4.0.0') ]]]

Make a specific webhook client send a webhook message builder.
Don't forget to register the client before, then use the registered name on this effect.
The builder have to be made through a webhook message builder section! This effect should also be inside the section.
Because of Discord's limitation, you can only get back the message's ID. You have to retrieve it through DiSky's retrieve message effect.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    make [the] [webhook] client %string% send [the] [message] %webhookmessage% [and store (it|the message id) in %-string%]
    ```

## Register Webhook

[[[ macros.required_version('1.0.0') ]]]

Register a new webhook client through its Discord URL.
The URL contains both webhook's ID and token. Anyone who have it can therefore control your webhook.
Once a client is registered, feel free to use it specifying its name registered here.
=== "Examples"

    ```applescript
    register webhook name "my_webhook" with url "XXXXXX"
    ```
=== "Patterns"

    ```applescript
    register [new] webhook (named|with name) %string% with [the] url %string%
    ```

## Builder Embeds

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('embedbuilder') ]]]

Change the embeds of any webhook message builder.
=== "Examples"

    ```applescript
    set webhook embeds of builder to last embed builder
    add last embed builder to webhook embeds of builder
    ```
=== "Patterns"

    ```applescript
    [all] [the] webhook embeds of %webhookmessage%
    [all] [the] %webhookmessage%'[s] webhook embeds
    ```

## Builder Files

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Change the files of any webhook message builder.
=== "Examples"

    ```applescript
    set webhook files of builder to "file/path"
    add "file/path" to webhook files of builder
    ```
=== "Patterns"

    ```applescript
    [all] [the] webhook files of %webhookmessage%
    [all] [the] %webhookmessage%'[s] webhook files
    ```

## Webhook Message Builder

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('webhookmessage') ]]]

The current webhook message builder from the current 'make message' section.

=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [last] [message] builder
    ```

## Builder Avatar

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Change the avatar of any webhook message builder.
=== "Examples"

    ```applescript
    set webhook avatar of builder to "avatar url"
    ```
=== "Patterns"

    ```applescript
    [the] webhook avatar of %webhookmessage%
    %webhookmessage%'[s] webhook avatar
    ```

## Builder Content

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Change the content of any webhook message builder.
=== "Examples"

    ```applescript
    set webhook content of builder to "Here's some text"
    ```
=== "Patterns"

    ```applescript
    [the] webhook content of %webhookmessage%
    %webhookmessage%'[s] webhook content
    ```

## Builder Name

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Change the name of any webhook message builder.
=== "Examples"

    ```applescript
    set webhook name of builder to "username"
    ```
=== "Patterns"

    ```applescript
    [the] webhook name of %webhookmessage%
    %webhookmessage%'[s] webhook name
    ```

## Builder TTS State

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('boolean') ]]]

Change the tts state of any webhook message builder.
If enabled, Discord will read the message aloud to the user.
=== "Examples"

    ```applescript
    set webhook tts of builder to true
    ```
=== "Patterns"

    ```applescript
    [the] webhook tts [state] of %webhookmessage%
    %webhookmessage%'[s] webhook tts [state]
    ```

## Make Message

[[[ macros.required_version('4.0.0') ]]]

Make a new webhook message builder to change its avatar, name, text and embeds, all that though a section.
=== "Examples"

    ```applescript
    make new webhook message:
    	set webhook avatar of builder to "avatar url"
    	set webhook name of builder to "avatar url"
    	set webhook content of builder to "Here's some text"
    ```
=== "Patterns"

    ```applescript
    make [a] [new] webhook message [builder]
    ```

