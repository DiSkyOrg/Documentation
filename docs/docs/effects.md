---
icon: material/check-all
---

# Effects

[[[% import 'macros.html' as macros %]]]

## Forward Message

[[[ macros.required_version('4.20.0') ]]]

Forward a message to another channel. No additional content can be added to the message.

=== "Examples"

    ```applescript
    forward event-message to channel with id "000"
    forward event-message to channel with id "000" and store it in {_msg}
    ```

=== "Patterns"

    ```applescript
    forward [the] [message] %message% to %channel/textchannel% [and store (it|the message) in %-object%]
    ```

## Publish/Crosspost Message

Publish or crosspost a message to a news channel. This will only work if the message is in a news channel.

=== "Examples"

    ```applescript
    publish event-message
    crosspost event-message
    ```

=== "Patterns"

    ```applescript
    [discord] (publish|crosspost) [message] %message%
    ```

## Execute X Using Bot

[[[ macros.required_version('4.0.0') ]]]

This effect is for utilities purpose.
It will wrap the actual effect from DiSky and execute it using the specified bot.
The syntax MUST come from DiSky, and at least ONE bot MUST be loaded (if the specified one is wrong / not loaded)
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    execute (with|using) [the] %bot% <.+>
    execute <.+> (with|using) [the] %bot%
    ```

## Change

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    (add|give) %objects% to (%~objects%) (with|using) %-bot%
    increase %~objects% by (%objects%) (with|using) %-bot%
    give %~objects% (%objects%) (with|using) %-bot%
    set %~objects% to (%objects%) (with|using) %-bot%
    remove (all|every) %objects% from (%~objects%) (with|using) %-bot%
    (remove|subtract) %objects% from (%~objects%) (with|using) %-bot%
    reduce %~objects% by (%objects%) (with|using) %-bot%
    (delete|clear) (%~objects%) (with|using) %-bot%
    reset (%~objects%) (with|using) %-bot%
    ```

## Manage Command Permissions

[[[ macros.required_version('4.0.0') ]]]

This effect allows you to manage the permissions of slash commands, with the following rules:

- By default, the command is marked as ENABLED, and anyone can see & use it.
- You can DISABLE completely the command (first pattern), only admins will be able to use it.
- Or you can ENABLE the commands for specific PERMISSIONS (second pattern).

=== "Examples"

   ```applescript
   disable command{_cmd1} # disable the command for everyone, except the admins.
   enable command {_cmd2} for manage server # enable the command only for the users who have the 'manage server' permission.
   ```
=== "Patterns"

    ```applescript
    disable [the] [command] %slashcommand%
    enable [the] [command] %slashcommands% (for|to) [the] [permissions] %permissions%
    ```

## Update Slash Commands

[[[ macros.required_version('4.0.0') ]]]

Update a **list** of [slash commands](../interactions/slash-commands.md) in a bot (globally) or in a guild (locally).

=== "Examples"
    See the [slash commands](../interactions/slash-commands.md) page for examples.
=== "Patterns"

    ```applescript
    (update|register) [the] [command[s]] %slashcommands% [(globally|locally)] in [the] [(bot|guild)] %bot/guild%
    ```

## Unregister Command

[[[ macros.required_version('4.0.0') ]]]

Unregister a specific slash command from local or global context of a bot.
You must provide the command's name. Keep in mind this **SHOULD NOT** be used!
The best way remains to update bot's commands without the command you want to delete!
=== "Examples"

    ```applescript
    unregister command "test" locally in guild with id "000"
    ```
=== "Patterns"

    ```applescript
    unregister [the] [command[s]] %strings% [(1�globally|2�locally)] (in|from|of) [the] [(bot|guild)] %bot/guild%
    ```

