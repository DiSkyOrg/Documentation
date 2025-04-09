---
icon: material/texture-box
---

# Types

[[[% import 'macros.html' as macros %]]]

This page will explain the different types available on DiSky, and some specification about them.

## General

### `bot`

Represent a **DiSky** bot, which is a bot that is **connected to Discord**. It holds information like the token, the shard manager, and the cache.

### `user`

The **User** type represent a Discord account, or a bot account. There's only one "user instance", meaning each user are uniques across all guilds. Due to obvious reasons, we cannot cache all users, thus you'll have to [retrieve](../docs/effects.md#retrieve-user) them.

### `member`

The **Member** type represent a Discord account that is in a guild. It holds more information than a user, like the roles, nickname, and the guild it's in. It's unique for each guild, meaning a user can have multiple member instances.

### `guild`

The **Guild** type represent a Discord server. It holds information like the name, icon, owner, and the members.

### `message`

The **Message** type represent a message sent in a channel. It holds information like the content, the author, and the channel it was sent in. It can also hold attachments, embeds, and reactions.

Most actions about a message may only be done by its owner (e.g. edit), but some actions can be done by anyone (e.g. delete).

### `invite`

Represent a Discord invitation to a guild. It always points to a channel (that is of course in the guild), and can have a limited number of uses, and an expiration date.

??? example "Related Syntax"
    |                    Expressions                    |                     Effects                     |                         Events                          |
    |:-------------------------------------------------:|:-----------------------------------------------:|:-------------------------------------------------------:|
    |     [Invite Code](expressions.md#invite-code)     |    [Create Invite](effects.md#create-invite)    | [Invite Create Event](events.md#on-invite-create-event) |
    |  [Invite Inviter](expressions.md#invite-inviter)  |  [Retrieve Invite](effects.md#retrieve-invite)  | [Invite Delete Event](events.md#on-invite-delete-event) |
    |  [Invite Max Age](expressions.md#invite-max-age)  | [Retrieve Invites](effects.md#retrieve-invites) |                                                         |
    | [Invite Max Uses](expressions.md#invite-max-uses) |                                                 |                                                         |
    |      [Invite URL](expressions.md#invite-url)      |                                                 |                                                         |

## Channels

### `channel`

The **Channel** type is the base type for all channels, and is used to represent a channel in Discord. For instance, it can be a voice or text channel from a guild, or a private channel.

### `messagechannel`

The **MessageChannel** type is the base type for all channels that can hold messages or files. For instance, it can be a text channel, or a private channel.

### `guildchannel`

The **GuildChannel** type is the base type for all channels that are in a guild, and is used to represent a channel in Discord.

!!! info
    Don't forget that, for Discord, a **category** is a channel too! Therefore, a category is a **GuildChannel**.

### `audiochannel`

The **AudioChannel** type is the base type for all channels that are in a guild and can be used to play audio. For instance, it can be a voice channel, or a stage channel. It can't be a text channel.

### `textchannel`

The **TextChannel** is a concrete type that represents a text channel in Discord. It holds several messages, and can be used to send messages. They have a topic, slow mode, and can be marked as NSFW.

### `voicechannel`

The **VoiceChannel** is a concrete type that represents a voice channel in Discord. It can be used to play audio, and can have a bitrate, user limit, and a region. People can join and leave the channel, and it can be used to move people from one channel to another.

### `stagechannel`

The **StageChannel** is a concrete type that represents a stage channel in Discord.  It can be used to play audio, and can have a bitrate, user limit, and a region. People can join and leave the channel, and it can be used to move people from one channel to another.

### `newschannel`

The **NewsChannel** is a concrete type that represents a news channel in Discord. It can be used to send messages, and can have a topic, slow mode, and can be marked as NSFW. It can also be followed by other channels.

### `threadchannel`

The **ThreadChannel** is a concrete type that represents a thread channel in Discord. It can be used to send messages, and can have a topic, slow mode, and can be marked as NSFW. It can also be archived or unarchived.

### `forumchannel`

The **ForumChannel** is a concrete type that represents a forum channel in Discord. It can be used to send messages, and can have a topic, slow mode, and can be marked as NSFW. It can also be archived or unarchived.

### `category`

The **Category** is a concrete type that represents a category in Discord. It can be used to organize channels, and can have a name, position, and a topic. One category can hold several channels, and one channel can only be in one category or none.

### `privatechannel`

The **PrivateChannel** type is the base type for all channels that are private, and is used to represent a channel in Discord. For instance, it can be a private text channel, or a private voice channel.

### `memberflag`

This type is used to represent a flag of a member. This was introduced in Discord recently, therefore old members may not have any flag.

You can check the [member flags expression](expressions.md#member-flags) for getting/adding flags to a member. **Some flags cannot be added manually!**

=== "`did rejoin`"
    The Member has left and rejoined the guild

    !!! warning "This flag **is not** modifiable"
=== "`complete onboarding`"
    The Member has completed the onboarding process
    
    !!! warning "This flag **is not** modifiable"
=== "`bypasses verification`"
    The Member has bypassed the verification step
    
    !!! success "This flag **is** modifiable"
=== "`started onboarding`"
    The Member has started the onboarding process

    !!! warning "This flag **is not** modifiable"