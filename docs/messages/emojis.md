---
icon: material/sticker-emoji
---

# Emojis

[[[% import 'macros.html' as macros %]]]

This guide will show you how to use and interact with emojis in your Discord bot using DiSky. 

## Structure

The terms *emoji* and *emote* are **completely different** in Discord:

* An **Emoji** is a __unicode__ character, that are **built-in** in Discord, and can be used by anyone, bots included.
* An **Emote** is a __custom__ emoji, that are **created** by a user in a **guild**.

!!! note
    As you've read, **emotes** are **guild-specific**, thus to difference two emotes with the same name, we use **their IDs** (the same way we do for users).

## Getting and using Emojis

There's only one expression to gather an emojis:

!!! example ""
    === "Emoji"
        ```applescript
        set {_emoji} to reaction "joy" # DiSky will 'translate' it to the unicode character '😂'
        ```

    === "Emote (via ID)"
        ```applescript
        set {_emote} to reaction "123456789012345678"
        ```
 
        Each IDs are unique, and are the best way to get an emote.

    === "Emote (via name)"
        !!! warning
            This method is **not recommended** because of the potential name conflicts and unloaded emotes.
    
        ```applescript
        set {_emote} to reaction "Checkmark"
        ```
    
        DiSky will try to find an emote from any guild the bot is in, with the name `Checkmark`.
    
    === "Emote (via full reference)"
        ```applescript
        set {_emote} to reaction "<:Checkmark:123456789012345678>"
        ```
    
        In this case, DiSky will split the given string and apply different state of filter to determine the emote. This method can sometime be faster for a lot of emotes.
    
        Now you got your emoji/emote, you can use it in messages (using a mention) or in reactions:
    
    === "In Messages"
        ```applescript
        reply with "Hello, I'm using an emoji: {_emoji}" # Will send, for the first case, "Hello, I'm using an emoji: 😂"    
        ```

=== "In Reactions"
    ```applescript
    react to {_message} with {_emote}: # where {_message} is a message
        reply with "Oh, someone reacted with an emote!" # Will fire when someone reacts to the message with the given emote    
    ```

## Super Reactions

To put it simply: **bots can't react with super reactions**. However, they can do anything else with them, such as getting them, removing them, checking if a user reacted with them, etc.

!!! warning
    This is a Discord limitation, and there's nothing we can do about it yet. Maybe it'll come in the near future? Who knows!

## Reaction Emotes 

[[[ macros.required_version('4.12.2') ]]]

When the [reaction event](../docs/events.md#on-reaction-add) is fired, you can get the emote that was used to react with, but also some other information: this is called a **Reaction Emote**.

!!! tip
    You can easily get any reaction emote from a reaction event using the `event-reaction` expression!

There's not a lot of things about them, simply two small things:

=== "Is Self?"
    You can check if the reaction was added by the bot itself, or not:

    ```applescript
    if event-reaction is self:
        reply with "Oh, looks like I reacted to my own message!"
    ```

=== "Is Super?"
    You can check if the reaction is a super reaction, or not:

    ```applescript
    if event-reaction is super:
        reply with "Oh, looks like someone reacted with a super reaction!"
    ```

    !!! info
        Funny enough, the only 'way' to know if a reaction is a super reaction is by the reaction add event, and this expression!