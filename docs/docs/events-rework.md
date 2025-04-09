---
icon: material/check-all
---

# Events

[[[% import 'macros.html' as macros %]]]

## Information: Retrieve-Values

For some event, you can see a `retrieve values` section. Some values are given by Discord directly, and others needs another **request** to Discord to get the value (those are in as `retrieve values`).

!!! example ""
    For instance in the [Reaction Add Event](#reaction-add), Discord gives us the message ID only, so you can use its retrieve value to get the actual message:

    ```applescript
    on reaction add:
        # </>

        retrieve event value "message" and store it in {_message}
        # now you can use {_message} as the message that was reacted to!
    ```

## Bot Join Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the bot joins a new guild/server.
This event is useful for setting up initial configurations when the bot enters a new server,
such as adding default roles, sending welcome messages, or initializing server-specific settings.

=== "Examples"
    ```applescript
    on bot join:
    broadcast "Bot joined a new server: %event-guild%!"
    ```

=== "Patterns"
    ```applescript
    bot [guild] join[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)


## Bot Leave Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the bot leaves a guild/server.
This event can be used for cleanup operations or logging when the bot is removed from a server,
either by being kicked, the server being deleted, or the bot owner removing it manually.

=== "Examples"
    ```applescript
    on bot leave:
    broadcast "Bot left the server: %event-guild%"
    ```

=== "Patterns"
    ```applescript
    bot [guild] (leave|left) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)


## Bot Shutdown Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a bot is shutting down or being stopped.
This event is triggered when the bot's connection to Discord is closing,
which can happen during server restarts, plugin reloads, or manual bot shutdowns.
It provides an opportunity to perform cleanup operations or save data before the bot goes offline.

=== "Examples"
    ```applescript
    on bot shutdown:
    broadcast "Bot %event-bot% is shutting down!"
    ```

=== "Patterns"
    ```applescript
    bot (shutdown|stop) [seen by %-string%]
    ```

=== "Event Values"


## Guild Ready Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a guild is fully loaded and all its data is accessible.
This event occurs for each guild the bot is connected to when starting up.
It's fired before the global Ready event and indicates that guild-specific data
like members, channels, and roles have been loaded and are available for use.

=== "Examples"
    ```applescript
    on guild ready:
    broadcast "Guild %event-guild% is now fully loaded!"
    ```

=== "Patterns"
    ```applescript
    guild (ready|load[ed]) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)


## Bot Ready Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a bot is fully loaded and connected to Discord.
This event is triggered once all guilds are ready and the bot's connection to Discord
is completely established. This is the ideal event to use for initialization code that
needs to run once when the bot starts up, such as scheduling tasks or initializing resources.

=== "Examples"
    ```applescript
    on bot loaded:
    broadcast "Bot %event-bot% is now online and ready!"
    ```

=== "Patterns"
    ```applescript
    (ready|bot load[ed]) [seen by %-string%]
    ```

=== "Event Values"


## Interaction Command Events

These events are fired when a user interacts with a command:

- Slash Command: Fired when a user executes a slash command. (+ includes an auto-complete event)
- Message Command: Fired when a user interacts with a message command (right click on a message).
- User Command: Fired when a user interacts with a user command (right click on a user).

Refer to individual event documentation for more details.

### Slash Command

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user execute a specific slash command.
Use 'used command' to get the command name. Don't forget to either reply or defer the interaction, You can only defer using the wait pattern  e.g: 'defer the interaction and wait [silently].
You can get value of arguments using 'argument "name" as string' for example.

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    slash command [receive[d]] [seen by %-string%]
    ```

=== "Event Values"
    * `(execute|use)[d] [slash] command` - Returns a `string`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-string`](../docs/types.md#string)
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Message Command

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when someone click on a message application command.
Use `used command` to get the command name and `target message` for the targeted message. Don't forget to either reply to the interaction. Defer doesn't work here.

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    message command [receive[d]] [seen by %-string%]
    ```

