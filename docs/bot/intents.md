---
status: updated
icon: material/key-chain
---

# Gateway Intents in Discord

## Introduction

Gateway Intents are a crucial concept in Discord bot development. They allow developers to specify which events and data their bot should receive from Discord, optimizing performance and reducing unnecessary data transfer.

## What are Gateway Intents?

Gateway Intents act as filters for the events and data your bot receives from Discord. By selecting specific intents, you can:

1. Reduce the amount of data sent to your bot
2. Focus on the events that are relevant to your bot's functionality
3. Comply with Discord's requirements for accessing certain types of data

??? info "Diagram"
    ```mermaid
    graph TD
        A[Discord Intents] --> B[Privileged Intents]
        A --> C[Standard Intents]
        A --> D[Message Poll Intents]
        
        B --> E[Guild Members]
        B --> F[Message Content]
        B --> G[Guild Presences]
        
        C --> H[Guild Moderation]
        C --> I[Guild Emojis and Stickers]
        C --> J[Guild Webhooks]
        C --> K[Guild Invites]
        C --> L[Guild Voice States]
        C --> M[Guild Messages]
        C --> N[Guild Message Reactions]
        C --> O[Guild Message Typing]
        C --> P[Direct Messages]
        C --> Q[Direct Message Reactions]
        C --> R[Direct Message Typing]
        C --> S[Scheduled Events]
        
        D --> T[Guild Message Polls]
        D --> U[Direct Message Polls]
    ```

## Categories of Intents

As visualized in the diagram above, Discord intents can be categorized into three main groups:

1. **Privileged Intents**: Require explicit enabling in the Discord Developer Portal
2. **Standard Intents**: Available to all bots without special permission
3. **Message Poll Intents**: Specific to handling poll-related events

### Privileged Intents

Privileged intents require special approval from Discord for bots in 100+ servers. They include:

- Guild Members
- Message Content
- Guild Presences

!!! warning "Important"
    Enabling privileged intents is crucial for certain bot functionalities. For example, without the Message Content intent, your bot won't be able to read message content in most situations.

### Standard Intents

These intents cover a wide range of bot functionalities and don't require special approval:

- Guild Moderation
- Guild Emojis and Stickers
- Guild Webhooks
- Guild Invites
- Guild Voice States
- Guild Messages
- Guild Message Reactions
- Guild Message Typing
- Direct Messages
- Direct Message Reactions
- Direct Message Typing
- Scheduled Events

### Message Poll Intents

Introduced for handling poll-related events:

- Guild Message Polls
- Direct Message Polls

## Best Practices for Using Intents

1. **Only enable necessary intents**: This reduces the load on both your bot and Discord's servers.
2. **Plan for privileged intents**: If your bot requires privileged intents, plan for the approval process, especially if you expect rapid growth.
3. **Stay updated**: Discord occasionally updates its intent system. Keep your bot and knowledge up-to-date.
4. **Optimize for scale**: Consider how your intent choices will affect your bot's performance as it grows to serve more servers.

## Conclusion

Understanding and properly implementing Gateway Intents is essential for creating efficient and compliant Discord bots. By carefully selecting the intents your bot needs, you can ensure optimal performance and adhere to Discord's guidelines.

For the most up-to-date information on intents and their implementation, always refer to the official Discord Developer Documentation.