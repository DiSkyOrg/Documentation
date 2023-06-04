# 📗 Expressions

## Discord Command Argument

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Works same as Skript's command argument. You can specify the argument number or the argument type (in case there's only one user or member for example) to get the selected value.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [][the] last arg[ument][s]
    [][the] arg[ument][s](-| )<(\d+)>
    [][the] <(\d*1)st|(\d*2)nd|(\d*3)rd|(\d*[4-90])th> arg[ument][s]
    [][the] arg[ument][s]
    [][the] %*classinfo%( |-)arg[ument][( |-)<\d+>]
    [][the] arg[ument]( |-)%*classinfo%[( |-)<\d+>]
    ```

## Used Alias

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the used alias in a discord command trigger section.
It can only be used here, and will throw an error if not.
=== "Examples"

    ```applescript
    set {_alias} to the used alias
    ```
=== "Patterns"

    ```applescript
    [the] use[d]( |-)alias[es]
    ```

## Used Argument

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the plain formatter of the discord command's argument
You should however use (arg-1) for example which will return the argument value directly.
This is intended to be for test purpose only, and therefore only return a String formatted containing every used arguments.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] use[d]( |-)arg[ument][s]
    ```

## Used Prefix

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the used prefix in a discord command trigger section.
=== "Examples"

    ```applescript
    set {_p} to the used prefix
    ```
=== "Patterns"

    ```applescript
    [the] use[d]( |-)prefix[es]
    ```

## ExprArgumentChoices

|Since|v4.0.0|class:version|
|Return Type|slashchoice|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] [option] choices of %slashoption%
    [all] [the] %slashoption%'[s] [option] choices
    ```

## Sub-command Groups

|Since|v4.0.0|class:version|
|Return Type|slashcommandgroup|class:version|

Represent every sub-slash-command groups a slash command have.
You can add sub-slash-commands to a group, then add this group into the base slash command.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] sub[[( |-)]command[s]] group[s] of %slashcommand%
    [all] [the] %slashcommand%'[s] sub[[( |-)]command[s]] group[s]
    ```

## Group / Command Sub-Commands

|Since|v4.0.0|class:version|
|Return Type|subslashcommand|class:version|

Represent every sub-slash-command a slash-command or a group have.
You can add sub-slash-commands to a group or a core slash-command, then add this group into the base slash command.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] sub[( |-)]command[s] of %slashcommandgroup/slashcommand%
    [all] [the] %slashcommandgroup/slashcommand%'[s] sub[( |-)]command[s]
    ```

## New Button

|Since|v4.0.0|class:version|
|Return Type|button|class:version|

Create a new button with an ID and some optional options. It can be either enabled or disabled, and either link or action. If the button is a link-type, then the ID will be the URL that the user will be redirect to.
=== "Examples"

    ```applescript
    set {_btn} to new enabled danger button with id "button-id" named "Hello world :p"
    ```
=== "Patterns"

    ```applescript
    [a] new [(enabled|disabled)] %buttonstyle% [link] button [with (id|url)] %string% [(named|with label) %-string%][,] [with [emoji] %-emote%]
    ```

## New Components Row

|Since|v4.0.0|class:version|
|Return Type|row|class:version|

Create a new (empty) components row.
You can add either max 5 buttons or one dropdown to it.
A single message can hold 5 components rows.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new component[s] row
    ```

## New Dropdown Option

|Since|v4.0.0|class:version|
|Return Type|selectoption|class:version|

Create a new dropdown option with different properties.
This is a predefined option holding a string value. It can only be used in string dropdowns.
The value represent the returned string that this dropdown will return if this option is selected.
The name / label is the actual shown name on the option.
Description and emote are optional.
=== "Examples"

    ```applescript
    set {_btn} to new enabled danger button with id "button-id" named "Hello world :p"
    ```
=== "Patterns"

    ```applescript
    [a] new [default] [dropdown] option with value %string% (named|with label) %-string% [with description [%-string%]] [with [emoji] %-emote%]
    ```

## Command Localization

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Represents the localization of the name or the description of a slash/sub command.
You can add **Locale Data** (check for expression) to them.
Basically, the command's name & description will be according to the client's language code.
Documentation: https://docs.disky.me/advanced-stuff/slash-commands#using-localizations-v4.3.0+
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] (name|description)['s] (localization[s]|locale[s]) of %slashcommand/subslashcommand%
    [all] [the] %slashcommand/subslashcommand%'[s] (name|description)['s] (localization[s]|locale[s])
    ```

## PropOptions

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] option[s] [mapping[s]] of %slashcommand/subslashcommand/dropdown%
    [all] [the] %slashcommand/subslashcommand/dropdown%'[s] option[s] [mapping[s]]
    ```

## Selected Entities

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

The list of the selected entities, in the current entity dropdown update event.
=== "Examples"

    ```applescript
    selected entities
    ```
=== "Patterns"

    ```applescript
    select[ed] entit(y|ies)
    ```

## Selected Values

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

The list of the selected values' IDs, in the current dropdown update event.
=== "Examples"

    ```applescript
    selected values
    ```
=== "Patterns"

    ```applescript
    select[ed] value[s]
    ```

## Emoji / Emote

|Since|v4.0.0|class:version|
|Return Type|emote|class:version|

Get an emoji or an emote from its name, ID or unicode.
- An emoji is discord-side only, can be used everywhere, and don't have any attached guild.
- An emote is guild-side only, have a custom long ID and are attached to a guild.
It the specified reaction doesn't exist, DiSky will simply return null and say it in console.
We highly recommend the specification of the guild when retrieving an emote, to avoid conflicts with other that potentially have the same name.
=== "Examples"

    ```applescript
    reaction "joy"
    emoji "sparkles"
    emote "disky" in event-guild
    ```
=== "Patterns"

    ```applescript
    (emoji|emote|reaction)[s] %strings% [(from|in) %-guild%]
    ```

## Last DiSky Exception

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the last occurred DiSky or Discord exception in the current event.
This expression is event-based, means you cannot get the last error that happened on another event.
Once this has been called, it will remove the returned value from the errors list to avoid having two times the same error message.
=== "Examples"

    ```applescript
    if last disky exception is set: # an error occurred
    ```
=== "Patterns"

    ```applescript
    [the] last (disky|discord) (error|exception)
    ```

## BotGuilds

|Since|v4.0.0|class:version|
|Return Type|guild|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] guilds of %bot%
    [all] [the] %bot%'[s] guilds
    ```

## ExprPresence

|Since|v4.0.0|class:version|
|Return Type|activity|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    listening [to] %string%
    watching [to] %string%
    playing [to] %string%
    streaming [to] %string% with [the] url %string%
    competing [to] %string%
    ```

