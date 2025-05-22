---
icon: material/check-all
---

# Sections

[[[% import 'macros.html' as macros %]]]

## Creator Components Row

[[[ macros.required_version('4.0.0') ]]]

Creates a row of components.
The specified variable will contains the created row once the section is executed.
For now, a row can only hold multiple components of type Button!
Use 'the last row builder' expression (within the section) to change the values of the row!
=== "Examples"

    ```applescript
    create a new row and store it in {_row}:
            
        add new danger button with id "test" named "Hello World" with reaction "smile" to the components of the row
        add new success button with id "test2" named "yuss" to the components of the row
    ```

=== "Patterns"

    ```applescript
    (make|create) [a] [new] [component[s]] row and store (it|the result) in %-objects%
    ```

## Embed Builder

[[[ macros.required_version('3.0') ]]]

This builder allow you to make embed easily. You can specify the template used, you must register this template before
use it!
=== "Examples"

    ```applescript
    discord command embed:
    	prefixes: !
    	trigger:
    		make embed:
    			set title of embed to "Title"
    			set description of embed to "Description%nl%The title leads to the URL, if given"
    			set author of the embed to "Author name (Can point to URL)"
    			set author icon of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    			set author url of embed to "https://www.youtube.com/watch?v=i33DB6R8YUY"
    			set embed color of the embed to orange
    			add inline field named "Field Name" with value "Colour sets %nl%< that" to fields of embed
    			add inline field named "Field Name" with value "Color is a java Color%nl%Not a string" to fields of embed
    			add inline field named "Field Name" with value "Field value" to fields of embed
    			add field named "Non-inline field name" with value "The number of fields that can be shown on the same row is limited to 3, but is limited to 2 when an image is included" to fields of embed
    			set image of embed to "https://media.discordapp.net/attachments/237757030708936714/390520880242884608/8xAac.png?width=508&height=522"
    			set thumbnail of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    			set title url of embed to "https://www.crunchyroll.com/fr/tonikawa-over-the-moon-for-you"
    			set footer of embed to "Footer text"
    			set footer icon of embed to "https://cdn.discordapp.com/emojis/825811394963177533.png?v=1"
    			set timestamp of embed to now
    		reply with last embed
    ```

=== "Patterns"

    ```applescript
    make [new] [discord] [message] embed [using [the] [template] [(named|with name|with id)] %-string%]
    ```

## Create (rich) Message

[[[ macros.required_version('4.0.0') ]]]

Creates a rich message.
A rich message can receive the following data:

- Content
- Embed[s] (default max is 1, webhooks can send up to 5)
- Attachment(s) (supports images if SkImage is installed)
  - Components
    This will be used to both post & edit a message.
    Simply change what you want and pass the result of the section to the edit effect.
    === "Examples"

     ```applescript
    create a new message and store it in {_msg}:
      set the content of the message to "Hello World!"

      make embed:
          set title of embed to "Amazing embeds :D"
          set embed color of embed to orange
          set footer of embed to "Created with DiSky v4!"
      add last embed to the embeds of the message

      add "plugins/Skript/scripts/msg.sk" to the attachments of the message

      # simple button that'll take one row for itself
      add new danger button with id "btn-1" named "RDR II" to rows of the message 
      # mutliple buttons within the same row
      make new component row and store it in {_row}:
          add new success button with id "btn-2" named "Green lands!" with reaction "smile" to components of the row builder
          add new link button with id "https://forum.itsthesky.info/discord/" named "DiSky's Discord" to components of the row builder
      add {_row} to rows of the message

      # dropdown/select menu
      set {_dp} to new dropdown with id "selector"
      set min range of {_dp} to 1
      set max range of {_dp} to 2
      set placeholder of {_dp} to "Dropdown"
      add new option with value "one" named "One!" with description "Click to select" with reaction "sparkles" to options of {_dp}
      add new option with value "two" named "Two!?" with description "Click to select" with reaction "sparkles" to options of {_dp}
      add new option with value "three" named "THREE!!!" with description "Click to select" with reaction "sparkles" to options of {_dp}
      add {_dp} to the rows of message

    reply with {_msg}
     ```

=== "Patterns"

    ```applescript
    (make|create) [a] [new] [:silent] message and store (it|the result) in %-objects%
    ```

## ReactSection

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    react to [the] [message] %message% with [the] %emote% [to run [(1�one time)] [[and] wait for %-user%]]
    ```

## Modify Welcome Screen

[[[ macros.required_version('4.10.0') ]]]

Modify the welcome screen of a guild.
At the end, the request will be sent to discord to update the welcome screen.
=== "Examples"

    ```applescript
    discord command setup <guild>:
        trigger:
            modify welcome screen of arg-1:
                change the screen description to "Welcome to the server! Please read the rules and get roles before chatting."
                add channel with id "937001799896956991" named "Read our rules" with reaction "?" to the screen
                add channel with id "952199041335316520" named "Get roles" with reaction "??" to the screen
    ```

=== "Patterns"

    ```applescript
    modify [the] welcome screen (of|for) [the] [guild] %guild%
    ```

## LoadFailure

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    [on] load[ed] (failure|error|exception)
    ```

## MultipleLoad

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    [on] multiple [track] load[ed]
    [on] playlist load[ed]
    ```

## NoMatches

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    [on] no [track] match[es]
    ```

## SingleLoad

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    [on] single [track] load[ed]
    ```

## LoadItems

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    load [the] items (with|from) [the] url %string%
    ```

## SearchItems

[[[ macros.required_version('4.0.0') ]]]

No description provided.
=== "Examples"

    ```applescript
    No examples provided.
    ```

=== "Patterns"

    ```applescript
    search [the] items (with|from) [the] input %string%
    ```

## Find Members

[[[ macros.required_version('4.14.3') ]]]

Find member filter! It's a section that lets you filter by yourself the members you want to retrieve.

Wants only members with a role, or specific nickname, that are not connected to a channel? You've got it!

=== "Examples"

    ```applescript
    find members in event-guild and store them in {_members::*} with filter var {_m}:
        # {_m} now contains the member to apply the filter to. For instance:
        {_m} has discord role with id "XXX"
        {_m} is muted
        return true
   
    reply with "I have found %size of {_members::*}% that has the role and is muted!"
    ```

=== "Patterns"

    ```applescript
    find [the] [discord] member[s] (in|from) [guild] %guild% and store (them|the members) in %~objects% with filter var[iable] %~objects%
    ```
