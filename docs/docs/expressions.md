---
search:
  boost: 2
icon: material/check-all
---

# Expressions

[[[% import 'macros.html' as macros %]]]

## User's Avatar Decoration URL

[[[ macros.required_version('4.15.0') ]]]
[[[ macros.return_type('string') ]]]

Get the URL of the user's avatar decoration URL. This will return none if the user doesn't have a decoration selected.

=== "Examples"

    ```applescript
    discord command decorations [<user>]:
        prefixes: ?
        trigger:
            set {_dec} to avatar decoration of arg-1
            if {_dec} is not set:
                reply with ":x: **Error:** You do not have an avatar decoration."
                stop

            make embed and store it in {_e}:
                set title of embed to "Your avatar decoration"
                set embed color of embed to orange
                set image of embed to {_dec}
            reply with {_e}
    ```

=== "Patterns"

    ```applescript
    [the] [user] (decoration[s] avatar|avatar decoration[s]) of %user%
    %user%'[s] [user] (decoration[s] avatar|avatar decoration[s])
    ```

## Discord Command Argument

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

Works same as Skript's command argument. You can specify the argument number or the argument type (in case there's only one user or member for example) to get the selected value.
=== "Examples"

    ```applescript
    set {_args} last arguments
    set {_args} last args
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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Return the plain formatter of the discord command's argument
You should however use (arg-1) for example which will return the argument value directly.
This is intended to be for test purpose only, and therefore only return a String formatted containing every used arguments.

=== "Examples"

    ```applescript
    set {_args} to the used arguments
    ```

=== "Patterns"

    ```applescript
    [the] use[d]( |-)arg[ument][s]
    ```

## Used Prefix

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('slashchoice') ]]]

No description provided.
=== "Examples"

    ```applescript
    
    ```
=== "Patterns"

    ```applescript
    [all] [the] [option] choices of %slashoption%
    [all] [the] %slashoption%'[s] [option] choices
    ```

## Sub-command Groups

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('slashcommandgroup') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('subslashcommand') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('button') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('row') ]]]

Create a new (empty) components row.
You can add either max 5 buttons or one dropdown to it.
A single message can hold 5 components rows.
=== "Examples"

    ```applescript
    make new component row and store it in {_row}:
        add new success button with id "btn-2" named "Green lands!" with reaction "smile" to components of the row builder
        add new link button with id "https://forum.itsthesky.info/discord/" named "DiSky's Discord" to components of the row builder
    add {_row} to rows of the message

    ```
=== "Patterns"

    ```applescript
    [a] new component[s] row
    ```

## New Dropdown Option

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('selectoption') ]]]

Create a new dropdown option with different properties.
This is a predefined option holding a string value. It can only be used in string dropdowns.
The value represent the returned string that this dropdown will return if this option is selected.
The name / label is the actual shown name on the option.
Description and emote are optional.
=== "Examples"

    ```applescript
    add new option with value "one" named "One!" with description "Click to select" with reaction "sparkles" to options of {_dp}
    add new option with value "two" named "Two!?" with description "Click to select" with reaction "sparkles" to options of {_dp}
    add new option with value "three" named "THREE!!!" with description "Click to select" with reaction "sparkles" to options of {_dp}
    ```
=== "Patterns"

    ```applescript
    [a] new [default] [dropdown] option with value %string% (named|with label) %-string% [with description [%-string%]] [with [emoji] %-emote%]
    ```

## Command Localization

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

Represents the localization of the name or the description of a slash/sub command.
You can add **Locale Data** (check for expression) to them. Basically, the command's name & description will be according to the client's language code.

**For more information, check the [dedicated wiki page](../interactions/slash-commands.md#using-localizations)!**

=== "Examples"

    See the [dedicated wiki page](../interactions/slash-commands.md#using-localizations) for examples.

=== "Patterns"

    ```applescript
    [all] [the] (name|description)['s] (localization[s]|locale[s]) of %slashcommand/subslashcommand%
    [all] [the] %slashcommand/subslashcommand%'[s] (name|description)['s] (localization[s]|locale[s])
    ```

## PropOptions

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

## Selected Dropdown Values

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

The list of the selected entities, in the current entity dropdown update event.
=== "Examples"

    ```applescript
    if "%selected value%" is "login":
    ```
=== "Patterns"

    ```applescript
    select[ed] entit(y|ies)
    ```

## Selected Values

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('emote') ]]]

Get an emoji or an emote from its name, ID or unicode.

- An emoji is discord-side only, can be used everywhere, and don't have any attached guild.
- An emote is guild-side only, have a custom long ID and are attached to a guild.

If the specified reaction doesn't exist, DiSky will simply return null and say it in console.
We highly recommend the specification of the guild when retrieving an emote, to avoid conflicts with other that potentially have the same name.

!!! success "Check the [dedicated wiki page](../messages/emojis.md) for more information!"

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

## Bot Guilds

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guild') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_guilds::*} to guilds of event-bot
    ```
