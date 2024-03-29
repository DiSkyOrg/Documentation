# 📘 Effects

## Execute X Using Bot

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

## EffUpdateCommand

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    (update|register) [the] [command[s]] %slashcommands% [(1�globally|2�locally)] in [the] [(bot|guild)] %bot/guild%
    ```

## Unregister Command

|Since|v4.0.0|class:version|

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

## OpenModal

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    (show|enable) [the] [modal] %modal% [to [the] [event[( |-)]]user]
    ```

## Archive / Unarchive Thread

|Since|v4.4.0|class:version|

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

## Ban Member

|Since|v4.0.0|class:version|

Bans a member from a guild.
=== "Examples"

    ```applescript
    ban discord event-member because of "being lame" and delete 10 days worth of messages
    ```
=== "Patterns"

    ```applescript
    [discord] ban [the] discord [member] %member% [(due to|because of|with [the] reason) %-string%] [and (delete|remove) %-timespan% [worth ]of messages]
    ```

## Connect / Disconnect Bot

|Since|v4.9.0|class:version|

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

## CreateAction

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    create [the] [(action|manager)] %roleaction/channelaction% and store (it|the (role|channel)) in %object%
    ```

## Create Emote

|Since|v4.0.0|class:version|

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

## CreateInvite

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    (make|create) [the] [new] invite in [the] [(guild|channel)] %guild/channel% [with max us(e|age)[s] %-number%] [with max (time|age) %-number%] and store (it|the invite) in %object%
    ```

## Create Post

|Since|v4.4.4|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

Create a new thread in a text channel with a base name.
The bot used in that effect will automatically join the thread, so you don't have to make it join yourself.
If you create a private thread, then you cannot specify a message.
Else, the Thread will be created based on the specified message.
Creating private thread need the guild to be level 2 or more, else it'll throw an exception.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    (make|create) [the] [new] [private] thread (named|with name) %string% in [the] [channel] %channel/textchannel% [(with|using) [the] [message] [as reference] %-message%] [(with|using) [the] [bot] %-bot%] and store (it|the thread) in %object%
    ```

## Defer Interaction

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

Destroy on Discord the wanted entity.
=== "Examples"

    ```applescript
    destroy event-channel
    destroy event-message
    ```
=== "Patterns"

    ```applescript
    destroy %guild/message/role/channel/emote%
    ```

## Edit Message

|Since|v4.4.0|class:version|

Edit a specific message/interaction hook to show a new rich or simple message.
The interaction hook will only be editable for the next 15 minutes once it's sent!
=== "Examples"

    ```applescript
    # We are in a slash command event!
    reply with hidden "Wanna see a magic trick? ..." and store it in {_msg}
    wait a second
    # The variable does not contains a 'real' message, it contains the interaction hook.edit {_msg} to show "Abracadabra!"
    ```
=== "Patterns"

    ```applescript
    edit [the] [message] %message/interactionhook% (with|to show) %string/messagecreatebuilder/embedbuilder%
    ```

## Kick Member

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.4.0|class:version|

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

## Move Member

|Since|v4.0.0|class:version|

Move a member to another voice chat.
You can only move a member if they were previously in a voice channel.
=== "Examples"

    ```applescript
    move event-member to {_voice}
    ```
=== "Patterns"

    ```applescript
    [voice] move [the] discord [member] %member% to [a] [voice[( |-)channel]] %voicechannel%
    ```

## Move Role Above/Under Role

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

## Post Message

|Since|v4.4.0|class:version|

Posts a message to a message-channel.
You can send messages in a text, private, news, post or thread channel.
=== "Examples"

    ```applescript
    post "Hello world!" to text channel with id "000"
    post last embed to thread channel with id "000" and store it in {_message}
    ```
=== "Patterns"

    ```applescript
    (post|dispatch) %string/messagecreatebuilder/sticker/embedbuilder% (in|to) [the] %channel% [and store (it|the message) in %-objects%]
    ```

## Purge Messages

|Since|v4.0.0|class:version|

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

|Since|v4.4.0|class:version|

Reply with a specific message to the channel where a message-event was triggered.
It can also be used to acknowledge & reply to an interaction, such as button click or slash command.
In interaction only, you can use the keyword 'hidden' to reply with an ephemeral message (only the executor can see it).
Therefore, the value stored in the variable, if specified, will be an interaction hook, and not a compete message.
You can also provide a message as reference. The replied message be linked with the provided one.
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
    ```

