---
icon: material/package-variant
---

# Data Structures

!!! info "Check the [data structure wiki](../concepts/ds.md) to know how to use them!"

[[[% import 'macros.html' as macros %]]]

## Embed

[[[ macros.required_version('4.21.0') ]]]

!!! tip "Creation Expression: `new embed`"

=== "Definition"
    ### Embed Properties

    | Key           | Type       | Accepting Type | Optional                          | Example Value                         |
    |---------------|------------|----------------|:---------------------------------:|---------------------------------------|
    | `title`       | Single     | String         | :material-check-bold:{ .correct } | `"Hello World"`                       |
    | `description` | Single     | String         | :material-check-bold:{ .correct } | `"This is a description"`             |
    | `footer`      | Single     | String         | :material-check-bold:{ .correct } | `"This is a footer"`                  |
    | `footer icon` | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com/icon.png"`      |
    | `thumbnail`   | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com/thumbnail.png"` |
    | `image`       | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com/image.png"`     |
    | `color`       | Single     | Skript color   | :material-check-bold:{ .correct } | `blue`                                |
    | `url`         | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com"`               |
    | `author`      | Single     | String         | :material-check-bold:{ .correct } | `"Author Name"`                       |
    | `author url`  | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com"`               |
    | `author icon` | Single     | String (URL)   | :material-check-bold:{ .correct } | `"https://example.com/icon.png"`      |
    | `timestamp`   | Single     | Date           | :material-check-bold:{ .correct } | `now`                                 |
    | `field`       | Repeatable | Field          | :material-check-bold:{ .correct } | -                                     |
    
    ### Field Properties
    
    | Key      | Type   | Accepting Type | Optional                             | Example Value   |
    |----------|--------|----------------|:------------------------------------:|-----------------|
    | `name`   | Single | String         | :material-close-thick:{ .incorrect } | `"Field Name"`  |
    | `value`  | Single | String         | :material-close-thick:{ .incorrect } | `"Field Value"` |
    | `inline` | Single | Boolean        | :material-check-bold:{ .correct }    | `true`          |

=== "Example"
    ```applescript
    set {_e} to new embed:
        title: "Hello World"
        description: "This is a description"
        footer: "This is a footer"
        footer icon: "https://example.com/icon.png"
        thumbnail: "https://example.com/thumbnail.png"
        image: "https://example.com/image.png"
        color: blue
        url: "https://example.com"
        author: "Author Name"
        author url: "https://example.com"
        author icon: "https://example.com/icon.png"
        timestamp: now
        field:
            name: "Field Name"
            value: "Field Value"
            inline: true
    ```

<figure markdown>
  ![Image title](../images/ds-embed.png)
  <figcaption>Result of the code above</figcaption>
</figure>

## Button

[[[ macros.required_version('4.21.0') ]]]

!!! tip "Creation Expression: `new button`"

=== "Definition"
    ### Button Properties

    | Key        | Type   | Accepting Type | Optional                             | Example Value                    |
    |------------|--------|----------------|:------------------------------------:|----------------------------------|
    | `style`    | Single | ButtonStyle   | :material-close-thick:{ .incorrect } | `primary`                       |
    | `emote`    | Single | Emote         | :material-check-bold:{ .correct }    | `reaction "👋"`                 |
    | `label`    | Single | String        | :material-check-bold:{ .correct }    | `"Click me!"`                   |
    | `url`      | Single | String (URL)  | :material-check-bold:{ .correct }    | `"https://example.com"`         |
    | `disabled` | Single | Boolean       | :material-check-bold:{ .correct }    | `false`                         |
    | `id`       | Single | String        | :material-check-bold:{ .correct }    | `"unique-button-id"`            |

    !!! note "Validation Rules"
        - Either `label` OR `emote` must be present
        - Either `id` OR `url` must be present
        - If `url` is set, the button becomes a link button and `style` is ignored

=== "Example"
    ```applescript
    set {_b} to new button:
        label: "Click me!"
        emote: "👋"
        style: primary
        id: "unique-button-id"
        disabled: false
    ```