=== "Patterns"

    ```applescript
    [all] [the] guilds of %bot%
    [all] [the] %bot%'[s] guilds
    ```

## Bot Presences

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('activity') ]]]

No description provided.
=== "Examples"

    ```applescript
    set the presence of the bot named "BOTNAME" to listening "with feelings"
    set the presence of the bot named "BOTNAME" to watching "over the"
    set the presence of the bot named "BOTNAME" to playing "with the API"
    set the presence of the bot named "BOTNAME" to streaming "with the API" with the url "https://itsthesky.info"
    set the presence of the bot named "BOTNAME" to competing "with the API"
    ```
=== "Patterns"

    ```applescript
    listening [to] %string%
    watching [to] %string%
    playing [to] %string%
    streaming [to] %string% with [the] url %string%
    competing [to] %string%
    ```

## Channel of Category

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_channels::*} to channels of event-category
    set {_channels::*} to channels of category with id "0000"
    ```
=== "Patterns"

    ```applescript
    [all] [the] [discord] channel[s] of %category%
    [all] [the] %category%'[s] [discord] channel[s]
    ```

## Voice Channel Members

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

[[[ macros.required_version('4.0.0, 4.4.4 (threads of forum channel)') ]]]
[[[ macros.return_type('threadchannel') ]]]

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

## New Category Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('channelaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new category action in event-guild
    set channel name of {_action} to "Dog"
    create {_action} and store it in {_category}
    ```
=== "Patterns"

    ```applescript
    [a] new category (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## New News Channel Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('channelaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new news channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "News"

    create {_action} and store it in {_text}
    ```
=== "Patterns"

    ```applescript
    [a] new news[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## New Stage Channel Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('channelaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new stage channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "Stage"

    create {_action} and store it in {_text}
    ```
=== "Patterns"

    ```applescript
    [a] new stage[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## New Text Channel Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('channelaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new text channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "Text"
    
    create {_action} and store it in {_text}
    ```
=== "Patterns"

    ```applescript
    [a] new text[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## New Voice Channel Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('channelaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new voice channel action in event-guild
    set channel parent of {_action} to {_category}
    set channel name of {_action} to "Voice"
    set max users of {_action} to 5
    
    create {_action} and store it in {_voice}
    ```
=== "Patterns"

    ```applescript
    [a] new voice[( |-)]channel (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## Discord Members of Guild / Channel

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('role') ]]]

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

[[[ macros.required_version('1.0') ]]]
[[[ macros.return_type('embedbuilder') ]]]

This expression returns the last generated embed using the embed builder.
=== "Examples"

    ```applescript
    reply with {_embed}
    reply with last embed
    ```
=== "Patterns"

    ```applescript
    [the] [last] [(made|created|generated)] embed
    ```

## Guild Boosters

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guildchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('newschannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('scheduledevent') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('stagechannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('oicechannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('attachment') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('embedbuilder') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('emote') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('role') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('user') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('oicechannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('emote') ]]]

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

## New Role Action

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('roleaction') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new role action in event-guild
    set role name of {_action} to "Member"
    
    create {_action} and store it in {_role}
    ```
=== "Patterns"

    ```applescript
    [a] new role (action|manager) in [the] [guild] %guild% [(using|with) [the] [bot] %-bot%]
    ```

## Get Tag

[[[ macros.required_version('4.4.4') ]]]
[[[ macros.return_type('forumtag') ]]]

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

