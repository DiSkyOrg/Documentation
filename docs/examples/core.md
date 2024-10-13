---
icon: material/record-circle
---

# Core 

## Basic Bot Definition

```applescript
define new bot named "MyBot":
    token: "YOUR_BOT_TOKEN_HERE"
    intents: default intents
    policy: all
    auto reconnect: true
    compress: none
```

## Bot with All Optional Sub-triggers

```applescript
define new bot named "AdvancedBot":
    token: "YOUR_BOT_TOKEN_HERE"
    intents: default intents, message content
    policy: all
    auto reconnect: true
    compress: none

    on ready:
        send "%event-bot% is now online and ready!" to console
        set presence of event-bot to watching "for commands"

    on guild ready:
        set {_guild} to event-guild
        send "%{_guild}% (ID: %discord id of {_guild}%) is now loaded!" to console
        post "Hello, I'm now ready to serve this guild!" to first elements of (guild channels of {_guild})

    on shutdown:
        send "%event-bot% is shutting down. Goodbye!" to console
```

## Bot with Specific Intents and Cache Policy

```applescript
define new bot named "CustomBot":
    token: "YOUR_BOT_TOKEN_HERE"
    intents: guild members, guild messages, guild voice states
    policy: none
    cache flags: member cache policy voice
    auto reconnect: true
    compress: none

    on ready:
        send "CustomBot is online with specific intents and cache policy!" to console

    on guild ready:
        set {_guild} to event-guild
        set {_member_count} to size of discord members of {_guild}
        send "%{_guild}% is ready with %{_member_count}% cached members!" to console
```

## Bot with Global Slash Command Registration

```applescript
define new bot named "SlashBot":
    token: "YOUR_BOT_TOKEN_HERE"
    intents: default intents
    policy: all
    auto reconnect: true
    compress: none

    on ready:
        send "SlashBot is online and registering commands!" to console

        set {_cmd} to new slash command named "hello" with description "Say hello to the bot"
        update {_cmd} globally in event-bot
```