## ChannelChannels

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] channel[s] of %category%
    [all] [the] %category%'[s] [discord] channel[s]
    ```

## Voice Channel Members

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

The list of members that are connected to this actual voice channel.
=== "Examples"

    ```applescript
    audio members of event-channel
    voice members of voice channel with id "0000"
    ```
=== "Patterns"

    ```applescript
    [all] [the] (audio|stage|voice) member[s] [list] of %voicechannel%
    [all] [the] %voicechannel%'[s] (audio|stage|voice) member[s] [list]
    ```

## Threads of Channel / Guild

|Since|v4.0.0, 4.4.4 (threads of forum channel)|class:version|
|Return Type|threadchannel|class:version|

Gets the threads of a specific forum/text channel or a guild.
=== "Examples"

    ```applescript
    threads of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] threads of %forumchannel/textchannel/guild%
    [all] [the] %forumchannel/textchannel/guild%'[s] threads
    ```

## NewCategoryAction

|Since|v4.0.0|class:version|
|Return Type|channelaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new category (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## NewNewsChannel

|Since|v4.0.0|class:version|
|Return Type|channelaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new news[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## NewStageChannel

|Since|v4.0.0|class:version|
|Return Type|channelaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new stage[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## NewTextAction

|Since|v4.0.0|class:version|
|Return Type|channelaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new text[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## NewVoiceAction

|Since|v4.0.0|class:version|
|Return Type|channelaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new voice[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## Discord Members of Guild / Channel

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Returns a list of members.
For Message text-related channel & category, it returns members with permission to view the channel
For Audio Channels it returns the currently connected members of the channel.
For threads & posts, it returns the members who are in the thread. You can add or remove a member in this case.
=== "Examples"

    ```applescript
    members of event-channel
    members of voice channel with id "0000"
    add event-member to discord members of thread channel with id "000"
    ```
=== "Patterns"

    ```applescript
    [all] [the] discord member[s] [list] of %guildchannel/guild/threadchannel%
    [all] [the] %guildchannel/guild/threadchannel%'[s] discord member[s] [list]
    ```

## Guild / Member Roles

|Since|v4.0.0|class:version|
|Return Type|role|class:version|

Represent the roles that a guild or a member currently have.
Can be changed, SET and ADD ChangeMode can be used when passing a member.
To modify guild's roles, check delete and create role effects.
=== "Examples"

    ```applescript
    add role with id "000" to roles of event-member
    remove event-role from roles of event-member
    reply with "Amount of roles in the guild: %size of roles of event-guild%"
    ```
=== "Patterns"

    ```applescript
    [all] [the] roles of %guild/member%
    [all] [the] %guild/member%'[s] roles
    ```

## Last Embed

|Since|v1.0|class:version|
|Return Type|embedbuilder|class:version|

This expression returns the last generated embed using the embed builder.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [last] [(made|created|generated)] embed
    ```

## Guild Boosters

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Represent the current members booster of the guild.
=== "Examples"

    ```applescript
    reply with "Boosters: %boosters of event-guild%!"
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] booster[s] [member[s]] of %guild%
    [all] [the] %guild%'[s] [guild] booster[s] [member[s]]
    ```

## All Guild Guild Channels

|Since|v4.0.0|class:version|
|Return Type|guildchannel|class:version|

Get every guild channel in the guild, including text, voice, stage, news, and thread channels.
=== "Examples"

    ```applescript
    guild channels of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] guild[( |-)]channels of %guild%
    [all] [the] %guild%'[s] [guild] [all] guild[( |-)]channels
    ```

## Guild News Channels

|Since|v4.0.0|class:version|
|Return Type|newschannel|class:version|

Gets all news channels of a guild.
=== "Examples"

    ```applescript
    all news channels of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] news[( |-)]channels of %guild%
    [all] [the] %guild%'[s] [guild] [all] news[( |-)]channels
    ```

## All Guild Scheduled Events

|Since|v4.0.0|class:version|
|Return Type|scheduledevent|class:version|

Returns all scheduled events of a guild.
=== "Examples"

    ```applescript
    all scheduled events of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] scheduled events of %guild%
    [all] [the] %guild%'[s] [guild] [all] scheduled events
    ```

## All Guild Stage Channels

|Since|v4.0.0|class:version|
|Return Type|stagechannel|class:version|

Returns all stage channels of a guild.
=== "Examples"

    ```applescript
    all stage channels of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] stage[( |-)]channels of %guild%
    [all] [the] %guild%'[s] [guild] [all] stage[( |-)]channels
    ```

## All Guild Text Channels

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

Returns all text channels of a guild.
=== "Examples"

    ```applescript
    all text channels of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] text[( |-)]channels of %guild%
    [all] [the] %guild%'[s] [guild] [all] text[( |-)]channels
    ```

## Guild Voice Channels

|Since|v4.0.0|class:version|
|Return Type|voicechannel|class:version|

Gets all voice channels of a guild.
=== "Examples"

    ```applescript
    all voice channels of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [guild] [all] voice[( |-)]channels of %guild%
    [all] [the] %guild%'[s] [guild] [all] voice[( |-)]channels
    ```

## Message Attachment

|Since|v4.0.0|class:version|
|Return Type|attachment|class:version|

Get every attachment as custom object of a message
=== "Examples"

    ```applescript
    attachments of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] attachment[s] of %message%
    [all] [the] %message%'[s] [discord] [message] attachment[s]
    ```

## Message Embeds

|Since|v4.0.0|class:version|
|Return Type|embedbuilder|class:version|

Get every embeds of a specific messages. Keep in mind only webhook are allowed to send more than one embed!
=== "Examples"

    ```applescript
    embeds of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] embeds of %message%
    [all] [the] %message%'[s] [discord] [message] embeds
    ```

## Message Text Channels

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

Get every mentioned text channels in a message.
=== "Examples"

    ```applescript
    mentioned text channels of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned text channels of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned text channels
    ```

## Message Emotes

|Since|v4.0.0|class:version|
|Return Type|emote|class:version|

Get every mentioned emotes in a message.
This will only return custom emote, and will therefore not include discord emotes.
=== "Examples"

    ```applescript
    mentioned emotes of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned emote[s] of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned emote[s]
    ```

## Message Mentioned Members

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Get every mentioned members in a message. If the message doesn't come from a guild it will return an empty array!
=== "Examples"

    ```applescript
    mentioned members of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned members of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned members
    ```

## Message Mentioned Roles

|Since|v4.0.0|class:version|
|Return Type|role|class:version|

Get every mentioned Roles in a message. If the message doesn't come from a guild it will return an empty array!
=== "Examples"

    ```applescript
    mentioned roles of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned roles of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned roles
    ```

## Message Mentioned Users

|Since|v4.0.0|class:version|
|Return Type|user|class:version|

Get every mentioned users in a message.
=== "Examples"

    ```applescript
    mentioned users of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned users of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned users
    ```

## Message Voice Channels

|Since|v4.0.0|class:version|
|Return Type|voicechannel|class:version|

Get every mentioned voice channels in a message.
=== "Examples"

    ```applescript
    mentioned voice channels of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] mentioned voice channels of %message%
    [all] [the] %message%'[s] [discord] [message] mentioned voice channels
    ```

## Message Reactions

|Since|v4.0.0|class:version|
|Return Type|emote|class:version|

Get every reactions of a message.
Because of Discord's limitation, we cannot get which user reacted with which reaction, you'll have to count them yourself.
=== "Examples"

    ```applescript
    reactions of event-message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] [message] (emo(te|ji)|reaction)[s] of %message%
    [all] [the] %message%'[s] [discord] [message] (emo(te|ji)|reaction)[s]
    ```

## NewRoleAction