[[[ macros.required_version('4.4.4') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

## Parent Channel of Thread

[[[ macros.required_version('4.13.0') ]]]
[[[ macros.return_type('guildchannel') ]]]

Get the parent channel of a thread channel. It can return a text, news or forum channel.

=== "Examples"

    ```applescript
    set {_parent} to thread parent of event-thread
    ```

=== "Patterns"

    ```applescript
    [the] thread parent [channel] of %guildchannel%
    %guildchannel%'[s] thread parent [channel]
    ```

## Guild Bot's Role

[[[ macros.required_version('4.16.0') ]]]
[[[ macros.return_type('role') ]]]

Get the bot's specific role for a given guild. Each bot has a specific role in each guild it is in, to define its permissions and restrictions.

=== "Examples"

    ```applescript
    set {_role} to bot role of event-guild
    ```

=== "Patterns"

    ```applescript
    [the] [guild] bot role of %guild%
    [the] %guild%'[s] [guild] bot role
    ```

## Guild Boost Tier

[[[ macros.required_version('4.16.0') ]]]
[[[ macros.return_type('string') ]]]
[[[ macros.no_changers() ]]]

Get the boost tier of a guild, according to the number of boosts it has. It can return the following values:

| Returns  | Description            | Max Bitrate | Max Emojis |
|----------|------------------------|-------------|------------|
| `None`   | No boost (or only one) | 96kbps      | 50         |
| `Tier 1` | 2 boosts               | 128kbps     | 100        |
| `Tier 2` | 7 boosts               | 256kbps     | 150        |
| `Tier 3` | 14 boosts              | 384kbps     | 250        |

=== "Examples"

    ```applescript
    set {_tier} to boost tier of event-guild
    ```

=== "Patterns"

    ```applescript
    [the] [guild] boost[(ing|er)] tier of %guild%
    [the] %guild%'[s] [guild] boost[(ing|er)] tier
    ```

## User Badges

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]
[[[ macros.no_changers() ]]]

Represent every badges' name a user have.
This does not and cannot contain any intro-related badges (nitro membership or nitro boosting), it needs OAuth2 to be enabled.

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guild') ]]]
[[[ macros.no_changers() ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('row') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('messagecreatebuilder') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

Attachments of a message builder
Supports SkImage's images if the addon is installed.
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    add "plugins/Skript/scripts/msg.sk" to the attachments of the message
    ```
=== "Patterns"

    ```applescript
    [all] [the] (attachment|image)[s] of %messagecreatebuilder%
    [all] [the] %messagecreatebuilder%'[s] (attachment|image)[s]
    ```

## Message Builder Embeds

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('embedbuilder') ]]]

Embeds of a message builder
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    add last embed to the embeds of the message
    ```
=== "Patterns"

    ```applescript
    [all] [the] embed[s] of %messagecreatebuilder%
    [all] [the] %messagecreatebuilder%'[s] embed[s]
    ```

## Message Builder Component Rows

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

Component rows of a message builder
See also: 'Creator Components Row'
=== "Examples"

    ```applescript
    add {_row} to rows of the message
    ```
=== "Patterns"

    ```applescript
    [all] [the] [component[s]] row[s] of %messagecreatebuilder/modal%
    [all] [the] %messagecreatebuilder/modal%'[s] [component[s]] row[s]
    ```

## New Message Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('slashchoice') ]]]

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

## New Slash Command

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

Create a new Slash Command builder, where you'll be able to add options, subcommands, etc...
For a more detailed guide, take a look at [this tutorial](../interactions/slash-commands.md).

=== "Examples"

    Check the tutorial for a complete example: [Slash Commands](../interactions/slash-commands.md)

=== "Patterns"

    ```applescript
    [a] [new] [nsfw] slash[( |-)]command [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    [a] [new] sub [slash][( |-)]command [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    [a] [new] [slash][( |-)][command] group [with] [(the name|named)] %string% [and] with [the] desc[ription] %string%
    ```

## ExprNewSlashOption

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('slashoption') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.6.0') ]]]
[[[ macros.return_type('dropdown') ]]]

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

## Modal Text Input

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textinput') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_input} to new short text input with id "description" named "Description"
    set {_input} to new text input with id "description" named "Description"
    ```
=== "Patterns"

    ```applescript
    [a] [new] text[( |-)]input [with] [the] [id] %string% (named|with name) %string%
    [a] [new] short text[( |-)]input [with] [the] [id] %string% (named|with name) %string%
    ```

## New Modal

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('modal') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_modal} to a new modal with id "unique-id" named "My modal"
    ```
=== "Patterns"

    ```applescript
    [a] [new] modal [with] [the] [id] %string% (named|with name) %string%
    ```

## Modal Component Value / Values

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('message') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('user') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('audiochannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('bot') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('category') ]]]

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

[[[ macros.required_version('4.4.2') ]]]
[[[ macros.return_type('channel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('forumchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guild') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guildchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('newschannel') ]]]

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

[[[ macros.required_version('4.12.0') ]]]
[[[ macros.return_type('timespan') ]]]

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

[[[ macros.required_version('4.12.0') ]]]
[[[ macros.return_type('memberflags') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('role') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('scheduledevent') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('stagechannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('sticker') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('threadchannel') ]]]

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

## Get User

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

No description provided.
=== "Examples"

    ```applescript
    user with id "Id_Here"
    ```
=== "Patterns"

    ```applescript
    user (with|from) [the] id %string% [(with|using) [the] bot [(named|with name)] %-bot%]
    ```

## User in Guild

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

Get the member related to the specified user in a specific guild.
Users are common to whole Discord, two user cannot have the same instance.
Members are common to guilds, but also holding an user as reference.
User can have multiple instance according to which guild they are in, therefore they are considered as member.
=== "Examples"

    ```applescript
    user with id "000" in guild with id "000"
    ```
=== "Patterns"

    ```applescript
    %user% in [the] [guild] %guild%
    ```

## Get Voice Channel

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('oicechannel') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('permission') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.4.1, 4.4.3 (component-only)') ]]]
[[[ macros.return_type('messagecreatebuilder') ]]]

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

[[[ macros.required_version('4.11.0') ]]]
[[[ macros.return_type('user') ]]]

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

[[[ macros.required_version('4.11.0') ]]]
[[[ macros.return_type('guild') ]]]

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

[[[ macros.required_version('4.11.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.11.0') ]]]
[[[ macros.return_type('object') ]]]

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

## Dropdown/Modal Text Input Max Range

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    # Modal
    set maximum range of {_input} to 30 # Maximum length of the input
    
    # Dropdown
    set max range of {_dp} to 2
    ```
=== "Patterns"

    ```applescript
    [the] max[imum] range of %dropdown/textinput%
    %dropdown/textinput%'[s] max[imum] range
    ```

## Dropdown/Modal Text Input Min Range

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    # Modal
    set minimum range of {_input} to 30 # Maximum length of the input
    
    # Dropdown
    set min range of {_dp} to 2
    ```
=== "Patterns"

    ```applescript
    [the] min[imum] range of %dropdown/textinput%
    %dropdown/textinput%'[s] min[imum] range
    ```

## Placeholder of Dropdown/Modal Text Input

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    # Modal
    set placeholder of {_input} to "Input whatever you want here ..."

    # Dropdown
    set placeholder of {_dp} to "Select a role ..."
    ```
=== "Patterns"

    ```applescript
    [the] [discord] place[( |-)]holder of %dropdown/textinput%
    %dropdown/textinput%'[s] [discord] place[( |-)]holder
    ```

## Modal Require State Of Modal Text Input

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('boolean') ]]]

No description provided.
=== "Examples"

    ```applescript
    set required state of {_input} to true # Whether the input is required or not
    ```
=== "Patterns"

    ```applescript
    [the] require[d] state of %textinput%
    %textinput%'[s] require[d] state
    ```

## Modal Text Input Default Value

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set default value of {_input} to "This is a default value"
    ```
=== "Patterns"

    ```applescript
    [the] [default] value of %textinput%
    %textinput%'[s] [default] value
    ```

## Color from Hex

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('color') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('emote') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('1.7') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('1.7') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('1.7') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('user') ]]]

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

## Bot Name

!!! danger "Deprecated: removed since DiSky v4.18.0"
    Use [`discord name`](#name-of-discord-entity) to have the same behavior.

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_name} to bot name of event-bot
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot name of %bot%
    %bot%'[s] [discord] bot name
    ```

## Bot Ping

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_ping} to bot ping of event-bot
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot ping of %bot%
    %bot%'[s] [discord] bot ping
    ```

## Bot Presence

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('activity') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_presence} to presence of event-bot
    ```
=== "Patterns"

    ```applescript
    [the] [discord] presence of %bot%
    %bot%'[s] [discord] presence
    ```

## EnumBotStatus

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('onlinestatus') ]]]

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

## Bot Token

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_token} to bot token of event-bot
    ```
=== "Patterns"

    ```applescript
    [the] [discord] bot token of %bot%
    %bot%'[s] [discord] bot token
    ```

## Bot Uptime

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('timespan') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_uptime} to bot uptime of event-bot
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [bot] uptime of %bot%
    %bot%'[s] [discord] [bot] uptime
    ```

## Bot Self Member

[[[ macros.required_version('4.9.0') ]]]
[[[ macros.return_type('member') ]]]

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

## Channel Bitrate

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_bitrate} to bitrate of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] [channel] bitrate of %channel/channelaction%
    %channel/channelaction%'[s] [channel] bitrate
    ```

## Channel Jump URL

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

## Channel Max User

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_max} to max user of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] [channel] max[imum] user[s] of %channel/channelaction%
    %channel/channelaction%'[s] [channel] max[imum] user[s]
    ```

## Channel Name

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_name} to channel name of event-channel
    set channel name of event-channel to "new name"
    ```
=== "Patterns"

    ```applescript
    [the] channel name of %channel/channelaction%
    %channel/channelaction%'[s] channel name
    ```

## Channel NSFW

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('boolean') ]]]

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

## Channel Parent

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('category') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_parent} to parent of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] [channel] parent of %channel/channelaction%
    %channel/channelaction%'[s] [channel] parent
    ```

## Voice Channel Status

[[[ macros.required_version('4.13.0') ]]]
[[[ macros.return_type('string') ]]]

Represent the *temporary* status of a voice channel. Can be get, but also set with the following conditions:
* If the bot is **connected** to the channel, with the `voice set status` permission
* If the bot is **not connected** to the channel, with the `manage server` permission
* The status must be up to 500 characters long

!!! warning
    This status is temporary, and will be reset when the bot is disconnected from the channel.

=== "Examples"

    ```applescript
    set voice channel status of event-channel to "Doing some maths homework"
    ```

=== "Patterns"

    ```applescript
    [voice] channel status
    ```

## Channel Region

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_region} to region of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] [channel] region of %channel/channelaction%
    %channel/channelaction%'[s] [channel] region
    ```

## Channel Slowmode

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

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

## Channel Topic

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set channel topic of event-channel to "New topic"
    set {_topic} to channel topic of event-channel
    ```
=== "Patterns"

    ```applescript
    [the] [channel] topic of %channel/channelaction%
    %channel/channelaction%'[s] [channel] topic
    ```

## Embed Color

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('color') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('date') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Get the unique long value (ID) that represent a discord entity.
=== "Examples"

    ```applescript
    discord id of event-channel
    discord id of event-guild
    discord id of event-user
    ```
=== "Patterns"

    ```applescript
    [the] discord id of %channel/role/user/threadchannel/scheduledevent/member/sticker/message/dropdown/button/guild/webhook%
    %channel/role/user/threadchannel/scheduledevent/member/sticker/message/dropdown/button/guild/webhook%'[s] discord id
    ```

## Name of Discord Entity

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]
[[[ macros.accept_type('string') ]]]

This represents the current name of any discord entity that can hold one.
You can change the name of every entity except member and user by defining a new text.
Check for [nickname of member](#member-nickname) if you want to check / change custom member's name.

!!! info "This property accepts __string__, and will change the name of a **bot**, **channel** or **role**."

=== "Examples"

    ```applescript
    discord name of event-guild
    discord name of event-user
    discord name of event-member

    set discord name of event-bot to "My Bot" # Will change the Discord's Bot name (not the username)
    ```

=== "Patterns"

    ```applescript
    [the] [the] discord name of %channel/user/member/sticker/scheduledevent/emote/threadchannel/role/guild/webhook/bot%
    %channel/user/member/sticker/scheduledevent/emote/threadchannel/role/guild/webhook/bot%'[s] [the] discord name
    ```

## Author of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set author of the embed to "Author name (Can point to URL)" # author must be set first
    set author icon of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    ```
=== "Patterns"

    ```applescript
    [the] author of %embedbuilder%
    %embedbuilder%'[s] author
    ```

## Author Icon of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set author of the embed to "Author name (Can point to URL)" # author must be set first
    set author icon of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    ```
=== "Patterns"

    ```applescript
    [the] author icon of %embedbuilder%
    %embedbuilder%'[s] author icon
    ```

## Embed Author URL

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set author url of embed to "https://www.youtube.com/watch?v=i33DB6R8YUY"
    ```
=== "Patterns"

    ```applescript
    [the] author url of %embedbuilder%
    %embedbuilder%'[s] author url
    ```

## Description of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set description of embed to "Description of the embed"
    ```
=== "Patterns"

    ```applescript
    [the] description of %embedbuilder%
    %embedbuilder%'[s] description
    ```

## Footer of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set footer of embed to "Footer text"
    ```
=== "Patterns"

    ```applescript
    [the] footer of %embedbuilder%
    %embedbuilder%'[s] footer
    ```

## Footer Icon of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set footer icon of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    ```
=== "Patterns"

    ```applescript
    [the] footer icon of %embedbuilder%
    %embedbuilder%'[s] footer icon
    ```

## Image of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set image of embed to "https://media.discordapp.net/attachments/237757030708936714/390520880242884608/8xAac.png?width=508&height=522"
    ```
=== "Patterns"

    ```applescript
    [the] image of %embedbuilder%
    %embedbuilder%'[s] image
    ```

## Thumbnail of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set thumbnail of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    ```
=== "Patterns"

    ```applescript
    [the] thumbnail of %embedbuilder%
    %embedbuilder%'[s] thumbnail
    ```

## TimeStamp of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('date') ]]]

No description provided.
=== "Examples"

    ```applescript
    set timestamp of embed to now
    ```
=== "Patterns"

    ```applescript
    [the] time[( |-)]stamp of %embedbuilder%
    %embedbuilder%'[s] time[( |-)]stamp
    ```

## Title of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set title of embed to "Title"
    ```
=== "Patterns"

    ```applescript
    [the] title of %embedbuilder%
    %embedbuilder%'[s] title
    ```

## Embed URL

[[[ macros.required_version('4.12.0') ]]]
[[[ macros.return_type('string') ]]]

Get or change the URL of this embed. The Discord client mostly only uses this property in combination with the title for a clickable Hyperlink.
If multiple embeds in a message use the same URL, the Discord client will merge them into a single embed and aggregate images into a gallery view.

!!! warning
This is different from the [Embed Title URL](#title-of-embed) property: this one can be used even if there's **no title yet**, while the other one can only be used if **there's a title**!

=== "Examples"

    ```applescript
    set embed url of embed to "https://disky.me/"
    ```
=== "Patterns"

    ```applescript
    [the] embed url of %embedbuilder%
    %embedbuilder%'[s] embed url
    ```

## Title URL of Embed

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set title url of embed to "https://www.crunchyroll.com/fr/tonikawa-over-the-moon-for-you"
    ```
=== "Patterns"

    ```applescript
    [the] title url of %embedbuilder%
    %embedbuilder%'[s] title url
    ```

## Emote Name

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Get the URL of this emote. Only emote have image URL, emoji are from Discord and will therefore return none here.

=== "Examples"

    ```applescript
    emote url of event-emote
    emote image of reaction "<:disky:825811394963177533>" #(1)!
    ```

    1. See the [emojis page](../messages/emojis.md) for more information about emojis.

=== "Patterns"

    ```applescript
    [the] [the] emo(te|ji) (ur(i|l)|image [url]) of %emote%
    %emote%'[s] [the] emo(te|ji) (ur(i|l)|image [url])
    ```

## Channel of Scheduled Event

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('audiochannel') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('user') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('date') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('date') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.8.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('emote') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('boolean') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guild') ]]]

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

## AFK Channel of Guild

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('voicechannel') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_afk} to afk channel of event-guild
    set afk channel of event-guild to voice channel with id "AFK"
    ```
=== "Patterns"

    ```applescript
    [the] [discord] afk [voice( |-)] channel of %guild%
    %guild%'[s] [discord] afk [voice( |-)] channel
    ```

## AFK Timeout of Guild

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_timeout} to afk timeout of event-guild
    set afk timeout of event-guild to 300
    ```
=== "Patterns"

    ```applescript
    [the] [discord] afk time[( |-)]out [second[s]] of %guild%
    %guild%'[s] [discord] afk time[( |-)]out [second[s]]
    ```

## Banner of Guild

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_banner} to banner of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [discord] banner of %guild%
    %guild%'[s] [discord] banner
    ```

## Guild Boost Count

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('role') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('role') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]
[[[ macros.accept_type('string') ]]]

Represent the verification level of the guild. It can either be:
- None
- Low
- Medium
- High
- Very High

=== "Examples"

    ```applescript
    reply with verification level of event-guild

    set verification level of event-guild to "Low" #(1)!
    reset verification level of event-guild #(2)!
    ```

    1. Requires **DiSky v4.20.0**
    2. Requires **DiSky v4.20.0**

=== "Patterns"

    ```applescript
    [the] [guild] verification level[s] of %guild%
    %guild%'[s] [guild] verification level[s]
    ```

## Invite Code

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('user') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Simple way to get the effective name of a member in a guild:
If the nickname is not set, it will return the [discord name of the member](#name-of-discord-entity).

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('date') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Represent the member nickname. Can be none if the member doesn't have any nickname currently.
Use [effective name](#member-effective-name) expression to get member's name of its nickname is not set.

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

## Voice Channel of Member

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('audiochannel') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_channel} to voice channel of event-member
    ```
