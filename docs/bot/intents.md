---
icon: material/key-chain
---

# Gateway Intents

It can be a weird terms, right? You've maybe heard of it before, but what does it mean? What does it do? How do I use it? Well, let's get into it!

## What are Gateway Intents?

Gateway Intents are a way to tell Discord what __events__ and __data__ you want to receive from them. This is useful for bots that don't need to receive all the data, and can help reduce the amount of data that is sent to your bot.

For instance, a specific `message content` intent is required to get any message's content, while `guild moderation` intent is required for any moderation action (such as ban, kick, getting logs, etc...)!

## Privileged Intents

Some intents are considered "privileged", which means that you need to enable them in your bot's application page. You can do this by going to your [application page](https://discord.com/developers/applications), selecting your bot, and going to the "Bot" tab. There, you can enable the intents you want to use.

They will be marked in the following intent list.

## Information per Intent

### Guild Members (`guild members`)

!!! warning ""
    This intent is [privileged](#privileged-intents).

Events which inform us about member update/leave/join of a guild.
This is required to chunk all members of a guild.
This will also update user information such as name/avatar.


### Message Content (`message content`)

!!! warning ""
    This intent is [privileged](#privileged-intents).

Access to message content.

This specifically affects messages received through the message history of a channel, or through Message Events. The content restriction does not apply if the message mentions the bot directly (using @username), sent by the bot itself, or if the message is a direct message from a PrivateChannel. Affected syntaxes are:

* [`content of %message%`](../docs/expressions.md#message-content)
* [`embeds of %message%`](../docs/expressions.md#message-embeds)
* [`components of %message%`](../docs/expressions.md#message-builder-component-rows)

### Guild Presences (`guild presences`)

!!! warning ""
    This intent is [privileged](#privileged-intents).

This is used to lazy load members and update user properties such as name/avatar.
!!! danger
    **This is a very heavy intent!** Presence updates are 99% of traffic the bot will receive. To get user update events you should consider using [`guild members`](#guild-members-guild-members) instead.

### Message Polls

This intent is used to get poll events from messages. There's two version for the guild & direct message polls:

* `guild message polls` to get poll events from guild messages.
* `direct message polls` to get poll events from direct messages.

!!! example "Related Events"
    * [On Poll Vote Add](../docs/events.md#on-poll-vote-add)
    * [On Poll Vote Remove](../docs/events.md#on-poll-vote-remove)

---

## Less Important Intents

### Guild Moderation (`guild moderation`)

Moderation events, such as ban/unban/audit-log.

### Guild Emojis and Stickers (`guild emojis and stickers`)

Custom emoji and sticker add/update/delete events.

### Guild Webhooks (`guild webhooks`)

Webhook add/update/delete events.

### Guild Invites (`guild invites`)

Invite add/update/delete events.

### Guild Voice States (`guild voice states`)

Voice state events. This is used to determine which members are connected to a voice channel.

### Guild Messages (`guild messages`)

Message events from text channels in guilds.

### Guild Message Reactions (`guild message reactions`)

Reaction add/update/delete events from text channels in guilds.

### Guild Message Typing (`guild message typing`)

Typing events from text channels in guilds.

### Direct Messages (`direct messages`)

Message events from direct/private messages.

### Direct Message Reactions (`direct message reactions`)

Reaction add/update/delete events from direct/private messages.

### Direct Message Typing (`direct message typing`)

Typing events from direct/private messages.

### Scheduled Events (`scheduled events`)

Scheduled Events events.