|Since|v4.0.0|class:version|
|Return Type|roleaction|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] new role (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## Get Tag

|Since|v4.4.4|class:version|
|Return Type|forumtag|class:version|

Get a tag from a forum channel using its name.
=== "Examples"

    ```applescript
    tag named "v4" from forum channel with id "000"
    ```
=== "Patterns"

    ```applescript
    [forum] tag ((from|with) name|named) %string% (of|from|in) %forumchannel%
    ```

## New Forum Tag

|Since|v4.4.4|class:version|
|Return Type|object|class:version|

Create a new forum tag with a specific name & optional emoji.
You can also specify if the tag is 'moderate' or not.
=== "Examples"

    ```applescript
    new forum tag named "solved" with reaction "white_check_mark"
    new moderated forum tag named "internal"
    ```
=== "Patterns"

    ```applescript
    new [forum] tag [named] %string% [with %-emote%]
    new moderated [forum] tag [named] %string% [with %-emote%]
    ```

## Post / Forum Tags

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Get all tags of a forum channel or a thread channel.
You can also add or remove tags from a thread channel using this expression.
You must add the tag to the forum itself before adding it to the post.
=== "Examples"

    ```applescript
    set {_tags::*} to tags of event-forumchannel
    add new tag named "resolved" with reaction "x" to tags of forum with id "000"
    ```
=== "Patterns"

    ```applescript
    [all] [the] tags of %threadchannel/forumchannel%
    [all] [the] %threadchannel/forumchannel%'[s] tags
    ```

## User Badges

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent every badges' name a user have.
This does not and cannot contain any intro-related badges (nitro membership or nitro boosting), it need OAuth2 to be enabled.
=== "Examples"

    ```applescript
    reply with "Whoa! You got all of them? %join badges of event-user with nl%"
    ```
=== "Patterns"

    ```applescript
    [all] [the] [user] badge[s] of %user%
    [all] [the] %user%'[s] [user] badge[s]
    ```

## User Mutual Guilds

|Since|v4.0.0|class:version|
|Return Type|guild|class:version|

Represent every guild that the bot and the user have in common.
=== "Examples"

    ```applescript
    reply with "Oh boi, we have %size of mutual guilds event-user% mutual guilds!"
    ```
=== "Patterns"

    ```applescript
    [all] [the] [user] mutual[s] guild[s] of %user%
    [all] [the] %user%'[s] [user] mutual[s] guild[s]
    ```

## Last Row Builder

|Since|v4.0.0|class:version|
|Return Type|row|class:version|

Represents the last row builder created within a section.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [last] row [builder]
    ```

## Row Builder Components

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Components of a row builder
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] component[s] of %row%
    [all] [the] %row%'[s] component[s]
    ```

## Last Message Builder

|Since|v4.0.0|class:version|
|Return Type|messagecreatebuilder|class:version|

Represents the last message builder created within a section.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [last] message [builder]
    ```

## Message Builder Attachments

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Attachments of a message builder
Supports SkImage's images if the addon is installed.
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] (attachment|image)[s] of %messagecreatebuilder%
    [all] [the] %messagecreatebuilder%'[s] (attachment|image)[s]
    ```

## Message Builder Embeds

|Since|v4.0.0|class:version|
|Return Type|embedbuilder|class:version|

Embeds of a message builder
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] embed[s] of %messagecreatebuilder%
    [all] [the] %messagecreatebuilder%'[s] embed[s]
    ```

## Message Builder Component Rows

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Component rows of a message builder
See also: 'Creator Components Row'
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [all] [the] [component[s]] row[s] of %messagecreatebuilder/modal%
    [all] [the] %messagecreatebuilder/modal%'[s] [component[s]] row[s]
    ```

## New Message Command

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Create a new message command, to be updated on discord later.
This will create a context command of MESSAGE type.
Once created, you can execute it by right-clicking on a message, then going in 'Applications' -> <your message command name>
=== "Examples"

    ```applescript
    new message command named "Warn Message"
    ```
=== "Patterns"

    ```applescript
    [a] [new] message[( |-)]command [with] [(the name|named)] %string%
    ```

## New Option Choice

|Since|v4.0.0|class:version|
|Return Type|slashchoice|class:version|

Create a new slash command option choice with an unique name and a string or number value.
Choices are only available for STRING, NUMBER and INTEGER slash command option type.
Of course, the provided value type must be compatible with the option type (you cannot add string choice to a NUMBER option).
=== "Examples"

    ```applescript
    add new choice named "Example choice" with value 100 to choices of {_option} # it's a NUMBER option
    ```
=== "Patterns"

    ```applescript
    [a] new [option] choice [(named|with name)] %string% with [the] value %string/number%
    ```