=== "Patterns"

    ```applescript
    [the] [member] (voice|audio) channel of %member%
    %member%'[s] [member] (voice|audio) channel
    ```

## Mention Tag

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('user') ]]]

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

## Message/Webhook Channel

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('textchannel') ]]]

Get the text channel were the message was sent. Can be null if it's in PM or not in guild!

Starting DiSky v4.15.0, this can also be used to get the channel of a [webhook](../messages/webhooks.md#manage-webhooks).

=== "Examples"

    ```applescript
    channel of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [(message|webhook)] [text]( |-)channel of %message/webhook%
    %message/webhook%'[s] [discord] [(message|webhook)] [text]( |-)channel
    ```

## Message Content

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('guild') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('member') ]]]

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

## Reference Message

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('message') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_message} to discord message referencing message of event-message
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [message] referenc(ing|ed) message of %message%
    %message%'[s] [discord] [message] referenc(ing|ed) message
    ```

## Profile Banner

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]
[[[ macros.accept_type('string') ]]]

Get the profile banner URL. If the user doesn't have a custom banner, this will return none.
Use the 'profile color' expression to get the color instead of the banner URL in that case!

!!! info "This property accepts __string__, and will change the banner of a **bot** only."

=== "Examples"

    ```applescript
    retrieve profile with id "329999814546817024" from event-user and store it in {_m}
    set {_banner} to profile banner url of {_m}

    set profile banner of event-bot to "<file path or URL>"
    ```
=== "Patterns"

    ```applescript
    [the] profile banner [ur(l|i)] of %userprofile%
    %userprofile%'[s] profile banner [ur(l|i)]
    ```

## Profile Color

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('color') ]]]

Get the profile color accent. If the user have a custom banner, this will return none.
Use the 'profile banner' expression to get the avatar URL instead of the color accent in that case!
=== "Examples"

    ```applescript
    retrieve profile with id "329999814546817024" from event-user and store it in {_m}
    set {_color} to profile color of {_m}
    ```
=== "Patterns"

    ```applescript
    [the] profile color [accent] of %userprofile%
    %userprofile%'[s] profile color [accent]
    ```

## Role Color

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('color') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new role action in event-guild
    set role color of {_action} to orange

    set {_color} to role color of role with id "000"
    ```
