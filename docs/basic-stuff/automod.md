# 🛡️ AutoMod

AutoMod is a system implemented by Discord, helping administrators to moderate their servers, by filtering messages, status, names and more.

## How it works?

A message, member's name or status will **trigger** an **automod rule**, and then take the **desired __actions__** to counter it. Multiple rules can be triggered at the same time, and multiple actions can be taken for the same rule.

### Triggers

* Message Received (Triggered when the message contains a specific word/[regex](https://en.wikipedia.org/wiki/Regular_expression) pattern)

!!! note
    Currently (as of 12/06/2023), JDA only supports **message** trigger. Other triggers will be added in the near future.

!!! success "Different Filter's Type"
    You can use different filters to trigger the message received rule:
    
    * **Keyword**: The message contains the specified words
    * **Pattern**: The message matches the specified [regex](https://en.wikipedia.org/wiki/Regular_expression) pattern
    * **Mention**: The message contains more than the specified amount of mentions

### Actions

* Block the message (*with an optional reason*)
* Send an alert in a channel
* Timeout the member for a specific duration

## Script Code

### Creating a Rule

Now we've seen how it works, let's see how to implement it in a script. First, we need to create a new **automod rule**, to then create the rule in a **guild**:

```applescript
create a new automod rule and store it in {_rule}: #(1)!
```

1. This will create a new automod rule, and store it in the _local_ variable `rule`. It can then be used outside the section.

### Changing the Rule's Trigger

We'll put all of our code related to automod rule creation inside this section. Let's now see how to change its **trigger**:

=== "Message Filter (Keyword)"

    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to (message with keyword filter "morb" named "no morb rule")
    ```

    *Will be triggered if a message contains the word `morb`*

=== "Message Filter (Pattern)"

    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to (message with pattern filter "m(\\d+)rb" named "no morb rule with pattern")
    ```

    *Will be triggered if a message matches the regex pattern `m(\d+)rb` (e.g. `m123rb`)*

=== "Message Filter (Mention)"

    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to (message with mention filter 5 named "no mention spam rule")
    ```

    *Will be triggered if a message contains more than 5 mentions (roles not included)*


### Adding Actions

We can now add **actions/responses** to our rule:

=== "Block Message"

    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to ...

        add block message to responses of rule #(1)!
    ```

    1. You can also specific a reason such as:
        
        ```applescript
        add block message with "no morb" to responses of rule
        ```

    *Will make the AutoModeration bot delete the message, with the optionally specified reason. It'll look like this:*

    ![Block Example](../images/automod-block.png)

=== "Send Alert"

    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to ...

        add send alert in channel with id "000" to responses of rule
    ```

    *Will make the AutoModeration bot send an alert in the specified channel. It'll look like this:*
    
    ![Alert Example](../images/automod-alert.png)

=== "Timeout Member"
    
    ```applescript
    create a new automod rule and store it in {_rule}:
        set type of rule to ...

        add timeout member for 2 hours to responses of rule
    ```

    *Will make the AutoModeration bot timeout the member for 1 hour. It'll look like this:*
    
    ![Timeout Example](../images/automod-timeout.png)

### Creating the Rule in a Guild

Now that we've created our rule, we can create it in a guild:

```applescript
create a new automod rule and store it in {_rule}:
    set type of rule to ...
    
    add ... to responses of rule

create rule {_rule} in guild with id "000" # or any other guild
```

And here you go ✨, you've created your first automod rule! 