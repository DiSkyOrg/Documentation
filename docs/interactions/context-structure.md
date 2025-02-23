---
icon: material/cursor-default-click
---

# Context Commands

DiSky v4.21.0 introduces a new way to create context menu commands using a structure-based system. Context commands appear when right-clicking on either a user or a message in Discord, allowing for quick actions without typing commands.

## Core Structure

The core structure for a context command follows this pattern:

```applescript
user/message command {name}:
    # Entries (see below)
```

You have two things to specify:
1. The command type (`user` or `message`)
2. The command name (what appears in the context menu)

### Example

```applescript
user command userinfo:
    description: Get information about a user
    bot: my_bot
    
    trigger:
        set {_e} to new embed:
            title: "User Information"
            description: "Information about %target user%"
            color: blue
            
            field:
                name: "Tag"
                value: "%discord name of target user%"
            
            field:
                name: "ID"
                value: "%discord id of target user%"
            
            field:
                name: "Account Created"
                value: "%creation date of target user%"
            
            thumbnail: avatar url of target user
        
        reply with {_e}
```

## Entries

### Bot (Required)
Specifies which bot will register and handle the command:

```applescript
user command avatar:
    bot: my_bot
```

### Guilds (Optional)
Specifies in which guilds the command should be registered. If not specified, the command will be registered globally:

```applescript
message command report:
    bot: my_bot
    guilds: 937001799896956988, 952199041335316520
```

### Name Localizations (Optional)
Allows you to provide different command names for different Discord client languages:

```applescript
user command profile:
    bot: my_bot
    name:
        fr: profil
        es: perfil
        de: profil
```

### Permissions (Optional)
Controls who can use the command using the `enabled for` entry:

```applescript
message command pin:
    bot: my_bot
    enabled for: manage messages
```

You can specify multiple permissions:
```applescript
message command delete:
    bot: my_bot
    enabled for: manage messages, administrator
```

Special values:
- `enabled for: all` - Everyone can use the command (default)
- `enabled for: none` - No one can use the command except administrators

### Trigger (Required)
Contains the code that will be executed when the command is used. You have access to special values depending on the command type:

#### User Commands
- `target user` - The user that was right-clicked
- `event-user` - The user who used the command
- `event-member` - The member who used the command (if in a guild)
- `event-guild` - The guild where the command was used (if in a guild)

```applescript
user command avatar:
    bot: my_bot
    trigger:
        set {_e} to new embed:
            title: "Avatar"
            description: "Avatar of %target user%"
            image: avatar url of target user
            color: blue
        reply with {_e}
```

#### Message Commands
- `target message` - The message that was right-clicked
- `event-user` - The user who used the command
- `event-member` - The member who used the command (if in a guild)
- `event-guild` - The guild where the command was used (if in a guild)

```applescript
message command quote:
    bot: my_bot
    trigger:
        set {_e} to new embed:
            author: discord name of author of target message
            author icon: avatar url of author of target message
            description: content of target message
            color: blue
            footer: "Quoted by %event-user%"
        reply with {_e}
```

!!! note "Additional Notes"
    - Context commands must follow Discord's naming guidelines (32 characters max, alphanumeric with spaces)
    - Each bot can have up to 5 global user commands and 5 global message commands
    - Guild commands have a shared limit of 100 commands per guild (including slash commands)
    - The command name can only contain letters, numbers, and spaces