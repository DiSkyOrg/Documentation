---
icon: material/view-grid
status: new
---

# Discord Containers

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.24.0') ]]]

Discord Containers are a new way to create rich, interactive message layouts using Discord's Components V2 system. They provide a structured approach to organizing content, images, buttons, and other interactive elements within Discord messages.

!!! info "Components V2 System"
    Containers are part of Discord's new Components V2 system, introduced in March 2025. This system allows for much more flexible and visually appealing message layouts compared to traditional embeds and components.

## Overview

Containers provide a hierarchical structure for organizing message content:

- **Container**: The top-level component that holds all other elements
- **Sections**: Organize related content with optional accessories (buttons/thumbnails)
- **Text Displays**: Show formatted text content with markdown support
- **Media Galleries**: Display collections of images or media
- **Separators**: Provide visual separation between content blocks
- **Components**: Interactive elements like buttons and dropdowns

## Container Structure

### Basic Container

A container is the root element that holds all other components:

```applescript
create a new container with unique id 50 and store it in {_container}:
    # Add content here
    add "Hello World!" to content of the container
```

### Container Properties

| Property | Description | Example |
|----------|-------------|---------|
| `unique id` | Identifier for component replacement | `50` |
| `accent color` | Color accent (like embed color) | `0xFF0000` |
| `spoiler` | Mark container as spoiler content | `true/false` |

## Sections

Sections group related content together and can have accessories (buttons or thumbnails):

```applescript
create a new container section and store it in {_section}:
    add "### Section Title" to content of the section
    add "This is section content with **markdown** support" to content of the section
    
    # Optional: Add an accessory (button or thumbnail)
    set {_button} to new button:
        label: "Click me!"
        style: primary
        id: "section-button"
    set accessory of the section to {_button}

add {_section} to content of the container
```

### Section Limits

- **Maximum 3 text displays** per section
- **One accessory** per section (either button or thumbnail)
- Accessories appear on the right side of the section

## Content Types

### Text Display

Simple text content with full markdown support:

```applescript
# Direct text addition (creates text display automatically)
add "Simple text content" to content of the container
add "**Bold text** with *italics* and [links](https://example.com)" to content of the container

# With emoji support
add "Text with emoji 💸👍❤" to content of the container
```

### Media Gallery

Display collections of images:

```applescript
add new media gallery with images (file upload from local file "path/to/image.png") to content of the container

# Multiple images
set {_gallery} to new media gallery
add new media gallery item with source (file upload from url "https://example.com/image1.png") to {_gallery}
add new media gallery item with source (file upload from url "https://example.com/image2.png") to {_gallery}
add {_gallery} to content of the container
```

### Separators

Visual dividers between content:

```applescript
# Small separator
add new small separator to content of the container

# Large separator (default)
add new separator to content of the container
```

### Thumbnails

Clickable image accessories for sections:

```applescript
create a new container section and store it in {_section}:
    add "Content with thumbnail" to content of the section
    
    set {_thumbnail} to new thumbnail with source (file upload from local file "image.png")
    set accessory of the section to {_thumbnail}
```

## Interactive Components

### Buttons in Containers

Buttons can be used as section accessories or in component rows:

```applescript
# As section accessory
set {_button} to new button:
    label: "View Details"
    style: secondary
    emote: reaction "👀"
    id: "view-details"
set accessory of the section to {_button}

# In component rows
set {_row} to a new component row with {_button1} and {_button2}
add {_row} to content of the container
```

### Component Rows

Traditional component rows still work within containers:

```applescript
create a new row and store it in {_row}:
    set {_btn1} to new button:
        label: "Previous"
        style: primary
        id: "prev-btn"
    add {_btn1} to components of the row
    
    set {_btn2} to new button:
        label: "Next"  
        style: primary
        id: "next-btn"
    add {_btn2} to components of the row

add {_row} to content of the container
```

## Unique IDs and Component Replacement

### The Unique ID System

Each container has a unique identifier used for component replacement:

```applescript
create a new container with unique id 50 and store it in {_container}:
    add "Original content" to content of the container
```

### Component Replacement

Use the `apply component replacement` section to update containers:

```applescript
on button click:
    apply component replacement for event-message:
        the unique id is 50  # Target container with ID 50
        replace the component with createNewContainer()
```

### Replacement Context

Within the replacement section, you have access to:

- `the unique id`: The ID of the component being tested for replacement
- `the component`: The actual component being iterated (for additional info)

```applescript
apply component replacement for event-message:
    # Check if this is the container we want to replace
    the unique id is 50
    
    # Optionally access component info
    if type of the component is "container":
        replace the component with createUpdatedContainer()
```

## Limitations and Constraints

### Container Limits

- **Maximum 10 top-level components** per message
- **Maximum 30 nested components** total
- **4000 UTF-8 characters** total message length (including all component content)

### Section Limits

- **Maximum 3 components** per section
- **One accessory** per section (button or thumbnail)

### Component Restrictions

When using Components V2:

- Cannot set traditional message `content` or `embeds`
- Audio files not supported
- URLs won't generate automatic embeds
- Text preview for text/plain files not supported

## Message Requirements

To use containers, you must set the Components V2 flag:

```applescript
# In DiSky, this is handled automatically when using containers
reply with {_container}
post {_container} to event-channel
```

## Complete Example

Here's a comprehensive example showing various container features:

```applescript
function createExampleContainer() :: container:
    create a new container with unique id 100 and store it in {_container}:
        # Banner image
        add new media gallery with images (file upload from url "https://example.com/banner.png") to content of the container
        
        # Small separator
        add new small separator to content of the container
        
        # Main content section with thumbnail
        create a new container section and store it in {_mainSection}:
            add "## Welcome to our Service" to content of the section
            add "This is a **comprehensive example** of Discord containers." to content of the section
            add "Features include *rich text*, links, and more!" to content of the section
            
            # Add thumbnail accessory
            set {_thumb} to new thumbnail with source (file upload from url "https://example.com/icon.png")
            set accessory of the section to {_thumb}
        
        add {_mainSection} to content of the container
        
        # Separator between sections
        add new separator to content of the container
        
        # Action section with button
        create a new container section and store it in {_actionSection}:
            add "### Get Started" to content of the section
            add "Click the button below to begin!" to content of the section
            
            # Button accessory
            set {_actionBtn} to new button:
                label: "Start Now"
                style: success
                emote: reaction "🚀"
                id: "start-action"
            set accessory of the section to {_actionBtn}
        
        add {_actionSection} to content of the container
        
        # Navigation buttons
        create a new row and store it in {_navRow}:
            set {_backBtn} to new button:
                label: "Back"
                style: secondary
                id: "nav-back"
            add {_backBtn} to components of the row
            
            set {_homeBtn} to new button:
                label: "Home"
                style: primary
                id: "nav-home"
            add {_homeBtn} to components of the row
        
        add {_navRow} to content of the container
    
    return {_container}

# Usage
slash command demo:
    description: "Show container demo"
    trigger:
        reply with createExampleContainer()
```

## Handling Interactions

```applescript
on button click:
    set {_parts::*} to event-string split by ":"
    set {_action} to {_parts::1}
    
    if {_action} is "start-action":
        apply component replacement for event-message:
            the unique id is 100
            replace the component with createSuccessContainer()
    
    else if {_action} is "nav-back":
        apply component replacement for event-message:
            the unique id is 100
            replace the component with createPreviousContainer()
```