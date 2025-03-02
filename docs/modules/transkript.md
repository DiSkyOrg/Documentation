---
icon: material/script-text
---

# TranSkript

!!! success "How to download?"
    TranSkript is only available for **Patreons** of [ItsTheSky](https://www.patreon.com/itsthesky).

    [Access Patreon-only Resources](https://resources.disky.me/resources/modules/9){ .md-button }

## Overview

This module will provide support for Discord(like website generation. You'll be able to re-create and save forever a conversation while including the replies, attachments, colors, references, and much more! It requires Java 16+ and DiSky v4.21.0+

### What can be saved?

* The message's content (formatted, aka **bold**, _italic_, etc...)
* Code blocks/inline code
* Spoilers/quotes
* Attachments
* Embeds
* Reactions, with their count
* Referenced message
* Slash commands
* Webhook & bot messages
* Components (buttons)

## Examples

!!! note
    The following images **are not Discord**!

<figure markdown>
  ![Image title](../images/image (1).png)
  <figcaption>Simple discussion, featuring mentions, role's colors &#x26; a bot.</figcaption>
</figure>

<figure markdown>
  ![Image title](../images/image (3).png)
  <figcaption>Several links &#x26; their rendering</figcaption>
</figure>

<figure markdown>
  ![Image title](../images/image.png)
  <figcaption>Threads/post creation</figcaption>
</figure>

<figure markdown>
  ![Image title](../images/image (11).png)
  <figcaption>Replies</figcaption>
</figure>

<figure markdown>
  ![Image title](../images/image (4).png)
  <figcaption>Buttons</figcaption>
</figure>

## Usage

There's only one syntax for this module, where you can generate a template according to two contexts:

* **Referencing a channel.** The module will retrieve the last 100 messages (that's the max) and create history on them.
* **Referencing specific messages.**

```applescript
set {_channel} to event-channel # can be any messaging channel, including private
generate transcript from channel {_channel} and store it in "plugins/ts.html"
```

Or, if you have a list of messages:

```applescript
set {_messages::*} to ... # specify the messages there
generate transcript from messages {_messages::*} and store it in "plugins/ts.html"
```

## Options

When generating a transcript, it will use the default "airy" and dark theme of Discord. You can however enable the compact mode and/or the light theme when generating the template! Here's how to do so:

```applescript
set {_opts} to new transcript options with compact mode # just compact mode
set {_opts} to new transcript options with light theme # just light theme
set {_opts} to new transcript options with compact mode and light theme # both

# We specify in the effect the options to use
generate transcript from channel {_channel} with {_opts} and store it in "plugins/ts.html"
```