## Open Modal

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    show {_moda_variable}
    show {_moda_variable} to event-user
    show the {_moda_variable} to event-user
    show the modal {_moda_variable} to the event-user
    ```
=== "Patterns"

    ```applescript
    (show|enable) [the] [modal] %modal% [to [the] [event[( |-)]]user]
    ```

## Archive / Unarchive Thread

[[[ macros.required_version('4.4.0') ]]]

Archive or unarchive a specific thread.
=== "Examples"

    ```applescript
    archive event-threadchannel
    unarchive thread channel with id "000"
    ```
=== "Patterns"

    ```applescript
    archive [the] [thread] %threadchannel%
    unarchive [the] [thread] %threadchannel%
    ```

## Ban User

[[[ macros.required_version('4.0.0') ]]]

Bans a member from a guild.

!!! tip "Starting DiSky v4.20.0, you can just specify a USER ID to ban a user, without having to retrieve the member first!"

=== "Examples"

    ```applescript
    ban discord event-member because of "being lame" and delete 10 days worth of messages
    ban discord member "00000000000" from guild with id "000" due to "being lame"
    ```

=== "Patterns"

    ```applescript
    [discord] ban [the] discord [member] %member% [(due to|because of|with [the] reason) %-string%] [and (delete|remove) %-timespan% [worth ]of messages]
    [discord] ban [the] discord [member] %string% (from|of) [the] [guild] %guild% [(due to|because of|with [the] reason) %-string%] # Starting DiSky v4.20.0
    ```

## Connect / Disconnect Bot

[[[ macros.required_version('4.9.0') ]]]

Connect or disconnect a bot to a specific audio channel (or disconnect it from the current one).
The bot must have the required permissions to connect to the channel.
If using the disconnect pattern, only the guild will be required.
=== "Examples"

    ```applescript
    connect bot "bot_name" to voice channel with id "000"
    disconnect from event-guild
    ```
=== "Patterns"

    ```applescript
    connect %bot% to [the] [(audio|voice)] [channel] %audiochannel%
    disconnect [[the] [bot] %bot%] from [the] [guild] %guild%
    ```

## Create Action Channel/Role

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    # Role
    set {_action} to new role action in event-guild
    set role name of {_action} to "Member"
    create {_action} and store it in {_role}

    # Text Channel
    set {_action} to new text channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "Text"
    create {_action} and store it in {_text}

    # Voice Channel
    set {_action} to new voice channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "Voice"
    set max users of {_action} to 5
    create {_action} and store it in {_voice}
    ```
=== "Patterns"

    ```applescript
    create [the] [(action|manager)] %roleaction/channelaction% and store (it|the (role|channel)) in %object%
    ```

## Create Emote

[[[ macros.required_version('4.0.0') ]]]

Create a new emote in a specific guild.
The name must be between 2 and 32 chars and the guild should not have an emote with the same name.
The URL will represent the image, and can be either a web URL or a local path.
=== "Examples"

    ```applescript
    create new emote named "test" with url "https://static.wikia.nocookie.net/leagueoflegends/images/a/ae/This_Changes_Everything_Emote.png/revision/latest/scale-to-width-down/250?cb=20211019231749" in event-guild and store it in {_emote}
    make emote with name "test2" with path "plugins/path/image.png" in event-guild and store it in {_emote}
    ```
=== "Patterns"

    ```applescript
    (make|create) [the] [new] emote (named|with name) %string% with [the] (url|path) %string% in [the] [guild] %guild% and store (it|the emote) in %object%
    ```

## Create Invite

[[[ macros.required_version('4.0.0') ]]]

Create an invitation for a specific channel, and store it in a variable.

!!! warning 
    Creating an invitation for a **guild** is not supported anymore. DiSky will default the invite to the guild's default channel, if any!

=== "Examples"

    ```applescript
    create new invite in event-channel with max uses 5 with max age 50 and store it in {_invite}
    ```
=== "Patterns"

    ```applescript
    (make|create) [the] [new] invite in [the] [(guild|channel)] %guild/channel% [with max us(e|age)[s] %-number%] [with max (time|age) %-number%] and store (it|the invite) in %object%
    ```

!!! example "See Also the [Invite Type](types.md#invite)"

## Create Post

[[[ macros.required_version('4.4.4') ]]]

Create a new post in a forum channel. The output value will be the newly created thread channel.

=== "Examples"

    ```applescript
    create a new post in forum channel with id "000" named "I need help!" with message "please help me!"
    create a new post in forum channel with id "000" named "I need help!" with message "please help me!" with tags "help" and "support"
    ```
=== "Patterns"

    ```applescript
    create [a] [new] post in [channel] %forumchannel% (with name|named) %string% [with message] %string/messagecreatebuilder/embedbuilder% [with [the] tags %-strings%] [and store (it|the thread) in %-object%]
    ```

## Create Scheduled Event

[[[ macros.required_version('4.0.0') ]]]

Create a new scheduled event in a specific channel or at a specific place.
If you use the second pattern (without channel), you'll have to specify the guild where the event will be created, and a start & end date.
If you use the first pattern (with channel), you'll just have to specific the channel itself and a start date.
Scheduled events currently only support stage & voice channels.
=== "Examples"

    ```applescript
    create scheduled event named "Let's Talk Together" in stage channel with id "000" at (5 hours after now) and store it in {_event}
    create scheduled event named "Concerto" at "6 routes of XXX" starting (1 hour after now) and ending (5 hours after now) in event-guild and store it in {_event}
    ```
