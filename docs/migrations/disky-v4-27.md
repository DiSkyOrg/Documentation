---
icon: material/package-up
status: new
---

# DiSky v4.26 -> v4.27

DiSky v4.27.0 introduces new features and improvements for thread management, server tags, and slash command structures. This migration guide will help you update your DiSky scripts to be compatible with the new version.

## New Features

### Thread Owner and Message Count

You can now retrieve the owner of a thread channel and get the total message count of a thread. These expressions work with thread channels, including forum posts.

```applescript
# Get the owner of a thread
set {_owner} to owner of {_thread}
set {_owner} to thread owner of {_threadChannel}

# Get the message count of a thread
set {_count} to message count of {_thread}
set {_msgCount} to thread message count of {_threadChannel}
```

**Use Cases:**
- Check who created a forum post
- Display thread statistics in embeds
- Moderate threads based on their creator
- Track activity in forum channels

**Example - Forum Post Information:**
```applescript
on thread create:
    set {_owner} to owner of event-threadchannel
    set {_count} to message count of event-threadchannel

    send "New post created by %discord name of {_owner}% with %{_count}% message(s)" to channel with id "logs-channel-id"
```

### Member Equipped Server Tag

Added support for retrieving a member's equipped server tag (also called "primary guild tag"). This feature allows you to access the tag that a user has chosen to display on their profile for a specific server.

```applescript
# Get the equipped server tag of a user
set {_tag} to user tag of {_user}
set {_tag} to user primary guild tag of {_member}

# Get the tag icon URL
set {_icon} to user tag icon of {_user}
set {_iconUrl} to user primary guild tag icon url of {_user}
```

!!! info "Server Tags"
    Server tags are a Discord feature that allows users to choose a tag representing their identity or role in a server. The "equipped" tag is the one displayed on their profile.

**Example - Display User Tag:**
```applescript
discord command profile [<user>]:
    prefixes: !
    trigger:
        set {_user} to arg-1 ? event-user
        set {_tag} to user tag of {_user}

        if {_tag} is set:
            set {_icon} to user tag icon url of {_user}
            make embed:
                set title of embed to "%discord name of {_user}%'s Profile"
                set description of embed to "Equipped Tag: %discord name of {_tag}%"
                set thumbnail of embed to {_icon} if {_icon} is set
            reply with last embed
        else:
            reply with ":x: This user has no equipped server tag."
```

### Hyphen Support in Slash Structure Arguments

You can now use hyphens (`-`) in slash structure argument names. Previously, this would cause parsing errors.

**Before v4.27:**
```applescript
# This would cause an error
local slash command "test":
    set description of command to "Test command"
    add "user-name" as text argument named "name" to arguments of command  # ❌ Error!
```

**Since v4.27:**
```applescript
# Now this works perfectly
local slash command "test":
    set description of command to "Test command"
    add "user-name" as text argument named "name" to arguments of command  # ✅ Works!
    add "max-count" as integer argument named "count" to arguments of command  # ✅ Works!
```

!!! success "Improved Readability"
    This enhancement allows for more readable argument names that follow Discord's naming conventions, especially when you want to separate words without using underscores or camelCase.

**Example - Better Argument Names:**
```applescript
local slash command "user-info":
    set description of command to "Get information about a user"
    add "target-user" as user argument named "user" to arguments of command
    add "show-avatar" as boolean argument named "avatar" to arguments of command
    add "include-roles" as boolean argument named "roles" to arguments of command
    register command

on slash command:
    if event-string is "user-info":
        set {_user} to argument "user" as user
        set {_showAvatar} to argument "avatar" as boolean
        set {_includeRoles} to argument "roles" as boolean

        # Process command...
```

## Summary

Version 4.27.0 focuses on quality-of-life improvements:

- **Thread Management**: New expressions for thread owner and message count
- **Server Tags**: Access to equipped server tags for users
- **Better Slash Commands**: Hyphen support in argument names for clearer naming

All these features are non-breaking and can be adopted gradually in your existing code.