## ExprNewSlashCommand

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] [new] [nsfw] slash[( |-)]command [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    [a] [new] sub [slash][( |-)]command [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    [a] [new] [slash][( |-)][command] group [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    ```

## ExprNewSlashOption

|Since|v4.0.0|class:version|
|Return Type|slashoption|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] [new] [slash[( |-)]command] [(1�required)] [(2�auto[( |-)]complete)] %optiontype% option [(named|with name)] %string% with [the] desc[ription] %string%
    ```

## New User Command

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Create a new user command, to be updated on discord later.
This will create a context command of USER type.
Once created, you can execute it by right-clicking on a user, then going in 'Applications' -> <your user command name>
=== "Examples"

    ```applescript
    new user command named "Warn User"
    ```
=== "Patterns"

    ```applescript
    [a] [new] user[( |-)]command [with] [(the name|named)] %string%
    ```

## New Dropdown

|Since|v4.6.0|class:version|
|Return Type|dropdown|class:version|

Create a new dropdown menu with different properties.
There's two type of dropdown available:
- String, only text values are accepted & pre-defined
- Entity, only the specified entity type (role, channel and/or user) are accepted
Therefore, you cannot add user, channel or role to a string dropdown and vice-versa.
For entity dropdown, you can accept each type independently, or mix roles & users.
:warning: YOU CANNOT MIX CHANNELS WITH ROLES OR USERS!
=== "Examples"

    ```applescript
    new dropdown with id "string" # Default string dropdown
    new entity dropdown with id "entities" targeting "user" and "role" # Only user and role are accepted
    new entity dropdown with id "channels" targeting "channel" # Only channel are accepted
    ```
=== "Patterns"

    ```applescript
    [a] [new] [string] drop[( |-)]down [with] [the] [id] %string%
    [a] [new] entit(y|ies) drop[( |-)]down [with] [the] [id] %string% targeting %strings%
    ```

## ExprNewInput

|Since|v4.0.0|class:version|
|Return Type|textinput|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] [new] text[( |-)]input [with] [the] [id] %string% (named|with name) %string%
    [a] [new] short text[( |-)]input [with] [the] [id] %string% (named|with name) %string%
    ```

## ExprNewModal

|Since|v4.0.0|class:version|
|Return Type|modal|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [a] [new] modal [with] [the] [id] %string% (named|with name) %string%
    ```

## Modal Component Value / Values

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Get the current value(s) of a sent component, currently only working in modals with text input & select menus.
You have to precise what type of component you are trying to get, either 'textinput' or 'dropdown'.
=== "Examples"

    ```applescript
    values of dropdown with id "XXX"
    value of textinput with id "XXX"
    ```
=== "Patterns"

    ```applescript
    [the] [current] value[s] of [the] (1�text[( |-)]input|2�drop[( |-)]down) [with [the] id] %string%
    ```

## New Locale Data

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Returns the a new locale data for the given locale and the given value.
You have to provide the locale using its code (list can be found here: https://discord.com/developers/docs/reference#locales) and the value to set.
Documentation: https://docs.disky.me/advanced-stuff/slash-commands#using-localizations-v4.3.0+
=== "Examples"

    ```applescript
    new locale data for "FR" as "niveau"
    ```
=== "Patterns"

    ```applescript
    new local[e] [data] for %string% (as|with [value]) %string%
    ```

## Target Message

|Since|v4.0.0|class:version|
|Return Type|message|class:version|

Represent the target message in a message command event.
It basically represent the message that was clicked on.
=== "Examples"

    ```applescript
    target message
    ```
=== "Patterns"

    ```applescript
    [the] target message
    ```

## Slash Command Argument

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Represents a slash command argument.
The name is the ID used when defining the slash command.
Specify the type, so that Skript can parse it correctly. (if it's a number, operation wil be allowed for example)
The type should be the same used when defining the argument in the command.
=== "Examples"

    ```applescript
    # I'm doing /ban time:30 user:*user id*, so:
    set {_time} to argument "time" as integer
    set {_user} to argument "user" as user
    ```
=== "Patterns"

    ```applescript
    [the] arg[ument] [(named|with name)] %string% as %optiontype%
    ```

## Slash Command Argument

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

Represents a slash command argument.
The name is the ID used when defining the slash command.
Specify the type, so that Skript can parse it correctly. (if it's a number, operation wil be allowed for example)
The type should be the same used when defining the argument in the command.
=== "Examples"

    ```applescript
    # I'm doing /ban time:30 user:*user id*, so:
    set {_time} to argument "time" as integer
    set {_user} to argument "user" as user
    ```
=== "Patterns"

    ```applescript
    [the] arg[ument] [(named|with name)] %string% as %optiontype%
    ```

## Current Argument

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

The current argument being completed.
=== "Examples"

    ```applescript
    current argument
    ```
=== "Patterns"

    ```applescript
    current( |-)arg[ument] [name]
    ```

## Target User

|Since|v4.0.0|class:version|
|Return Type|user|class:version|

Represent the target user in a user command event.
It basically represent the user that was clicked on.
=== "Examples"

    ```applescript
    target user
    ```
=== "Patterns"

    ```applescript
    [the] target user
    ```

## Get Audio Channel

|Since|v4.0.0|class:version|
|Return Type|audiochannel|class:version|

This is an utility expression.
It will returns an Audio Channel out of the provided ID.
It will returns either the voice or stage channel corresponding to the provided ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    audio channel with id "000"
    ```
=== "Patterns"

    ```applescript
    audio channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Bot / Bot Named X

|Since|v4.0.0|class:version|
|Return Type|bot|class:version|

Get a cached bot from DiSky using its unique name.
If the desired bot does not exist or is not loaded yet, this expression will return none.
This expression cannot be changed.
=== "Examples"

    ```applescript
    get bot "name"
    bot named "name"
    ```
=== "Patterns"

    ```applescript
    [get] [the] bot [(named|with name)] %string%
    ```

## Get Category

|Since|v4.0.0|class:version|
|Return Type|category|class:version|

Get a category from a guild using its unique ID.
Categories are global on discord, means different categories cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    category with id "000"
    ```
=== "Patterns"

    ```applescript
    category (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Channel

|Since|v4.4.2|class:version|
|Return Type|channel|class:version|

A generic expression to get any channel from its ID.
This can return a text, private, news, voice, category, stage, thread or post channel.
=== "Examples"

    ```applescript
    post last embed to channel with id "000"
    ```
=== "Patterns"

    ```applescript
    channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Forum Channel

|Since|v4.0.0|class:version|
|Return Type|forumchannel|class:version|

Get a forum channel from a guild using its unique ID.
Channels are global on discord, means different forum channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    forum channel with id "000"
    ```
=== "Patterns"

    ```applescript
    forum channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Guild

|Since|v4.0.0|class:version|
|Return Type|guild|class:version|

Get a guild from a guild using its unique ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    guild with id "000"
    ```
=== "Patterns"

    ```applescript
    guild (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Channel

|Since|v4.0.0|class:version|
|Return Type|guildchannel|class:version|

Get a channel from a guild using its unique ID.
Channels are global on discord, means different channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    guild channel with id "000"
    ```
=== "Patterns"

    ```applescript
    guild channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Member

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Get a cached member from its unique ID
This expression could return null, according to if the actual member was cached or not.
To be sure it will return the corresponding member, use the retrieve member effect.
This expression cannot be changed
=== "Examples"

    ```applescript
    member with id "000" in event-guild
    ```
=== "Patterns"

    ```applescript
    [get] [the] member with id %string% (from|in|of) [the] [guild] %guild%
    ```

## Get Message Channel

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

This is an utility expression.
It will returns a Message Channel (text, news or thread) out of the provided ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    message channel with id "000"
    ```
=== "Patterns"

    ```applescript
    message channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get News Channel

|Since|v4.0.0|class:version|
|Return Type|newschannel|class:version|

Get a news channel from a guild using its unique ID.
Channels are global on discord, means different channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    news channel with id "000"
    ```
=== "Patterns"

    ```applescript
    news channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Attachment Duration

|Since|v4.12.0|class:version|
|Return Type|timespan|class:version|

Get the duration of the voice message attachment. You should check before if the attachment is an audio file using the [`attachment is audio`](conditions.md#is-attachment-audio) expression.

!!! note
This expression will only work with **voice message audio**, and not all audio files!

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
    [the] [discord] duration of %attachment%
    %attachment%'[s] [discord] duration
    ```

## Member Flags

|Since|v4.12.0|class:version|
|Return Type|memberflags|class:version|

Get or change [member flags](types.md#memberflag) of a specific member. **Some of these flags cannot be added/removed manually!**

=== "Examples"

    ```applescript
    set {_flags::*} to member flags of event-member
    ```

=== "Patterns"

    ```applescript
    [all] [the] [member] [discord] flag[s] of %member%
    [all] [the] %member%'[s] [discord] flag[s]
    ```

## Get Role

|Since|v4.0.0|class:version|
|Return Type|role|class:version|

Get a role from a guild using its unique ID.
Role are global on discord, means two role from two different guild could never have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    role with id "000"
    ```
=== "Patterns"

    ```applescript
    role (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Scheduled Event

|Since|v4.0.0|class:version|
|Return Type|scheduledevent|class:version|

Get a scheduled event from a guild using its unique ID.
Scheduled events are global on discord, means different scheduled events cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    scheduled event with id "000"
    ```
=== "Patterns"

    ```applescript
    scheduled event (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Stage Channel

|Since|v4.0.0|class:version|
|Return Type|stagechannel|class:version|

Get a stage channel from a guild using its unique ID.
Channels are global on discord, means different channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    stage channel with id "000"
    ```
=== "Patterns"

    ```applescript
    stage channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Sticker

|Since|v4.0.0|class:version|
|Return Type|sticker|class:version|

Get a cached sticker from its per-guild name
This expression is here to get a sticker from its name.
If you success to get a sticker's ID, use the retrieve sticker effect instead!
This expression cannot be changed
=== "Examples"

    ```applescript
    sticker with named "meliodas" from event-guild
    ```
=== "Patterns"

    ```applescript
    [get] [the] sticker (with name|named) %string% (from|in|of) [the] [guild] %guild%
    ```

## Get Text Channel

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

Get a text channel from a guild using its unique ID.
Channels are global on discord, means different text channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    text channel with id "000"
    ```
=== "Patterns"

    ```applescript
    text channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Get Thread Channel

|Since|v4.0.0|class:version|
|Return Type|threadchannel|class:version|

Get a thread channel from a guild using its unique ID.
Threads are global on discord, means different threads cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    thread with id "000"
    ```
=== "Patterns"

    ```applescript
    thread [channel] (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## GetUser

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    user (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## User in Guild

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Get the member related to the specified user in a specific guild.
Users are common to whole Discord, two user cannot have the same instance.
Members are common to guilds, but also holding an user as reference.
User can have multiple instance according to which guild they are in, therefore they are considered as member.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    %user% in [the] [guild] %guild%
    ```

## Get Voice Channel

|Since|v4.0.0|class:version|
|Return Type|voicechannel|class:version|

Get a voice channel from a guild using its unique ID.
Channels are global on discord, means different channels cannot have the same ID.
This expression cannot be changed.
=== "Examples"

    ```applescript
    voice channel with id "000"
    ```
=== "Patterns"

    ```applescript
    voice channel (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## Discord Permissions Of

|Since|v4.0.0|class:version|
|Return Type|permission|class:version|

Get or change the permissions of a specific member or role in an optional channel.
=== "Examples"

    ```applescript
    add (manage server) to permissions of event-member in event-channel
    remove (administrator) from permissions of event-role
    ```
=== "Patterns"

    ```applescript
    permissions of %member/role% [in %-channel%]
    ```

## User Locale

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the language code defined as user-side client of Discord.
Basically, return the language user's client is loaded in.
This expression only works in interactions event, and cannot be used outside of them.
=== "Examples"

    ```applescript
    the user locale
    ```
=== "Patterns"

    ```applescript
    [the] user['s] local[e] [(code|language)]
    ```

## Inline Rich Message Builder

|Since|v4.4.1, 4.4.3 (component-only)|class:version|
|Return Type|messagecreatebuilder|class:version|

Create a new rich message in one line only.
WARNING: This could slow a lot the Skript's parsing time if used too many times!
We still recommend to use the create message section instead!
You can also use the second pattern to send component-only messages.
=== "Examples"

    ```applescript
    reply with message "hello world" with embed last embed with components {_row}
    post components new danger button with id "id" named "Hey" to event-channel
    ```
=== "Patterns"

    ```applescript
    [rich] [:silent] message %string/embedbuilder% [with embed[s] %-embedbuilders%] [with (component[s]|row[s]) %-rows/buttons/dropdowns%] [with (file|attachment)[s] %-strings%]
    rich [:silent] component[s] %rows/buttons/dropdowns%
    ```

## Logged User

|Since|v4.11.0|class:version|
|Return Type|user|class:version|

The user who triggered the log entry.
=== "Examples"

    ```applescript
    logged user of event-logentry
    ```
=== "Patterns"

    ```applescript
    [the] log[ged] (user|author) of %logentry%
    %logentry%'[s] log[ged] (user|author)
    ```

## Logged Guild

|Since|v4.11.0|class:version|
|Return Type|guild|class:version|

The guild where the log entry has been triggered.
=== "Examples"

    ```applescript
    logged guild of event-logentry
    ```
=== "Patterns"

    ```applescript
    [the] log[ged] guild of %logentry%
    %logentry%'[s] log[ged] guild
    ```

## Logged ID

|Since|v4.11.0|class:version|
|Return Type|string|class:version|

The ID of the log entry.
=== "Examples"

    ```applescript
    logged id of event-logentry
    ```
=== "Patterns"

    ```applescript
    [the] log[ged] id of %logentry%
    %logentry%'[s] log[ged] id
    ```

## Logged Action

|Since|v4.11.0|class:version|
|Return Type|object|class:version|

The action type of the log entry.
=== "Examples"

    ```applescript
    logged action of event-logentry
    ```
=== "Patterns"

    ```applescript
    [the] log[ged] action [type] of %logentry%
    %logentry%'[s] log[ged] action [type]
    ```

## ExprMaxRange

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] max[imum] range of %dropdown/textinput%
    %dropdown/textinput%'[s] max[imum] range
    ```

## ExprMinRange

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] min[imum] range of %dropdown/textinput%
    %dropdown/textinput%'[s] min[imum] range
    ```

## ExprPlaceholder

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] place[( |-)]holder of %dropdown/textinput%
    %dropdown/textinput%'[s] [discord] place[( |-)]holder
    ```

## ExprRequireState

|Since|v4.0.0|class:version|
|Return Type|boolean|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] require[d] state of %textinput%
    %textinput%'[s] require[d] state
    ```

## ExprValue

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [default] value of %textinput%
    %textinput%'[s] [default] value
    ```

## Color from Hex

|Since|v4.0.0|class:version|
|Return Type|color|class:version|

Get a color from a hexadecimal string.
Do not include the # in the string.
=== "Examples"

    ```applescript
    set embed color of embed to hex "ff0000"
    ```
=== "Patterns"

    ```applescript
    [the] (hex|color) %string%
    ```

## ActivityEmote

|Since|v4.0.0|class:version|
|Return Type|emote|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] activity emo(ji|te) of %activity%
    %activity%'[s] activity emo(ji|te)
    ```

## ActivityText

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] activity (text|content|name) of %activity%
    %activity%'[s] activity (text|content|name)
    ```

## ActivityType

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] activity type of %activity%
    %activity%'[s] activity type
    ```

## ActivityURL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] activity ur(i|l) of %activity%
    %activity%'[s] activity ur(i|l)
    ```

## Attachments File Extension

|Since|v1.7|class:version|
|Return Type|string|class:version|

Get the file extension of an attachment.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] file ext[ension] of %attachment%
    %attachment%'[s] [discord] file ext[ension]
    ```

## Attachments File Name

|Since|v1.7|class:version|
|Return Type|string|class:version|

Get the file name of an attachment.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] file name of %attachment%
    %attachment%'[s] [discord] file name
    ```

## Attachments URL

|Since|v1.7|class:version|
|Return Type|string|class:version|

Get the url of an attachment.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [attachment] ur(l|i) of %attachment%
    %attachment%'[s] [discord] [attachment] ur(l|i)
    ```

## User / Bot / Guild Avatar

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the avatar URL of any user, guild or bot.
This can be changed for guilds and bots only!
=== "Examples"

    ```applescript
    avatar of event-guild
    avatar of event-user
    ```
=== "Patterns"

    ```applescript
    [the] avatar [url] of %guild/user/sticker/member/bot%
    %guild/user/sticker/member/bot%'[s] avatar [url]
    ```

## Ban Reason

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

The optional reason which say why the user of this ban was banned.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [ban[ned]] reason of %ban%
    %ban%'[s] [ban[ned]] reason
    ```

## Ban User

|Since|v4.0.0|class:version|
|Return Type|user|class:version|

The user linked to this ban.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [banned] user of %ban%
    %ban%'[s] [banned] user
    ```

## BotName

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot name of %bot%
    %bot%'[s] [discord] bot name
    ```

## BotPing

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot ping of %bot%
    %bot%'[s] [discord] bot ping
    ```

## BotPresence

|Since|v4.0.0|class:version|
|Return Type|activity|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] presence of %bot%
    %bot%'[s] [discord] presence
    ```

## EnumBotStatus

|Since|v4.0.0|class:version|
|Return Type|onlinestatus|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [online] status of %bot/member%
    %bot/member%'[s] [discord] [online] status
    ```

## BotToken

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot token of %bot%
    %bot%'[s] [discord] bot token
    ```

## BotUptime

|Since|v4.0.0|class:version|
|Return Type|timespan|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [bot] uptime of %bot%
    %bot%'[s] [discord] [bot] uptime
    ```

## Bot Self Member

|Since|v4.9.0|class:version|
|Return Type|member|class:version|

Get the self member instance of a bot, in a specific guild.
=== "Examples"

    ```applescript
    self member of event-bot in event-guild
    self member of bot "name"
    ```
=== "Patterns"

    ```applescript
    [the] self [member] of [the] [bot] %bot% [in [the] [guild] %guild%]
    [the] [bot] %bot%'s self [member] [in [the] [guild] %guild%]
    ```

## ChannelBitrate

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] bitrate of %channel/channelaction%
    %channel/channelaction%'[s] [channel] bitrate
    ```

## Channel Jump URL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Returns the jump-to URL for this channel.
Clicking this URL in the Discord client will cause the client to jump to the specified channel.
=== "Examples"

    ```applescript
    reply with channel url of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] channel [jump] url of %channel%
    %channel%'[s] channel [jump] url
    ```

## ChannelMaxUser

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] max[imum] user[s] of %channel/channelaction%
    %channel/channelaction%'[s] [channel] max[imum] user[s]
    ```

## ChannelName

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] channel name of %channel/channelaction%
    %channel/channelaction%'[s] channel name
    ```

## ChannelNSFW

|Since|v4.0.0|class:version|
|Return Type|boolean|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] nsfw of %channel/channelaction%
    %channel/channelaction%'[s] [channel] nsfw
    ```

## ChannelParent

|Since|v4.0.0|class:version|
|Return Type|category|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] parent of %channel/channelaction%
    %channel/channelaction%'[s] [channel] parent
    ```

## ChannelPosition

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] position of %channel/channelaction%
    %channel/channelaction%'[s] [channel] position
    ```

## ChannelRegion

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] region of %channel/channelaction%
    %channel/channelaction%'[s] [channel] region
    ```

## ChannelSlowmode

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] slow[( |-)]mode of %channel/channelaction%
    %channel/channelaction%'[s] [channel] slow[( |-)]mode
    ```

## ChannelTopic

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [channel] topic of %channel/channelaction%
    %channel/channelaction%'[s] [channel] topic
    ```

## Embed Color

|Since|v4.0.0|class:version|
|Return Type|color|class:version|

Get or change the color of an embed builder.
The color input must come from Skript, and will be converted by DiSky.
=== "Examples"

    ```applescript
    set embed color of embed to red
    ```
=== "Patterns"

    ```applescript
    [the] (embed|discord) colo[u]r of %embedbuilder%
    %embedbuilder%'[s] (embed|discord) colo[u]r
    ```

## Creation Date

|Since|v4.0.0|class:version|
|Return Type|date|class:version|

Get the creation date (as Skript date) of any ISnowFlake entity, including, but not limited to:
- Member
- User
- Role
- Guild
- Channel
- etc...
=== "Examples"

    ```applescript
    creation date of event-user
    created date of event-member
    ```
=== "Patterns"

    ```applescript
    [the] creat(ion|ed) date of %guild/member/user/role/channel/message/emote%
    %guild/member/user/role/channel/message/emote%'[s] creat(ion|ed) date
    ```

## Discord ID

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the unique long value (ID) that represent a discord entity.
=== "Examples"

    ```applescript
    discord id of event-channel
    discord id of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] discord id of %channel/role/user/threadchannel/scheduledevent/member/sticker/message/dropdown/button/guild%
    %channel/role/user/threadchannel/scheduledevent/member/sticker/message/dropdown/button/guild%'[s] discord id
    ```

## Name of Discord Entity

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

This represent the current name of any discord entity that can hold one.
You can change name of every entity except member and user by defining a new text.
Check for 'nickname of member' if you want to check / change custom member's name.
=== "Examples"

    ```applescript
    discord name of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [the] discord name of %channel/user/member/sticker/scheduledevent/emote/threadchannel/role/guild%
    %channel/user/member/sticker/scheduledevent/emote/threadchannel/role/guild%'[s] [the] discord name
    ```

## EmbedAuthor

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] author of %embedbuilder%
    %embedbuilder%'[s] author
    ```

## EmbedAuthorIcon

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] author icon of %embedbuilder%
    %embedbuilder%'[s] author icon
    ```

## EmbedAuthorURL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] author url of %embedbuilder%
    %embedbuilder%'[s] author url
    ```

