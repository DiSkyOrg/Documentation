---
icon: material/developer-board
---

# Slash Structure

!!! warning
    This feature is still in **beta**, meaning a lot of bugs can be expected. If you find any, please report them to our [GitHub](https://github.com/DiSkyOrg/DiSky)!

    We highly recommend turning on **debug mode** (in DiSky's configuration) to see more details about the errors you may encounter!

DiSky v4.19 introduces a brand-new way to create, register and handle slash commands, in an all-in-one way! It utilizes the new Skript structure system to make it easier to create and manage your slash commands.

!!! danger ""
    * The 'old' way to create slash commands (registering commands in `on ready` and using `on slash command` events) are sort of deprecated (although they won't be removed, they are not compatible with this new system).
    * This system is still in **beta**, meaning a lot of bugs can be expected. If you find any, please report them to our [GitHub](https://github.com/DiSkyOrg/DiSky)!
    * Skript 2.10+ is required to use this system.

## Core Structure

!!! info "If you're not familiar with Skript structures, read [this tutorial](https://sovdee.gitbook.io/skript-tutorials/readme/syntax-overview#structures)"

The core structure of a slash command is the following:

```applescript
slash command {name} {arguments}:
    # Entries (see below)
```

You have two things to replace here:

### `{name}`

This is the name of your slash command. It must be unique and can only contain alphanumeric characters. Do not include the `/` prefix. The name can have up to three parts to create command groups and subcommands (see Command Groups section below).

### `{arguments}`

This is the list of arguments your slash command will have. It works the same as Skript's command arguments, but only a few **types** are supported:

| Type         | Description                                           | Support Choices            |
|--------------|-------------------------------------------------------|:-------------------------:|
| `string`     | A simple text argument                                | :material-check-bold:     |
| `integer`    | An integer argument (`1`, `2`, `3`, ...)             | :material-check-bold:     |
| `number`     | A number argument (`6`, `3.14`, ...)                 | :material-check-bold:     |
| `user`       | A Discord user argument                              | :material-close-thick:    |
| `channel`    | A Discord channel argument (also includes categories) | :material-close-thick:    |
| `role`       | A Discord role argument                              | :material-close-thick:    |
| `boolean`    | A boolean argument (`true` or `false`)               | :material-close-thick:    |
| `attachment` | A file attachment argument                           | :material-close-thick:    |

An argument format is `<type="name">`, and can be surrounded by `[]` to make it optional.

## Command Groups and Subcommands

DiSky supports organizing commands into groups and subcommands using a space-separated naming convention. You can create up to three levels of command hierarchy:

1. Base Command
2. Subcommand Group (optional)
3. Subcommand

### Basic Subcommands

To create a subcommand, use a space in the command name:

```applescript
slash command profile view [<user="target">]:
    description: View a user's profile
    bot: my_bot
    
    arguments:
        target: The user whose profile you want to view
    
    trigger:
        reply with "Viewing profile of %arg-1%"

slash command profile edit:
    description: Edit your profile
    bot: my_bot

    trigger:
        reply with "Editing your profile..."
```

This creates two subcommands under the `profile` command:
- `/profile view [user]`
- `/profile edit`

### Subcommand Groups

You can organize related subcommands into groups using a three-part name:

```applescript
slash command settings roles add <role="role">:
    description: Add a role
    bot: my_bot
    
    arguments:
        role: The role to add
    
    trigger:
        reply with "Adding role..."

slash command settings roles remove <role="role">:
    description: Remove a role
    bot: my_bot
    
    arguments:
        role: The role to remove
    
    trigger:
        reply with "Removing role..."

slash command settings prefix set <string="new_prefix">:
    description: Set the server prefix
    bot: my_bot
    
    arguments:
        new_prefix: The new prefix
    
    trigger:
        reply with "Setting prefix to %arg-1%"
```

This creates:
- A `settings` base command
- Two subcommand groups: `roles` and `prefix`
- Subcommands under these groups:
  - `/settings roles add <role>`
  - `/settings roles remove <role>`
  - `/settings prefix set <text>`

### Important Notes

1. Command names at all levels must:
   - Start with a letter
   - Contain only letters, numbers, underscores, and hyphens
   - Be in English and use ASCII characters only

2. You can have up to:
   - One base command (e.g., `settings`)
   - One subcommand group (e.g., `roles`)
   - One subcommand (e.g., `add`)

3. The order of registration doesn't matter - DiSky will properly group related commands together.

4. Each subcommand can have its own:
   - Description
   - Arguments
   - Permissions
   - Cooldowns
   - Trigger code

## Entries

### Description

If not specified, the description will default to `No description provided.`. It is recommended to provide a description for your command:

=== "Normal"
    ```applescript
    slash command level:
        description: Check your own level
    ```
=== "Using Localizations"
    ```applescript
    slash command level:
        description:
            fr: Vérifiez votre niveau
            en: Check your own level # same as 'en-US'
    ```
    In this case it'll use `Check your own level` for English clients, and `Vérifiez votre niveau` for French clients. Check the list of Discord locales [here](https://discord.com/developers/docs/reference#locales).

### Registration

This will tell DiSky where and how to register your slash command:

* If there's only a `bot` entry, it'll register **globally**.
* If there's also a `guild` entry, it'll register **per-guild** (with the specified bot)

!!! example
    === "Global"
        ```applescript
        slash command level:
            description: Check your own level
    
            bot: my_bot
        ```
    
    === "Local"
        ```applescript
        slash command level:
            description: Check your own level
    
            bot: my_bot
            guilds: 937001799896956988 # those are guild IDs
        ```

### Execution

This is where you put the code that will be executed when the command is called:

```applescript
slash command level:
    description: Check your own level

    bot: my_bot

    trigger:
        # Your code here. It's like a 'on slash command' event, meaning you can reply to the interaction and all.
        # You can also uses the argument system, such as `arg-1` for the first argument, `arg-2` for the second, etc.
        reply with hidden "You're level XXX!"
```

### Arguments

Although we defined the argument's type (and name) in the command's structure, we can add more details about them, such as the argument's description and choices. This entry takes argument's names as keys:

#### Description

```applescript
slash command level [<user="target">]:
    description: Check your level

    arguments:
        target: #(1)!
            description: The user to check the level of
```

1. If you only provide a description, you can directly write it after the argument's name, like this:

    ```applescript
    slash command level [<user="target">]:
        description: Check your level
   
        guilds: 937001799896956988
        bot: disky

        arguments:
            target: The user to check the level of
   
        trigger:
            reply with "Checking %mention tag of arg-1%'s level..."
    ```

#### Choices

Choices are a way to limit the user's input to a list of predefined values. They are only available for `string`, `integer` and `number` arguments.

```applescript
slash command set_level <user="target"> [<integer="level">]:
    description: Change someone's level
    
    guilds: 937001799896956988
    bot: disky

    arguments:
        target: The user to change the level of
        level:
            description: The new level
            choices:
                # <name on Discord> : <value in Skript>
                Level 1: 1
                Level 2: 2
                Level 3: 3
    
    trigger:
        reply with "Changed %mention tag of arg-1%'s level to %arg-2%"
```

In this example, the `level` argument will only accept `Level 1`, `Level 2` or `Level 3`, and `arg-2` will be replaced by the corresponding value (`1`, `2` or `3`).

#### Auto Completion

If you want to provide auto-completion for your arguments, you can use the `on completion request` entry. The provided code will be run when the user is typing the argument's value.

```applescript
slash command set_level <user="target"> [<integer="level">]:
    description: Change someone's level
    
    guilds: 937001799896956988
    bot: disky

    arguments:
        target: The user to change the level of
        level:
            description: The new level
            
            on completion request:
                loop 5 times:
                    add new choice "Level %loop-value%" with value loop-value to {_c::*}
                return {_c::*}
    
    trigger:
        reply with "Changed %mention tag of arg-1%'s level to %arg-2%"
```

!!! warning "You cannot mix `choices` and `on completion request`, as one argument cannot have both."

### Permissions

You can restrict who can use your command by using the `enabled for` entry. It takes a list of permissions, and will only allow users with one of these permissions to use the command. In addition, you can set `true` to the `disabled` entry to disable the command to everyone except admins:

```applescript
slash command level:
    description: Check your own level

    bot: my_bot

    enabled for: manage server, administrator
    
    trigger:
        reply with hidden "You're level XXX!"
```

### Cooldown System

DiSky offers a built-in cooldown system for slash commands. Cooldowns are per-user, and specific code can be run when the user is on cooldown.

```applescript
slash command level:
    description: Check your own level

    bot: my_bot

    cooldown: 1 minute
    on cooldown:
        if discord id of event-user is "XXX":
            cancel event #(1)!
            stop
            
        reply with "You still have to wait %remaining time% before using this command again!"

    trigger:
        reply with hidden "You're level XXX!"
```

1. The `on cooldown` section runs the same as a slash command event and can be used to let specific users bypass the cooldown. Simply use `cancel event` to let the command execute normally!