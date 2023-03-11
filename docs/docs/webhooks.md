# 📥 Webhooks

!!! success
    This documentation page includes all the elements from the module **[Webhooks](../../modules/webhooks)**.

## Make Client Send Builder

|Since|v4.0.0|class:version|

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

|Since|v1.0.0|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|embedbuilder|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|webhookmessage|class:version|

The current webhook message builder from the current 'make message' scope.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [last] [message] builder
    ```

## Builder Avatar

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

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

|Since|v4.0.0|class:version|
|Return Type|boolean|class:version|

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

|Since|v4.0.0|class:version|

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

