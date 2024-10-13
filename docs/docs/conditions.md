---
icon: material/check-all
---

# Conditions

[[[% import 'macros.html' as macros %]]]

## Is Message Forwarded

[[[ macros.required_version('4.20.0') ]]]

Check if a message is a 'forwarded message' or not, basically a message that was sent from another channel.

=== "Examples"

    ```applescript
    if event-message is forwarded:
    if event-message is not forwarded:
    ```

=== "Patterns"

    ```applescript
    %message% (is|are) forwarded
    %message% (isn't|is not|aren't|are not) forwarded
    ```

## Member / Bot is in Thread

[[[ macros.required_version('4.0.0') ]]]

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

## Member is muted

[[[ macros.required_version('4.14.3') ]]]

Check if a member is muted in a voice channel. You can specify if you want to get its **guild** or **self** state. Keep in mind the default condition (e.g. `... is muted`) will check both states!

=== "Examples"

    ```applescript
    if event-member is muted:
    if event-member is self muted:
    ```

=== "Patterns"

    ```applescript
    %member% (is|are) [discord] [member] [(:self|:guild)] deafen[ed]
    %member% (isn't|is not|aren't|are not) [discord] [member] [(:self|:guild)] deafen[ed]
    ```

## Member is Deafened

[[[ macros.required_version('4.14.3') ]]]

Check if a member is deafened in a voice channel. You can specify if you want to get its **guild** or **self** state. Keep in mind the default condition (e.g. `... is deafened`) will check both states!

=== "Examples"

    ```applescript
    if event-member is deafened:
    if event-member is guild deafened:
    ```

=== "Patterns"

    ```applescript
    %member% (is|are) [discord] [member] [(:self|:guild)] deafen[ed]
    %member% (isn't|is not|aren't|are not) [discord] [member] [(:self|:guild)] deafen[ed]
    ```

## ChannelType

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.12.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('1.7') ]]]

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

[[[ macros.required_version('1.7') ]]]

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

[[[ macros.required_version('1.7') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.0.0') ]]]

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

[[[ macros.required_version('4.8.0') ]]]

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

[[[ macros.required_version('4.8.0') ]]]

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

[[[ macros.required_version('4.8.0') ]]]

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

