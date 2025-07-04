---
icon: material/check-all
---

# ConsoleLogs

[[[% import 'macros.html' as macros %]]]

!!! success
    This documentation page includes all the elements from the module **[ConsoleLogs](../modules/consolelogs.md)**.

## EffLogMessage

[[[ macros.required_version('4.0.0') ]]]

Logs a message with the given log level.
=== "Examples"

    ```applescript
    print "hi" with severity of trace to console
    send "hello I am a log message" with severity of info to console
    log "this is a custom log message" with severity of debug to console
    ```
=== "Patterns"

    ```applescript
    (print|send|log) %strings% with [the|a] severity [of] fatal to [the] console
    (print|send|log) %strings% with [the|a] severity [of] error to [the] console
    (print|send|log) %strings% with [the|a] severity [of] warn[ing] to [the] console
    (print|send|log) %strings% with [the|a] severity [of] info[rmation] to [the] console
    (print|send|log) %strings% with [the|a] severity [of] debug to [the] console
    (print|send|log) %strings% with [the|a] severity [of] trace to [the] console
    ```

## Log Event

[[[ macros.required_version('4.0.0') ]]]

By using the log event, you can use this (alongside the required expression) to send console log messages to discord!
=== "Examples"

    ```applescript
    on log:
        post logged message to channel with id "000"
    ```
=== "Patterns"

    ```applescript
    [on] [console] log
    ```

## Logged Message

[[[ macros.required_version('4.0.0') ]]]

This expressions **returns** the logged message (in chunks, to prevent rate limiting). This **cannot** be set or deleted.
=== "Examples"

    ```applescript
    set {_message} to the logged message
    ```
=== "Patterns"

    ```applescript
    [the] log[ged] message
    ```

## Last Logged Message

[[[ macros.required_version('4.0.0') ]]]

This returns the latest logged message that was sent in console. **May not always be accurate** This **cannot** be used inside the on log event.
=== "Examples"

    ```applescript
    set {_message} to the last logged message
    ```
=== "Patterns"

    ```applescript
    [the] last log[ged] message
    ```

## Log Level

[[[ macros.required_version('4.0.0') ]]]

This returns the log level of a logged message in an on log event.
=== "Examples"

    ```applescript
    if the log level is error:
    ```
=== "Patterns"

    ```applescript
    [the] log [message] level
    ```

## Log Level Types

[[[ macros.required_version('4.0.0') ]]]

This is the types of log levels that are valid.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    info, warning, error, fatal, trace, debug, all
    ```
