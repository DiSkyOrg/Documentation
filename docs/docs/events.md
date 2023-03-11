# 🎒 Events

## On Bot Creation Scope

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Discord Command

|Since|v3.0|class:version|
|Cancellable|Yes|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Disky Command

|Since|v4.0.0|class:version|
|Cancellable|Yes|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Bot Join Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Shutdown Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Guild Ready Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Ready Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On DiSky Error / Exception

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Guild AFK Channel Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

## On Invite Create Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Guild Log Entry Create Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

Fired when a new log entry is created in a guild.
=== "Patterns"

    ```applescript
    [discord] guild log [entry] create [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    on guild log entry create:
    ```
=== "Event Values"

    ```applescript
    event-guild
    event-logentry
    event-bot
    ```
=== "Retrieve Values"

    ```applescript
    author
    ```

## On Guild Name Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Entity Dropdown Click

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Message Command

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Modal Receive

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Slash Command

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Slash Completion

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On String Dropdown Click

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Command

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Accept Screen Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Avatar Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Boost Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

Fired when a member starts or stops boosting a guild can be used to get the old/new boosting time and the guild.
=== "Patterns"

    ```applescript
    [discord] [guild] member boost (change|update) [seen by %-string%]
    ```
=== "Examples"

    ```applescript
    member boost change:
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

## On Member Join Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Nickname Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Leave Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Role Add Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Role Remove Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Voice Join Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Member Voice Leave Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Message Delete

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Message Receive

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Reaction Add

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Role Create

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Thread Leave Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Activity Order Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Avatar Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Discriminator Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Name Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Online Status Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On User Typing Event

|Since|v4.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

## On Track Event

|Since|v2.0.0|class:version|
|Cancellable|No|class:version|

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
=== "Retrieve Values"

    ```applescript
    
    ```

