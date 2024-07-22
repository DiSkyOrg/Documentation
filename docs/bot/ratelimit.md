(note for Sky: I do not know how MkDocs works, so modify anything as you wish.)
# Rate Limits
A rate limit is a strategy to limit network activity, that caps the amount of times someone can repeat an action. If someone repeats an action many times, they are "rate limited".<br>
In DiSky (and Discord bots), a rate limit is the same definition. It is a network activity limiter, and when you perform the same action over and over again, you will get "rate limited", in this case, temporarily prohibited from using the Discord API.

## How does it look like?
In your server console, you may see the following:
```
[09:41:31 ERROR]: [net.dv8tion.jda.api.requests.RestRateLimiter] Encountered cloudflare rate limit! Retry-After: 100 s
```
Your bot will not be connected to Discord, and you will be unable to perform any bot action.

Keep in mind if you are hosting your bot locally (in your house and not with a hosting provider), you will see this screen (as if you didn't have internet): 
![image](https://github.com/user-attachments/assets/7665d79e-2013-498e-9ded-8b6a1b4771cd)
## How can I fix it?
Here are possible things you can do:
1. Check if your bot is doing repetitive Discord actions (retrieve, post, reply, ect), if you found anything like that, change your code.
2. If you are running multiple bots, do the check above for all of your bots (only when you're running all your bots in the same server/pc, if one of your bots gets rate limited, ALL of them will become ratelimited).
3. If your token got leaked, hackers and bad actors may use your bot to spam requests using your bot. Simply change your token in the developer portal.
5. If your bot is used by lots of people, make sure to add command cooldowns per user, so that users will not spam commands. If your bot is still getting ratelimited on normal operations, contact Discord here: https://dis.gd/contact

## More Information
For more information regarding rate limits, visit the Discord Developer page for rate limits: https://discord.com/developers/docs/topics/rate-limits
