# import modules
from flask import Flask, send_file, redirect
from youtube_search import YoutubeSearch
import json
import os

# create app
app = Flask(__name__)

# route for /{id}.mp4
@app.route('/<string:id>.mp4')
def get_mp4(id):
    # # download youtube video using pytube
    # yt = pytube.YouTube(f'https://www.youtube.com/watch?v={id}')
    # # get the first video
    # vid = yt.streams.first()
    # # download the video to /videos
    # vid.download('videos')
    # # serve the video file from /videos
    # return app.send_from_directory('videos', vid.default_filename)

    # run yt-dlp to download the video
    os.system(f'yt-dlp -f best -o videos/{id}.mp4 https://www.youtube.com/watch?v={id}')

    # serve the mp4 file
    return send_file(f'videos/{id}.mp4', mimetype='video/mp4')

# route for /search/{query}.mp4
@app.route('/search/<string:query>')
def get_search_mp4(query):
    # search youtube for the query
    result = YoutubeSearch(query, max_results=1).to_json()
    # parse the json result
    result = json.loads(result)
    result = result["videos"][0]
    # get the video id
    id = result["id"]
    # redirect to the video id
    return redirect(f'/{id}.mp4')

    print(result)
    return 'hello'