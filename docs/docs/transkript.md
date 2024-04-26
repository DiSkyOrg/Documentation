---
icon: material/check-all
---

# TranSkript

[[[% import 'macros.html' as macros %]]]

!!! success
    This documentation page includes all the elements from the module **[TranSkript](../modules/transkript.md)**.

## EffGenerateTemplate

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```
=== "Patterns"

    ```applescript
    generate [a] [new] transcript [template] (with|from|using) [the] message[s] %messages% [with [the] [options] %-tsoption%] and (store|save) (it|the file) (at|in) %string%
    generate [a] [new] transcript [template] (with|from|using) [the] channel %channel% [with [the] [options] %-tsoption%] and (store|save) (it|the file) (at|in) %string%
    ```

## New Transcript Options

[[[ macros.required_version('4.0.0') ]]]
[[[ macros.return_type('tsoption') ]]]

Create a new transcript options object, specifying:
- If the template should be compact mode or not
- If the template should be light theme or not
=== "Examples"

    ```applescript
    set {_options} to new transcript options with compact mode and light theme
    ```
=== "Patterns"

    ```applescript
    [a] [new] transcript [template] [option[s]] with [compact mode] [[and] light theme]
    ```

