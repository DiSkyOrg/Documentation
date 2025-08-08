---
icon: material/signal-distance-variant
---

# Listen Once

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.19.0') ]]]

## Overview

The "Listen Once" feature in DiSky allows you to create a one-time event listener that automatically unregisters after being triggered. As the name suggests, this feature lets you listen one time to a specific event and then automatically unregister the listener.

There's also a built-in timeout system to execute specific code once it's expired, while the other "actual" code isn't executed. Every DiSky event can be used with this feature.

## Key Features

1. **One-time Listening**: The listener automatically unregisters after the first trigger.
2. **Timeout System**: You can set a timeout period, after which a specific code block will execute if the event hasn't occurred.
3. **Versatility**: Compatible with all DiSky events.

## Limitations

Because of Skript, you don't have easy control on context **outside** the `listen once` section. The best way to handle this is to use `set {_var} to ...` and then use this variable inside the `listen once` section.

!!! success "Good to know"
    You have two ways to "execute" code in the outer event context:

    - For effects that require a specific context (e.g. the `reply with` effect that requires an interaction), simply **prefix** the effect with `outer` (e.g. `outer reply with "Hello"`)
    - For the outer event's values, again, prefix the expression with `outer` (e.g. `set {_var} to outer event-message`)

## Usage and Syntax

```applescript
listen once to "event name" with timeout X seconds:
    on subscribe:
        # Code to execute when the event occurs
    
    on timeout:
        # Code to execute if the timeout is reached
```

- Replace `"event name"` with the desired DiSky event (e.g., "message received").
- Set `X` to the number of seconds for the timeout (optional).

## Examples

=== "With Timeout"
    ```applescript
    discord command listen:
        prefixes: ?
        trigger:
            set {_prefix} to used prefix #(1)!
            listen once to "message received" with timeout 5 seconds: #(2)!
            on subscribe:
                reply with "%jump url of event-message% (original message: %jump url of outer event-message%). Used prefix: %{_prefix}%"

                on timeout:
                    outer reply with "Timeout reached (%used prefix%)" #(3)!
    ```

    1. Variables are shared before & during the `listen once` section. You can use them in the `listen once` section.
    2. Any event is accepted between the quotes. Simply use an event name without the 'on' prefix.
    3. The `on timeout` sub-section is run using the outer context, so in this case, the discord command event.

=== "Without Timeout (not recommended)"

    !!! tips "You can see that the 'subscribe' sub-section is not required"
    
    ```applescript
    discord command listen:
        prefixes: ?
        trigger:
            set {_prefix} to used prefix #(1)!
            listen once to "message received": #(2)!
                reply with "%jump url of event-message% (original message: %jump url of outer event-message%). Used prefix: %{_prefix}%"
    ```

    1. Variables are shared before & during the `listen once` section. You can use them in the `listen once` section.
    2. Any event is accepted between the quotes. Simply use an event name without the 'on' prefix.
