# 🎵 LavaPlayer

[[[% import 'macros.html' as macros %]]]

!!! success
    This documentation page includes all the elements from the module **[LavaPlayer](../modules/lavaplayer.md)**.

## Load Local Track

[[[ macros.required_version('2.0.0') ]]]

Loads a local track from the files of your server.
The supported file types are:
- MP3
- FLAC
- WAV
- Matroska/WebM (AAC, Opus or Vorbis codecs)
- MP4/M4A (AAC codec)
- OGG streams (Opus, Vorbis and FLAC codecs)
- AAC streams
- Stream playlists (M3U and PLS)
=== "Examples"

    ```applescript
    load local track from "plugins/music/mytrack.mp3" and store it in {_track}
    ```
=== "Patterns"

    ```applescript
    load local track [from] [the] [file] %string% and store (it|the track) in %-objects%
    ```

## Pause Track

[[[ macros.required_version('2.0.0') ]]]

Pause the current track & player.
This won't clear the queue, nor will remove the current track.
You can use 'resume track' to resume the track.
=== "Examples"

    ```applescript
    pause the track of event-guild
    ```
=== "Patterns"

    ```applescript
    pause [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

## Resume Track

[[[ macros.required_version('2.0.0') ]]]

Resume the current track & player, if it's paused.
=== "Examples"

    ```applescript
    resume the track of event-guild
    ```
=== "Patterns"

    ```applescript
    resume [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

## Skip Track

[[[ macros.required_version('2.0.0') ]]]

Skip the current track of a guild player.
The new track will be returned.
=== "Examples"

    ```applescript
    skip the track of event-guild and store it in {_track}
    skip track of event-guild
    ```
=== "Patterns"

    ```applescript
    skip [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%] [and store (it|[the] audiotrack) in %-objects%]
    ```

## Stop Track

[[[ macros.required_version('2.0.0') ]]]

Stop the current track of a guild player.
This will also remove the current track from the queue.
=== "Examples"

    ```applescript
    stop the track of event-guild
    ```
=== "Patterns"

    ```applescript
    stop [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

## Loaded Playlist

[[[ macros.required_version('2.0.0') ]]]
|Return Type|audioplaylist|class:version|

Represent the loaded playlist in a 'on playlist loaded' sub-load section.
=== "Examples"

    ```applescript
    loaded playlist
    ```
=== "Patterns"

    ```applescript
    [the] loaded playlist
    ```

## Loaded Track

[[[ macros.required_version('2.0.0') ]]]
|Return Type|audiotrack|class:version|

Represent the loaded track in a 'on single load' sub-load section.
=== "Examples"

    ```applescript
    loaded track
    ```
=== "Patterns"

    ```applescript
    [the] loaded track
    ```

## Load Exception

[[[ macros.required_version('2.0.0') ]]]
|Return Type|string|class:version|

Represent the exception that occurred during the load of a research or items.
This is the message only.
=== "Examples"

    ```applescript
    the exception
    ```
=== "Patterns"

    ```applescript
    [the] exception
    ```

## Guild Playing Track

[[[ macros.required_version('2.0.0') ]]]
|Return Type|audiotrack|class:version|

Get the current track playing in a guild.
This cannot be changed via this expression, but you can use the 'play' effect to play a track.
=== "Examples"

    ```applescript
    set {_track} to playing track of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [audio] playing track of %guild%
    [all] [the] %guild%'[s] [audio] playing track
    ```

## Guild Queue

[[[ macros.required_version('2.0.0') ]]]
|Return Type|audiotrack|class:version|

Represents the audio queue of a guild.
You can get the queue, but also add or remove tracks from it.
=== "Examples"

    ```applescript
    if queue of event-guild is empty:
    add {_track} to queue of event-guild
    ```
=== "Patterns"

    ```applescript
    [all] [the] [audio] queue of %guild%
    [all] [the] %guild%'[s] [audio] queue
    ```

## Playlist Tracks

[[[ macros.required_version('2.0.0') ]]]
|Return Type|audiotrack|class:version|

Get all the ordered tracks of a loaded playlist.
=== "Examples"

    ```applescript
    set {_tracks::*} to tracks of the loaded playlist
    ```
=== "Patterns"

    ```applescript
    [all] [the] [audio[ ]]tracks of %audioplaylist%
    [all] [the] %audioplaylist%'[s] [audio[ ]]tracks
    ```

## Audio Mono Level

[[[ macros.required_version('4.0.0') ]]]
|Return Type|number|class:version|

This is an audio effect/filter.
Set the mono level of the current audio track.
The default value is 1.0
=== "Examples"

    ```applescript
    set mono level of event-guild to 0.5
    ```
=== "Patterns"

    ```applescript
    [the] (audio|track) mono [level] of %guild%
    %guild%'[s] (audio|track) mono [level]
    ```

## Audio Pitch

[[[ macros.required_version('4.0.0') ]]]
|Return Type|number|class:version|

This is an audio effect/filter.
Change the pitch of the current audio track.
The default pitch is 1.0.
=== "Examples"

    ```applescript
    set audio speed of event-guild to 1.5
    ```
=== "Patterns"

    ```applescript
    [the] (audio|track) pitch [level] of %guild%
    %guild%'[s] (audio|track) pitch [level]
    ```

## Audio Rotation

[[[ macros.required_version('4.0.0') ]]]
|Return Type|number|class:version|

This is an audio effect/filter.
Change the rotation of the current audio track.
(Sort of 8D effect)
The default rotation is 1
=== "Examples"

    ```applescript
    set audio rotation of event-guild to 2
    ```
=== "Patterns"

    ```applescript
    [the] (audio|track) rotation [level] of %guild%
    %guild%'[s] (audio|track) rotation [level]
    ```

## Audio Speed

[[[ macros.required_version('4.0.0') ]]]
|Return Type|number|class:version|

This is an audio effect/filter.
Change the speed of the current audio track.
The default speed is 1.0.
=== "Examples"

    ```applescript
    set audio speed of event-guild to 2
    ```
=== "Patterns"

    ```applescript
    [the] (audio|track) speed [level] of %guild%
    %guild%'[s] (audio|track) speed [level]
    ```

## Guild Auto Play

[[[ macros.required_version('2.0.0') ]]]
|Return Type|boolean|class:version|

If enabled, when a track ends, the next will be played automatically.
By default, this is disabled.
=== "Examples"

    ```applescript
    set auto play of event-guild to true
    ```
=== "Patterns"

    ```applescript
    [the] [auto[( |-)]]play [state] of %guild%
    %guild%'[s] [auto[( |-)]]play [state]
    ```

## Guild Repeat

[[[ macros.required_version('2.0.0') ]]]
|Return Type|boolean|class:version|

If enabled, when a track ends, the same track will be played again.
By default, this is disabled.
=== "Examples"

    ```applescript
    set repeat of event-guild to true
    ```
=== "Patterns"

    ```applescript
    [the] [auto[( |-)]]repeat [state] of %guild%
    %guild%'[s] [auto[( |-)]]repeat [state]
    ```

## Guild Volume

[[[ macros.required_version('2.0.0') ]]]
|Return Type|integer|class:version|

Get the volume of a guild, or null if the guild have not player.
This can be changed to change the audio volume of a guild.
If the guild does not have any player, nothing will change.
Note that the volume is a number between 0 and 1000.
=== "Examples"

    ```applescript
    set guild volume of event-guild to 100
    set {_volume} to guild volume of event-guild
    ```
=== "Patterns"

    ```applescript
    [the] [audio[ ]]guild volume of %guild%
    %guild%'[s] [audio[ ]]guild volume
    ```

## Playlist Name

[[[ macros.required_version('2.0.0') ]]]
|Return Type|string|class:version|

Get the name of a loaded playlist.
=== "Examples"

    ```applescript
    playlist name of the loaded playlist
    ```
=== "Patterns"

    ```applescript
    [the] [audio[ ]]playlist name of %audioplaylist%
    %audioplaylist%'[s] [audio[ ]]playlist name
    ```