## EmbedDescription

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] description of %embedbuilder%
    %embedbuilder%'[s] description
    ```

## EmbedFooter

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] footer of %embedbuilder%
    %embedbuilder%'[s] footer
    ```

## EmbedFooterIcon

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] footer icon of %embedbuilder%
    %embedbuilder%'[s] footer icon
    ```

## EmbedImage

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] image of %embedbuilder%
    %embedbuilder%'[s] image
    ```

## EmbedThumbnail

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] thumbnail of %embedbuilder%
    %embedbuilder%'[s] thumbnail
    ```

## EmbedTimeStamp

|Since|v4.0.0|class:version|
|Return Type|date|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] time[( |-)]stamp of %embedbuilder%
    %embedbuilder%'[s] time[( |-)]stamp
    ```

## EmbedTitle

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] title of %embedbuilder%
    %embedbuilder%'[s] title
    ```

## Embed URL

|Since|v4.12.0|class:version|
|Return Type|string|class:version|

Get or change the URL of this embed. The Discord client mostly only uses this property in combination with the title for a clickable Hyperlink.
If multiple embeds in a message use the same URL, the Discord client will merge them into a single embed and aggregate images into a gallery view.

!!! warning
    This is different from the [EmbedTitleURL](#embedtitleurl) property: this one can be used even if there's **no title yet**, while the other one can only be used if **there's a title**!

=== "Examples"

    ```applescript
    set embed url of embed to "https://disky.me/"
    ```
=== "Patterns"

    ```applescript
    [the] embed url of %embedbuilder%
    %embedbuilder%'[s] embed url
    ```

## EmbedTitleURL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] title url of %embedbuilder%
    %embedbuilder%'[s] title url
    ```

