---
icon: material/text-search
---

# Logs Manipulation

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.11.0') ]]]

In this section, we'll see how to manipulate a guild's logs, listen to them and more. 

## Model

In Discord, logs are called **Audit Logs**. They are a list of actions that have been performed on a guild. For instance, when a member is banned, or when a message is dedleted.

Each **Audit Log** have different info, such as its type (what action has been made), the author of the action, and more, that we'll see soon.

## Fetching

To fetch manually the logs of a guild, you'll have to use the `retrieve audit logs` effect, such as:

```applescript
...
set {_guild} to event-guild # Get the guild from the event, or replace by any guild
retrieve audit logs from {_guild} and store it in {_logs::*}
```

Now, `{_logs::*}` is a list of all the logs of the guild. You can loop through them, and get the info you want for each entry.

## Listening

Another way to get info of an entry log is by listening to them. To do so, you'll have to use the `on guild log create` event, such as:

```applescript
on guild log create:
    set {_entry} to event-logentry # Get the entry log from the event
    # ... do something with the entry log
```

!!! warning
    In order to retrieve and listen to logs, the bot must have:
    
    * the `GUILD_MODERATION` intent enabled
    
    * the `VIEW_AUDIT_LOGS` permission

## LogEntry

A **LogEntry** is an object that represents an entry log. It contains all the info of the entry, such as its type, the author of the action, and more.

You can get the following information from a **LogEntry**:

|Property|Type|Description|
|:-:|:-:|:-:|
|`logged author`|`user`|The user who made the action|
|`logged guild`|`guild`|The guild where the action has been made|
|`logged id`|`channel`|The unique id of the entry|
|`logged action`|`text`|The action that has been made|

!!! info
    To use these, simply follow this syntax:
    
    ```applescript
    set {_entry} to ... # Get the entry log from the event, or replace by any entry log
    set {_author} to logged author of {_entry}
    set {_guild} to logged guild of {_entry}
    # ... and so on ...
    ```