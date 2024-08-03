---
icon: material/sync
---

# Asynchronous Operations

## What is Asynchronous Operations?

DiSky is designed with native asynchronous functionality, which means that most of its operations are non-blocking and can be executed concurrently. This design ensures that interactions with Discord's API don't impede the Minecraft server's main thread, maintaining smooth gameplay and server performance.

### Caching and API Interactions

DiSky employs a caching mechanism for certain Discord information, such as channel names. This approach allows for quick access to frequently used data without constantly querying Discord's API. As a result, DiSky operations can be categorized into two types:

1. **Cached Operations**: These are instant and don't require API calls. For example, retrieving a channel's name using `discord name` returns the cached value immediately.

2. **API-Dependent Operations**: These require communication with Discord's API. For instance, changing a channel's name with `set discord name of %channel% to "new name"` necessitates an API request.

### Asynchronous Handling of API Requests

When an API-dependent operation is executed, DiSky doesn't block the thread. Instead, it queues the request to be processed asynchronously. This means:

- The code following the API request continues to execute immediately.
- The actual API request is processed in the background.

While this approach ensures server responsiveness, it can lead to some unexpected behaviors. For example, code placed after a `set` operation might execute before the change is reflected on Discord's side.

### Using 'await' for Synchronous Behavior

To manage these asynchronous operations more effectively, DiSky provides an 'await' keyword. When used, it ensures that the code waits for the API operation to complete before moving on to the next instruction. This can be crucial when subsequent code depends on the success or result of an API operation.

Understanding the difference between awaited and non-awaited operations is key to writing efficient and predictable DiSky scripts.

## TL;DR

=== "Without `await`"
    ```mermaid
    sequenceDiagram
        participant M as Minecraft
        participant D as DiSky
        participant A as Discord API
        
        M->>D: Set channel name
        D-->>M: Queue request
        M->>M: Continue execution
        D->>A: Send API request
        A-->>D: Response (later)
    ```

=== "With `await`"
    ```mermaid
    sequenceDiagram
        participant M as Minecraft
        participant D as DiSky
        participant A as Discord API
    
        M->>D: await Set channel name
        D->>A: Send API request
        A-->>D: Response
        D-->>M: Operation complete
        M->>M: Continue execution
    ```

## How to handle it?

Since v4.17.2,
DiSky now offers the way to **await** the request to be sent and executed before continuing the code execution,
__**without blocking the thread**__.
Prefix the expression with `await` to wait for the request to be sent and executed.

Our previous example would then look like this:

```applescript
await set discord name of %channel% to "new name"

# This will only be executed once Discord has confirmed the name change
reply with "The channel name has been updated!"
```

!!! success "Even better cache!"
    Some expression that returned cached values will now send a request to discord if used with `await`,
    **only if the cached value is not present!**

    Example:
    ```applescript
    set {_user} to user with id "000" # Will only look in cache
    retrieve user with id "000" # Will always send a request to discord

    await set {_user} to user with id "000" # Will send a request to discord if not in cache
    ```