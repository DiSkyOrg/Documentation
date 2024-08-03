---
icon: material/stop-circle-outline
---

# Error Handling

Since DiSky v4.18.0, a basic try/catch system has been implemented. For those who don't know what it is, it's a way to catch errors that can occur in your code and handle them in a specific way.

This can especially be useful when, for instance, you're trying to send a DM to someone who has their DMs disabled: 
you can catch the error and handle it in a way that makes sense for your user.

## How to use it?

You need to wrap your code in a `try` block and then catch the error in a `catch` block,
also giving a variable where the exception will be stored in.

Here's an example:

```applescript
# ... {_channel} is the DM channel of a user

try:
    post "Hello, I'm a bot!" to {_channel}
catch {_error}:
    reply with "Oh no, I wasn't able to send a DM to you! Error: `%{_error}%`"
    stop #(1)!
```

1. Keep in mind code after a "catch" section **will always run by default;** it's your job to stop if you desire.

!!! tips "Local variables are shared between all those sections!"

## What can I catch?

Because this is a relatively new feature, only some features can be caught. Here's a non-exhaustive list of what can be caught:

- Posting an invalid message / to an invalid channel
- Changing the Icon of a guild/bot/user with an invalid URL/file path
- Invalid message content/components in reply/post effect
- Giving the wrong webhooks name in any webhook syntax