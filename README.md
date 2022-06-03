# yt-server

Provides a web api to access YouTube video files directly by their ID. Initially created for use in VRChat video players.

:warning: **Downloads full quality videos, so can easily take up a large amount of space on a server** :warning:

## Installation
1. Install Python 3
2. Install modules `pip install -r requirements.txt`
3. Install yt-dlp (this directly calls `yt-dlp` in the terminal)

## Usage

### Running the server
```shell
# Run the server
flask run
```

### API Endpoints
 - Directly access a video: `/<video ID>.mp4`
 - Search for a video: `/search/<search term>`

## Features
 - [x] Access videos by ID
 - [x] Basic search
 - [ ] Use Python only, no other dependencies
 - [ ] Better video caching
 - [ ] Search caching 
 - [ ] Delete video files if not requested for a while or if file size limit reached
 - [ ] Playlist support

## Contributing

For development, setup in the same way as general installation.

Pull requests and bug reports welcome, feature requests too.