## Emote Name

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the name of this emote.
This, instead of 'discord name of %emote%' will return the name of an emote, and not an emoji.
You can change this property to change the emote's name itself.
=== "Examples"

    ```applescript
    emote name of event-emote
    set emote name of reaction "disky" to "disky2" # Will now be 'reaction "disky2"' to get it back
    ```
=== "Patterns"

    ```applescript
    [the] emo(te|ji) name of %emote%
    %emote%'[s] emo(te|ji) name
    ```

## Emote Image URL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the URL of this emote.
Only emote have image URL, emoji are from Discord and will therefore return none here.
=== "Examples"

    ```applescript
    emote url of event-emote
    emote image of reaction "disky" # Custom emoji only
    ```
=== "Patterns"

    ```applescript
    [the] [the] emo(te|ji) (ur(i|l)|image [url]) of %emote%
    %emote%'[s] [the] emo(te|ji) (ur(i|l)|image [url])
    ```

## Channel of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|audiochannel|class:version|

Get the channel of a scheduled event.
Can be null if the event is external. Will returns either a stage or voice channel.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] channel of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] channel
    ```

## Cover of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|string|class:version|

Get the cover of a scheduled event.
Links to a potentially heavily compressed image. You can append a size parameter to the URL if needed. Example: ?size=4096
This can returns null if no cover is set for the event.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] cover of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] cover
    ```

