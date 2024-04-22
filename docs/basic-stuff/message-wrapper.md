# ✉️ Message Wrapper

## ⚠️ Disclaimer

!!! warning
    This system is here to helps you **cache** messages, in order to keep infos about deleted & edited messages. This **is not** provided by Discord and everything is self-handled by DiSky.

    Even with all correct settings, __**some factors can make this system not working**__! (like Discord API issues, or cache issues, etc...)

    Please, do not reports issues about this system, unless you are sure that you have all correct settings and that you have waited enough time for the cache to be filled.

## How it works

For both edited & deleted cache, DiSky will cache **received** messages in memory. That mean any messages that were not cached (aka not sent while the bot was running) won't have any info stored!

### Edited Messages

DiSky will update the cached previous/current message text when a message is edited. This will allow you to get the previous message content, and the new one.

The message itself still exists on Discord, so only the message's content is updated and cached.

!!! success "Usage"
    In the [`on message edit`](../docs/events.md#on-message-edit) event, you can use the `event-string` expression to get the old message content. `event-message` is also available, and will contain the current/new content.

    ```applescript
    on message edit:
        reply with "Message edited! From `%event-string%` to `%event-message%`!"
    ```

### Deleted Messages

DiSky will do its best to **recreate** a whole **fake** message object, with all the infos it can get from the previously-cached message.

This will allow you to get the message's content, the author, the channel, the attachments, etc... basically, all information of an actual message.

!!! warning "This is not a real message!"
    This is a fake message, so you won't be able to destroy, reference, etc... it with DiSky. It'll always lead to a `10008: Unknown Message` error!

!!! success "Usage"
    In the [`on message delete`](../docs/events.md#on-message-delete) event, you can use the `event-message` expression to get the deleted message object.

    ```applescript
    on message delete:
        reply with "Message deleted! Content: `%event-message%`" #(1)!
    ```

    1. For instance, if you try to do `destroy event-message`, it'll lead to a `10008: Unknown Message` error.

## Why this system?

Discord doesn't provide any way to get deleted/edited messages, so this system is here to help you to get these messages.