---
icon: material/file-document
---

# Bot Application Info

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.14.3') ]]]

The `application info` expression allows you to get information about the application of the desired bot. 

!!! tips 
    You must have created an application before the bot, as the bot is linked to the application!

First, you'll have to **retrieve** your bot's application. Here's how to do it:

```applescript
retrieve application info of bot "Bot Name" and store it in {_app}
```

Once you have the application, there's several properties attached to it, such as:

=== "Basic"
    - Avatar URL (`avatar url of {_app}`)
    - Name (`discord name of {_app}`)
    - Discord ID (`discord id of {_app}`)

=== "Meta"
    - Privacy Policy URL (`privacy policy url of {_app}`)
    - Terms of Service URL (`terms of service url of {_app}`)
    - Description (`application description of {_app}`)
    - Owner (`application owner of {_app}`)

!!! example
    Here's an example of how to retrieve the application info of a bot:

    ```applescript
    discord command app:
        prefixes:!
        trigger:
            retrieve application info of event-bot and store it in {_app}
    
            add "**Application Information of `%discord name of {_app}%`:**" to {_m::*}
            add "- **ID:** `%discord id of {_app}%`" to {_m::*}
            add "- **Owner:** %mention tag of application owner of {_app}%" to {_m::*}
            add "- **Avatar:** %avatar url of {_app}%" to {_m::*}
            
            add "- **Description:** %application description of {_app}%" to {_m::*}
            add "- **Privacy Policy:** %privacy policy url of {_app}%" to {_m::*}
            add "- **Terms of Service:** %terms of service url of {_app}%" to {_m::*}
    
            reply with join {_m::*} with nl
    ```