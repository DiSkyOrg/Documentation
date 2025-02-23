---
icon: material/package-variant
---

# Data Structures

[[[% import 'macros.html' as macros %]]]
[[[ macros.required_version('4.21.0') ]]]

Data Structures are a new way to create and configure complex objects in DiSky using a clean, YAML-like syntax. They provide an intuitive way to set multiple properties at once.

## Basic Usage

A Data Structure uses a section-style syntax where you define properties using simple `key: value` pairs. Here's a basic example:

```applescript
set {_embed} to new embed:
    title: "Hello World"
    description: "This is a description"
    color: blue
```

!!! info
    The creation expression (here, `new embed`) may vary according to what you want to create. Check the [data structure documentation](../docs/ds.md) for more details.

## Repeatable Properties

Some properties can be repeated multiple times. For example, embed fields:

```applescript
set {_embed} to new embed:
    title: "Stats"
    color: orange
    
    # First field
    field:
        name: "Users"
        value: "1,234"
    
    # Second field
    field:
        name: "Servers"
        value: "42"
        inline: true
```

You simply have to repeat the property's key (in singular form) to add a new item.