=== "Event Values"
    * `(execute|use)[d] [message] command` - Returns a `string`.
    * `[the] target message` - Returns a `message`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-string`](../docs/types.md#string)
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-message`](../docs/types.md#message)


### User Command

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when someone click on a user application command.
Use `used command` to get the command name and `target user` for the targeted user. Don't forget to either reply to the interaction. Defer doesn't work here.

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    user command [receive[d]] [seen by %-string%]
    ```

=== "Event Values"
    * `(execute|use)[d] [user] command` - Returns a `string`.
    * `[the] target user` - Returns a `user`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-string`](../docs/types.md#string)
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Slash Command Completion Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when Discord requests argument autocompletion for a slash command.
Use 'event-string' to get the command name.
Use the 'return' effect to provide completion choices to the user.
You can access the focused argument with 'current argument' and other argument values with 'argument "name" as type'.

=== "Examples"
    ```applescript
    on slash completion:
    if event-string is "mycommand":
        if current argument is "option":
            return choice "Option 1" with value "option1", choice "Option 2" with value "option2"
    ```

=== "Patterns"
    ```applescript
    slash completion [receive[d]] [seen by %-string%]
    ```

=== "Event Values"
    * `current( |-)arg[ument] [name]` - Returns a `string`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-string`](../docs/types.md#string)


## Channel Events

These events are fired when a channel is created, deleted, or updated.
This include all types of channels, including text, voice, forum, private, ... channels.

### Channel Create Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel is created.

=== "Examples"
    ```applescript
    on channel creation:
    broadcast "%event-channel%, %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel creat(e|ion) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Delete Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel is deleted.

=== "Examples"
    ```applescript
    on channel deletion:
    broadcast "%event-channel%, %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel delet(e|ion) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Name Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's name is changed.

=== "Examples"
    ```applescript
    on channel name change:
    broadcast "Channel %event-channel% was renamed from %previous channel name% to %current channel name%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel name (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] name` - Returns a `string`.
    * `(old|past|previous) [channel] name` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Topic Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's topic is changed.

=== "Examples"
    ```applescript
    on channel topic change:
    broadcast "Channel %event-channel% had its topic changed from '%previous channel topic%' to '%current channel topic%'"
    ```

=== "Patterns"
    ```applescript
    [discord] channel topic (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] topic` - Returns a `string`.
    * `(old|past|previous) [channel] topic` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel NSFW Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's NSFW status is changed.

=== "Examples"
    ```applescript
    on channel nsfw change:
    broadcast "Channel %event-channel% NSFW status changed from %past nsfw state% to %current nsfw state%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel nsfw (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] nsfw state` - Returns a `boolean`.
    * `(old|past|previous) [channel] nsfw state` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Position Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's position is changed.

=== "Examples"
    ```applescript
    on channel position change:
    broadcast "Channel %event-channel% position changed from %past channel position% to %current channel position%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel position (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [chaannel] position` - Returns a `integer`.
    * `(old|past|previous) [chaannel] position` - Returns a `integer`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Parent Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's parent category is changed.

=== "Examples"
    ```applescript
    on channel parent change:
    broadcast "Channel %event-channel% was moved from %past parent% to %parent%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel parent (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [category] parent` - Returns a `category`.
    * `(old|past|previous) [category] parent` - Returns a `category`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Slowmode Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's slowmode setting is changed.

=== "Examples"
    ```applescript
    on channel slowmode change:
    broadcast "Channel %event-channel% slowmode changed from %past channel slowmode% to %new channel slowmode% seconds"
    ```

=== "Patterns"
    ```applescript
    [discord] channel slowmode (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] slowmode` - Returns a `number`.
    * `(old|past|previous) [channel] slowmode` - Returns a `number`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Type Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's type is changed.

=== "Examples"
    ```applescript
    on channel type change:
    broadcast "Channel %event-channel% type changed from %past channel type% to %current channel type%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel type (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] type` - Returns a `channeltype`.
    * `(old|past|previous) [channel] type` - Returns a `channeltype`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel User Limit Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a voice channel's user limit is changed.

=== "Examples"
    ```applescript
    on channel user limit change:
    broadcast "Channel %event-channel% user limit changed from %past user limit% to %current user limit%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel user limit (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] user limit` - Returns a `number`.
    * `(old|past|previous) [channel] user limit` - Returns a `number`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Bitrate Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a voice channel's bitrate is changed.

=== "Examples"
    ```applescript
    on channel bitrate change:
    broadcast "Channel %event-channel% bitrate changed from %past bitrate% to %current bitrate%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel bitrate (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] bitrate` - Returns a `number`.
    * `(old|past|previous) [channel] bitrate` - Returns a `number`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Region Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a voice channel's region is changed.

=== "Examples"
    ```applescript
    on channel region change:
    broadcast "Channel %event-channel% region changed from %past channel region% to %current channel region%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel region (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] region` - Returns a `string`.
    * `(old|past|previous) [channel] region` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Voice Status Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a voice channel's status (video or voice) is changed.

=== "Examples"
    ```applescript
    on channel voice status change:
    broadcast "Channel %event-channel% voice status changed from %past channel voice status% to %current channel voice status%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel voice status (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] voice status` - Returns a `string`.
    * `(old|past|previous) [channel] voice status` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Applied Tags Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a forum channel's applied tags are changed.

=== "Examples"
    ```applescript
    on channel tags change:
    broadcast "Channel %event-channel% applied tags changed from %old applied tags% to %new applied tags%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel [applied] tags (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [applied] tags` - Returns a list of `forumtag`.
    * `(old|past|previous) [applied] tags` - Returns a list of `forumtag`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Archived Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a thread channel's archived status is changed.

=== "Examples"
    ```applescript
    on channel archived change:
    broadcast "Channel %event-channel% archived status changed from %past channel archived state% to %current channel archived state%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel archived (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] archive[d] state` - Returns a `boolean`.
    * `(old|past|previous) [channel] archive[d] state` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Archive Timestamp/Date Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a thread channel's archive timestamp is changed.

=== "Examples"
    ```applescript
    on channel archive timestamp change:
    broadcast "Channel %event-channel% archive timestamp changed from %past channel archive timestamp% to %current channel archive timestamp%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel archive (timestam|date) (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] archive (timestamp|date)` - Returns a `date`.
    * `(old|past|previous) [channel] archive (timestamp|date)` - Returns a `date`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Auto Archive Duration Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a thread channel's auto archive duration is changed.

=== "Examples"
    ```applescript
    on channel auto-archive duration change:
    broadcast "Channel %event-channel% auto archive duration changed from %past channel auto archive duration% to %current channel auto archive duration%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel auto[( |-)]archive duration (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] auto archive duration` - Returns a `timespan`.
    * `(old|past|previous) [channel] auto archive duration` - Returns a `timespan`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Default Layout Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a forum channel's default layout is changed.

=== "Examples"
    ```applescript
    on channel default layout change:
    broadcast "Channel %event-channel% default layout changed from %old default layout% to %new default layout%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel default layout (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] default layout` - Returns a `string`.
    * `(old|past|previous) [channel] default layout` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Default Reaction Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a forum channel's default reaction is changed.

=== "Examples"
    ```applescript
    on channel default reaction change:
    broadcast "Channel %event-channel% default reaction changed from %old default reaction% to %new default reaction%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel default reaction (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] default reaction` - Returns a `emote`.
    * `(old|past|previous) [channel] default reaction` - Returns a `emote`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Default Sort Order Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a forum channel's default sort order is changed.

=== "Examples"
    ```applescript
    on channel default sort order change:
    broadcast "Channel %event-channel% default sort order changed from %old default sort order% to %new default sort order%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel default sort order (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] default sort order` - Returns a `string`.
    * `(old|past|previous) [channel] default sort order` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Default Thread Slowmode Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a forum channel's default thread slowmode is changed.

=== "Examples"
    ```applescript
    on channel default thread slowmode change:
    broadcast "Channel %event-channel% default thread slowmode changed from %old default thread slowmode% to %new default thread slowmode%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel default thread slowmode (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] default thread slowmode` - Returns a `number`.
    * `(old|past|previous) [channel] default thread slowmode` - Returns a `number`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Flags Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel's flags are changed.

=== "Examples"
    ```applescript
    on channel flags change:
    broadcast "Channel %event-channel% flags changed from %old channel flags% to %new channel flags%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel flags (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] flags` - Returns a list of `string`.
    * `(old|past|previous) [channel] flags` - Returns a list of `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Invitable Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a thread channel's invitable status is changed.

=== "Examples"
    ```applescript
    on channel invitable change:
    broadcast "Channel %event-channel% invitable status changed from %past channel invitable state% to %current channel invitable state%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel invitable (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] invitable [state]` - Returns a `boolean`.
    * `(old|past|previous) [channel] invitable [state]` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Channel Locked Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a thread channel's locked status is changed.

=== "Examples"
    ```applescript
    on channel locked change:
    broadcast "Channel %event-channel% locked status changed from %past channel locked state% to %current channel locked state%"
    ```

=== "Patterns"
    ```applescript
    [discord] channel locked (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [channel] locked [state]` - Returns a `boolean`.
    * `(old|past|previous) [channel] locked [state]` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


## Role Events

These events are triggered when a role is created, deleted, or updated in a Discord server.
They provide access to the role and guild involved in the event.
These events are useful for tracking changes to roles, managing permissions, and implementing role-based features.

### Role Create Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a new role is created in a guild.
This event provides access to the newly created role and the guild it belongs to.
It's useful for tracking administrative changes or implementing role management systems.

=== "Examples"
    ```applescript
    on role create:
    broadcast "New role created: %event-role% in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role create[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Delete Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a role is deleted from a guild.
This event provides access to the deleted role and the guild it belonged to.
It can be used for auditing purposes or to trigger cleanup actions in your bot.

=== "Examples"
    ```applescript
    on role delete:
    broadcast "Role %event-role% was deleted from %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role delete [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Color Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the color of a role changes.
This event provides access to both the old and new colors of the role.
It can be used for tracking aesthetic changes to roles or for synchronization systems.

=== "Examples"
    ```applescript
    on role color change:
    broadcast "Role %event-role% color changed from %previous role color% to %current role color%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role color (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role color` - Returns a `color`.
    * `(old|past|previous) role color` - Returns a `color`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Name Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the name of a role changes.
This event provides access to both the old and new names of the role.
It's useful for tracking role identity changes or updating external systems that reference roles by name.

=== "Examples"
    ```applescript
    on role name change:
    broadcast "Role name changed from '%previous role name%' to '%current role name%' in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role name (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role name` - Returns a `string`.
    * `(old|past|previous) role name` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Hoisted Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the hoisted status of a role changes.
Hoisted roles are displayed separately in the member list.
This event provides access to both the old and new hoisted states.
It's useful for tracking changes to role visibility in the member sidebar.

=== "Examples"
    ```applescript
    on role hoisted change:
    if current role hoisted state is true:
        broadcast "Role %event-role% is now shown separately in the member list"
    else:
        broadcast "Role %event-role% is no longer shown separately in the member list"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role hoist[ed] (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role hoisted [state]` - Returns a `boolean`.
    * `(old|past|previous) role hoisted [state]` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Icon Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the icon of a role changes.
This event provides access to both the old and new icon URLs.
It can be used for tracking visual changes to roles or updating external systems.

=== "Examples"
    ```applescript
    on role icon change:
    broadcast "Role %event-role% icon changed from %previous role icon% to %current role icon%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role icon (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role icon` - Returns a `string`.
    * `(old|past|previous) role icon` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Position Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the position of a role changes in the role hierarchy.
This event provides access to both the old and new positions.
It's useful for tracking changes to the role hierarchy that may affect permissions.

=== "Examples"
    ```applescript
    on role position change:
    broadcast "Role %event-role% position changed from %previous role position% to %current role position%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role position (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role position` - Returns a `integer`.
    * `(old|past|previous) role position` - Returns a `integer`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Permissions Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the permissions of a role change.
This event provides access to both the old and new permission sets.
It's crucial for security monitoring, permission auditing, and tracking administrative changes.

=== "Examples"
    ```applescript
    on role permissions change:
    broadcast "Permissions for role %event-role% have been updated in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role permission[s] (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role permission[s]` - Returns a list of `permission`.
    * `(old|past|previous) role permission[s]` - Returns a list of `permission`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


### Role Mentionable Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the mentionable status of a role changes.
This event tracks whether a role can be mentioned by regular users.
It provides access to both the old and new mentionable states.
It's useful for tracking changes that affect role notifications and visibility.

=== "Examples"
    ```applescript
    on role mentionable change:
    if current role mentionable state is true:
        broadcast "Role %event-role% can now be mentioned by everyone"
    else:
        broadcast "Role %event-role% can no longer be mentioned by everyone"
    ```

=== "Patterns"
    ```applescript
    [discord] [guild] role mentionable (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] role mentionable [state]` - Returns a `boolean`.
    * `(old|past|previous) role mentionable [state]` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-role`](../docs/types.md#role)


## Guild Events

Events related to guilds (servers) on Discord.
These events are triggered when certain actions occur within a guild, such as changes to settings, member actions, or administrative tasks.

### AutoMod Execution

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an automated automod response has been triggered through an automod Rule. Can be used to get the channel, user content, keyword that was found, the automod response and the id of the automod rule, the user, the id of the message which triggered the rule, the guild it occurred in, and the id of the alert message sent to the alert channel (if configured).

=== "Examples"
    ```applescript
    on automod execute:
    broadcast "AutoMod rule triggered by %event-user% in %event-channel%"
    ```

=== "Patterns"
    ```applescript
    [discord] automod (execution|execute) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-null`](../docs/types.md#null)
    * [`event-null`](../docs/types.md#null)
    * [`event-string`](../docs/types.md#string)
    * [`event-string`](../docs/types.md#string)
    * [`event-user`](../docs/types.md#user)


### Guild Ban Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user is banned from a guild. A member doesn't exist here because the member is not in the guild anymore! Can be used to get the banned user, the author and the guild.

=== "Examples"
    ```applescript
    on guild ban:
    broadcast "%event-user% was banned from %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [user] ban [seen by %-string%]
    ```

=== "Event Values"
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)


### Guild Join Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the bot joins a guild. Use this to set up initial configurations or welcome messages.

=== "Examples"
    ```applescript
    on bot join guild:
    broadcast "Bot joined %event-guild%!"
    ```

=== "Patterns"
    ```applescript
    [discord] bot join guild [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)


### Guild Log Entry Create Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a new log entry is created in a guild. Can be used to monitor administrative actions within a guild.

=== "Examples"
    ```applescript
    on guild log entry create:
    broadcast "New audit log entry created in %event-guild% for action type %event-entry's type%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild log [entry] create [seen by %-string%]
    ```

=== "Event Values"
    * [`event-logentry`](../docs/types.md#logentry)
    * [`event-guild`](../docs/types.md#guild)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `author`


### Guild Unban Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user is unbanned from a guild. Can be used to get the unbanned user, the author and the guild.

=== "Examples"
    ```applescript
    on guild unban:
    broadcast "%event-user% was unbanned from %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [user] unban [seen by %-string%]
    ```

=== "Event Values"
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)


### Invite Create Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an invite is created in a guild. Can be used to get the invite properties, the channel, the author and the guild.

=== "Examples"
    ```applescript
    on guild invite create:
    broadcast "New invite created in %event-channel% with code %event-invite's code%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild invite create [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-invite`](../docs/types.md#invite)
    * [`event-guild`](../docs/types.md#guild)


### Invite Delete Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an invite is deleted from a guild. Can be used to get the invite code, the channel, the author and the guild.

=== "Examples"
    ```applescript
    on guild invite delete:
    broadcast "Invite deleted from %event-channel% in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild invite delete [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-guild`](../docs/types.md#guild)


### Guild AFK Channel Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the AFK channel of a guild changes. Can be used to get the old/new channel, the author and the guild.

=== "Examples"
    ```applescript
    on guild afk channel change:
    broadcast "Guild %event-guild% changed AFK channel from %past afk channel% to %current afk channel%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild afk channel (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] afk channel` - Returns a `voicechannel`.
    * `(old|past|previous) afk channel` - Returns a `voicechannel`.
    * [`event-guild`](../docs/types.md#guild)


### Guild AFK Timeout Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the AFK timeout of a guild changes. Can be used to get the old/new timeout value, the author and the guild.

=== "Examples"
    ```applescript
    on guild afk timeout change:
    broadcast "Guild %event-guild% changed AFK timeout from %past afk timeout% to %current afk timeout%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild afk timeout (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] afk timeout` - Returns a `null`.
    * `(old|past|previous) afk timeout` - Returns a `null`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Banner Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the banner of a guild changes. Can be used to get the old/new banner URL, the author and the guild.

=== "Examples"
    ```applescript
    on guild banner change:
    broadcast "Guild %event-guild% changed banner from %past banner% to %current banner%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild banner (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] banner` - Returns a `string`.
    * `(old|past|previous) banner` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Boost Count Update

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the boost count of a guild changes. Can be used to get the old/new count, and the guild.

=== "Examples"
    ```applescript
    on guild boost count change:
    broadcast "Guild %event-guild% boost count changed from %past boost count% to %current boost count%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild boost count (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] boost count` - Returns a `integer`.
    * `(old|past|previous) boost count` - Returns a `integer`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Boost Tier Update

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the boost tier of a guild changes. Can be used to get the old/new tier, and the guild.

=== "Examples"
    ```applescript
    on guild boost tier change:
    broadcast "Guild %event-guild% boost tier changed from %past boost tier% to %current boost tier%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild boost tier (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] boost tier` - Returns a `string`.
    * `(old|past|previous) boost tier` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Icon Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the icon of a guild changes. Can be used to get the old/new icon URL, the author and the guild.

=== "Examples"
    ```applescript
    on guild icon change:
    broadcast "Guild %event-guild% changed icon from %past icon% to %current icon%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild icon (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] icon` - Returns a `string`.
    * `(old|past|previous) icon` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Name Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the name of a guild is changed. Can be used to get the old/new name, the author and the guild.

=== "Examples"
    ```applescript
    on guild name change:
    broadcast "Guild name changed from '%past guild name%' to '%current guild name%'"
    ```

=== "Patterns"
    ```applescript
    [discord] guild name (update|change) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] guild name` - Returns a `string`.
    * `(old|past|previous) guild name` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Owner Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the owner of a guild changes. Can be used to get the old/new owner, the author and the guild.

=== "Examples"
    ```applescript
    on guild owner change:
    broadcast "Guild %event-guild% owner changed from %past owner% to %current owner%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild owner (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] owner` - Returns a `member`.
    * `(old|past|previous) owner` - Returns a `member`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Splash Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the splash image of a guild changes. Can be used to get the old/new splash URL, the author and the guild.

=== "Examples"
    ```applescript
    on guild splash change:
    broadcast "Guild %event-guild% splash changed from %past splash% to %current splash%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild splash (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] splash` - Returns a `string`.
    * `(old|past|previous) splash` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Deafen Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is deafened or undeafened by the guild. Can be used to track moderation actions in voice channels.

=== "Examples"
    ```applescript
    on guild voice deafen:
    if event-boolean is true:
        broadcast "%event-member% was deafened in %event-guild%"
    else:
        broadcast "%event-member% was undeafened in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] deafen[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Mute Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is muted or unmuted by the guild. Can be used to track moderation actions in voice channels.

=== "Examples"
    ```applescript
    on guild voice mute:
    if event-boolean is true:
        broadcast "%event-member% was muted in %event-guild%"
    else:
        broadcast "%event-member% was unmuted in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] mute[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Mute Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is muted or unmuted by the guild. Can be used to track moderation actions in voice channels.

=== "Examples"
    ```applescript
    on guild voice mute:
    if event-boolean is true:
        broadcast "%event-member% was muted in %event-guild%"
    else:
        broadcast "%event-member% was unmuted in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] mute[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Request To Speak Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member requests to speak in a stage channel. Can be used to track moderation actions in voice channels.
You may use `event-boolean` to check if the state is true (user requested to speak) or false (user cancelled the request).

=== "Examples"
    ```applescript
    on guild voice request to speak:
    if event-boolean is true:
        broadcast "%event-member% requested to speak in %event-guild%"
    else:
        broadcast "%event-member% cancelled their request to speak in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] request to speak [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] request to speak` - Returns a `date`.
    * `(old|past|previous) request to speak` - Returns a `date`.
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Stream Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member starts or stops streaming in a voice channel. Can be used to track moderation actions in voice channels.
You may use `event-boolean` to check if the state is true (user started streaming) or false (user stopped streaming).

!!! warning "This **DOES NOT** include camera! Use the `GuildVoice Video Event` for that."

=== "Examples"
    ```applescript
    on guild voice stream:
    if event-boolean is true:
        broadcast "%event-member% started streaming in %event-guild%"
    else:
        broadcast "%event-member% stopped streaming in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] stream[ing] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Guild Voice Video Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member starts or stops its camera in a voice channel. Can be used to track moderation actions in voice channels.
You may use `event-boolean` to check if the state is true (user started its camera) or false (user stopped its camera).

!!! warning "This **DOES NOT** include streams! Use the `Guild Voice Stream Event` instead."

=== "Examples"
    ```applescript
    on guild voice video:
    if event-boolean is true:
        broadcast "%event-member% started video in %event-guild%"
    else:
        broadcast "%event-member% stopped video in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [discord] guild [voice] video[ing] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-boolean`](../docs/types.md#boolean)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Thread Join Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a tread, either by joining itself or by a moderator can be used to get the thread, the guild and the member.

=== "Examples"
    ```applescript
    on thread join:
    ```

=== "Patterns"
    ```applescript
    [discord] thread join [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### Thread Leave Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member leaves a thread, either by leaving itself or by a moderator can be used to get the thread, the guild and the member.

=== "Examples"
    ```applescript
    on thread leave:
    ```

=== "Patterns"
    ```applescript
    [discord] thread leave [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


## Component Interaction Events

Events that are fired when a component is interacted with.
This includes buttons, select menus, and modals.

!!! info "Check individual details to see if you are able to show a modal!"

### Button Click

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any button sent by the button is clicked.
You can use the `clicked id` to get the clicked button id.

!!! info "Modal can be shown in this interaction!"

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    on button clicked:
    reply with hidden "You clicked the button with id '%clicked id%'!" # This will defer the interaction!
    ```

=== "Patterns"
    ```applescript
    button click[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `click[ed] (id|button)` - Returns a `string`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-string`](../docs/types.md#string)
    * [`event-button`](../docs/types.md#button)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-user`](../docs/types.md#user)
    * [`event-member`](../docs/types.md#member)
    * [`event-number`](../docs/types.md#number)
    * [`event-message`](../docs/types.md#message)


### Modal Received

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a modal has been sent to the bot from any user.
Use 'received modal' to get the modal id. Don't forget to either reply or defer the interaction.

!!! warning "Modal can NOT be shown in this interaction!"

=== "Examples"
    ```applescript
    on modal received:
    reply with hidden "You clicked the button with id '%received modal%'!" # This will defer the interaction!
    ```

=== "Patterns"
    ```applescript
    modal (click[ed]|receive[d]) [seen by %-string%]
    ```

=== "Event Values"
    * `receive[d] (id|modal)` - Returns a `string`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-string`](../docs/types.md#string)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-user`](../docs/types.md#user)
    * [`event-member`](../docs/types.md#member)
    * [`event-number`](../docs/types.md#number)
    * [`event-message`](../docs/types.md#message)


### String Dropdown Click Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user selects one or more choices in a string dropdown menu.
This event provides access to the selected string values and dropdown details.
Don't forget to either reply to or defer the interaction to acknowledge it.
You can show a modal in response to this interaction.

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    on dropdown clicked:
    reply with "You selected: %selected values%"
    ```

=== "Patterns"
    ```applescript
    drop[( |-)]down click[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `select[ed] value[s]` - Returns a list of `string`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-message`](../docs/types.md#message)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-dropdown`](../docs/types.md#dropdown)
    * [`event-string`](../docs/types.md#string)
    * [`event-interaction`](../docs/types.md#interaction)


### Entity Dropdown Click Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user selects one or more entities in an entity dropdown menu.
This event provides access to the selected entities (users, roles, channels, etc.).
Don't forget to either reply to or defer the interaction to acknowledge it.
You can show a modal in response to this interaction.

!!! info "You can reply with a **modal** in this event."

=== "Examples"
    ```applescript
    on entity dropdown clicked:
    broadcast "User %event-user% selected entities: %selected entities%"
    ```

=== "Patterns"
    ```applescript
    entit(y|ies) drop[( |-)]down click[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `select[ed] entit(y|ies)` - Returns a list of `object`.
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-message`](../docs/types.md#message)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-dropdown`](../docs/types.md#dropdown)
    * [`event-string`](../docs/types.md#string)
    * [`event-interaction`](../docs/types.md#interaction)


## Message Events

These events are fired when a message is received, edited or deleted.
This will be fired, by default, both guild & private messages, use the `event is from guild` condition to avoid confusion in your events.

### Message Receive

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any bot receive an actual message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    on message received:
        if message is from guild:
            reply with "I just received '%event-message%' from %mention tag of event-channel%!"
        else:
            reply with "I just received '%event-message%' from %mention tag of event-user%!"
    ```

=== "Patterns"
    ```applescript
    message receive[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-message`](../docs/types.md#message)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Message Delete

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any message is deleted.
Use 'event-string' to get the old message content, only works if this message was cached by DiSky before hand.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    message delete[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-string`](../docs/types.md#string)
    * [`event-message`](../docs/types.md#message)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-number`](../docs/types.md#number)


### Message Edit

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any message is edited / updated.
Use 'event-string' to get the old message content, only works if this message was cached by DiSky before hand.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    message edit[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-message`](../docs/types.md#message)
    * [`event-string`](../docs/types.md#string)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Poll Vote Add

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user adds their vote to a poll in a message.

=== "Examples"
    ```applescript
    on poll vote add:
    ```

=== "Patterns"
    ```applescript
    [message] poll vote add[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-number`](../docs/types.md#number)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `message`
    * `member`
    * `user`


### Poll Vote Remove

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user removes their vote from a poll in a message.

=== "Examples"
    ```applescript
    on poll vote remove:
        send "User %event-user% removed their vote from a poll in %event-channel%!" to console
    ```

=== "Patterns"
    ```applescript
    [message] poll vote remove[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-number`](../docs/types.md#number)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `message`
    * `member`
    * `user`


### Reaction Add

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a message, that can be seen by the bot, receive a reaction.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    (reaction|emote)[s] add[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-emote`](../docs/types.md#emote)
    * [`event-reaction`](../docs/types.md#reaction)
    * [`event-null`](../docs/types.md#null)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `message`


### Reaction Remove

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user remove a reaction from a specific message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    (reaction|emote)[s] remove[d] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)
    * [`event-emote`](../docs/types.md#emote)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `message`


### Reaction Remove All

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user remove every reactions from a message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.

=== "Examples"
    ```applescript
    No examples provided.
    ```

=== "Patterns"
    ```applescript
    (reaction|emote)[s] (remove[d] all|clear|reset) [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)

=== "REST/Retrieve Event Values"

    !!! info "Check the [retrieve values docs](#information-retrieve-values)!"

    * `message`


## User/Member Events

Events related to user/member actions and updates.
Keep in mind most user update events requires a member to be seen by the bot in any guild, with the intent 'guild presence' enabled.

### Member Join Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a guild.

=== "Examples"
    ```applescript
    on member join:
    broadcast "Welcome %event-member% to %event-guild%!"
    ```

=== "Patterns"
    ```applescript
    member join[ed] [guild] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Leave Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is removed from a guild either by leaving or being punished. Use the ban/kick event instead to check the exact reason.

=== "Examples"
    ```applescript
    on member leave:
    broadcast "%event-member% has left %event-guild%"
    ```

=== "Patterns"
    ```applescript
    member (leave|left) [guild] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Role Add Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member receives new roles. This is a log action, so event-author returns who made the action and event-roles returns a list of added roles.

=== "Examples"
    ```applescript
    on role add:
    broadcast "%event-author% added roles %added roles% to %event-member%"
    ```

=== "Patterns"
    ```applescript
    [member] role add[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `added roles` - Returns a list of `role`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Role Remove Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when roles are removed from a member. This is a log action, so event-author returns who made the action and event-roles returns a list of removed roles.

=== "Examples"
    ```applescript
    on role remove:
    broadcast "%event-author% removed roles %removed roles% from %event-member%"
    ```

=== "Patterns"
    ```applescript
    [member] role remove[d] [seen by %-string%]
    ```

=== "Event Values"
    * `removed roles` - Returns a list of `role`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Nickname Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member changes their nickname in a guild.

=== "Examples"
    ```applescript
    on member nickname change:
    broadcast "%event-member% changed their nickname from '%previous nickname%' to '%current nickname%'"
    ```

=== "Patterns"
    ```applescript
    [guild] member nickname (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] nickname` - Returns a `string`.
    * `(old|past|previous) [member] nickname` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Avatar Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member changes their server-specific avatar.

=== "Examples"
    ```applescript
    on member avatar change:
    broadcast "%event-member% changed their server avatar. New URL: %current avatar url%"
    ```

=== "Patterns"
    ```applescript
    [guild] member avatar (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] avatar url` - Returns a `string`.
    * `(old|past|previous) [member] avatar url` - Returns a `string`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Accept Screen Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member has agreed to membership screen requirements. This can be useful for adding roles since the member is not fully available until they've accepted the screen requirements.

=== "Examples"
    ```applescript
    on member screen accept:
    broadcast "%event-member% has completed the membership screening in %event-guild%"
    ```

=== "Patterns"
    ```applescript
    [guild] member screen accept [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] pending state` - Returns a `boolean`.
    * `(old|past|previous) [member] pending state` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Boost Time Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member's boost time is updated, which can happen when they start or stop boosting a server.

=== "Examples"
    ```applescript
    on member boost time change:
    broadcast "%event-member% boost time updated from %previous boost time% to %current boost time%"
    ```

=== "Patterns"
    ```applescript
    [guild] member boost time (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] boost time` - Returns a `date`.
    * `(old|past|previous) [member] boost time` - Returns a `date`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)


### Member Boost Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member boosts a server, which is detected through a system message in the server.

=== "Examples"
    ```applescript
    on member boost:
    broadcast "Thank you %event-user% for boosting %event-guild%!"
    ```

=== "Patterns"
    ```applescript
    member boost[ed] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-message`](../docs/types.md#message)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-user`](../docs/types.md#user)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### Member Timeout Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is timed out (temporarily restricted from interacting with the server).

=== "Examples"
    ```applescript
    on member timeout:
    broadcast "%event-member% has been timed out until %event-date%"
    ```

=== "Patterns"
    ```applescript
    member time[ ]out[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] timeout end` - Returns a `date`.
    * `(old|past|previous) [member] timeout end` - Returns a `date`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-user`](../docs/types.md#user)


### Member Self Mute Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member mutes or unmutes themselves in a voice channel.

=== "Examples"
    ```applescript
    on member mute:
    if event-boolean is true:
        broadcast "%event-member% muted themselves"
    else:
        broadcast "%event-member% unmuted themselves"
    ```

=== "Patterns"
    ```applescript
    member [self] [un]mute[d] [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] mute[d] state` - Returns a `boolean`.
    * `(old|past|previous) [member] mute[d] state` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Self Deafen Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member deafens or undeafens themselves in a voice channel.

=== "Examples"
    ```applescript
    on member deafen:
    if event-boolean is true:
        broadcast "%event-member% deafened themselves"
    else:
        broadcast "%event-member% undeafened themselves"
    ```

=== "Patterns"
    ```applescript
    member [self] [un]deafen[ed] [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [member] deafen[ed] state` - Returns a `boolean`.
    * `(old|past|previous) [member] deafen[ed] state` - Returns a `boolean`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Voice Join Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a voice or stage channel. This event also fires when a member moves from one voice channel to another.

=== "Examples"
    ```applescript
    on voice channel join:
    broadcast "%event-member% joined voice channel %event-voice-channel%"
    ```

=== "Patterns"
    ```applescript
    [member] voice [channel] join [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [joined] voice channel` - Returns a `audiochannel`.
    * `(old|past|previous) [joined] voice channel` - Returns a `audiochannel`.
    * `[(new|current)] [joined] voice` - Returns a `voicechannel`.
    * `(old|past|previous) [joined] voice` - Returns a `voicechannel`.
    * `[(new|current)] [joined] stage` - Returns a `stagechannel`.
    * `(old|past|previous) [joined] stage` - Returns a `stagechannel`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### Member Voice Leave Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member leaves a voice or stage channel. This includes both disconnecting completely and moving to another channel.

=== "Examples"
    ```applescript
    on voice channel leave:
    broadcast "%event-member% left voice channel %event-voice-channel%"
    ```

=== "Patterns"
    ```applescript
    [member] voice [channel] leave [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] [left] voice channel` - Returns a `audiochannel`.
    * `(old|past|previous) [left] voice channel` - Returns a `audiochannel`.
    * `[(new|current)] [left] voice` - Returns a `voicechannel`.
    * `(old|past|previous) [left] voice` - Returns a `voicechannel`.
    * `[(new|current)] [left] stage` - Returns a `stagechannel`.
    * `(old|past|previous) [left] stage` - Returns a `stagechannel`.
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### User Activity Order Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their activity order.
This event is triggered when a user starts a new activity or changes between activities.
Activities include playing games, listening to music, streaming, or custom status messages.

=== "Examples"
    ```applescript
    on user activity change:
    broadcast "%event-user% is now %event-user's activities%"
    ```

=== "Patterns"
    ```applescript
    [discord] user activity [order] (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `user activit(y|ies)` - Returns a list of `activity`.
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)


### User Avatar Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their avatar.
This event provides access to both the old and new avatar URLs.
It can be used for monitoring profile changes or updating cached user information.

=== "Examples"
    ```applescript
    on user avatar change:
    broadcast "%event-user% changed their avatar from %previous avatar url% to %current avatar url%"
    ```

=== "Patterns"
    ```applescript
    [discord] user avatar (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] avatar [url]` - Returns a `string`.
    * `(old|past|previous) avatar [url]` - Returns a `string`.
    * [`event-user`](../docs/types.md#user)


### User Discriminator Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their discriminator.
The discriminator is the four-digit number following a username (e.g., #1234).
This event provides access to both the old and new discriminator values.
Note: With Discord's migration to the new username system, this event may become less relevant.

=== "Examples"
    ```applescript
    on user discriminator change:
    broadcast "%event-user% changed their discriminator from %previous discriminator% to %current discriminator%"
    ```

=== "Patterns"
    ```applescript
    [discord] user discriminator (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] discriminator` - Returns a `string`.
    * `(old|past|previous) discriminator` - Returns a `string`.
    * [`event-user`](../docs/types.md#user)


### User Name Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their username (not nickname).
This event provides access to both the old and new usernames.
It can be used for monitoring identity changes or updating user databases.

=== "Examples"
    ```applescript
    on user name change:
    broadcast "User changed their name from %previous name% to %current name%"
    ```

=== "Patterns"
    ```applescript
    [discord] user name (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] name` - Returns a `string`.
    * `(old|past|previous) name` - Returns a `string`.
    * [`event-user`](../docs/types.md#user)


### User Online Status Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their online status.
This event provides access to both the old and new online status values.
It can be used for tracking user presence, activity patterns, or triggering actions when users come online.

=== "Examples"
    ```applescript
    on user online status change:
    if current online status = online:
        broadcast "%event-user% has come online"
    ```

=== "Patterns"
    ```applescript
    [discord] user online status (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] online status` - Returns a `onlinestatus`.
    * `(old|past|previous) online status` - Returns a `onlinestatus`.
    * [`event-user`](../docs/types.md#user)
    * [`event-member`](../docs/types.md#member)
    * [`event-guild`](../docs/types.md#guild)


### User Typing Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user starts typing in a channel.
This event is triggered when the typing indicator appears for a user.
It can be used to detect activity in channels or for interactive bot responses.

=== "Examples"
    ```applescript
    on user typing:
    if event-channel is text channel with id "123456789":
        broadcast "%event-user% is typing in the support channel!"
    ```

=== "Patterns"
    ```applescript
    [discord] user typ[e|ing] [seen by %-string%]
    ```

=== "Event Values"
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-member`](../docs/types.md#member)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-messagechannel`](../docs/types.md#messagechannel)
    * [`event-audiochannel`](../docs/types.md#audiochannel)
    * [`event-voicechannel`](../docs/types.md#voicechannel)
    * [`event-stagechannel`](../docs/types.md#stagechannel)
    * [`event-privatechannel`](../docs/types.md#privatechannel)
    * [`event-guildchannel`](../docs/types.md#guildchannel)
    * [`event-textchannel`](../docs/types.md#textchannel)
    * [`event-newschannel`](../docs/types.md#newschannel)
    * [`event-threadchannel`](../docs/types.md#threadchannel)
    * [`event-forumchannel`](../docs/types.md#forumchannel)


### User Global Name Update Event

[[[ macros.required_version('4.23.0-alpha2') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes their global display name.
This event provides access to both the old and new global names.
With Discord's new username system, this tracks the display name shown across all servers.

=== "Examples"
    ```applescript
    on user global name change:
    broadcast "%event-user% changed their display name from '%previous global name%' to '%current global name%'"
    ```

=== "Patterns"
    ```applescript
    [discord] user global name (change|update) [seen by %-string%]
    ```

=== "Event Values"
    * `[(new|current)] global name` - Returns a `string`.
    * `(old|past|previous) global name` - Returns a `string`.
    * [`event-user`](../docs/types.md#user)


