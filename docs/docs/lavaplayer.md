---
icon: material/music
---

# LavaPlayer

[[[% import 'macros.html' as macros %]]]

!!! success "Docs has been Updated!"
    You're now viewing the full documentation for [LavaPlayer v2.1+](https://patreon.disky.me/)

!!! warning
    **Load sections** are not listed here. Feel free to use the [sample code provided here](../modules/lavaplayer.md#full-example) as it'll be much easier to understand.

## Effects

### Pause Track

[[[ macros.required_lp_version('2.1.0') ]]]

Pause the current track & player.
This won't clear the queue, nor will remove the current track.
You can use 'resume track' to resume the track.

=== "Patterns"

    ```applescript
    pause [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

=== "Examples"

    ```applescript
    pause the track of event-guild
    ```


### Resume Track

[[[ macros.required_lp_version('2.1.0') ]]]

Resume the current track & player, if it's paused.

=== "Patterns"

    ```applescript
    resume [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

=== "Examples"

    ```applescript
    resume the track of event-guild
    ```


### Skip Track

[[[ macros.required_lp_version('2.1.0') ]]]

Skip the current track of a guild player.
The new track will be returned.

=== "Patterns"

    ```applescript
    skip [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%] [and store (it|[the] audiotrack) in %-objects%]
    ```

=== "Examples"

    ```applescript
    skip the track of event-guild and store it in {_track}
    skip track of event-guild
    ```


### Stop Track

[[[ macros.required_lp_version('2.1.0') ]]]

Stop the current track of a guild player.
This will also remove the current track from the queue.

=== "Patterns"

    ```applescript
    stop [the] (audio|track) (in|of) [the] [guild] %guild% [with [the] [bot] %bot%]
    ```

=== "Examples"

    ```applescript
    stop the track of event-guild
    ```


### Load Local Track

[[[ macros.required_lp_version('2.1.0') ]]]

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

=== "Patterns"

    ```applescript
    load local track [from] [the] [file] %string% and store (it|the track) in %-objects%
    ```

=== "Examples"

    ```applescript
    load local track from "plugins/music/mytrack.mp3" and store it in {_track}
    ```


### Play First Track

[[[ macros.required_lp_version('2.1.0') ]]]

Play the specified track in the specified guild.
You can specify either the track must be forced to play, and interrupt the current one.

=== "Patterns"

    ```applescript
    [force] play [the] [track] %audiotrack/audioplaylist% [the] [first] [track] [of the queue] in %guild% [with [the] [bot] %bot%]
    ```

=== "Examples"

    ```applescript
    play {_track} in event-guild
    force play {_track} in event-guild
    ```


## Expressions

### Audio Effects

#### Audio Mono Level

[[[ macros.return_type('number') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

This is an audio effect/filter.
Set the mono level of the current audio track.
The default value is 1.0

=== "Patterns"

    ```applescript
    [the] (audio|track) mono [level] of %guild%
    %guild%'[s] (audio|track) mono [level]
    ```

=== "Examples"

    ```applescript
    set mono level of event-guild to 0.5
    ```

#### Audio Pitch

[[[ macros.return_type('number') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

This is an audio effect/filter.
Change the pitch of the current audio track.
The default pitch is 1.0.

=== "Patterns"

    ```applescript
    [the] (audio|track) pitch [level] of %guild%
    %guild%'[s] (audio|track) pitch [level]
    ```

=== "Examples"

    ```applescript
    set audio speed of event-guild to 1.5
    ```

#### Audio Rotation

[[[ macros.return_type('number') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

This is an audio effect/filter.
Change the rotation of the current audio track.
(Sort of 8D effect)
The default rotation is 1

=== "Patterns"

    ```applescript
    [the] (audio|track) rotation [level] of %guild%
    %guild%'[s] (audio|track) rotation [level]
    ```

=== "Examples"

    ```applescript
    set audio rotation of event-guild to 2
    ```

#### Audio Speed

[[[ macros.return_type('number') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

This is an audio effect/filter.
Change the speed of the current audio track.
The default speed is 1.0.

=== "Patterns"

    ```applescript
    [the] (audio|track) speed [level] of %guild%
    %guild%'[s] (audio|track) speed [level]
    ```

=== "Examples"

    ```applescript
    set audio speed of event-guild to 2
    ```

### Guild Properties

#### Guild Playing Track

[[[ macros.return_type('audiotrack') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Get the current track playing in a guild.
This cannot be changed via this expression, but you can use the 'play' effect to play a track.

=== "Patterns"

    ```applescript
    [all] [the] [audio] playing track of %guild%
    [all] [the] %guild%'[s] [audio] playing track
    ```

=== "Examples"

    ```applescript
    set {_track} to playing track of event-guild
    ```

#### Guild Queue

[[[ macros.return_type('audiotrack') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Represents the audio queue of a guild.
You can get the queue, but also add or remove tracks from it.

=== "Patterns"

    ```applescript
    [all] [the] [audio] queue of %guild%
    [all] [the] %guild%'[s] [audio] queue
    ```

=== "Examples"

    ```applescript
    if queue of event-guild is empty:
    add {_track} to queue of event-guild
    ```

#### Guild Auto Play

[[[ macros.return_type('boolean') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

If enabled, when a track ends, the next will be played automatically.
By default, this is disabled.

=== "Patterns"

    ```applescript
    [the] [auto[( |-)]]play [state] of %guild%
    %guild%'[s] [auto[( |-)]]play [state]
    ```

=== "Examples"

    ```applescript
    set auto play of event-guild to true
    ```

#### Guild Repeat

[[[ macros.return_type('boolean') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

If enabled, when a track ends, the same track will be played again.
By default, this is disabled.

=== "Patterns"

    ```applescript
    [the] [auto[( |-)]]repeat [state] of %guild%
    %guild%'[s] [auto[( |-)]]repeat [state]
    ```

=== "Examples"

    ```applescript
    set repeat of event-guild to true
    ```

#### Guild Volume

[[[ macros.return_type('integer') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Get the volume of a guild, or null if the guild have not player.
This can be changed to change the audio volume of a guild.
If the guild does not have any player, nothing will change.
Note that the volume is a number between 0 and 1000.

=== "Patterns"

    ```applescript
    [the] [audio[ ]]guild volume of %guild%
    %guild%'[s] [audio[ ]]guild volume
    ```

=== "Examples"

    ```applescript
    set guild volume of event-guild to 100
    set {_volume} to guild volume of event-guild
    ```

### Track & Playlist Properties

#### Playlist Tracks

[[[ macros.return_type('audiotrack') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Get all the ordered tracks of a loaded playlist.

=== "Patterns"

    ```applescript
    [all] [the] [audio[ ]]tracks of %audioplaylist%
    [all] [the] %audioplaylist%'[s] [audio[ ]]tracks
    ```

=== "Examples"

    ```applescript
    set {_tracks::*} to tracks of the loaded playlist
    ```

#### Playlist Name

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Get the name of a loaded playlist.

=== "Patterns"

    ```applescript
    [the] [audio[ ]]playlist name of %audioplaylist%
    %audioplaylist%'[s] [audio[ ]]playlist name
    ```

=== "Examples"

    ```applescript
    playlist name of the loaded playlist
    ```

#### Track Author

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the author of a specific track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track author of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track author
    ```

=== "Examples"

    ```applescript
    set {_author} to author of last played track.
    ```

#### Track Duration

[[[ macros.return_type('timespan') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the duration of a specific track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track duration of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track duration
    ```

=== "Examples"

    ```applescript
    set {_duration} to duration of last played track.
    ```

#### Track Identifier

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the unique identifier of a track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track id[entifier] of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track id[entifier]
    ```

=== "Examples"

    ```applescript
    set {_id} to identifier of current track of event-guild
    ```

#### Track Position

[[[ macros.return_type('timespan') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the position of a specific track
This property can be changed to move the current position of the track.
It will only accept timespan (e.g. '1 second', '25 minutes', etc...)!

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track position of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track position
    ```

=== "Examples"

    ```applescript
    set {_position} to track position of track event-bot is playing in event-guild
    add 10 second to track position of track event-bot is playing in event-guild
    ```

#### Track Thumbnail

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the thumbnail URL of a specific track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track thumbnail of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track thumbnail
    ```

=== "Examples"

    ```applescript
    set thumbnail of embed to thumbnail of last played track.
    ```

#### Track Title

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the title of a specific track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track title of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track title
    ```

=== "Examples"

    ```applescript
    set {_title} to title of last played track.
    ```

#### Track URL

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Return the YouTube URL of a track

=== "Patterns"

    ```applescript
    [the] [discord] [audio] track (url|uri) of %audiotrack%
    %audiotrack%'[s] [discord] [audio] track (url|uri)
    ```

=== "Examples"

    ```applescript
    set {_url} to url of last played track.
    ```

### Loading Results

#### Load Exception

[[[ macros.return_type('string') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Represent the exception that occurred during the load of a research or items.
This is the message only.

=== "Patterns"

    ```applescript
    [the] exception
    ```

=== "Examples"

    ```applescript
    the exception
    ```

#### Loaded Playlist

[[[ macros.return_type('audioplaylist') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Represent the loaded playlist in a 'on playlist loaded' sub-load section.

=== "Patterns"

    ```applescript
    [the] loaded playlist
    ```

=== "Examples"

    ```applescript
    loaded playlist
    ```

#### Loaded Track

[[[ macros.return_type('audiotrack') ]]]
[[[ macros.required_lp_version('2.1.0') ]]]

Represent the loaded track in a 'on single load' sub-load section.

=== "Patterns"

    ```applescript
    [the] loaded track
    ```

=== "Examples"

    ```applescript
    loaded track
    ```