=== "Patterns"

    ```applescript
    create [a] [new] scheduled event (with name|named) %string% in %guildchannel% at %date% and store (it|the event) in %objects%
    create [a] [new] scheduled event (with name|named) %string% at %string% starting [at] %date% [and] ending [at] %date% in %guild% and store (it|the event) in %objects%
    ```

## Create Thread

[[[ macros.required_version('4.0.0') ]]]

Create a new thread in a text channel with a base name.
The bot used in that effect will automatically join the thread, so you don't have to make it join yourself.
If you create a private thread, then you cannot specify a message.
Else, the Thread will be created based on the specified message.
Creating private thread need the guild to be level 2 or more, else it'll throw an exception.
=== "Examples"

    ```applescript
    create new thread named "abc" in (channel with id "abc") using the message (message with id "abc") and store it in {_thread}
    create new private thread named "abc" in (channel with id "abc") using the message (message with id "abc") and store it in {_thread}
    ```
=== "Patterns"

    ```applescript
    (make|create) [the] [new] [private] thread (named|with name) %string% in [the] [channel] %channel/textchannel% [(with|using) [the] [message] [as reference] %-message%] [(with|using) [the] [bot] %-bot%] and store (it|the thread) in %object%
    ```

## Defer Interaction

[[[ macros.required_version('4.0.0') ]]]

Only usable in interaction event, currently button click/dropdown update/modal event!
This will force the interaction to be acknowledge, you have 3 seconds to do so, the effect will send a success message to Discord or hold the interaction to send a message later.
Keep in mind that replying in an interaction event will automatically defer the interaction, and therefore you don't need to defer it.
If you need to wait more than 3 seconds use the and wait pattern
An interaction can only be deferred once!
=== "Examples"

    ```applescript
    defer the interaction
    defer the interaction and wait
    defer the interaction and wait silently
    ```
=== "Patterns"

    ```applescript
    (acknowledge|defer) [the] interaction [and wait [(1�silently)]]
    ```

## Destroy Discord Entity

[[[ macros.required_version('4.0.0') ]]]

Destroy on Discord the wanted entity.

=== "Examples"

    ```applescript
    destroy event-channel
    destroy event-message
    ```
=== "Patterns"

    ```applescript
    destroy %guild/message/role/channel/emote/webhook%
    ```

## Edit Message

[[[ macros.required_version('4.4.0') ]]]

Edit a message with new content:

!!! info "In Interactions (SlashCommands/Buttons/SelectMenus)"
    The effect will, by default, edit the **interaction** itself, and thus **acknowledge** it. 
    If you want to acknowledge an interaction in another way, while also editing the message, you'll have to edit the message **directly**, by specifying `direct` in the pattern:

    ```applescript
    on button click:
        if event-string is "my-button":
            reply with hidden "That message will acknowledge the interaction!"
            edit direct event-message with "I by-passed the interaction!"
    ```

!!! info "Anywhere Else"
    This will simply edit the message with the new desired content. By default, it overrides all the message content (text content, components, embeds, etc...).

=== "Examples"

    ```applescript
    # We are in a slash command event!
    reply with hidden "Wanna see a magic trick? ..." and store it in {_msg}
    wait a second
    # The variable does not contains a 'real' message, it contains the interaction hook.edit {_msg} to show "Abracadabra!"
    ```

=== "Patterns"

    ```applescript
    edit [:direct] [the] [message] %message% (with|to show) %string/messagecreatebuilder/embedbuilder%
    ```

