---
icon: material/television
---

# Presence & Status

[[[% import 'macros.html' as macros %]]]

As a user, your bot will be able to have a custom **online status** and **presence.**

* **Status:** the little circle in the bottom-right corner of your bot's avatar.
* **Presence:** the text shown in the bot's profile, defining what it's doing.

## Presence

The presence will define what your bot is actually doing. It can be one of the following actions:

* Listening
* Watching
* Playing
* Competing
* Streaming

When defining the presence, you'll have to provide the **text shown**, for example, what game your bot is playing or what music is it listening to.

Here's an example of each presence, and a way to change the bots:

=== "Listening"
    ```applescript
    set the presence of the bot named "bot-name" to listening "awesome music!"
    ```
=== "Playing"
    ```applescript
    set the presence of the bot named "bot-name" to playing "awesome games!"
    ```
=== "Competing"
    ```applescript
    set the presence of the bot named "bot-name" to competing "Arena World Champions"
    ```
=== "Watching"
    ```applescript
    set the presence of the bot named "bot-name" to watching "YouTube"
    ```
=== "Streaming"
    !!! warning "The URL must be from YouTube or Twitch!"

    ```applescript
    set the presence of the bot named "bot-name" to streaming "things" with url "stream url"
    ```

## Online Status

The online status will define the little circle at the bottom-right corner of your bot's avatar.

Here's the available online status your bot can have:

* Online (`online`, shown as :green_circle:)
* Idle (`idle`, shown as :yellow_circle:)
* Do not disturb (`do not disturb`, shown as :red_circle:)
* Offline (`offline`, shown as :white_circle:, **the bot won't be shown as online and will be hidden!**)
* Invisible (`invisible`, no circle shown, **the bot will be shown as offline, but it's actually online!**)

To change the bot's online status, simply use this syntax:

=== "Online"
    ```applescript
    set the online status of bot "bot-name" to online
    ```

=== "Idle"
    ```applescript
    set the online status of bot "bot-name" to idle
    ```

=== "Do not disturb"
    ```applescript
    set the online status of bot "bot-name" to do not disturb
    ```

=== "Offline"
    ```applescript
    set the online status of bot "bot-name" to offline
    ```

=== "Invisible"
    ```applescript
    set the online status of bot "bot-name" to invisible
    ```