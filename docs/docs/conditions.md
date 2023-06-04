# 📕 Conditions

## Member / Bot is in Thread

|Since|v4.0.0|class:version|

Check if a specific member or bot is in a guild thread.
Useful to avoid exception while using join & leave effects.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %member/bot% (is|are) in [the] thread %threadchannel%
    %member/bot% (isn't|is not|aren't|are not) in [the] thread %threadchannel%
    ```

## ChannelType

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %channel% is of [the] %channeltype% type
    %channel% is of [the] type %channeltype%
    ```

## Member Has Permissions

|Since|v4.0.0|class:version|

Check if a member has permissions in an optional channel.
=== "Examples"

    ```applescript
    if event-member has discord permission administrator: # global permission
    if event-member has discord permission send message in event-channel: # channel specific permission
    ```
=== "Patterns"

    ```applescript
    %member% (has|have) discord permission[s] %permissions% [in [the] [channel] %-guildchannel%]
    %member% (doesn't|does not|do not|don't) have discord permission[s] %permissions% [in [the] [channel] %-guildchannel%]
    ```

## Member Has Role

|Since|v4.0.0|class:version|

Check if a member has a specific role.
=== "Examples"

    ```applescript
    if event-member has discord role with id "000":
    ```
=== "Patterns"

    ```applescript
    %member% (has|have) discord [role] %role%
    %member% (doesn't|does not|do not|don't) have discord [role] %role%
    ```

## Is Attachment Audio

|Since|v4.12.0|class:version|

Check if the specified attachement is an **audio file** (aka a vocal message).
If it is, you'll be able to use [`duration of attachment`](expressions.md#attachment-duration) expression.

=== "Examples"

    ```applescript
    discord command vocal [<string>]:
    prefixes: !
    trigger:
        retrieve message with id arg-1 in event-channel and store it in {_msg}
        loop {_msg}'s attachments:
            set {_att} to loop-value
            if {_att} is audio:
                reply with "It's %duration of {_att}% long!"
                stop
        
        reply with "This message is not a voice message!"
    ```
=== "Patterns"

    ```applescript
    %attachment% (is|are) [an] audio
    %attachment% (isn't|is not|aren't|are not) [an] audio
    ```

## User is Bot

|Since|v4.0.0|class:version|

Check either the provided user is a discord bot or not.
=== "Examples"

    ```applescript
    event-user is a discord bot
    event-member is not a discord bot
    ```
=== "Patterns"

    ```applescript
    %users% (is|are) [a] discord bot
    %users% (isn't|is not|aren't|are not) [a] discord bot
    ```

## Message is From Guild

|Since|v4.0.0|class:version|

Check either a message related event come from a guild or from private messages.
This condition work with every event where a message is sent / received.
=== "Examples"

    ```applescript
    if event is from guild:
    if message come from private message:
    ```
=== "Patterns"

    ```applescript
    [the] (message|event) (is coming|come from|is from) guild [channel]
    [the] (message|event) (is coming|come from|is from) (dm|(private|direct) message) [channel]
    ```

## Is Attachment Image

|Since|v1.7|class:version|

See if a specific attachment is an image.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    att[achment[s]] %attachment% is [an] (image|img)
    att[achment[s]] %attachment% (isn't|is not|wasn't|was not) [an] (image|img)
    ```

## Is Attachment Spoiler

|Since|v1.7|class:version|

See if a specific attachment is marked as a spoil.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    att[achment[s]] %attachment% is [a] spoil[er]
    att[achment[s]] %attachment% (isn't|is not|wasn't|was not) [a] spoil[er]
    ```

## Is Attachment Video

|Since|v1.7|class:version|

See if a specific attachment is a video.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    att[achment[s]] %attachment% is [a] (vdo|video)
    att[achment[s]] %attachment% (isn't|is not|wasn't|was not) [a] (vdo|video)
    ```

## BotIsLoaded

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %string% (is|are) [been] loaded (in|on|from|over) discord
    %string% (isn't|is not|aren't|are not) [been] loaded (in|on|from|over) discord
    ```

## EmoteIsAnimated

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %emote% (is|are) animated
    %emote% (isn't|is not|aren't|are not) animated
    ```

## EmoteIsEmote

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %emote% (is|are) [a[n]] emote
    %emote% (isn't|is not|aren't|are not) [a[n]] emote
    ```

## Tag Required

|Since|v4.0.0|class:version|

Check if a forum channel require a tag to be set when creating a new post.
Can be changed using the 'tag required' expression.
=== "Examples"

    ```applescript
    if event-forumchannel is tag required:
    set tag required of event-forumchannel to false
    ```
=== "Patterns"

    ```applescript
    %forumchannel% (is|are) tag required
    %forumchannel% (isn't|is not|aren't|are not) tag required
    ```

## Is Edited

|Since|v4.0.0|class:version|

Return true if the message was edited. Because of discord limitations, we cannot get the editing date.
=== "Examples"

    ```applescript
    event-message is edited
    ```
=== "Patterns"

    ```applescript
    %message% (is|are) edited
    %message% (isn't|is not|aren't|are not) edited
    ```

## Is Ephemeral

|Since|v4.0.0|class:version|

Return true if the message was ephemeral, e.g. private / hidden.
Action on hidden messages are limited.
=== "Examples"

    ```applescript
    event-message is ephemeral
    ```
=== "Patterns"

    ```applescript
    %message% (is|are) ephemeral
    %message% (isn't|is not|aren't|are not) ephemeral
    ```

## Is Pinned

|Since|v4.0.0|class:version|

Return true if the message is pinned.
=== "Examples"

    ```applescript
    event-message is pinned
    ```
=== "Patterns"

    ```applescript
    %message% (is|are) pin[ned]
    %message% (isn't|is not|aren't|are not) pin[ned]
    ```

## Is Posted

|Since|v4.0.0|class:version|

Return true if the message is posted, means sent in every guild that follow this news channel.
=== "Examples"

    ```applescript
    event-message is posted
    ```
=== "Patterns"

    ```applescript
    %message% (is|are) (publish|post|crosspost)ed
    %message% (isn't|is not|aren't|are not) (publish|post|crosspost)ed
    ```

## Is TTS

|Since|v4.0.0|class:version|

Return true if the message is TTS (TextToSpeech).
=== "Examples"

    ```applescript
    event-message is tts
    ```
=== "Patterns"

    ```applescript
    %message% (is|are) (tts|text to speech)
    %message% (isn't|is not|aren't|are not) (tts|text to speech)
    ```

## Profile Has Banner

|Since|v4.0.0|class:version|

Check if the specified profile have a custom banner set or not.
Useful to manage either its banner URL of color accent.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %userprofile% (has|have) [custom] banner
    %userprofile% (doesn't|does not|do not|don't) have [custom] banner
    ```

## Thread Is Archived

|Since|v4.8.0|class:version|

Check if a thread is archived or not.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %threadchannel% (is|are) [a] archived [thread]
    %threadchannel% (isn't|is not|aren't|are not) [a] archived [thread]
    ```

## Thread Is Locked

|Since|v4.8.0|class:version|

Check if a thread is locked or not.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %threadchannel% (is|are) [a] locked [thread]
    %threadchannel% (isn't|is not|aren't|are not) [a] locked [thread]
    ```

## Thread Is Public

|Since|v4.8.0|class:version|

Check if a thread is public or not.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %threadchannel% (is|are) [a] public [thread]
    %threadchannel% (isn't|is not|aren't|are not) [a] public [thread]
    ```

