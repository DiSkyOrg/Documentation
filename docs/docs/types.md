---
icon: material/check-all
---

# Types

[[[% import 'macros.html' as macros %]]]

This page will explain the different types available on DiSky, and some specification about them.

## Channels

### `channel`

The **Channel** type is the base type for all channels, and is used to represent a channel in Discord. For instance, it can be a voice or text channel from a guild, or a private channel.

### `guildchannel` (extends [`channel`](#channel))

The **GuildChannel** type is the base type for all channels that are in a guild, and is used to represent a channel in Discord.

!!! info
    Don't forget that, for Discord, a **category** is a channel too! Therefore, a category is a **GuildChannel**.

### `audiochannel` (extends [`guildchannel`](#guildchannel-extends-channel))

The **AudioChannel** type is the base type for all channels that are in a guild and can be used to play audio. For instance, it can be a voice channel, or a stage channel. It can't be a text channel.

### `textchannel` (extends [`guildchannel`](#guildchannel-extends-channel))

The **TextChannel** is a concrete type that represents a text channel in Discord. It holds several messages, and can be used to send messages. They have a topic, slow mode, and can be marked as NSFW.

### `voicechannel` (extends [`guildchannel`](#guildchannel-extends-channel))

The **VoiceChannel** is a concrete type that represents a voice channel in Discord. It can be used to play audio, and can have a bitrate, user limit, and a region. People can join and leave the channel, and it can be used to move people from one channel to another.

### `stagechannel` (extends [`guildchannel`](#guildchannel-extends-channel))

The **StageChannel** is a concrete type that represents a stage channel in Discord.  It can be used to play audio, and can have a bitrate, user limit, and a region. People can join and leave the channel, and it can be used to move people from one channel to another.

### `category` (extends [`guildchannel`](#guildchannel-extends-channel))

The **Category** is a concrete type that represents a category in Discord. It can be used to organize channels, and can have a name, position, and a topic. One category can hold several channels, and one channel can only be in one category or none.

### `privatechannel` (extends [`channel`](#channel))

The **PrivateChannel** type is the base type for all channels that are private, and is used to represent a channel in Discord. For instance, it can be a private text channel, or a private voice channel.

### `memberflag`

This type is used to represent a flag of a member. This was introduced in Discord recently, therefore old members may not have any flag.

You can check the [member flags expression](expressions.md#) for getting/adding flags to a member. **Some flags cannot be added manually!**

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