from flask import Flask, render_template
from mpd import MPDClient
from jinja2 import Environment, PackageLoader
#TODO add logging functionality

app = Flask('flask-mpd')

#stackoverflow: https://stackoverflow.com/questions/35802741/jinja-cant-find-template-path
env = Environment(loader=PackageLoader('flask_mpd_client', 'templates'))
template = env.get_template('index.html')


client = MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)

PLAY, PAUSE, STOP = 'Play', 'Pause', 'Stop'
MPD_COMMANDS = {
    'Play': PLAY,
    'Pause': PAUSE,
    'Stop': STOP
}

def ConnectMPD (c):
  try:
    c.connect (mpdhost, 6600)
  except mpd.ConnectionError():
    return False
  
  return True




@app.route("/")
def index():
    x = client.currentsong()
    return render_template(template, mpd_song_title=x["title"], \
    mpd_artist=x["artist"], mpd_album=x["album"], commands=MPD_COMMANDS)


