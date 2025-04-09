---
icon: material/package-check
---

# Member Cache Policy & Cache Flags

When [defining a bot](../getting-started/2-bot-loading.md#bot-loading), you can specify the way you want to cache members, and what you cache about them and other entities.

## Member Cache Policy

This will define how the bot will handle members cache itself, for instance what member can be get using [member getter](../docs/expressions.md#get-member) instead of being [retrieved](../docs/effects.md#retrieve-member)

| Code name | Description                           |                                                                                                      [Required Intents](../bot/intents.md) |
|-----------|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------:|
| `all`     | Cache all members of all guilds       |                                                                           [`guild members`](../bot/intents.md#guild-members-guild-members) |
| `none`    | Cache no members                      |                                                                                                                                       None |
| `owner`   | Cache only the owner of the guild     |                                                                                                                                       None |
| `online`  | Cache only online members             |                                                                     [`guild presences`](../bot/intents.md#guild-presences-guild-presences) |
| `voice`   | Cache only members in a voice channel |                                                                     [`guild presences`](../bot/intents.md#guild-presences-guild-presences) |
| `booster` | Cache only boosters of the guild      |                                                                           [`guild members`](../bot/intents.md#guild-members-guild-members) |
| `default` | Default cache policy                  | [`guild presences`](../bot/intents.md#guild-presences-guild-presences)<br>[`guild members`](../bot/intents.md#guild-members-guild-members) |

## Cache Flags

This will define what you want to cache about members and other entities, for instance if you want to cache their **online status** or not.

### Available Cache Flags

| Flag               | Description                                          | Required Intent                                                                 |
|--------------------|------------------------------------------------------|---------------------------------------------------------------------------------|
| `activity`         | Enables cache for member activities                  | [`guild presences`](../bot/intents.md#guild-presences-guild-presences)          |
| `voice state`      | Enables cache for member voice states                | [`guild voice states`](../bot/intents.md#guild-voice-states-guild-voice-states) |
| `emoji`            | Enables cache for guild's emojis                     | [`guild expressions`](../bot/intents.md#guild-expressions)                      |
| `sticker`          | Enables cache for guild's stickers                   | [`guild expressions`](../bot/intents.md#guild-expressions)                      |
| `client status`    | Enables cache for member (online) client status      | [`guild presences`](../bot/intents.md#guild-presences-guild-presences)          |
| `member overrides` | Enables cache for member permission overrides        | None                                                                            |
| `role tags`        | Enables cache for role tags                          | None                                                                            |
| `forum tags`       | Enables cache for forum tags and thread applied tags | None                                                                            |
| `online status`    | Enables cache for member online status               | [`guild presences`](../bot/intents.md#guild-presences-guild-presences)          |
| `scheduled events` | Enables cache for scheduled events                   | [`scheduled events`](../bot/intents.md#scheduled-events-scheduled-events)       |

### Special Cache Flag Options

DiSky provides several options for configuring multiple cache flags at once:

| Option          | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `all`           | Enables all available cache flags                                           |
| `none`          | Disables all cache flags                                                    |
| `default cache` | Enables the following flags: `activity`, `voice state`, and `online status` |

### Usage Example

```applescript
define new bot named "MyBot": 
    token: "BOT TOKEN"
    intents: default intents, guild expressions, scheduled events
    policy: all
    cache flags: emoji, sticker, scheduled events, forum tags
```

### Important Notes

1. **Intent Requirements**: Some cache flags require specific intents to be enabled. Make sure to include the necessary intents when defining your bot.

2. **Memory Usage**: Each enabled cache flag increases the memory footprint of your bot. Only enable the caches you actually need for your bot's functionality.

3. **Privileged Intents**: Cache flags that require the `guild presences` intent (such as `activity`, `client status`, and `online status`) are considered privileged and require special verification for bots in 100+ servers.