=== "See Also"
    * [Edit Event-Component](#edit-event-component)
    * [Edit Message's Component](#edit-messages-component)

## Kick Member

[[[ macros.required_version('4.0.0') ]]]

Kick a specific member out of its guild. You can also specify a reason if needed.
=== "Examples"

    ```applescript
    kick discord event-member due to "ur bad guys!"
    ```
=== "Patterns"

    ```applescript
    kick [the] discord [member] %member% [(due to|because of|with [the] reason) %-string%]
    ```

## Load Members

[[[ macros.required_version('4.0.0') ]]]

Load every members of a guild.
This effect will also cache members that were not, so execution may be delayed.
consider calling this effect once, then use the default member expression to get the members.
=== "Examples"

    ```applescript
    load members of event-guild and store them in {_members::*}
    ```
=== "Patterns"

    ```applescript
    load [all] members (of|from) [the] %guild% and store (them|the members) in %-objects%
    ```

## Lock / Unlock Thread

[[[ macros.required_version('4.4.0') ]]]

Lock or unlock a specific thread.
=== "Examples"

    ```applescript
    lock event-threadchannel
    unlock thread channel with id "000"
    ```
=== "Patterns"

    ```applescript
    lock [the] [thread] %threadchannel%
    unlock [the] [thread] %threadchannel%
    ```

## Move/Disconnect Member

[[[ macros.required_version('4.14.2') ]]]

Move a member to another voice chat. You can only move a member if they were previously in a voice channel.

Use the second pattern to **disconnect/kick** the member from its current voice channel. Requires DiSky v4.14.2 or higher.

=== "Examples"

    ```applescript
    move discord event-member to {_voice}
    disconnect discord event-member
    ```

=== "Patterns"

    ```applescript
    [voice] move [the] discord [member] %member% to [a] [voice[( |-)channel]] %voicechannel%
    [voice] disconnect [the] discord [member] %member%
    ```

## Move Role Above/Under Role

[[[ macros.required_version('4.0.0') ]]]

Move a specific role above or under another role within the same guild.
The indexes will be updated automatically.
=== "Examples"

    ```applescript
    move role {_role} above role with id "000"
    ```
=== "Patterns"

    ```applescript
    move [the] [discord] role %role% above [the] [discord] %role%
    move [the] [discord] role %role% under [the] [discord] %role%
    ```

## Mute Member

[[[ macros.required_version('4.0.0') ]]]

Mute or unmute a member in their guild.
=== "Examples"

    ```applescript
    voice mute event-member
    unmute member event-member
    ```
=== "Patterns"

    ```applescript
    [voice] mute [the] [discord] [member] %member%
    [voice] un[ |-]mute [the] [discord] [member] %member%
    ```

## Open Private Channel

[[[ macros.required_version('4.0.0') ]]]

Opens a private channel with a specific user.
The opened channel can be null and an exception can be thrown if the user does not accept message.
=== "Examples"

    ```applescript
    open private channel of event-user and store it in {_channel}
    if {_channel} is not set:
    	reply with "Please enable your private messages!"
    else:
    	post "Hello world!" to {_channel}
    ```
=== "Patterns"

    ```applescript
    open [the] private (channel|message[s]) of [the] [member] %user% and store (it|the [private] channel) in %objects%
    ```

## Pin / Unpin Message

[[[ macros.required_version('4.14.3') ]]]

Pin or unpin a message in a text channel or private channel. You can also use [`is pinned`](conditions.md#is-pinned) to check if a message is pinned.

=== "Examples"

    ```applescript
    pin event-message
    unpin event-message
    ```

=== "Patterns"

    ```applescript
    pin [the] [message] %message%
    unpin [the] [message] %message%
    ```

## Post Message

[[[ macros.required_version('4.4.0') ]]]

Posts a message to a message-channel. You can send messages in a text, private, news, post or thread channel.

* Starting DiSky v4.14.3, you can also **reference** a message (the bot will then reply to that message).
* Starting DiSky v4.20.0, you can also **specify** a bot to use to post the message.

=== "Examples"

    ```applescript
    post "Hello world!" to text channel with id "000"
    post last embed to thread channel with id "000" and store it in {_message}
    ```
=== "Patterns"

    ```applescript
    (post|dispatch) %string/messagecreatebuilder/sticker/embedbuilder/messagepollbuilder% (in|to) [the] %channel% [(using|with) [the] [bot] %-bot%] [with [the] reference[d] [message] %-message%] [and store (it|the message) in %-~objects%]
    ```

## Purge Messages

[[[ macros.required_version('4.0.0') ]]]

Discord provide a better way to delete multiple messages at once.
This effect only works with messages, and a list is recommended here.
If you want to delete a single message, use the destroy effect.
=== "Examples"

    ```applescript
    retrieve last 50 messages from event-channel and store them in {_msg::*}
    purge {_msg::*}
    ```
=== "Patterns"

    ```applescript
    purge [the] [message[s]] %messages%
    ```

## Reply With

[[[ macros.required_version('4.4.0') ]]]

Reply with a specific message to the channel where a message-event was triggered.
It can also be used to acknowledge & reply to an interaction, such as button click or slash command.
In interaction only, you can use the keyword 'hidden' to reply with an ephemeral message (only the executor can see it).
Therefore, the value stored in the variable, if specified, will be an interaction hook, and not a compete message.
You can also provide a message as reference. The replied message be linked with the provided one.

Starting DiSky v4.14.3, you can use `reply with premium message` to reply with a Discord-made message, meant to warn users about a feature they have to pay for. The bot/server **MUST** have monetization enabled for this to work!

=== "Examples"

    ```applescript
    reply with "Hello world!"
    reply with last embed with reference event-message
    reply with hidden "Hello ..." and store it in {_msg}
    wait a second
    edit {_msg} to show "... world!"
    ```
=== "Patterns"

    ```applescript
    reply with [hidden] %string/messagecreatebuilder/sticker/embedbuilder% [with [the] reference[d] [message] %-message%] [and store (it|the message) in %-objects%]
    reply with premium [required] message
    ```

## Retrieve Webhooks

[[[ macros.required_version('4.20.0') ]]] 

Retrieve all webhooks from a specific channel or guild.

=== "Examples"

    ```applescript
    retrieve webhooks from event-channel and store them in {_webhooks::*}
    ```

=== "Patterns"

    ```applescript
    retrieve [the] webhook[s] (from|of) [the] [channel] %channel/textchannel/guild% and store (them|the webhook[s]) in %objects%
    ```

## Retrieve Start Message

[[[ macros.required_version('4.17.2') ]]]

Retrieve the start message of a **thread** channel (this will only work in thread channels). Keep in mind the start message may not always be available, and the effect will return `none` if it's not.

If you want to get the **first** message (first != start), you can simply use the [`retrieve last X messages`](#retrieve-messages) effect, and get the first message from the list.

=== "Examples"

    ```applescript
    retrieve start message from event-threadchannel and store it in {_start}
    ```

=== "Patterns"

    ```applescript
    retrieve start message (from|with|of|in) %threadchannel% and store (it|the message) in %~objects%
    ```

??? failure "Possible Errors"
    - `MISSING_ACCESS`: The bot does not have access to the thread channel.
    - `MISSING_PERMISSION`: The bot does not have the `message history` permission in the thread channel.

## Retrieve Bans

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    retrieve all bans of event-guild and store them in {_bans::*}
	send "%{_bans::*}%" to console
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] bans (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the bans) in %-objects%
    ```

## Retrieve Guild Emotes

[[[ macros.required_version('4.0.0') ]]]

Retrieve (and cache) all emotes from a specific guild.

=== "Examples"

    ```applescript
    retrieve all emotes from event-guild and store them in {_emotes::*}
    ```

=== "Patterns"

    ```applescript
    retrieve [(all|every)] emotes (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the emotes) in %-objects%
    ```

## Retrieve Interested Members

[[[ macros.required_version('4.0.0') ]]]

Retrieve (and cache) the interested members from a scheduled event.

=== "Examples"

    ```applescript
    retrieve all interested members from {_event} and store them in {_members::*}
    ```

=== "Patterns"

    ```applescript
    retrieve [(all|every)] interested members (from|with|of|in) %scheduledevent% [(with|using) [the] [bot] %-bot%] and store (them|the interested members) in %-objects%
    ```

## Retrieve Invite

[[[ macros.required_version('4.0.0') ]]]

Retrieve an invitation from a guild using its invite code/ID.

=== "Examples"

    ```applescript
    retrieve invite with id "000" from event-guild and store it in {_invite}
    ```

=== "Patterns"

    ```applescript
    retrieve invite (with|from) id %string% (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the invite) in %~objects%
    ```

## Retrieve Invites

[[[ macros.required_version('4.0.0') ]]]


Retrieve all invites from a specific guild.

=== "Examples"

    ```applescript
    retrieve invites of event-guild and store them in {_invites::*}
    ```

=== "Patterns"

    ```applescript
    retrieve [all [of]] [the] invite[s] (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|them|the invites) in %~objects%
    ```

## Retrieve Logs

[[[ macros.required_version('4.11.0') ]]]

Retrieve the audit logs of a guild.
=== "Examples"
    See [Logs Manipulation page](../guild/logs-manipulation.md)

=== "Patterns"

    ```applescript
    retrieve [(all|every)] [audit] log[s] [entries] (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the [audit] log[s] [entries]) in %-objects%
    ```

## Retrieve Member

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    retrieve member with id "329999814546817024" in event-guild and store it in {_m}
    ```
=== "Patterns"

    ```applescript
    retrieve member (with|from) id %string% (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the member) in %-object%
    ```

## Retrieve Message

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    retrieve message with id discord id of event-message in event-channel and store it in {_message} 
    ```
=== "Patterns"

    ```applescript
    retrieve message (with|from) id %string% (from|with|of|in) %channel% [(with|using) [the] [bot] %-bot%] and store (it|the message) in %-object%
    ```

## Retrieve Messages

[[[ macros.required_version('4.0.0') ]]]

Retrieve last X messages from a specific message channel.
You can retrieve up to 100 last messages, others will be ignored.
Don't forget to use 'purge' effect to delete a lot of messages the most enhanced way ever.
=== "Examples"

    ```applescript
    retrieve last 30 messages from event-channel and store them in {_msg::*}
    ```
=== "Patterns"

    ```applescript
    retrieve [last] %number% [amount of] message[s] (of|in|from) %channel% and store (them|the messages) in %-objects%
    ```

## Retrieve Owner 

[[[ macros.required_version('4.0.0') ]]]

Retrieve the owner of a specific guild.

=== "Examples"

    ```applescript
    retrieve owner of event-guild and store it in {_member}
    ```

=== "Patterns"

    ```applescript
    retrieve [the] owner (of|from) %guild% and store (it|the member) in %~object%
    ```

## Retrieve Profile

[[[ macros.required_version('4.0.0') ]]]

Retrieve the profile of the specified user.
Profile represent mainly the banner of the user, could return the accent color if non set.
=== "Examples"

    ```applescript
    retrieve profile with id "329999814546817024" from event-user and store it in {_m}
    ```
=== "Patterns"

    ```applescript
    retrieve profile (with|from) id %string% (from|with|of|in) %user% [(with|using) [the] [bot] %-bot%] and store (it|the profile) in %-object%
    ```

## Retrieve Sticker

[[[ macros.required_version('4.0.0') ]]]

Retrieve a sticker from a guild using its per-guild name.
This will return a sticker from the guild, not a global one.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve sticker (with|from) id %string% (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the sticker) in %-object%
    ```

## Retrieve Stickers

[[[ macros.required_version('4.0.0') ]]]

Retrieve every stickers (and cache them) from a specific guild.
=== "Examples"

    ```applescript
    retrieve all stickers from event-guild and store them in {_m::*}
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] stickers (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the stickers) in %-objects%
    ```

## Retrieve Thread Members

[[[ macros.required_version('4.0.0') ]]]

Retrieve every members (and cache them) from a specific thread.
=== "Examples"

    ```applescript
    retrieve all thread members from event-threadchannel and store them in {_m::*}
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] thread members (from|with|of|in) %threadchannel% [(with|using) [the] [bot] %-bot%] and store (them|the thread members) in %-objects%
    ```

## Retrieve Threads

[[[ macros.required_version('4.0.0') ]]]

Retrieve every threads (and cache them) from a specific guild.
This effect will only get back the ACTIVE thread, and will pass on the archived ones.
=== "Examples"

    ```applescript
    retrieve all threads from event-guild and store them in {_threads::*}
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] thread[s] (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the thread[s]) in %-objects%
    ```

## Retrieve User

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    retrieve user with id "6516165135165135213" from event-bot and store it in {_user}
    retrieve user with id "6516165135165135213" from event-bot and store the user in {_user}
    retrieve user with id "6516165135165135213" with event-bot and store it in {_user}
    ```
=== "Patterns"

    ```applescript
    retrieve user (with|from) id %string% (from|with|of|in) %bot% and store (it|the user) in %-object%
    ```

## Retrieve Event Value

[[[ macros.required_version('4.0.0') ]]]

Retrieve an event-value instead of getting it. Only available in some events, that actually contains retrieve values. For more information, please [check this section](events.md#information-retrieve-values)!

=== "Examples"

    [Check the wiki](events.md#information-retrieve-values)
=== "Patterns"

    ```applescript
    retrieve [the] [event[(-| )]]value %string% and store (it|the value) in %objects%
    ```

## Send typing

[[[ macros.required_version('4.0.0') ]]]

Sends the typing status to discord. This is what is used to make the message "X is typing..." appear.
Typing status lasts for 10 seconds.
=== "Examples"

    ```applescript
    show typing status in event-channel
    ```
=== "Patterns"

    ```applescript
    [discord] (send|show) typing [status] (in|to) [[text[ |-]]channel] %channel%
    ```

## Shutdown Bot

[[[ macros.required_version('4.0.0') ]]]

Stop and disconnect a loaded bot from DiSky & discord.
If any requests was still remaining, they will be executed before the actual bot shutdown
Using the force pattern will cancel all requests and shutdown the bot instantly.
=== "Examples"

    ```applescript
    shutdown bot named "name"
    stop bot "name"
    ```
=== "Patterns"

    ```applescript
    [force] (stop|shutdown) [the] [bot] %bot%
    ```

## Suppress Reaction

[[[ macros.required_version('4.1.1') ]]]

Suppress one or more reactions of a message.
You can also specific the user who added the emote to remove it one time.
Without any specified user, it will be the bot's self user that removes the emote.
=== "Examples"

    ```applescript
    suppress reaction "x" of event-user from event-message
    suppress reaction "joy" from event-message # Remove the reaction ADDED BY THE BOT
    ```
=== "Patterns"

    ```applescript
    suppress [the] %emotes% [(of|from) [the] %-user%] (of|from) [the] %message%
    ```

## TimeOut Member

[[[ macros.required_version('4.0.0') ]]]

Timeout a member (temporal exclusion) for a specific duration and with an optional reason.
You can either timeout UNTIL a specific date (Skript date), or FOR a specific timespan (Skript timespan).
This also can be used to remove the current time out, if the bot has the permission to do so.
=== "Examples"

    ```applescript
    timeout event-member for 5 minutes due to "ur so bad"
    time out event-member until {_date}
    stop time out of event-member
    ```
=== "Patterns"

    ```applescript
    time[( |-)]out %member% for %timespan% [(for [the reason]|due to) %-string%]
    time[( |-)]out %member% until %date% [(for [the reason]|due to) %-string%]
    (stop|remove) time[( |-)]out (from|of) %member%
    ```

## Unban User

[[[ macros.required_version('4.0.0') ]]]

Unbans a user from a guild.
=== "Examples"

    ```applescript
    unban event-user in guild with id "818182471140114432"
    ```
=== "Patterns"

    ```applescript
    [discord] un[-| ]ban [the] [discord] [user] %user% (from|in) [guild] %guild%
    ```

## Download Attachment

[[[ macros.required_version('4.0.0') ]]]

Download the specific attachment to a file path.
=== "Examples"

    ```applescript
    download {_attachment} in folder "plugins/data/attachments/"
    ```
=== "Patterns"

    ```applescript
    (download|dl) [the] [attachment] %attachment% (in|to) [the] [(folder|path)] %string%
    ```

## Edit Event-Component

[[[ macros.required_version('4.14.2') ]]]

Edit the event component directly, without editing the whole message again. This effect only works in button, string dropdown and entities dropdown events.

!!! danger "This will <u>Acknowledge</u> the interaction!"

For concrete usage and example, check examples [here for buttons](../interactions/components.md#handling-button-interactions) and [here for dropdowns](../interactions/components.md#handling-dropdown-interactions).

=== "Patterns"

    ```applescript
    edit [component] (button|dropdown|select[( |-)]menu) [of [the] (interaction|event)] to [show] %button/dropdown%
    ```

=== "See Also"
    * [Edit Message](#edit-message)
    * [Edit Message's Component](#edit-messages-component)

## Edit Message's Component

[[[ macros.required_version('4.16.0') ]]]

Modify a single component via its ID in a specific message. This effect can only handle [buttons](../interactions/components.md#buttons) and [select menus](../interactions/components.md#select-menu).

!!! danger "This will <u>NOT Acknowledge</u> the interaction!"

=== "Examples"

    ```applescript
    edit button with id "first" of event-message to show new secondary button with id "third" named "ayo ?!" with reaction "sob"
    ```

=== "Patterns"

    ```applescript
    edit [message] (component|button|dropdown|select[( |-)]menu) with [the] id %string% (of|from|in) [the] [message] %message% (to [show]|with) %button/dropdown%
    ```

=== "See Also"
    * [Edit Event-Component](#edit-event-component)

## Add Embed field/inline field

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    add field named "field_name" with value "field_description" to embed
    add field named "field_name" with value "field_description" to fields of embed
    
    add inline field named "field_name" with value "field_description" to embed
    add inline field named "field_name" with value "field_description" to fields of embed
    ```
=== "Patterns"

    ```applescript
    add field (named|with name) %string% [and] with [the] value %string% to [fields of] %embedbuilder%
    add inline field (named|with name) %string% [and] with [the] value %string% to [fields of] %embedbuilder%
    ```

## Add Welcome Screen Channel

[[[ macros.required_version('4.10.0') ]]]

Add a channel to the welcome screen of a guild.
Can only be used in a 'modify welcome screen' section.
=== "Examples"

    ```applescript
    discord command setup <guild>:
        trigger:
            modify welcome screen of arg-1:
                change the screen description to "Welcome to the server! Please read the rules and get roles before chatting."
                add channel with id "937001799896956991" named "Read our rules" with reaction "?" to the screen
                add channel with id "952199041335316520" named "Get roles" with reaction "??" to the screen
    ```
=== "Patterns"

    ```applescript
    add [the] [channel] %channel% (named|with name) %string% [with [emoji] %-emote%] [to [the] [welcome] screen]
    ```

## Welcome Screen Description

[[[ macros.required_version('4.10.0') ]]]

Change the description of the welcome screen.
Can only be used in a 'modify welcome screen' section.
=== "Examples"

    ```applescript
    discord command setup <guild>:
        trigger:
            modify welcome screen of arg-1:
                change the screen description to "Welcome to the server! Please read the rules and get roles before chatting."
                add channel with id "937001799896956991" named "Read our rules" with reaction "?" to the screen
                add channel with id "952199041335316520" named "Get roles" with reaction "??" to the screen
    ```
=== "Patterns"

    ```applescript
    change [the] [welcome] screen description to %string%
    change [the] description of [the] [welcome] screen to %string%
    ```

## Register Webhook Client

[[[ macros.required_version('4.15.0') ]]]

Register a new webhook client with the specified name and URL. The name is only used for internal purposes and can be anything you want; it'll be used in other syntax to reference the registered webhook client.
The URL should be a valid Discord webhook URL (containing both the ID and the token). More information & examples can be found on the [webhooks page](../messages/webhooks.md).

=== "Examples"

    See the [webhooks page](../messages/webhooks.md) for examples.

=== "Patterns"

    ```applescript
    register [a] [new] webhook[s] [client] (in|using) [the] [bot] %bot% (with [the] name|named) %string% (and|with) [the] [webhook] url %string%
    ```

## Unregister Webhook Client

[[[ macros.required_version('4.15.0') ]]]

Unregister a webhook client with the specified name. This will remove the webhook client from the bot's memory, and it will no longer be usable in any further syntax.

=== "Examples"

    ```applescript
    unregister client named "my-webhook"
    ```

=== "Patterns"

    ```applescript
    unregister [the] [webhook] client (with [the] name|named) %string%
    ```

## Retrieve Webhooks

[[[ macros.required_version('4.15.0') ]]]

Retrieve all webhooks in a specific channel or guild. The output will be a list of webhook **clients**, which can be used in other webhook-related syntax.

=== "Examples"

    See the [webhooks page](../messages/webhooks.md) for examples.

=== "Patterns"

    ```applescript
    retrieve [all] [discord] webhooks (of|from) [the] [(guild|channel)] %guild/textchannel% and store (them|the webhooks) in %~objects%
    ```

## Make Webhook Post Message

[[[ macros.required_version('4.15.0') ]]]

Make the specified webhook client post a message to its channel. More information & examples can be found on the [webhooks page](../messages/webhooks.md).

=== "Examples"

    See the [webhooks page](../messages/webhooks.md) for examples.

=== "Patterns"

    ```applescript
    make [the] [webhook] client %string% (post|send) [the] [message] %string/messagecreatebuilder/embedbuilder/messagepollbuilder% [with [the] username %-string%] [[and] [with] [the] avatar [url] %-string%] [and store (it|the message) in %-~objects%]
    ```

## Post Voice Message 

[[[ macros.required_version('4.22.0') ]]]

Post a voice message to a message channel. The voice message must follow Discord's specific requirements:

- WAV file format only
- Duration between 1-60 seconds 
- 48000Hz sample rate
- Mono channel only
- Maximum file size of 25MB

=== "Examples"

    ```applescript
    discord command voicemsg:
        prefixes: !
        trigger:
            post voice message "plugins/MyBot/voice.wav" to event-channel and store it in {_msg}
            reply with "Voice message sent! %{_msg}%"
    ```

=== "Patterns"

    ```applescript
    (post|dispatch) voice message %string% (in|to) [the] %channel% [(using|with) [the] [bot] %-bot%] [and store (it|the message) in %-objects%]
    ```

??? failure "Possible Errors"
    - `FILE_NOT_FOUND`: The provided file path doesn't exist
    - `INVALID_FORMAT`: The file is not a WAV file
    - `FILE_TOO_LARGE`: The file exceeds Discord's 25MB limit
    - `INVALID_SAMPLE_RATE`: The audio sample rate is not 48000Hz
    - `INVALID_CHANNELS`: The audio is not mono (1 channel)
    - `INVALID_DURATION`: The audio duration is not between 1-60 seconds
    - `UNSUPPORTED_CHANNEL`: The channel doesn't support voice messages