---
icon: material/package-check
---

# Member Cache Policy & Flags

When [defining a bot](../getting-started/2-bot-loading.md#bot-loading), you can specify the way you want to cache members, and what you cache about them.

## Member Cache Policy

This will define how the bot will handle members cache itself, for instance what member can be get using [member getter](../docs/expressions.md#get-member) instead of being [retrieved](../docs/effects.md#retrievemember)

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

| Code name          | Description                                     |                                                                [Required Intents](../bot/intents.md) |
|--------------------|-------------------------------------------------|-----------------------------------------------------------------------------------------------------:|
| `activity`         | Enables cache for member activities             |                               [`guild presences`](../bot/intents.md#guild-presences-guild-presences) |
| `voice state`      | Enables cache for member voice states           |                      [`guild voice states`](../bot/intents.md#guild-voice-states-guild-voice-states) |
| `emoji`            | Enables cache for guild's emojis                | [`guild emojis and stickers`](../bot/intents.md#guild-emojis-and-stickers-guild-emojis-and-stickers) |
| `sticker`          | Enables cache for guild's stickers              | [`guild emojis and stickers`](../bot/intents.md#guild-emojis-and-stickers-guild-emojis-and-stickers) |
| `client status`    | Enables cache for member (online) client status |                               [`guild presences`](../bot/intents.md#guild-presences-guild-presences) |
| `scheduled events` | Enables cache for scheduled events              |                            [`scheduled events`](../bot/intents.md#scheduled-events-scheduled-events) |