## Creator of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|user|class:version|

Get the creator of a scheduled event.
May return none if user has deleted their account, the User object is not cached or the event was created before Discord started keeping track of event creators on October 21st, 2021
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] creator of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] creator
    ```

## End date of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|date|class:version|

Get the end date of a scheduled event.
Can be null if the event is made from a channel and not an external place.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] end date of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] end date
    ```

## Location of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|string|class:version|

Get the location of a scheduled event.
Returns the specified place if the event is external, or the audio channel's ID.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] location of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] location
    ```

## Start date of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|date|class:version|

Get the start date of a scheduled event. Cannot be null.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] [start] date of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] [start] date
    ```

## Status of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|string|class:version|

Get the status of a scheduled event between:
- Scheduled
- Active
- Completed
- Cancelled
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] status of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] status
    ```

## Type of Scheduled Event

|Since|v4.8.0|class:version|
|Return Type|string|class:version|

Get the type of a scheduled event.
It can either be 'voice/stage instance' or 'external' according to the type of the event.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] scheduled [event] type of %scheduledevent%
    %scheduledevent%'[s] scheduled [event] type
    ```

## Default Forum Emoji

|Since|v4.0.0|class:version|
|Return Type|emote|class:version|

Represent the default emoji of a forum channel.
It's the mote that is added automatically once a new post is created.
Can return none and can be changed.
=== "Examples"

    ```applescript
    set default emoji of event-forumchannel to reaction "smile"
    ```
=== "Patterns"

    ```applescript
    [the] default [forum] emoji of %forumchannel%
    %forumchannel%'[s] default [forum] emoji
    ```

## Tag Required

|Since|v4.0.0|class:version|
|Return Type|boolean|class:version|

Get a true/false value of the tag required state of a forum channel.
This property can be changed, and we recommend the tag required condition for checks.
=== "Examples"

    ```applescript
    set tag required of event-forumchannel to true
    ```
=== "Patterns"

    ```applescript
    [the] [the] tag required of %forumchannel%
    %forumchannel%'[s] [the] tag required
    ```

## Guild Of

|Since|v4.0.0|class:version|
|Return Type|guild|class:version|

Return the guild of a specific entity.
This can return null if the entity is not guild-based, like private message channel or message.
=== "Examples"

    ```applescript
    guild of event-member
    guild of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] guild of %channel/role/sticker/member/message%
    %channel/role/sticker/member/message%'[s] guild
    ```

## GuildAFKChannel

|Since|v4.0.0|class:version|
|Return Type|voicechannel|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] afk [voice( |-)] channel of %guild%
    %guild%'[s] [discord] afk [voice( |-)] channel
    ```

## GuildAFKTimeout

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] afk time[( |-)]out [second[s]] of %guild%
    %guild%'[s] [discord] afk time[( |-)]out [second[s]]
    ```

## GuildBanner

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] banner of %guild%
    %guild%'[s] [discord] banner
    ```

## Guild Boost Count

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

Represent how many people are boosting the guild currently.
=== "Examples"

    ```applescript
    reply with "There's %boost amount of event-guild% booster(s)!"
    ```
=== "Patterns"

    ```applescript
    [the] [guild] boost[(ing|er)] (amount|number|size) of %guild%
    %guild%'[s] [guild] boost[(ing|er)] (amount|number|size)
    ```

## Guild Booster Role

|Since|v4.0.0|class:version|
|Return Type|role|class:version|

Represent the booster role of this guild.
Any member that got this role is actually a booster of the guild.
=== "Examples"

    ```applescript
    reply with "Thanks to our %mention tag of boost role of event-guild%!"
    ```
=== "Patterns"

    ```applescript
    [the] [guild] boost[(ing|er)] role[s] of %guild%
    %guild%'[s] [guild] boost[(ing|er)] role[s]
    ```

## Everyone Role

|Since|v4.0.0|class:version|
|Return Type|role|class:version|

Represent the @everyone role of a guild.
Even if it's not a real role, it share multiple properties such as permissions.
=== "Examples"

    ```applescript
    reply with mention tag of everyone role of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [discord] (public|everyone) role of %guild%
    %guild%'[s] [discord] (public|everyone) role
    ```

## Guild Verification Level

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent the verification level of the guild. It can either be:
- None
- Low
- Medium
- High
- Very High
=== "Examples"

    ```applescript
    reply with verification level of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [guild] verification level[s] of %guild%
    %guild%'[s] [guild] verification level[s]
    ```

## Invite Code

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent the unique invite code used in the Discord URL.
=== "Examples"

    ```applescript
    reply with invite code of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite code of %invite%
    %invite%'[s] invite code
    ```

## Invite Inviter

|Since|v4.0.0|class:version|
|Return Type|user|class:version|

Represent the user who created the invite.
=== "Examples"

    ```applescript
    reply with mention tag of invite inviter of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite (inviter|author) of %invite%
    %invite%'[s] invite (inviter|author)
    ```

## Invite Max Age

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

Represent the max age time this invite can be used.
=== "Examples"

    ```applescript
    reply with invite max age of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite max age[s] of %invite%
    %invite%'[s] invite max age[s]
    ```

## Invite Max Uses

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

Represent the max amount of times this invite can be used.
=== "Examples"

    ```applescript
    reply with invite max use of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite max use[s] of %invite%
    %invite%'[s] invite max use[s]
    ```

## Invite URL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent the plain Discord URL that people have to click on in order to join the invite's guild.
=== "Examples"

    ```applescript
    reply with invite url of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite url of %invite%
    %invite%'[s] invite url
    ```

## Invite Uses

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

Represent the amount of times this invite has been used.
=== "Examples"

    ```applescript
    reply with invite uses of event-invite
    ```
=== "Patterns"

    ```applescript
    [the] invite use[s] of %invite%
    %invite%'[s] invite use[s]
    ```

## Member Effective Name

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Simple way to get the effective name of a member in a guild:
If the nickname is not set, it will return the discord name of the member, else its nickname.
=== "Examples"

    ```applescript
    reply with effective name of event-member
    ```
=== "Patterns"

    ```applescript
    [the] [member] effective name[s] of %member%
    %member%'[s] [member] effective name[s]
    ```

## Member Join Date

|Since|v4.0.0|class:version|
|Return Type|date|class:version|

Represent the skript's date of the member's join date.
It cannot be changed.
This is a specific element of the bot, so it can be used in the bots event.
=== "Examples"

    ```applescript
    reply with member join date of event-member
    ```
=== "Patterns"

    ```applescript
    [the] [member] [member] join date of %member%
    %member%'[s] [member] [member] join date
    ```

## Member Nickname

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent the member nickname. Can be none if the member doesn't have any nickname currently.
USe 'effective name' expression to get member's name of its nickname is not set.
=== "Examples"

    ```applescript
    reply with member nickname of event-member
    set member nickname of event-member to "ayo?!"
    ```
=== "Patterns"

    ```applescript
    [the] [member] nick[( |-)]name[s] of %member%
    %member%'[s] [member] nick[( |-)]name[s]
    ```

## MemberVoiceChannel

|Since|v4.0.0|class:version|
|Return Type|audiochannel|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [member] (voice|audio) channel of %member%
    %member%'[s] [member] (voice|audio) channel
    ```

