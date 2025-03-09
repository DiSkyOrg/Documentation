---
icon: material/application-parentheses
---

# ParseSK

ParseSK is a simple Skript addon allowing you to parse any string input with Skript.
You can programmatically handle the parsing errors it may throw,
and make it so it won't execute the given code (and only parse it).

## Installation

!!! success "How to download?"
    ParseSK is only available for **Patreons** of [ItsTheSky](https://www.patreon.com/itsthesky).

    [Access Patreon-only Resources](https://resources.disky.me/resources/5){ .md-button }

!!! warning "This is a separate Plugin, not a Module!"

## Usage

!!! info "Pattern"
    ```applescript
    eval[uate] [without executing] %string% [and store (it|the error[s]) in %-objects%]
    ```

Only one effect is added by ParseSK, which is `eval`. Here are some usage examples:

=== "Parse & Execute"
    ```java
    add "set {_test} to 1" to {_test::*}
    add "if {_test} is bigger than 0:" to {_test::*}
    add "    send ""&2Hello, world!""" to {_test::*}
    add "else:" to {_test::*}
    add "    huh send ""&4Goodbye, world!""" to {_test::*}

    set {_to-parse} to join {_test::*} with nl

    eval {_to-parse} and store it in {_errors::*}

    if {_errors::*} is not set:
        send "&aNo errors found in the string."
    else:
        send "&4Errors found in the given code:"
        loop {_errors::*}:
            send " &c- %loop-value%"
    ```

=== "Parse without executing"
    Simply starts the effect with `eval without executing` instead of `eval`:

    ```applescript hl_lines="9"
    add "set {_test} to 1" to {_test::*}
    add "if {_test} is bigger than 0:" to {_test::*}
    add "    send ""&2Hello, world!""" to {_test::*}
    add "else:" to {_test::*}
    add "    huh send ""&4Goodbye, world!""" to {_test::*}

    set {_to-parse} to join {_test::*} with nl

    eval without executing {_to-parse} and store it in {_errors::*}

    if {_errors::*} is not set:
        send "&aNo errors found in the string."
    else:
        send "&4Errors found in the given code:"
        loop {_errors::*}:
            send " &c- %loop-value%"
    ```