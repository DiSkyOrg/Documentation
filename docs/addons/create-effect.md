# 📘 Create an effect

!!! warning
    I highly recommend you to read [the first page of this wiki](getting-started.md) before continue. All elements are linked together, so you may need to know how to create an effect before creating a condition, for instance.

Create a new class, and name it `Eff<name>` where Name is your effect's short name. For this example, we'll create an expression returning player's gamemode:

```java
package my.addon.effects;

import org.bukkit.GameMode;
import org.bukkit.entity.Player;
import org.bukkit.event.Event;


```