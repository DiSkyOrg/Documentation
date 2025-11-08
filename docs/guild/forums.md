---
icon: material/forum
---

# Forums

This page will explain managing forums, including posts, tags, and more.

## Forum channel

There's a specific channel type in DiSky & Discord: **Forum Channel**

They act like a text channel, but you cannot write there; it only holds **threads** that represent the available posts. Therefore, if you want to get threads out of a forum channel, you can simply do:

```applescript
set {_threads::*} to threads of forum with id "000"
```

!!! success
    `forum` can also be used in **discord command's argument!**

* The **thread's name** will represent the **post's name**. (`discord name of XXX`)
* As a thread channel, you can use the `retrieve messages` effect to get the messages
* As a member container, `members of` expression is available to get active members of the post
* You can get the tags of a thread using `tags of <thread>`. Keep in mind this will only work with **posts' threads!**
* You can get the **owner** of a thread using [`thread owner of <thread>`](../docs/expressions.md#thread-owner) - useful to know who created the post
* You can get the **message count** using [`message count of <thread>`](../docs/expressions.md#thread-message-count) - helpful for tracking post activity

## Tags

A specific post (or thread) can have none, one or more **forum tags**. The only way to get a forum tag is by using its name:

```applescript
set {_tag} to tag named "resolved" from forum channel with id "000"
```

!!! warning
    Since each forum channel has its own created tags, we have to specify from which channel we're getting it.

You can also create tags, add them to the forum channel and finally add them to the posts:

```applescript
set {_created} to new tag named "test" with reaction "x"
```

At this stage, the tag itself is **not yet created on Discord,** so you cannot add it to posts! You'll have to add it to the forum channel first:

```applescript
add {_created} to tags of forum channel with id "000"
```

Now, you'll be able to add it to the post for instance:

```applescript
add {_created} to tags of thread channel with id "000"
```

## Working with Thread Information

Since DiSky v4.27.0, you can access additional thread information to build more interactive features:

```applescript
# Example: Display comprehensive thread statistics
discord command threadinfo <text>:
    prefixes: !
    trigger:
        set {_thread} to thread channel with id arg-1
        if {_thread} is not set:
            reply with ":x: Thread not found!"
            stop

        set {_owner} to owner of {_thread}
        set {_count} to message count of {_thread}
        set {_tags::*} to tags of {_thread}
        set {_members::*} to members of {_thread}

        make embed:
            set title of embed to "Thread Information"
            set description of embed to "**Thread:** %discord name of {_thread}%"
            add field named "Owner" with value "%mention tag of {_owner}%" to embed
            add field named "Messages" with value "%{_count}%" to embed
            add field named "Active Members" with value "%size of {_members::*}%" to embed
            if size of {_tags::*} > 0:
                add field named "Tags" with value "%join {_tags::*} with "", ""%"" to embed
            set color of embed to cyan

        reply with last embed
```

!!! tip "Reference Documentation"
    For more details on these expressions, check out:

    * [Thread Owner Expression](../docs/expressions.md#thread-owner) - Get who created a thread
    * [Thread Message Count Expression](../docs/expressions.md#thread-message-count) - Get the number of messages in a thread
    * [Thread Tags Expression](../docs/expressions.md#tags) - Get the tags applied to a thread