=== "Patterns"

    ```applescript
    [the] role color of %role/roleaction%
    %role/roleaction%'[s] role color
    ```

## Role Name

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_action} to new role action in event-guild
    set role name of {_action} to "Member"
    ```
=== "Patterns"

    ```applescript
    [the] role name of %role/roleaction%
    %role/roleaction%'[s] role name
    ```

## Channel/Role Position

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('number') ]]]
[[[ macros.accept_type('number') ]]]

Get or change the relative position of a channel (within its category) or role (among all roles). This is also supported by [role actions](#new-role-action) and [channel actions](#new-text-channel-action)!

!!! warning "Position Conflicts"
    If you try to set a position that is already taken, they will be **sorted** by their **creation date**!

=== "Examples"

    ```applescript
    discord command moveup:
        prefixes: ?
        trigger:
            remove 1 from channel position of event-channel # remove will move the channel up
    ```

=== "Patterns"

    ```applescript
    [the] [(role|channel)] position of %role/roleaction/channel/channelaction%
    %role/roleaction/channel/channelaction%'[s] [(role|channel)] position
    ```

!!! example ""

    - `add` (will increase the position)
    - `remove` (will decrease the position)
    - `set` (will set the position to the given number)

## Tag Emoji

[[[ macros.required_version('4.4.4') ]]]
[[[ macros.return_type('emote') ]]]

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

## User Discriminator (Deprecated)

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Text content of a message builder
See also: 'Create (rich) Message'
=== "Examples"

    ```applescript
    create a new message and store it in {_msg}:
        set the content of the message to "Hello World!"
    
    reply with {_msg}

    ```
=== "Patterns"

    ```applescript
    [the] content of %messagecreatebuilder%
    %messagecreatebuilder%'[s] content
    ```

## Track Author

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('timespan') ]]]

Return the duration of a specific track
=== "Examples"

    ```applescript
    set {_duration} to duration of last played track
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track duration of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track duration
    ```

## Track Identifier

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('timespan') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

Return the thumbnail URL of a specific track
=== "Examples"

    ```applescript
    set thumbnail of embed to thumbnail of last played track
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track thumbnail of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track thumbnail
    ```

## Title of Track

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

No description provided.
=== "Examples"

    ```applescript
    set {_title} to track title of last played track
    ```
=== "Patterns"

    ```applescript
    [the] [discord] [audio] track title of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track title
    ```

## Track URL

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('string') ]]]

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

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('object') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    [(multiple|list|array)] event-<.+>
    ```

