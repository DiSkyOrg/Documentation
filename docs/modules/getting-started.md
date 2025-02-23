---
icon: material/view-module
---

# Modules

!!! warning
    Modules are in beta! Any feedback is appreciated, from both users & developers!

!!! tip "A future page will be coming to explain how **you** can create your own module! Stay tuned!"

## Introduction

While DiSky is compiled and based on the JDA library, some other features from Discord need another library. This is where **Modules** enter the game;

These are JARS that can be added to DiSky's module folder, adding syntax related to Discord.

Modules were also meant for others to contribute to DiSky easily, but adding new features from other libraries, and covering all that Discord can offer us!

## v4.21.0 Update

Starting from v4.21.0, DiSky has a new way to handle modules. This mean, you **must have a specific minimal version of the modules** for them to work with DiSky. Here's a quick recap:

| Module                                    | Version for DiSky v4.21.0+ | Version for DiSky v4.20.2- |
|-------------------------------------------|---------------------------:|:---------------------------|
| [LavaPlayer2](lavaplayer.md)              |                   `v2.3.0` | `v2.2.4`                   |
| [TranSkript](transkript.md)               |                   `v1.2.0` | `v1.1.2`                   |
| [ParseSK](parsesk.md)          |                   `v1.1.0` | `v1.0.2`                   |
| [SkImage2](../skimage/getting-started.md) |                   `v2.1.0` | `v2.0.4`                   |

## Installation

It almost works like plugins. When the server starts with DiSky for the first time, a folder `/plugins/DiSky/modules/` is created. Simply put the module's JARS here, and restart your server.

You can take a look at the enabled & loaded modules through the `/disky modules` command.

## How to get them?

Only one module is free to download & use for DiSky. The others are paid additions to DiSky, obtainable by subscribing to a Patreon account. The minimum tier is enough to have access to all available modules and their updates for one month.