## RetrieveBans

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] bans (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the bans) in %-objects%
    ```

## RetrieveEmotes

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] emotes (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the emotes) in %-objects%
    ```

## RetrieveEmotes

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] interested members (from|with|of|in) %scheduledevent% [(with|using) [the] [bot] %-bot%] and store (them|the interested members) in %-objects%
    ```

## RetrieveInvite

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve invite (with|from) id %string% (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the invite) in %-object%
    ```

## RetrieveInvites

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] invites (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the invites) in %-objects%
    ```

## Retrieve Logs

|Since|v4.11.0|class:version|

Retrieve the audit logs of a guild.
=== "Examples"

    ```applescript
    retrieve audit logs from event-guild and store it in {_logs::*}
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] [audit] log[s] [entries] (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the [audit] log[s] [entries]) in %-objects%
    ```

## RetrieveMember

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve member (with|from) id %string% (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the member) in %-object%
    ```

## RetrieveMessage

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve message (with|from) id %string% (from|with|of|in) %channel% [(with|using) [the] [bot] %-bot%] and store (it|the message) in %-object%
    ```

## Retrieve Messages

|Since|v4.0.0|class:version|

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

## RetrieveOwner

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve owner (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (it|the owner) in %-object%
    ```

## Retrieve Profile

|Since|v4.0.0|class:version|

Retrieve the profile of the specified user.
Profile represent mainly the banner of the user, could return the accent color if non set.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve profile (with|from) id %string% (from|with|of|in) %user% [(with|using) [the] [bot] %-bot%] and store (it|the profile) in %-object%
    ```

## Retrieve Sticker

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

Retrieve every stickers (and cache them) from a specific guild.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] stickers (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the stickers) in %-objects%
    ```

## Retrieve Thread Members

|Since|v4.0.0|class:version|

Retrieve every members (and cache them) from a specific thread.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] thread members (from|with|of|in) %threadchannel% [(with|using) [the] [bot] %-bot%] and store (them|the thread members) in %-objects%
    ```

## Retrieve Threads

|Since|v4.0.0|class:version|

Retrieve every threads (and cache them) from a specific guild.
This effect will only get back the ACTIVE thread, and will pass on the archived ones.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [(all|every)] thread[s] (from|with|of|in) %guild% [(with|using) [the] [bot] %-bot%] and store (them|the thread[s]) in %-objects%
    ```

## RetrieveUser

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve user (with|from) id %string% (from|with|of|in) %bot% and store (it|the user) in %-object%
    ```

## RetrieveEventValue

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    retrieve [the] [event[(-| )]]value %string% and store (it|the value) in %objects%
    ```

## Send typing

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.1.1|class:version|

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

|Since|v4.0.0|class:version|

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

|Since|v4.0.0|class:version|

Unbans a user from a guild.
=== "Examples"

    ```applescript
    unban event-user in guild with id "818182471140114432"
    ```
=== "Patterns"

    ```applescript
    [discord] un[-| ]ban [the] [discord] [user] %user% (from|in) [guild] %guild%
    ```

## Return

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    return %slashchoices%
    ```

## Download Attachment

|Since|v4.0.0|class:version|

Download the specific attachment to a file path.
=== "Examples"

    ```applescript
    download {_attachment} in folder "plugins/data/attachments/"
    ```
=== "Patterns"

    ```applescript
    (download|dl) [the] [attachment] %attachment% (in|to) [the] [(folder|path)] %string%
    ```

## EffAddField

|Since|v4.0.0|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    add field (named|with name) %string% [and] with [the] value %string% to [fields of] %embedbuilder%
    add inline field (named|with name) %string% [and] with [the] value %string% to [fields of] %embedbuilder%
    ```

## Add Welcome Screen Channel

|Since|v4.10.0|class:version|

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

|Since|v4.10.0|class:version|

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

## Play First Track

|Since|v4.9.0|class:version|

Play the specified track in the specified guild.
You can specify either the track must be forced to play, and interrupt the current one.
=== "Examples"

    ```applescript
    play {_track} in event-guild
    force play {_track} in event-guild
    ```
=== "Patterns"

    ```applescript
    [force] play [the] [track] %audiotrack/audioplaylist% [the] [first] [track] [of the queue] in %guild% [with [the] [bot] %bot%]
    ```

