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


@app.route("/controls")
def admin():
    return render_template("controls.html")


def socketio_thread():
    socketio.run(app)



threading.Thread(target=socketio_thread).start()
print("Scoreboard is running on: http://127.0.0.1:5000")
print("Controls are running on: http://127.0.0.1:5000/controls")
global player_one_score
global player_two_score
player_one_score = 0
player_two_score = 0


@socketio.on("scoreup1")
def scoreup1():
    global player_one_score
    player_one_score += 1
    socketio.emit('score1', {'player_one_score': f"{player_one_score}"})


@socketio.on("scoredown1")
def scoredown1():
    global player_one_score
    player_one_score -= 1
    socketio.emit('score1', {'player_one_score': f"{player_one_score}"})


@socketio.on("scoreup2")
def scoreup2():
    global player_two_score
    player_two_score += 1
    socketio.emit('score2', {'player_two_score': f"{player_two_score}"})


@socketio.on("scoredown2")
def scoredown2():
    global player_two_score
    player_two_score -= 1
    socketio.emit('score2', {'player_two_score': f"{player_two_score}"})


@socketio.on("hide")
def hide():
    socketio.emit('fadeout')
    time.sleep(0.5)


@socketio.on("reset")
def reset():
    global player_one_score
    global player_two_score
    socketio.emit('reset', {'player_one_score': f"{player_one_score}",
                            'player_two_score': f"{player_two_score}"})
    player_one_score = 0
    player_two_score = 0
    socketio.emit('score1', {'player_one_score': f"{player_one_score}"})
    socketio.emit('score2', {'player_two_score': f"{player_two_score}"})


@socketio.on("fadein")
def fadein():
    socketio.emit('fadein')
    


while True:
    time.sleep(0.1)
    try:
        if keyboard.is_pressed('f21'):
            scoreup1()
        if keyboard.is_pressed('f22'):
            scoredown1()
        if keyboard.is_pressed("f23"):
            scoreup2()
        if keyboard.is_pressed("f24"):
            scoredown2()
        if keyboard.is_pressed("end"):
            hide()
        if keyboard.is_pressed("delete"):
            reset()
        if keyboard.is_pressed("page down"):
            fadein()

    except KeyboardInterrupt:
        break