## Automod Alert Message ID

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the alert message id sent to the alert channel.. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_alertmessageid} to alert message id of event-automod
    ```
=== "Patterns"

    ```applescript
    alert message id
    ```

## Automod Alert Rule ID

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the id of the AutoMod Rule which has been triggered. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_ruleid} to rule id of event-automod
    ```
=== "Patterns"

    ```applescript
    rule id
    ```

## Automod Moderated User

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('user') ]]]

Returns the moderated user that triggered the automod. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_moderateduser} to moderated user of event-automod
    ```
=== "Patterns"

    ```applescript
    moderated user
    ```

## Automod Message Content

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the message content that triggered the automod. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_messagecontent} to message content of event-automod
    ```
=== "Patterns"

    ```applescript
    message content
    ```

## Automod Matched Content

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the substring match of the message content which triggered this rule. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_matchedcontent} to matched content of event-automod
    ```
=== "Patterns"

    ```applescript
    matched content
    ```

## Automod Matched Keyword

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the keyword that was found in the message content. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_matchedkeyword} to matched keyword of event-automod
    ```
=== "Patterns"

    ```applescript
    matched keyword
    ```

## Automod Response

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the automod response that has been triggered by this event. This can only be used inside the automod execution event!

=== "Examples"

    ```applescript
    set {_automodresponse} to automod response of event-automod
    ```
=== "Patterns"

    ```applescript
    automod response
    ```

## Automod Action Type

[[[ macros.required_version('4.22.0') ]]]
[[[ macros.return_type('string') ]]]

Returns the action type of the automod. This can only be used inside the automod execution event! [Click here to see the automod trigger action types.](https://disky.me/docs/guild/automod/#triggers)

=== "Examples"

    ```applescript
    set {_automodaction} to automod action of event-automod
    ```
=== "Patterns"

    ```applescript
    automod action [type]
    ```