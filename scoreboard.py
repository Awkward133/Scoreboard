from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit
import keyboard
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")
print(socketio.async_mode)


@app.route("/")
def home():
    return render_template("index.html")

def socketio_thread():
    socketio.run(app)

threading.Thread(target=socketio_thread).start()
global player_one_score
global player_two_score
player_one_score = 0
player_two_score = 0

while True:
    time.sleep(0.1)
    try:
        if keyboard.is_pressed('f21'):
            player_one_score += 1
            socketio.emit('score1', {'player_one_score': f"{player_one_score}"})
            time.sleep(0.5)
        if keyboard.is_pressed('f22'):
            player_one_score -= 1
            socketio.emit('score1', {'player_one_score': f"{player_one_score}"})
            time.sleep(0.5)
        if keyboard.is_pressed("f23"):
            player_two_score += 1
            socketio.emit('score2', {'player_two_score': f"{player_two_score}"})
            time.sleep(0.5)
        if keyboard.is_pressed("f24"):
            player_two_score -= 1
            socketio.emit('score2', {'player_two_score': f"{player_two_score}"})
            time.sleep(0.5)
        if keyboard.is_pressed("end"):
            socketio.emit('fadeout')
            time.sleep(0.5)
        if keyboard.is_pressed("delete"):
            socketio.emit('reset', {'player_one_score': f"{player_one_score}", 'player_two_score': f"{player_two_score}"})
            player_one_score = 0
            player_two_score = 0
            socketio.emit('score1', {'player_one_score': f"{player_one_score}"})
            socketio.emit('score2', {'player_two_score': f"{player_two_score}"})
            time.sleep(0.5)
        if keyboard.is_pressed("page down"):
            socketio.emit('fadein')
            time.sleep(0.5)
        
    except KeyboardInterrupt:
        break