---
icon: material/package-up
status: new
---

# DiSky v4.25 -> v4.26

DiSky v4.26.0 introduces new features, bug fixes, and improvements to message editing and embed handling. This migration guide will help you update your DiSky scripts to be compatible with the new version.

## Breaking Changes

### Edit Message Effect - New Replacement Mode

The `edit message` effect has been enhanced to allow you to specify whether to replace the entire message or just update specific parts.

#### Before 4.26:

```applescript
# Editing a message would replace everything
edit message {_msg} to show "New content"
# This would remove any existing embeds, components, etc.
```

#### Since 4.26:

```applescript
# Default behavior - partial update (keeps unchanged elements)
edit message {_msg} to show "New content"
# Embeds, components, etc. are preserved

# To replace everything (old behavior)
edit and replace message {_msg} to show "New content"
# This removes embeds, components, etc. that aren't specified
```

!!! warning "Migration Required"
    If your code relied on the old behavior of replacing all message content, you now need to use the `and replace` or `by replacing` modifier.

**New Pattern:**
```applescript
edit [replace:([and] replace|[by] replacing)] [:direct] [the] [message] %message% (with|to show) %string/messagecreatebuilder/embedbuilder/container%
```

## New Features

### Embed Templates

DiSky v4.26.0 brings back the embed templates feature from DiSky v3! You can now register embed templates and reuse them throughout your code.

```applescript
# Register an embed template
register embed "success" with:
    title: "Success!"
    color: green
    
# Use the template
reply with embed template "success"
```

### Better Variable Handling for Discord Objects

Discord objects with IDs (channels, messages, members, roles, etc.) can now be used directly as variable indices, similar to how Skript handles entities.

#### Before 4.26:

```applescript
set {data::%discord id of {_member}%} to "value"
```

#### Since 4.26:

```applescript
set {data::%{_member}%} to "value"
```

This works for any Discord object with an ID, making your code cleaner and more intuitive.

### Embed Fields as Expressions

You can now get and manipulate embed fields as expressions, making it easier to work with existing embeds.

```applescript
set {_fields} to embed fields of {_embed}
```

### Member Boost Time

Added support for checking how long a member has been boosting a server.

```applescript
set {_boostTime} to time boosted of {_member}
```

## Bug Fixes

### Slash Command Registration

Fixed issues with global and guild slash command registration:
- Slash commands now maintain consistent IDs across server restarts
- Guild-specific slash commands load properly without hanging
- Command settings are preserved after restarts