## Mention Tag

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the mention name of the discord entity.
It will return the similar format that when you are doing @ (roles, users) or # (channels) followed by names.
=== "Examples"

    ```applescript
    mention tag of event-channel
    mention tag of channel with id "000"
    ```
=== "Patterns"

    ```applescript
    [the] mention [tag] of %channel/role/user/emote/member%
    %channel/role/user/emote/member%'[s] mention [tag]
    ```

## Message User Author

|Since|v4.0.0|class:version|
|Return Type|user|class:version|

Get the user instance of the message's author. Can be null in case of the message was sent by a webhook.
=== "Examples"

    ```applescript
    author of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] (user|author|writer) of %message%
    %message%'[s] [discord] [message] (user|author|writer)
    ```

## Message Text Channel

|Since|v4.0.0|class:version|
|Return Type|textchannel|class:version|

Get the text channel were the message was sent. Can be null if it's in PM or not in guild!
=== "Examples"

    ```applescript
    channel of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] [text]( |-)channel of %message%
    %message%'[s] [discord] [message] [text]( |-)channel
    ```

## Message Content

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the raw (non formatted) content of a sent message.
=== "Examples"

    ```applescript
    content of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] content of %message%
    %message%'[s] [discord] [message] content
    ```

## Message Guild

|Since|v4.0.0|class:version|
|Return Type|guild|class:version|

Get the guild where the message was sent. Can be null if it's in PM or not in guild!
=== "Examples"

    ```applescript
    guild of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] guild of %message%
    %message%'[s] [discord] [message] guild
    ```

## Message/Event Jump URL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the jump URL of a specific message/scheduled event
=== "Examples"

    ```applescript
    jump url of event-message
    jump url of scheduled event with id "000"
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] [jump] url of %message%
    %message%'[s] [discord] [message] [jump] url
    ```

## Message Member Author

|Since|v4.0.0|class:version|
|Return Type|member|class:version|

Get the member instance of the message's author. Can be null if it's in PM or not in guild!
=== "Examples"

    ```applescript
    member writer of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] member (author|writer) of %message%
    %message%'[s] [discord] [message] member (author|writer)
    ```

## MessageReferenced

|Since|v4.0.0|class:version|
|Return Type|message|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] referenc(ing|ed) message of %message%
    %message%'[s] [discord] [message] referenc(ing|ed) message
    ```

## Profile Banner

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Get the profile banner URL. If the user doesn't have a custom banner, this will return none.
Use the 'profile color' expression to get the color instead of the banner URL in that case!
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] profile banner [ur(l|i)] of %userprofile%
    %userprofile%'[s] profile banner [ur(l|i)]
    ```

## Profile Color

|Since|v4.0.0|class:version|
|Return Type|color|class:version|

Get the profile color accent. If the user have a custom banner, this will return none.
Use the 'profile banner' expression to get the avatar URL instead of the color accent in that case!
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] profile color [accent] of %userprofile%
    %userprofile%'[s] profile color [accent]
    ```

## RoleColor

|Since|v4.0.0|class:version|
|Return Type|color|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] role color of %role/roleaction%
    %role/roleaction%'[s] role color
    ```

## RoleName

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] role name of %role/roleaction%
    %role/roleaction%'[s] role name
    ```

## RolePosition

|Since|v4.0.0|class:version|
|Return Type|number|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [role] position of %role/roleaction%
    %role/roleaction%'[s] [discord] [role] position
    ```

## Tag Emoji

|Since|v4.4.4|class:version|
|Return Type|emote|class:version|

Gets the emoji of a forum tag. Can be null if the tag has no emoji.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] tag emo(te|ji) of %forumtag%
    %forumtag%'[s] tag emo(te|ji)
    ```

## User Discriminator

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Represent the four digit number after the # of a user's name.
These, mixed with the user name itself, are unique.
This **DOES NOT** include the `#` char, so you have to add it yourself.
=== "Examples"

    ```applescript
    reply with discriminator of event-user
    ```
=== "Patterns"

    ```applescript
    [the] [user] discriminator of %user%
    %user%'[s] [user] discriminator
    ```

## Message Builder Content

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Text content of a message builder
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] content of %messagecreatebuilder%
    %messagecreatebuilder%'[s] content
    ```

## Track Author

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the author of a specific track
=== "Examples"

    ```applescript
    set {_author} to author of last played track.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track author of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track author
    ```

## Track Duration

|Since|v4.0.0|class:version|
|Return Type|timespan|class:version|

Return the duration of a specific track
=== "Examples"

    ```applescript
    set {_duration} to duration of last played track.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track duration of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track duration
    ```

## Track Identifier

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the unique identifier of a track
=== "Examples"

    ```applescript
    set {_id} to identifier of current track of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track id[entifier] of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track id[entifier]
    ```

## Track Position

|Since|v4.0.0|class:version|
|Return Type|timespan|class:version|

Return the position of a specific track
This property can be changed to move the current position of the track.
It will only accept timespan (e.g. '1 second', '25 minutes', etc...)!
=== "Examples"

    ```applescript
    set {_position} to track position of track event-bot is playing in event-guild
    add 10 second to track position of track event-bot is playing in event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track position of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track position
    ```

## Track Thumbnail

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the thumbnail URL of a specific track
=== "Examples"

    ```applescript
    set thumbnail of embed to thumbnail of last played track.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track thumbnail of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track thumbnail
    ```

## ExprTrackTitle

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track title of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track title
    ```

## Track URL

|Since|v4.0.0|class:version|
|Return Type|string|class:version|

Return the YouTube URL of a track
=== "Examples"

    ```applescript
    set {_url} to url of last played track.
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track (url|uri) of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track (url|uri)
    ```

## ExprEventValues

|Since|v4.0.0|class:version|
|Return Type|object|class:version|

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [(multiple|list|array)] event-<.+>
    ```

