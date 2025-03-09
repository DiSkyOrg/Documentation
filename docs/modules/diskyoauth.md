---
icon: material/security-network
---

# DiSkyOAuth

<div class="grid" markdown>

=== "Introduction"

    The **DiSkyOAuth** module allows your DiSky bots to authenticate Discord users through OAuth2, providing access to user information like email, premium status, mutual servers, and more. It also enables advanced features like automatic joining to servers and token refreshing.

    This module implements a complete Discord OAuth2 flow with a built-in web server to handle redirects and process authorization codes.

=== "Features"

    - **User Authentication**: Allow users to authorize your bot to access their Discord account data
    - **Data Access**: Get user's email, premium status, guilds, and more
    - **Server Management**: Make authenticated users join servers with specific roles and settings
    - **Token Refreshing**: Automatically refresh OAuth tokens when they expire
    - **Comprehensive Events**: Handle OAuth requests and token refresh events

</div>

## Installation

1. Download the DiSkyOAuth module from [DiSky Resources](https://resources.disky.me/resources/7)
2. Place the JAR file in your `plugins/DiSky/modules` folder
3. Restart your server
4. Configure the module in `plugins/DiSky/modules/DiSkyOAuth/config.yml`

## Configuration

```yaml
# The port where the redirect web server will be used
port: 16334

# The URL to redirect in case someone accesses the root of the server
redirect-url: "https://disky.me/"

# The full, accessible URL to the server, including port
# This must be added to the OAuth2 redirect URIs in your Discord application
server-url: "http://your-server-address:16334"

# Enable debug mode for detailed logs
debug: false
```

!!! warning "Important"
    You must set up a **valid, publicly accessible URL** in the `server-url` field. This URL must be added to your Discord application's OAuth2 redirect URIs.

## Setup Discord Application

Before using the module, you need to create and configure a Discord application:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Navigate to the **OAuth2** tab
4. Add your server URL (from config) to the "Redirect URIs"
5. Copy your **Client ID** and **Client Secret** for use in DiSky
6. Set up the desired OAuth2 scopes (identify, email, guilds, etc.)

## Usage Examples

### Registering an OAuth Client

```applescript
# In your define bot structure:
on ready:
    # Register the OAuth client with Discord credentials
    register oauth client named "test" with id "YOUR_CLIENT_ID" with secret "YOUR_CLIENT_SECRET" with scopes "identify", "email", "guilds" using event-bot
```

### Creating an Authorization Flow

```applescript
slash command oauth:
    
    bot: disky
    guilds: YOUR_GUILD_ID  # Optional: makes command only available in specific guild

    description: "Authorize with Discord"

    trigger:
        # Get OAuth URL for the registered client
        set {_url} to oauth url of client "test"
        
        # Create a button that links to the authorization URL
        set {_btn} to a new button:
            url: {_url}
            label: "Authorize"
            style: link
            emote: reaction "🔗"

        # Send the button to the user
        reply with hidden rich components {_btn} and store it in {_msg}
        
        # Store some data for later
        set {OAUTH::%discord id of event-user%::MS} to now
        set {OAUTH::%discord id of event-user%::MESSAGE} to {_msg}
```

### Handling OAuth Requests

```applescript
on oauth request received:
    # Get stored message and timestamp
    set {_msg} to {OAUTH::%discord id of oauth user%::MESSAGE}
    set {_ms} to {OAUTH::%discord id of oauth user%::MS}

    # Store the tokens
    set {TOKENS::%discord id of event-user%::ACCESS} to oauth access token
    set {TOKENS::%discord id of event-user%::REFRESH} to oauth refresh token
    set {TOKENS::%discord id of event-user%::EXPIRE} to oauth expires in

    # Display information
    add "User: %oauth user%" to {_m::*}
    add "" to {_m::*}
    add "Gathered Guilds [`%size of oauth user's guilds%`]:" to {_m::*}
    loop guilds of oauth user:
        add "- %discord name of loop-value%" to {_m::*}

    add "User Premium Type: %premium type of oauth user%" to {_m::*}
    add "User Email: ||%email of oauth user%||" to {_m::*}
    add "" to {_m::*}
    add "> **You took %difference between now and {_ms}% to authorize :>**" to {_m::*}

    # Update the message with the results
    edit {_msg} to show (join {_m::*} with nl)
```

### Refreshing OAuth Tokens

```applescript
# Refresh tokens when they expire
slash command refresh_oauth [<boolean="force">]:
    bot: disky
    description: "Refresh your OAuth Token"
    
    trigger:
        # Check if a token exists
        if {TOKENS::%discord id of event-user%::REFRESH} is not set:
            reply with "You didn't authorize the bot yet! Use `/oauth` first."
            stop
            
        # Refresh the token
        set {_refresh} to {TOKENS::%discord id of event-user%::REFRESH}
        refresh oauth token {_refresh} for event-user with client "test"

# Handle the token refresh event
on oauth token refresh:
    set {_msg} to {REFRESH::%discord id of event-user%::MESSAGE}
    
    # Check if the refresh failed
    if refresh failed:
        edit {_msg} to show "Failed to refresh your token! Use /oauth to authorize again."
        stop

    # Store the new tokens
    set {TOKENS::%discord id of event-user%::ACCESS} to oauth access token
    set {TOKENS::%discord id of event-user%::REFRESH} to oauth refresh token
    set {TOKENS::%discord id of event-user%::EXPIRE} to oauth expires in

    # Confirm successful refresh
    edit {_msg} to show "Token refreshed successfully!"
```

### Make User Join a Server

```applescript
# In the OAuth request event
on oauth request received:
    # Make the user join a server with specific roles
    make oauth user join server with id "YOUR_SERVER_ID" with nickname "New Member" with roles "ROLE_ID_1", "ROLE_ID_2"
```

## Reference Guide

### Events

| Event | Description |
|-------|-------------|
| `on oauth request received` | Triggered when a user completes the OAuth2 flow |
| `on oauth token refresh` | Triggered when a token refresh is attempted |

### Expressions

| Expression | Return Type | Description |
|------------|-------------|-------------|
| `oauth user` | OAuthUser | The authenticated Discord user in OAuth events |
| `oauth access token` | String | The access token provided by Discord |
| `oauth refresh token` | String | The refresh token for renewing access |
| `oauth expires in` | Timespan | How long until the access token expires |
| `oauth url of client %string%` | String | Get the authorization URL for a client |
| `user's guilds` | Guild | Get mutual guilds for the authenticated user |
| `user's email` | String | Get the email address of the authenticated user |
| `user's premium type` | String | Get the premium status of the authenticated user |

### Effects

| Effect | Description |
|--------|-------------|
| `register oauth client named %string% with id %string% with secret %string% with scopes %strings% using the bot %bot%` | Register an OAuth client with DiSky |
| `refresh oauth token %string% for %user% with client %string%` | Refresh an OAuth token |
| `make oauth user join server with id %string% [with nickname %string%] [with roles %strings%] [(muted\|deafened\|muted and deafened)]` | Make a user join a server via OAuth |

### Conditions

| Condition | Description |
|-----------|-------------|
| `refresh failed` | Check if a token refresh attempt failed |

## Tips and Best Practices

1. **Security**: Always keep client secrets secure and never expose them in client-side code
2. **Error Handling**: Always check for errors when refreshing tokens
3. **Scopes**: Only request the OAuth scopes you actually need
4. **Storage**: Store tokens securely and clear them when no longer needed
5. **Expiration**: Always honor token expiration times and refresh as needed

!!! example "Requesting Minimal Scopes"
    Only request the scopes you need. For example, if you only need basic user information:
    ```applescript
    register oauth client named "basic" with id "YOUR_ID" with secret "YOUR_SECRET" with scopes "identify" using the bot named "disky"
    ```

## Troubleshooting

- **Make sure your server is publicly accessible**: The `server-url` in config must be reachable from Discord's servers
- **Check redirect URIs**: Ensure the redirect URI in your Discord application matches the `server-url` in config
- **Port forwarding**: If hosting on a local network, ensure the port is properly forwarded
- **Debug mode**: Enable debug mode in config for detailed logs
- **Scope issues**: If not receiving certain data, check if you requested the appropriate scopes