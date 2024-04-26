---
icon: material/frequently-asked-questions
---

# Frequently Asked Questions (FAQ)

This page contains answers to frequently asked questions about DiSky. If you have a question that is not answered here, please join [our Discord server](https://disky.me/discord)!

??? question "Even after an hour, slash commands aren't updated / deleted / added. Why?"
    You need to enable the "applications.commands" scope when you invite your bot to a guile. Without it the bot can't manage slash command

??? question "Why does my bot doesn't log on? Why I am getting a CloseCode (4014 / Disallowed intents error)?"
    You need to enable your bot intents at the bot page in discord developers to fix this issue
    ![faq intents](../images/faq-intents.png)

??? question "`a types.discordentity cannot be stored i.e. the content of the variable {x} will be lost when the server stops`"
    The entity is not serializable, therefore skript cant save it neither yml.
    Instead, you can save its ID and then get it back using the different getting expressions.

??? question "How does DiSky handle the new Discord username system?"
    This will depend on your DiSky version:

    === "Up to DiSky v4.12.0 (included)"
        Every discriminator will still be present and used in user/member names. For the updated users, it'll shows a discriminator of 0000, such as `itsthesky#0000`

    === "DiSky v4.12.1 and above"
        Only the discriminator event and expression are available. Any other reference to the discriminators has been removed. For instance, `"%event-member%"` will returns a string such as `itsthesky`.

??? question "I cannot change a member's nickname"
    That is a hierarchy issue. You cannot change the nickname of a member with a higher role than you. You can only change the nickname of a member with a lower role than you. Keep also in mind being the owner of the server make you have the highest role possible.

??? question "Why can't I use `XXX parsed as user`, or parsing other entities?"
    Most entities on Discord must be parsed with a context (e.g. a channel requires a guild to be got from). In additions, some entities also needs to be **retrieved**, and the `parse` expression is not able to do that.

    Keep in mind however most of those entities have a **getter** or a **retriever** available! Go take a look at the [docs](../docs/effects.md).

??? question "What is the difference between users and members?"
    A user is a Discord account, while a member is a user in a guild. A member (which holds a user) has a guild-specific nickname, roles, and permissions.

    Thus both a member and a user have an ID, avatar, name ... but only a member has a nickname, roles, and permissions.