---
status: new
icon: material/car-speed-limiter
---

# Rate Limits

## What are Rate Limits?

A rate limit is a strategy used to control network traffic by capping the frequency of repeated actions. In the context of Discord bots, rate limits are implemented by the Discord API to prevent abuse and ensure fair usage of their services.

When a user or bot performs the same action too frequently, they become "rate limited," which temporarily restricts their ability to make further requests to the Discord API.

## How Rate Limits Work in Discord

=== "Textual Description"

    Discord uses a sliding window rate limit system. Here's a simplified explanation of how it works:

    1. Each endpoint has its own rate limit, typically defined by X requests per Y seconds.
    2. When you make a request, Discord checks if you've exceeded the limit for that endpoint.
    3. If you haven't exceeded the limit, your request is processed normally.
    4. If you have exceeded the limit, Discord returns a 429 (Too Many Requests) error.
    5. The response includes a `Retry-After` header, indicating how long you should wait before making another request.

=== "TL;DR (Diagram)"

    ```mermaid
    sequenceDiagram
        participant Bot as DiSky
        participant API as Discord API
        participant Limit as Rate Limiter
    
        Bot->>API: Send Request
        API->>Limit: Check Rate Limit
        alt Limit Not Reached
            Limit->>API: Allow Request
            API->>Bot: Process Request
            API->>Bot: Return Response
        else Limit Reached
            Limit->>API: Block Request
            API->>Bot: Return 429 Too Many Requests
            API->>Bot: Provide Retry-After Header
        end
    ```

## Identifying Rate Limits

### In Server Console

When your bot encounters a rate limit, you may see messages like this in your server console:

```
[net.dv8tion.jda.api.requests.RestRateLimiter] Encountered cloudflare rate limit! Retry-After: 100 s
```

### For Self-Hosted Bots

If you're hosting your bot locally, you might experience a disconnection that looks like a loss of internet connectivity:

![Discord disconnection screen](https://github.com/user-attachments/assets/7665d79e-2013-498e-9ded-8b6a1b4771cd)

## Resolving Rate Limit Issues

To avoid or resolve rate limit issues, consider the following steps:

1. **Audit Your Code**: Review your bot's code for any repetitive Discord actions (retrieve, post, reply, etc.). Optimize these operations to reduce API calls.

2. **Implement Cooldowns**: Add command cooldowns per user to prevent rapid successive use of commands.

3. **Use Bulk Operations**: When possible, use bulk API endpoints (e.g., bulk delete messages) instead of making multiple single requests.

4. **Respect Retry-After**: When you receive a 429 error, always respect the `Retry-After` header and wait the specified time before retrying.

5. **Monitor Multiple Bots**: If you're running multiple bots on the same machine, check all of them for potential rate limit triggers. One bot's rate limit can affect others on the same IP.

6. **Secure Your Token**: If you suspect your bot token has been compromised, immediately regenerate it in the Discord Developer Portal. Unauthorized use of your token can lead to rate limits.

7. **Scale Responsibly**: As your bot grows in popularity, you may need to implement more sophisticated rate limiting on your end or consider reaching out to Discord for increased limits.

## Advanced Rate Limit Handling

For more advanced applications, consider implementing a rate limit handler in your bot. This could:

- Keep track of remaining requests for each endpoint
- Implement a queue system for requests when nearing the limit
- Automatically retry requests after the `Retry-After` period

## When to Contact Discord

If your bot is experiencing rate limits during normal operations, despite implementing best practices, you may need to contact Discord. Visit https://dis.gd/contact for support, especially if:

- Your bot serves a large number of servers
- You believe you're experiencing a bug related to rate limiting
- You need to request higher rate limits for a verified bot

## Further Reading

For more detailed information on Discord's rate limits, including specific limits for different endpoints, refer to the [Discord Developer Documentation on Rate Limits](https://discord.com/developers/docs/topics/rate-limits).