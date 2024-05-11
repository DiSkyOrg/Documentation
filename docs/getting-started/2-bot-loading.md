---
icon: material/numeric-3-box
---

# Bot Loading

!!! warning
    You should check [**Bot Creation**](1-bot-creation.md) before if you haven't yet!

You'll see here how to use DiSky in a Skript file, especially how to load your bot.

??? tips "What are scopes? (read if you're a newbie)"
    DiSky is using a lot of **scopes**, which are very similar to the event system. Instead of being in a trigger (such as on load or a command), a scope is the trigger itself and thus can be placed in a file without a parent.
    
    Scopes come with two sorts of **entry** (entry looks like `name: value`):
    
    * Value entry (form: `name: value`), event-related literals are forbidden (only global variable & script options works here):
    ````applescript
    <scope name>:
            token: "token"
    ````
    
    * Section entry (form: `name: <line break> code ...`), code that could be running.
    ````applescript
    <scope name>:
            on ready:
                send "%event-bot% has been loaded!" to console
    ````
    
    It will load automatically when the code is reloaded.

## Bot Scope

DiSky's bot creation scope looks like this: 
 
```applescript hl_lines="3 6 10 14 15 16 18 19 23 26 29"
# The name specified here doesn't matter with the one used in the developer portal. 
# This one will only be used for recognize your bot in Skript code.
define new bot named "BOT NAME": 
    
    # The bot's token, small reminder that it MUST be private!
    token: "BOT TOKEN"
    
    # Gateway intents enabled, others that are not listed here will be disabled.
    # If you're not sure about that, leave it as 'default intents'.
    intents: default intents #(1)!
    
    # Advanced bot option, defining websocket, connection and privacy parameters.
    # Here again, if you're not sure about that, leave it as shown below.
    policy: all #(2)!
    cache flags: default cache #(3)!
    compression: none #(4)!
    
    auto reconnect: true #(5)!
    force reload: false #(6)!
    
    # Optional section code:
    # Fired once the bot, and all guilds, are ready-to-use.
    on ready:
    	# </>
    # Fired once a guild, and all its members, are ready-to-use
    on guild ready:
    	# </>
    # Fired once the bot is about to be disconnected
    on shutdown:
    	# </>
```

1. Intents are a way to tell Discord what you want to do with your bot. If you're not sure about that, leave it as `default intents`. **[More information here](../bot/intents.md)**
2. **[More information here](../bot/policy.md)**
3. **[More information here](../bot/policy.md#cache-flags)**
4. Compression used when connecting to Discord's gateway. Default is `none`, the only one available is `zlib`.
5. If the bot should automatically reconnect when disconnected from Discord gateway.
6. If the bot's connection should be reloaded everytime the script is reloaded. (recommended to leave it as `false`)

Reload your **script**, and wait a little. Your bot should be marked as online!

## 2. Ready Sections

You can execute code as soon as a **bot** or a **guild** is ready to use.

!!! tip
    An entity being ready-to-use means every action or property is loaded correctly.

## `on ready`

This section will be run once the bot is fully loaded, all guilds included.

The only event-value here is `event-bot` to get the bot instance that's just loaded:

**Example:**

```applescript
<scope name>:
    on ready:
        send "&a%event-bot%&2 has been loaded!" to console
```

This section is also where **global application commands** are registered. You can get more information about those in the **Application Commands** page of this wiki.

## `on guild ready`

This section will be run once a guild is fully loaded by a bot. All of its members has been cached (according to the member policy) and same for other entities such as channels, roles, etc...

There's two event value here:

* `event-bot`, get the bot who loaded the guild
* `event-guild`, get the guild that has just been loaded

**Example:**

```applescript
<scope name>:
    on guild ready:
        send "&a%event-bot%&2 just loaded &a%event-guild%&2 guild!" to console
```

This section is also where **local application commands** are registered. You can get more information about those in the **Application Commands** page of this wiki.
