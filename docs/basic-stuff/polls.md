---
icon: material/chart-bar
---

# Polls

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.14.2') ]]]

Polls are a great way to get feedback from your community. 

Every poll has a **question** and a list of **answers** to choose from. In additions, they have an expiration date, after which the poll will be closed and no more votes can be cast. Results can be viewed by anyone, even if you haven't voted yet.

## Creating a poll

First things first, you'll have to create the poll itself, and configure its base settings:

```applescript
set {_poll} to new poll "What's the best programming language?" #(1)!
set poll duration of {_poll} to 5 hours #(2)!
```

1. Want to let people choose multiple answers? Simply appends `with multiple choices` at the end:
    ```applescript
    set {_poll} to new poll "What's the best programming language?" with multiple choices
    ```
2. The `poll duration` is the time the poll will be open for votes. It **must** stay between __one hour__ and __one week (7 days)__.

## Adding answers

Each answer have, well, an answer, but can also have an emoji to represent it. While the emoji is optional, the answer itself is required.

```applescript
add answer "Java" with reaction "coffee" to answers of {_poll}
add answer "Python" with reaction "snake" to answers of {_poll}
add answer "C##" with reaction "desktop" to answers of {_poll}
```

## Sending the poll

Now your poll is created, you can join it through a [rich message](../advanced-stuff/advanced-messages.md#add-poll "Advanced Messages"), or use the `inline message` expression as such:

=== "With message"
    ```applescript
    reply with message "Hey, check out my poll!" with poll {_poll}
    ```

=== "Only the poll"
    ```applescript
    reply with {_poll}
    ```

## Already-created polls

You can also manage already-created polls, sent by other bots or users. Basically, polls are part of a **message**, thus all message may not have a poll. 

Here's some examples on how to manage polls (we'll assume `{_message}` is the message containing the poll):

=== "Check if a message has a poll"
    ```applescript
    if poll {_message} is not set:
        reply with "This message doesn't have a poll."
    ```

=== "Get the poll's question"
    ```applescript
    set {_question} to poll question of poll of {_message}
    ```

=== "Get the poll's answers"
    ```applescript
    set {_answers::*} to answers of poll of {_message}

    loop {_answers::*}: #(1)!
        add "• `%answer text of loop-value%` [%mention tag of answer emote of loop-value%]: with %answer votes of loop-value% votes." to {_m::*}

    reply with "Here are the answers:%nl%%join {_m::*} with nl%"
    ```
    
    1. Every answers has the following properties:
        * `answer text`: the answer's text (e.g. the answer itself)
        * `answer emote`: the answer's emoji (may be not set)
        * `answer votes`: the number of votes the answer has.

In additions, you can check for the poll's state using the following conditions:

=== "Is Expired"
    ```applescript
    if poll of {_message} is expired:
        reply with "This poll has expired."
    ```

    That mean the poll is completly closed, and no votes can be cast anymore.

=== "Is Finalized"
    ```applescript
    if poll of {_message} is finalized:
        reply with "This poll has been finalized."
    ```

    That mean the poll is finished, but votes can still be cast.

## References

!!! example "Create Poll Example"
    Here's a full example of a poll creation:

    ```applescript
    discord command poll:
        prefixes: !
        trigger:
            set {_poll} to new poll "What's the best programming language?"
            set poll duration of {_poll} to 5 hours
            add answer "Java" with reaction "coffee" to answers of {_poll}
            add answer "Python" with reaction "snake" to answers of {_poll}
            add answer "C##" with reaction "desktop" to answers of {_poll}
            reply with {_poll}
    ```

!!! example "Manage Poll Example"
    Here's a full example of a poll management:

    ```applescript
    discord command pollinfo <string>:
        prefixes: !
        trigger:
            retrieve message with id arg-1 in event-channel and store it in {_msg}
            set {_poll} to poll of {_msg}
            if {_poll} is not set:
                reply with ":x: **Error:** This message does not contain a poll."
                stop
    
            set {_answers::*} to answers of {_poll}
            add "Poll: %poll question of {_poll}%" to {_m::*}
            
            if {_poll} is finalized:
                add "- This poll is finalized." to {_m::*}
            else:
                add "- This poll is not finalized, votes may not be accurate." to {_m::*}
            
            if {_poll} is expired:
                add "- This poll is over." to {_m::*}
            else:
                add "- This poll is not expired, votes may still be cast." to {_m::*}
    
            add "" to {_m::*}
    
            loop {_answers::*}:
                add "• `%answer text of loop-value%` [%mention tag of answer emote of loop-value%]: with %answer votes of loop-value% votes." to {_m::*}
            reply with join {_m::*} with nl
    ```

!!! warning ""
    * A poll's question title must be between **5 and 100 characters**.
    * An answer's text must be between **1 and 55 characters**.
    * A poll cannot have a duration of less than **1 hour** or more than **1 week (7 days)**.
    * A poll cannot have more than **10 answers**.