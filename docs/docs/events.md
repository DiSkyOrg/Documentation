---
icon: material/check-all
---

# Events

[[[% import 'macros.html' as macros %]]]

## Information: Retrieve-Values

For some event, you can see a `retrieve values` section. Some values are given by Discord directly, and others needs another **request** to Discord to get the value (those are in as `retrieve values`).

!!! example ""
    For instance in the [Reaction Add Event](#on-reaction-add), Discord gives us the message ID only, so you can use its retrieve value to get the actual message:

    ```applescript
    on reaction add:
        # </>

        retrieve event value "message" and store it in {_message}
        # now you can use {_message} as the message that was reacted to!
    ```

## On Bot Creation Structure

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

No description provided.
=== "Patterns"

    ```applescript
    define [the] [new] bot (with name|named) %string%
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    
    ```

## On Member Kick

[[[ macros.required_version('4.17.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is kicked from a guild. This use a "*tricky*" way to get the kicked member, since the member is not in the guild anymore, so this event requires some preparation:

!!! warning "Requirements"
    * The [`guild members` intent](../bot/intents.md#guild-members-guild-members) to be enabled
    * The [`guild moderation` intent](../bot/intents.md#guild-moderation-guild-moderation) to be enabled
    * Target (the one who was kicked) and author (the one who kicked) members to be [**cached**](../bot/policy.md)

!!! note "Note"
    * `event-user` represent the **kicked member** (as it's not a member anymore, it's a user)
    * `event-member` represent the **author** (the one who kicked the member)
    * There's no possible way to get the **reason** of the kick, as Discord doesn't provide it at all

=== "Patterns"

    ```applescript
    [discord] member kick[ed]
    ```

=== "Examples"

    ```applescript
    on member kick:
        broadcast "%event-user% has been kicked from %event-guild% by %event-member%!"
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-user`](../docs/types.md#user) (the kicked member)
    * [`event-member`](../docs/types.md#member) (the author)
    * [`event-bot`](../docs/types.md#bot)

## On Member Ban

[[[ macros.required_version('4.17.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is banned from a guild. This use a "*tricky*" way to get the banned member, since the member is not in the guild anymore, so this event requires some preparation:

!!! warning "Requirements"
    * The [`guild members` intent](../bot/intents.md#guild-members-guild-members) to be enabled
    * The [`guild moderation` intent](../bot/intents.md#guild-moderation-guild-moderation) to be enabled
    * Target (the one who was banned) and author (the one who banned) members to be [**cached**](../bot/policy.md)

!!! note "Note"
    * `event-user` represent the **banned member** (as it's not a member anymore, it's a user)
    * `event-member` represent the **author** (the one who banned the member)
    * There's no possible way to get the **reason** of the ban, as Discord doesn't provide it at all 

=== "Patterns"

    ```applescript
    [discord] member ban[ned]
    ```

=== "Examples"

    ```applescript
    on member ban:
        broadcast "%event-user% has been banned from %event-guild% by %event-member%!"
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-user`](../docs/types.md#user) (the banned member)
    * [`event-member`](../docs/types.md#member) (the author)
    * [`event-bot`](../docs/types.md#bot)

## On Discord Command

[[[ macros.required_version('3.0.0') ]]]
[[[ macros.is_cancellable('Yes') ]]]

Custom DiSky discord command system. Arguments works like the normal skript's one and accept both optional and require arguments.
=== "Patterns"

    ```applescript
    discord command <([^\s]+)( .+)?$>
    ```
=== "Examples"

    ```applescript
    discord command move <member> <voicechannel>:
    	prefixes: !
    	trigger:
    		reply with mention tag of arg-2
    		move arg-1 to arg-2
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-discordcommand
    event-guildchannel
    event-member
    event-bot
    event-message
    event-string
    ```


## On Disky Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('Yes') ]]]

Fired when a disky/discord command is executed.
=== "Patterns"

    ```applescript
    disky command [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on disky command:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-discordcommand
    event-member
    event-bot
    event-message
    ```


## On Bot Join Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any bot join a new guild.
=== "Patterns"

    ```applescript
    bot [guild] join[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    ```

## On Bot Leave Event

[[[ macros.required_version('4.11.1') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any bot leave a guild.

=== "Patterns"

    ```applescript
    bot [guild] (leave|left) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on bot guild leave:
    	broadcast "%event-bot% left %event-guild%"
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    ```

## On Shutdown Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a bot is stopped.
=== "Patterns"

    ```applescript
    bot (shutdown|stop) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-bot
    ```

## On Channel Create Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a channel is created in a guild.

=== "Examples"
    
    ```applescript
    on channel create:
        broadcast "%event-channel% has been created in %event-guild%!"
    ```

=== "Patterns"

    ```applescript
    [discord] channel creat(e|ion)
    ```

=== "Event Values"
    * [`event-guild`](../docs/types.md#guild)
    * [`event-channel`](../docs/types.md#channel)
    * [`event-bot`](../docs/types.md#bot)


## On Guild Ready Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a guild is fully loaded.
=== "Patterns"

    ```applescript
    guild (ready|load[ed]) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    ```


## On Ready Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a bot is fully loaded. 'guild ready' should be called before this one.
=== "Patterns"

    ```applescript
    (ready|bot load[ed]) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-bot
    ```


## On DiSky Error / Exception

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any DiSky error occur.
Since DiSky exception are per-event only, this regroup every exception occurred in every events.
=== "Patterns"

    ```applescript
    disky (error|exception)
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-string
    ```


## On Guild AFK Channel Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a afk channel of a guild changes can be used to get the old/new channel, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild afk channel (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild afk channel change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-voicechannel
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild AFK Timeout Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a afk timeout of a guild changes can be used to get the old/new timeout value, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild afk timeout (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild afk timeout change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Ban Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user is banned from a guild. A member doesn't exist here because the member is not in the guild anymore! Can be used to get the banned user, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild [user] ban [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild ban:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Banner Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a banner of a guild changes can be used to get the old/new banner, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild banner (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild banner change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Boost Count Update

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a boost count of a guild changes - can be used to get the old/new count, and the guild.
=== "Patterns"

    ```applescript
    [discord] guild boost count (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild boost count change:
    ```
=== "Event Values"

    ```applescript
    event-integer
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Boost Tier Update

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a boost tier of a guild changes - can be used to get the old/new tier, and the guild.
=== "Patterns"

    ```applescript
    [discord] guild boost tier (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild boost tier change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Icon Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the icon of a guild changes can be used to get the old/new icon, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild icon (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild icon change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Poll Vote Add

[[[ macros.required_version('4.17.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user vote on a poll.

!!! warning "Requirements"
    * The [`guild message polls` intent](../bot/intents.md#message-polls) (to work in guilds)
    * The [`direct message polls` intent](../bot/intents.md#message-polls) (to work in DMs)
    
    If none of these intents are enabled, the event will not be fired at all.

=== "Patterns"

    ```applescript
    [message] poll vote add[ed]
    ```

=== "Event Values"
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-bot`](../docs/types.md#bot)
    * [`event-channel`](../docs/types.md#channel) (and subtypes)
    * `event-number` (represents the message's ID)

=== "Retrieve Values"
    * [`message`](#information-retrieve-values) (to get the poll's message)
    * [`member`](#information-retrieve-values) (to get the voter as member)
    * [`user`](#information-retrieve-values) (to get the voter as user)

## On Poll Vote Remove

[[[ macros.required_version('4.17.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user remove their vote on a poll.

!!! warning "Requirements"
    * The [`guild message polls` intent](../bot/intents.md#message-polls) (to work in guilds)
    * The [`direct message polls` intent](../bot/intents.md#message-polls) (to work in DMs)
    
    If none of these intents are enabled, the event will not be fired at all.

=== "Patterns"

    ```applescript
    [message] poll vote remove[d]
    ```

=== "Event Values"
    * [`event-user`](../docs/types.md#user)
    * [`event-guild`](../docs/types.md#guild)
    * [`event-bot`](../docs/types.md#bot)
    * [`event-channel`](../docs/types.md#channel) (and subtypes)
    * `event-number` (represents the message's ID)

=== "Retrieve Values"
    * [`message`](#information-retrieve-values) (to get the poll's message)
    * [`member`](#information-retrieve-values) (to get the voter as member)
    * [`user`](#information-retrieve-values) (to get the voter as user)

## On Invite Create Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a invite is created in a guild can be used to get the invite property, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild invite create [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild invite create:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-invite
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Invite Delete Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a invite is deleted from a guild can be used to get the invite property, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild invite delete [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild invite delete:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-channel
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Join Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the bot joins in a guild.
=== "Patterns"

    ```applescript
    [discord] bot join guild [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on bot join guild:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    ```


## On Guild Log Entry Create Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a new log entry is created in a guild.

!!! warning "`logged author` will always return `none` for the logged entry of this event (as we only have its ID)"
    You can use the [**retrieve value `author`**](#information-retrieve-values) to get the actual author of the entry. (only for DiSky v4.17.0+)

=== "Patterns"

    ```applescript
    [discord] guild log [entry] create [seen by %-string%]
    ```

=== "Examples"

    ```applescript
    on guild log entry create:
    ```

=== "Event Values"

    * [`event-guild`](../docs/types.md#guild)
    * [`event-bot`](../docs/types.md#bot)
    * `event-logentry` (**Note**: `logged author` of the entry will always return `none`)
    * `event-number` (represent the author ID of the logged entry)

=== "Retrieve Values"

    * [`author`](#information-retrieve-values) (to get the actual author of the entry)

## On Guild Name Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the name of a guild is changed can be used to get the old/new name.
=== "Patterns"

    ```applescript
    [discord] guild name (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild name change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Owner Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a owner of a guild changes can be used to get the old/new owner, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild owner (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild owner change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Splash Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a banner of a guild changes can be used to get the old/new banner, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild splash (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild splash change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Unban Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user is unbanned can be used to get the unbanned user, the author and the guild.
=== "Patterns"

    ```applescript
    [discord] guild [user] unban [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild unban:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Button Click

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any button sent by the button is clicked.
Use 'event-button' to get the button id. Don't forget to either reply or defer the interaction.
Modal can be shown in this interaction.
=== "Patterns"

    ```applescript
    button click[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-button
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```


## On Entity Dropdown Click

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user select one or more choice in an entity dropdown.
Use 'event-dropdown' to get the dropdown id. Don't forget to either reply or defer the interaction.
Use 'selected entities' to get the selected entities.
Modal can be shown in this interaction.
=== "Patterns"

    ```applescript
    entit(y|ies) drop[( |-)]down click[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-dropdown
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```


## On Message Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when someone click on a message application command.
Use 'event-string' to get the command name. Don't forget to either reply to the interaction. Defer doesn't work here.
Modal can be shown in this interaction.
=== "Patterns"

    ```applescript
    message command [receive[d]] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```


## On Modal Receive

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a modal has been sent to the bot from any user.
Use 'event-string' to get the modal id. Don't forget to either reply or defer the interaction.
Modal can NOT be shown in this interaction.
=== "Patterns"

    ```applescript
    modal (click[ed]|receive[d]) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-string
    event-threadchannel
    ```


## On Slash Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user execute a specific slash command.
Use 'event-string' to get the command name. Don't forget to either reply or defer the interaction, You can only defer using the wait pattern  e.g: 'defer the interaction and wait [silently].
Modal can be shown in this interaction.
You can get value of arguments using 'argument "name" as string' for example.
=== "Patterns"

    ```applescript
    slash command [receive[d]] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-string
    event-threadchannel
    ```


## On Slash Completion

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when Discord ask an argument completion.
Use 'event-string' to get the command name. Use normal return effect to return the actual completions.
Modal can NOT be shown in this interaction.
=== "Patterns"

    ```applescript
    slash completion [receive[d]] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-string
    event-threadchannel
    ```


## On String Dropdown Click

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user select one or more choice in a string dropdown.
Use 'event-dropdown' to get the dropdown id. Don't forget to either reply or defer the interaction.
Use 'selected values' to get the selected string values.
Modal can be shown in this interaction.
=== "Patterns"

    ```applescript
    drop[( |-)]down click[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-dropdown
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```


## On User Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when someone click on an user application command.
Use 'event-string' to get the command name. Don't forget to either reply to the interaction. Defer doesn't work here.
Modal can be shown in this interaction.
=== "Patterns"

    ```applescript
    user command [receive[d]] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-string
    event-threadchannel
    ```


## On Member Accept Screen Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member has agreed to membership screen requirements it can be useful for adding roles since the member is not available if they haven't accepted it yet.
=== "Patterns"

    ```applescript
    [discord] [guild] member screen accept [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on member screen accept:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-boolean
    ```


## On Member Avatar Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member changes their avatar.
=== "Patterns"

    ```applescript
    [discord] [guild] member avatar (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on member avatar change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-string
    ```


## On Member Boost Time Change Event

[[[ macros.required_version('4.16.0') ]]]
[[[ macros.is_cancellable('No') ]]]

??? failure "What happened to the `member boost` event?"
    Discord only sends us the `premium type` of a member, thus either he is **boosting** or **not**. 

    It's impossible to tell how long he has been boosting, nor how many times, so the `member boost` event has been removed.

Fired when a member **starts** or **stops** boosting a guild.

!!! warning ""
    This event requires the [**`guild members` intents**](../bot/intents.md#guild-members-guild-members), and target members to be [**cached**](../getting-started/2-bot-loading.md#bot-structure)

=== "Patterns"

    ```applescript
    [discord] [guild] member boost time (change|update) [seen by %-string%]
    ```

=== "Examples"

    ```applescript
    on member boost time change:
        post "<3 **Thanks to %mention tag of event-member% for started boosting the server!** <3" to text channel with id "XXX"
    ```

=== "Event Values"

    ```applescript
    event-guild
    event-bot
    event-user
    event-member
    
    past event-date
    future event-date
    ```

!!! example ""
    **See also:**

    - [Guild Boost Count Update](#on-guild-boost-count-update)
    - [Guild Boost Tier Update](#on-guild-boost-tier-update)

## On Member Join Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a guild.
=== "Patterns"

    ```applescript
    [discord] member join[ed] [guild] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on member join:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    ```


## On Member Nickname Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member changes their nickname.
=== "Patterns"

    ```applescript
    [discord] [guild] member nickname (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on member nickname change:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-string
    ```


## On Member Leave Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member is removed from a guild either by leaving or being punished. Use the ban/kick event instead to check the exact reason
=== "Patterns"

    ```applescript
    [discord] member (leave|left) [guild] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on member leave:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    ```


## On Role Add Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member adds roles to another member, it's a log action so event-author returns who made the action event-roles returns a list of added roles
=== "Patterns"

    ```applescript
    [discord] [member] role add[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role add:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    ```


## On Role Remove Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member removes roles from another member, it's a log action so event-author returns who made the action event-roles returns a list of removed roles
=== "Patterns"

    ```applescript
    [discord] [member] role remove[d] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role remove:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    ```


## On Member Voice Join Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a voice or a stage channel, also fires when a member moves to another channel
=== "Patterns"

    ```applescript
    [discord] [member] voice [channel] join [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on voice channel join:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-audiochannel
    event-stagechannel
    event-voicechannel
    ```


## On Member Voice Leave Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member leaves a voice or a stage channel
=== "Patterns"

    ```applescript
    [discord] [member] voice [channel] leave [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on voice channel leave:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-audiochannel
    event-stagechannel
    event-voicechannel
    ```


## On Message Delete

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any message is deleted.
Use 'event-string' to get the old message content, only works if this message was cached by DiSky before hand.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    message delete[d] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-newschannel
    event-number
    event-guildchannel
    event-bot
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Message Edit

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any message is edited / updated.
Use 'event-string' to get the old message content, only works if this message was cached by DiSky before hand.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    message edit[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-newschannel
    event-guildchannel
    event-bot
    event-textchannel
    event-privatechannel
    event-message
    event-string
    event-threadchannel
    ```


## On Message Receive

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when any bot receive an actual message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    message receive[d] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on message received:
    	if message is from guild:
    		reply with "I just received '%event-message%' from %mention tag of event-channel%!"
    	else:
    		reply with "I just received '%event-message%' from %mention tag of event-user%!"
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-message
    event-threadchannel
    ```


## On Reaction Add

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a message, that can be seen by the bot, receive a reaction.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    (reaction|emote)[s] add[ed] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-emote
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-threadchannel
    ```
=== "Retrieve Values"

    ```applescript
    message
    ```

## On Reaction Remove All

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user remove every reactions from a message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    (reaction|emote)[s] (remove[d] all|clear|reset) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-newschannel
    event-guildchannel
    event-bot
    event-textchannel
    event-privatechannel
    event-threadchannel
    ```
=== "Retrieve Values"

    ```applescript
    message
    author
    ```

## On Reaction Remove

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when an user remove a reaction from a specific message.
This will be fired, by default, both guild & private messages, use the 'event is from guild' condition to avoid confusion.
=== "Patterns"

    ```applescript
    (reaction|emote)[s] remove[d] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Event Values"

    ```applescript
    event-emote
    event-user
    event-guild
    event-newschannel
    event-guildchannel
    event-member
    event-bot
    event-textchannel
    event-privatechannel
    event-threadchannel
    ```
=== "Retrieve Values"

    ```applescript
    message
    ```

## On Role Color Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the color of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role color (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role color change:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-color
    ```


## On Role Create

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a role is created in a guild
=== "Patterns"

    ```applescript
    [discord] [guild] role create[d] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role create:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    author
    ```

## On Role Delete

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a role is deleted from a guild.
=== "Patterns"

    ```applescript
    [discord] [guild] role delete [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role delete:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Role Hoist Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the hoist state of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role hoist[ed] (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role hoist change:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    event-boolean
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Role Icon Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the icon of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role icon (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role icon change:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Role Name Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the name of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role name (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role name change:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    event-string
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Role Permission Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the permissions of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role permission[s] (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role permissions change:
    ```
=== "Event Values"

    ```applescript
    event-role
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Role Position Change

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when the position of a role changes.
=== "Patterns"

    ```applescript
    [discord] [guild] role position (update|change) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on role position change:
    ```
=== "Event Values"

    ```applescript
    event-integer
    event-role
    event-guild
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Thread Join Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member joins a tread, either by joining itself or by a moderator can be used to get the thread, the guild and the member.
=== "Patterns"

    ```applescript
    [discord] thread join [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on thread join:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-threadchannel
    ```


## On Thread Leave Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a member leaves a thread, either by leaving itself or by a moderator can be used to get the thread, the guild and the member.
=== "Patterns"

    ```applescript
    [discord] thread leave [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on thread leave:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-member
    event-bot
    event-threadchannel
    ```


## On User Activity Order Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user in a guild changes its activity. Ex: by playing something different can be used to get the old/new activities.
=== "Patterns"

    ```applescript
    [discord] user activity [order] (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user activity change:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-member
    event-bot
    ```


## On User Avatar Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes its avatar.
=== "Patterns"

    ```applescript
    [discord] user avatar (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user avatar change:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-bot
    event-string
    ```


## On User Discriminator Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes its discriminator.
=== "Patterns"

    ```applescript
    [discord] user discriminator (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user discriminator change:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-bot
    event-string
    ```


## On User Name Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes its name (not nickname).
=== "Patterns"

    ```applescript
    [discord] user name (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user name change:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-bot
    event-string
    ```


## On User Online Status Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user changes its online status.
=== "Patterns"

    ```applescript
    [discord] user online status (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user online status change:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-member
    event-bot
    event-onlinestatus
    ```


## On User Typing Event

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a user starts typing in a channel.
=== "Patterns"

    ```applescript
    [discord] user typ[e|ing] [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on user typing:
    ```
=== "Event Values"

    ```applescript
    event-user
    event-guild
    event-member
    event-bot
    ```


## On Track Event

[[[ macros.required_version('2.0.0') ]]]
[[[ macros.is_cancellable('No') ]]]

Fired when a track receive a specific event. Use the literal to define the event's type such as:
  - START
  - END
  - STUCK
  - PAUSE
  - RESUME
  - SEEK
=== "Patterns"

    ```applescript
    track [event] %trackeventtype%
    ```
=== "Examples"

    ```applescript
    on track play:
    on track end:
    on track exception:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-audiotrack
    event-bot
    event-trackeventtype
    ```


